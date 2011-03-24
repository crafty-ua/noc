# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Usage: debug-script <profile> <script> <stream-url>
##
## WARNING!!!
## This module implements part of activator functionality.
## Sometimes via dirty hacks
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
## Python modules
from __future__ import with_statement
import logging
import sys
import ConfigParser
import Queue
import time
import cPickle
import threading
import signal
import os
import datetime
import pprint
from optparse import OptionParser, make_option
## Django modules
from django.core.management.base import BaseCommand, CommandError
## NOC modules
from noc.sa.profiles import profile_registry
from noc.sa.script import script_registry, Script
from noc.sa.activator import Service, ServersHub
from noc.sa.protocols.sae_pb2 import *
from noc.sa.rpc import TransactionFactory
from noc.lib.url import URL
from noc.lib.nbsocket import SocketFactory
from noc.lib.validators import is_int

class Controller(object):
    pass

##
## Canned beef output
##
class SessionCan(object):
    def __init__(self, script_name, input={}):
        self.cli={} # Command -> result
        self.input=input
        self.result=None
        self.motd=""
        self.script_name=script_name
        self.snmp_get={}
        self.snmp_getnext={}
    
    ## Store data
    def save_interaction(self, provider, cmd, data):
        if provider=="cli":
            self.cli[cmd]=data
    
    ##
    def save_snmp_get(self, oid, result):
        self.snmp_get[oid]=result
    
    ##
    def save_snmp_getnext(self, oid, result):
        self.snmp_getnext[oid]=result
    
    ## Save final result
    def save_result(self, result, motd=""):
        self.result=result
        self.motd=motd
    
    ## Dump canned data
    def dump(self, output):
        def format_stringdict(d):
            def lrepr(s):
                return repr(s)[1:-1]
            out=["{"]
            for k, v in d.items():
                lines=v.splitlines()
                if len(lines)<4:
                    out+=["%s:  %s, "%(repr(k), repr(v))]
                else:
                    out+=["## %s"%repr(k)]
                    out+=["%s: \"\"\"%s"%(repr(k), lrepr(lines[0]))]+[lrepr(l) for l in lines[1:-1]]+["%s\"\"\", "%lrepr(lines[-1])]
            out+=["}"]
            return "\n".join(out)
        vendor, profile, script=self.script_name.split(".")
        date=str(datetime.datetime.now()).split(".")[0]
        s="""# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## %(script)s test
## Auto-generated by manage.py debug-script at %(date)s
##----------------------------------------------------------------------
## Copyright (C) 2007-%(year)d The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class %(test_name)s_Test(ScriptTestCase):
    script="%(script)s"
    vendor="%(vendor)s"
    platform='<<<INSERT YOUR PLATFORM HERE>>>'
    version='<<<INSERT YOUR VERSION HERE>>>'
    input=%(input)s
    result=%(result)s
    motd=%(motd)s
    cli=%(cli)s
    snmp_get=%(snmp_get)s
    snmp_getnext=%(snmp_getnext)s
"""%{
            "test_name"    : self.script_name.replace(".", "_"),
            "script"       : self.script_name,
            "vendor"       : vendor,
            "year"         : datetime.datetime.now().year,
            "date"         : date,
            "input"        : pprint.pformat(self.input),
            "result"       : pprint.pformat(self.result),
            "cli"          : format_stringdict(self.cli),
            "snmp_get"     : pprint.pformat(self.snmp_get),
            "snmp_getnext" : pprint.pformat(self.snmp_getnext),
            "motd"         : pprint.pformat(self.motd),
        }
        with open(output, "w") as f:
            f.write(s)
    

##
## Activator emulation
##
class ActivatorStub(object):
    WAIT_TICKS=4
    def __init__(self, script_name, values=[], output=None):
        # Simple config stub
        self.config=ConfigParser.SafeConfigParser()
        self.config.read("etc/noc-activator.defaults")
        self.config.read("etc/noc-activator.conf")
        self.script_call_queue=Queue.Queue()
        self.ping_check_results=None
        self.factory=SocketFactory(tick_callback=self.tick, controller=self)
        self.servers=ServersHub(self)
        self.log_cli_sessions=None
        self.wait_ticks=self.WAIT_TICKS
        self.to_save_output=output is not None
        self.output=output
        self.use_canned_session=False
        self.scripts=[]
        if self.to_save_output:
            self.script_name=script_name
            args={}
            for k, v in values:
                args[k]=cPickle.loads(v)
            self.session_can=SessionCan(self.script_name, args)
    
    def tick(self):
        logging.debug("Tick")
        while not self.script_call_queue.empty():
            try:
                f, args, kwargs=self.script_call_queue.get_nowait()
            except:
                break
            logging.debug("Calling delayed %s(*%s, **%s)"%(f, args, kwargs))
            apply(f, args, kwargs)
        if len(self.factory.sockets)==0:
            self.wait_ticks-=1
            if self.wait_ticks==0:
                logging.debug("EXIT")
                if self.to_save_output:
                    logging.debug("Writing session test to %s"%self.output)
                    self.session_can.dump(self.output)
                # Finally dump results
                for s in self.scripts:
                    if s.result:
                        # Format output
                        r=cPickle.loads(s.result)
                        if not isinstance(r, basestring):
                            r=pprint.pformat(r)
                        logging.debug("SCRIPT RESULT: %s\n%s"%(s.debug_name, r))
                os._exit(0)
            logging.debug("%d TICKS TO EXIT"%self.wait_ticks)
        else:
            self.wait_ticks=self.WAIT_TICKS
        
    def on_script_exit(self, script):
        if script.parent is None:
            self.servers.close()
        
    def run_script(self, _script_name, access_profile, callback, timeout=0, **kwargs):
        pv, pos, sn=_script_name.split(".", 2)
        profile=profile_registry["%s.%s"%(pv, pos)]()
        script=script_registry[_script_name](profile, self, access_profile, **kwargs)
        self.scripts+=[script]
        script.start()
    
    def request_call(self, f, *args, **kwargs):
        logging.debug("Requesting call: %s(*%s, **%s)"%(f, args, kwargs))
        self.script_call_queue.put((f, args, kwargs))
    
    def can_run_script(self):
        return True
    ##
    ## Handler to accept canned input
    ##
    def save_interaction(self, provider, cmd, data):
        self.session_can.save_interaction(provider, cmd, data)
    ##
    ## Handler to save final result
    ##
    def save_result(self, result, motd=""):
        self.session_can.save_result(result, motd)
    ##
    def save_snmp_get(self, oid, result):
        self.session_can.save_snmp_get(oid, result)
    ##
    def save_snmp_getnext(self, oid, result):
        self.session_can.save_snmp_getnext(oid, result)

##
## debug-script handler
##
class Command(BaseCommand):
    help="Debug SA Script"
    option_list=BaseCommand.option_list+(
        make_option("-c", "--read-community", dest="snmp_ro"),
        make_option("-o", "--output", dest="output"),
    )
    
    ##
    ## Gentle SIGINT handler
    ##
    def SIGINT(self, signo, frame):
        logging.info("SIGINT")
        os._exit(0)
    
    ##
    ## Print usage and exit
    ##
    def _usage(self):
        print "USAGE:"
        print "%s debug-script [-c <community>] [-o <output>] <script> <obj1> [ .. <objN>] [<key1>=<value1> [ .. <keyN>=<valueN>]]"%sys.argv[0]
        print "Where:"
        print "\t-c <community> - SNMP RO Community"
        print "\t-o <output>    - Canned beef output"
        return
    
    ##
    ## Create access profile from URL
    ##
    def set_access_profile_url(self, access_profile, obj, profile, snmp_ro_community):
        if profile is None:
            raise CommandError("Script name must contain profile when using URLs")
        url=URL(obj)
        access_profile.profile = profile
        access_profile.scheme  = Script.get_scheme_id(url.scheme)
        access_profile.address = url.host
        if url.port:
            access_profile.port = url.port
        access_profile.user = url.user
        if "\x00" in url.password: # Check the password really the pair of password/enable password
            p, s=url.password.split("\x00", 1)
            access_profile.password = p
            access_profile.super_password = s
        else:
            access_profile.password = url.password
        access_profile.path = url.path
        if snmp_ro_community:
            access_profile.snmp_ro = snmp_ro_community
    
    ##
    ## Create access profile from Database
    ##
    def set_access_profile_name(self, access_profile, obj, profile, snmp_ro_community):
        from noc.sa.models import ManagedObject
        from django.db.models import Q
        
        # Prepare query
        if is_int(obj):
            q=Q(id=int(obj))|Q(name=obj) # Integers can be object id or name
        else:
            q=Q(name=obj) # Search by name otherwise
        # Get object from database
        try:
            o=ManagedObject.objects.get(q)
        except ManagedObject.DoesNotExist:
            raise CommandError("Object not found: %s"%obj)
        # Fill access profile
        access_profile.profile = o.profile_name
        access_profile.scheme = o.scheme
        access_profile.address= o.address
        if o.port:
            access_profile.port = o.port
        access_profile.user = o.user
        access_profile.password = o.password
        if o.super_password:
            access_profile.super_password=o.super_password
        if snmp_ro_community:
            if snmp_ro_community!="-":
                access_profile.snmp_ro=snmp_ro_community
            elif o.snmp_ro:
                access_profile.snmp_ro=o.snmp_ro
        if o.remote_path:
            access_profile.path=o.remote_path
    
    ##
    ## Prepare script request
    ##
    def get_request(self, script, obj, snmp_ro_community, values):
        vendor=None
        os_name=None
        profile=None
        r=ScriptRequest()
        # Normalize script name
        if "." in script:
            vendor, os_name, script=script.split(".", 2)
            profile="%s.%s"%(vendor, os_name)
        # Fill access profile and script name
        if "://" in obj:
            # URL
            self.set_access_profile_url(r.access_profile, obj, profile, snmp_ro_community)
            r.script="%s.%s"%(profile, script)
        else:
            # Database name or id
            self.set_access_profile_name(r.access_profile, obj, profile, snmp_ro_community)
            if profile and r.access_profile.profile!=profile:
                raise CommandError("Profile mismatch for '%s'"%obj)
            r.script="%s.%s"%(r.access_profile.profile, script)
        ## Fill values
        for k, v in values:
            a=r.kwargs.add()
            a.key=k
            a.value=v
        return r
    
    ##
    def run_script(self, service, request):
        def handle_callback(controller, response=None, error=None):
            if error:
                logging.debug("Error: %s"%error.text)
            if response:
                logging.debug("Script completed")
                logging.debug(response.config)
        logging.debug("Running script thread")
        controller=Controller()
        controller.transaction=self.tf.begin()
        service.script(controller=controller, request=request, done=handle_callback)
    
    ##
    ## Handle command
    ##
    def handle(self, *args, **options):
        if len(args)<2:
            return self._usage()
        script_name=args[0]
        objects=[]
        values=[]
        # Parse args
        for a in args[1:]:
            if "=" in a:
                # key=value
                k, v=a.split("=", 1)
                v=cPickle.dumps(eval(v, {}, {}))
                values+=[(k, v)]
            else:
                # object
                objects+=[a]
        # Canned beef for only one object
        output=options.get("output", None)
        if output and len(objects)!=1:
            raise CommandError("Can write canned beef for one object only")
        # Get SNMP community
        snmp_ro_community=None
        if options["snmp_ro"]:
            snmp_ro_community=options["snmp_ro"]
        # Prepare requests
        requests=[self.get_request(script_name, obj, snmp_ro_community, values) for obj in objects]
        # Set up logging and signal handlers
        logging.root.setLevel(logging.DEBUG)
        signal.signal(signal.SIGINT, self.SIGINT)
        ## Prepare activator stub
        self.tf=TransactionFactory()
        service=Service()
        service.activator=ActivatorStub(requests[0].script if output else None, values, output)
        ## Run scripts
        for r in requests:
            print r
            t=threading.Thread(target=self.run_script, args=(service, r))
            t.start()
        # Finally give control to activator's factory
        service.activator.factory.run(run_forever=True)
    
