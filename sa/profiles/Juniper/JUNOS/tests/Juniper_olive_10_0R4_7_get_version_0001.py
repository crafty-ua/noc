# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Juniper.JUNOS.get_version test
## Auto-generated by ./noc debug-script at 2011-07-22 07:11:14
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Juniper_JUNOS_get_version_Test(ScriptTestCase):
    script = "Juniper.JUNOS.get_version"
    vendor = "Juniper"
    platform = 'olive'
    version = '10.0R4.7'
    input = {}
    result = {'platform': 'olive', 'vendor': 'Juniper', 'version': '10.0R4.7'}
    motd = '--- JUNOS 10.0R4.7 built 2010-08-22 03:07:19 UTC\n'
    cli = {
'set cli screen-length 0':  ' set cli screen-length 0 \nScreen length set to 0\n\n', 
## 'show version'
'show version': """ show version 
Hostname: r2
Model: olive
JUNOS Base OS boot [10.0R4.7]
JUNOS Base OS Software Suite [10.0R4.7]
JUNOS Kernel Software Suite [10.0R4.7]
JUNOS Crypto Software Suite [10.0R4.7]
JUNOS Online Documentation [10.0R4.7]
JUNOS Voice Services Container package [10.0R4.7]
JUNOS Border Gateway Function package [10.0R4.7]
JUNOS Services AACL Container package [10.0R4.7]
JUNOS Services LL-PDF Container package [10.0R4.7]
JUNOS Services Stateful Firewall [10.0R4.7]
JUNOS AppId Services [10.0R4.7]
JUNOS IDP Services [10.0R4.7]
JUNOS Routing Software Suite [10.0R4.7]
""", 
}
    snmp_get = {}
    snmp_getnext = {}
