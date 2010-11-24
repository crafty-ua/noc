# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Force10.FTOS.get_portchannel test
## Auto-generated by manage.py debug-script at 2010-11-24 23:03:11
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Force10_FTOS_get_portchannel_Test(ScriptTestCase):
    script="Force10.FTOS.get_portchannel"
    vendor="Force10"
    platform='C300'
    version='8.3.1.1'
    input={}
    result=[{'interface': 'Po 1', 'members': ['Te 6/0', 'Te 7/0'], 'type': 'L'},
 {'interface': 'Po 2',
  'members': ['Gi 2/36', 'Gi 2/37', 'Gi 2/40', 'Gi 2/41'],
  'type': 'L'},
 {'interface': 'Po 3',
  'members': ['Gi 2/38', 'Gi 2/39', 'Gi 2/42', 'Gi 2/43'],
  'type': 'L'}]
    motd=' \n'
    cli={
## 'show interface port-channel brief'
'show interface port-channel brief': """show interface port-channel brief
Codes: L - LACP Port-channel


    LAG Mode  Status       Uptime      Ports          
L   1   L2L3  up           8w1d13h     Te 6/0     (Up)
                                       Te 7/0     (Up)
L   2   L2L3  up           28w6d10h    Gi 2/36    (Up)
                                       Gi 2/37    (Up)
                                       Gi 2/40    (Up)
                                       Gi 2/41    (Up)
L   3   L2L3  up           28w6d10h    Gi 2/38    (Up)
                                       Gi 2/39    (Up)
                                       Gi 2/42    (Up)
                                       Gi 2/43    (Up)
L   4   L2L3  down         00:00:00    """,
'terminal length 0':  'terminal length 0\n',
}
    snmp_get={}
    snmp_getnext={}
