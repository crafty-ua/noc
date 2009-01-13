from django.shortcuts import get_object_or_404
from noc.lib.render import render
from noc.cm.models import Config
from noc.sa.models import script_registry
from django.http import HttpResponseForbidden,HttpResponseNotFound
from xmlrpclib import ServerProxy, Error
from noc.settings import config
import pprint,types

def object_scripts(request,object_id):
    o=get_object_or_404(Config,id=int(object_id))
    if not o.has_access(request.user):
        return HttpResponseForbidden("Access denied")
    p=o.profile_name
    lp=len(p)+1
    scripts=[(x[0],x[0][lp:]) for x in script_registry.choices if x[0].startswith(p+".")]
    return render(request,"sa/scripts.html",{"object":o,"scripts":scripts})

def object_script(request,object_id,script):
    def get_result(script,object_id,**kwargs):
        server=ServerProxy("http://%s:%d"%(config.get("xmlrpc","server"),config.getint("xmlrpc","port")))
        result=server.script(script,object_id,kwargs)
        if type(result) not in [types.StringType,types.UnicodeType]:
            result=pprint.pformat(result)
        return result
        
    o=get_object_or_404(Config,id=int(object_id))
    if not o.has_access(request.user):
        return HttpResponseForbidden("Access denied")
    try:
        scr=script_registry[script]
    except:
        return HttpResponseNotFound("No script found")
    form=None
    result=None
    if scr.implements and scr.implements[0].requires_input():
        if request.POST:
            form=scr.implements[0].get_form(request.POST)
            if form.is_valid():
                data={}
                for k,v in form.cleaned_data.items():
                    if v:
                        data[k]=v
                result=get_result(script,object_id,**data)
        else:
            form=scr.implements[0].get_form()
    else:
        result=get_result(script,object_id)
    return render(request,"sa/script.html",{"object":o,"result":result,"script":script,"form":form})
