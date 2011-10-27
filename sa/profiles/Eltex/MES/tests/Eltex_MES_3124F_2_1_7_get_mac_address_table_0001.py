# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Eltex.MES.get_mac_address_table test
## Auto-generated by ./noc debug-script at 2011-10-21 16:24:12
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Eltex_MES_get_mac_address_table_Test(ScriptTestCase):
    script = "Eltex.MES.get_mac_address_table"
    vendor = "Eltex"
    platform = 'MES3124F'
    version = '2.1.7'
    input = {}
    result = [{'interfaces': ['Te 0/1'],
  'mac': '00:22:B0:14:6F:00',
  'type': 'D',
  'vlan_id': 1},
 {'interfaces': ['Gi 0/2'],
  'mac': 'E0:CB:4E:F8:90:B4',
  'type': 'D',
  'vlan_id': 1},
 {'interfaces': ['Te 0/1'],
  'mac': '00:04:61:75:B0:83',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:04:61:7B:C4:FD',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:04:61:A2:9C:E7',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:04:76:A1:A2:5D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:0D:61:0F:C9:60',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:0F:EA:54:35:39',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:11:5B:BD:55:32',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:11:5B:F1:A4:D9',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:13:20:E3:C6:88',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:13:77:F9:56:A8',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:13:D3:13:9B:E3',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:13:D3:A9:E1:C7',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:13:D4:13:89:8B',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:15:58:B9:85:18',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:16:76:D4:0E:B1',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:17:31:A9:37:05',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:18:F3:0F:D0:D2',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:19:17:50:B6:DA',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:19:17:50:B6:EB',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:19:5B:E9:AD:8C',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:19:66:EF:3F:27',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:19:66:EF:9E:54',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:19:7E:CB:FA:71',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1A:4D:35:CB:0F',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1A:4D:55:8E:B2',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1A:4D:91:FC:66',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:1A:92:2E:BD:BA',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1A:92:E8:E6:C0',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1B:21:3B:4D:E6',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1B:24:D0:8E:A9',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1B:B9:9D:60:5C',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:1B:FC:35:37:92',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:1B:FC:4A:CE:FB',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:1D:60:45:20:DE',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1D:60:5B:8D:56',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1D:7D:A0:A3:E8',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1E:68:81:D3:FB',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1E:8C:15:01:08',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1E:8C:1D:C4:2F',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:1E:8C:67:92:CD',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1F:C6:10:E3:00',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1F:C6:42:84:F2',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1F:C6:B4:C2:DF',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:1F:D0:89:28:B8',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:85:1D:E0:9E',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:20:E2:0A',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:21:91:3A:63:D5',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:42:27:03',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:44:AD:7B',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:F4:88:EE',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:22:15:44:30:5C',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:22:B0:F4:5A:E4',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/1'],
  'mac': '00:23:5A:8B:E2:B6',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:24:1D:82:BB:0F',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:24:1D:D9:59:57',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:24:1D:DE:14:BA',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:24:54:E8:CA:F9',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:24:8C:C8:C1:EC',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:25:22:30:B3:9E',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:25:22:33:99:4F',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:25:22:53:F4:86',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:26:18:79:12:74',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:26:18:9D:35:1E',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:26:18:E0:34:50',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:26:22:59:3F:C9',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:26:9E:1B:1F:15',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/1'],
  'mac': '00:26:9E:99:B5:50',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:30:16:04:2F:CC',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:30:16:04:31:3D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:50:8D:7E:AF:51',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:80:48:1F:46:51',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:80:C8:3C:E5:2A',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:90:F5:64:54:F1',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '00:E0:42:FD:04:2D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:4C:46:64:FB',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:E0:4C:51:AF:92',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:4C:A0:DB:E9',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:50:33:05:6E',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:50:5D:07:CA',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:52:96:31:E9',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:52:A2:30:49',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:52:A6:92:2C',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:52:A7:AF:80',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '00:E0:52:A8:C1:6F',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:E0:52:AF:23:90',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '14:D6:4D:83:A7:5D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:6F:65:41:ED:72',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:6F:65:D8:52:21',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:AF:F7:2D:22:3E',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:AF:F7:43:9C:9B',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:AF:F7:A3:07:0D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:BD:B9:29:F2:ED',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:BD:B9:29:F3:A7',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '1C:BD:B9:BF:89:7D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '20:CF:30:19:B7:BA',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '20:CF:30:87:E1:3D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '20:CF:30:C2:E0:04',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '34:08:04:BB:C7:51',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '34:08:04:D2:D1:67',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '44:87:FC:80:AD:FE',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/2'],
  'mac': '44:87:FC:82:5C:40',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '4C:00:10:27:1C:C2',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Gi 0/3'],
  'mac': '54:42:49:FD:19:E4',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '5C:D9:98:1B:BA:0B',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '5C:D9:98:2D:EA:DD',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '6C:F0:49:77:98:6D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '70:71:BC:50:8B:71',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '70:71:BC:BB:E3:08',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '88:AE:1D:63:01:5D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '8C:89:A5:11:AD:A6',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '94:0C:6D:FA:78:D1',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': 'E0:CB:4E:E7:CF:E8',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': 'E0:CB:4E:E7:D0:5D',
  'type': 'D',
  'vlan_id': 53},
 {'interfaces': ['Te 0/1'],
  'mac': '00:1B:21:1C:03:41',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:39:A9:5C',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:49:28',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:44',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:4C',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:7A',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:8C',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:8E',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:9A',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4B:B8',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4D:6C',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:4D:8E',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:52:94',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:52:AA',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:52:B8',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:6A:EA',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:6A:EE',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:6A:F6',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3B:6C:88',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3F:A9:EA',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:3F:AB:6E',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:40:38:D8',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:40:51:EC',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:42:63:8C',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:42:70:26',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:42:70:38',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:42:70:44',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:42:70:46',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:21:91:C7:D5:D0',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:22:B0:BC:5E:09',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:26:5A:AB:A3:A2',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': '00:A0:C5:FB:53:CA',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Gi 0/3'],
  'mac': '1C:BD:B9:52:E0:80',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Gi 0/1'],
  'mac': '1C:BD:B9:53:03:20',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Gi 0/2'],
  'mac': '1C:BD:B9:54:77:E0',
  'type': 'D',
  'vlan_id': 111},
 {'interfaces': ['Te 0/1'],
  'mac': 'F0:7D:68:97:3F:CC',
  'type': 'D',
  'vlan_id': 111}]
    motd = '*****\n\n'
    cli = {
'terminal datadump':  'terminal datadump\n', 
## 'show mac address-table'
'show mac address-table': """show mac address-table
Aging time is 630 sec

  Vlan        Mac Address         Port       Type    
-------- --------------------- ---------- ---------- 
   1       00:22:b0:14:6f:00     te0/1     dynamic   
   1       a8:f9:4b:80:b4:c0       0         self    
   1       e0:cb:4e:f8:90:b4     gi0/2     dynamic   
   53      00:04:61:75:b0:83     te0/1     dynamic   
   53      00:04:61:7b:c4:fd     gi0/2     dynamic   
   53      00:04:61:a2:9c:e7     te0/1     dynamic   
   53      00:04:76:a1:a2:5d     te0/1     dynamic   
   53      00:0d:61:0f:c9:60     gi0/2     dynamic   
   53      00:0f:ea:54:35:39     te0/1     dynamic   
   53      00:11:5b:bd:55:32     te0/1     dynamic   
   53      00:11:5b:f1:a4:d9     te0/1     dynamic   
   53      00:13:20:e3:c6:88     te0/1     dynamic   
   53      00:13:77:f9:56:a8     te0/1     dynamic   
   53      00:13:d3:13:9b:e3     te0/1     dynamic   
   53      00:13:d3:a9:e1:c7     gi0/3     dynamic   
   53      00:13:d4:13:89:8b     te0/1     dynamic   
   53      00:15:58:b9:85:18     gi0/3     dynamic   
   53      00:16:76:d4:0e:b1     te0/1     dynamic   
   53      00:17:31:a9:37:05     te0/1     dynamic   
   53      00:18:f3:0f:d0:d2     te0/1     dynamic   
   53      00:19:17:50:b6:da     te0/1     dynamic   
   53      00:19:17:50:b6:eb     te0/1     dynamic   
   53      00:19:5b:e9:ad:8c     te0/1     dynamic   
   53      00:19:66:ef:3f:27     te0/1     dynamic   
   53      00:19:66:ef:9e:54     gi0/3     dynamic   
   53      00:19:7e:cb:fa:71     te0/1     dynamic   
   53      00:1a:4d:35:cb:0f     te0/1     dynamic   
   53      00:1a:4d:55:8e:b2     te0/1     dynamic   
   53      00:1a:4d:91:fc:66     te0/1     dynamic   
   53      00:1a:92:2e:bd:ba     gi0/2     dynamic   
   53      00:1a:92:e8:e6:c0     te0/1     dynamic   
   53      00:1b:21:3b:4d:e6     te0/1     dynamic   
   53      00:1b:24:d0:8e:a9     te0/1     dynamic   
   53      00:1b:b9:9d:60:5c     te0/1     dynamic   
   53      00:1b:fc:35:37:92     gi0/2     dynamic   
   53      00:1b:fc:4a:ce:fb     gi0/2     dynamic   
   53      00:1d:60:45:20:de     gi0/3     dynamic   
   53      00:1d:60:5b:8d:56     te0/1     dynamic   
   53      00:1d:7d:a0:a3:e8     te0/1     dynamic   
   53      00:1e:68:81:d3:fb     te0/1     dynamic   
   53      00:1e:8c:15:01:08     te0/1     dynamic   
   53      00:1e:8c:1d:c4:2f     te0/1     dynamic   
   53      00:1e:8c:67:92:cd     gi0/3     dynamic   
   53      00:1f:c6:10:e3:00     te0/1     dynamic   
   53      00:1f:c6:42:84:f2     te0/1     dynamic   
   53      00:1f:c6:b4:c2:df     te0/1     dynamic   
   53      00:1f:d0:89:28:b8     gi0/2     dynamic   
   53      00:21:85:1d:e0:9e     te0/1     dynamic   
   53      00:21:91:20:e2:0a     te0/1     dynamic   
   53      00:21:91:3a:63:d5     gi0/2     dynamic   
   53      00:21:91:42:27:03     te0/1     dynamic   
   53      00:21:91:44:ad:7b     te0/1     dynamic   
   53      00:21:91:f4:88:ee     te0/1     dynamic   
   53      00:22:15:44:30:5c     te0/1     dynamic   
   53      00:22:b0:f4:5a:e4     te0/1     dynamic   
   53      00:23:5a:8b:e2:b6     gi0/1     dynamic   
   53      00:24:1d:82:bb:0f     gi0/2     dynamic   
   53      00:24:1d:d9:59:57     te0/1     dynamic   
   53      00:24:1d:de:14:ba     te0/1     dynamic   
   53      00:24:54:e8:ca:f9     te0/1     dynamic   
   53      00:24:8c:c8:c1:ec     te0/1     dynamic   
   53      00:25:22:30:b3:9e     te0/1     dynamic   
   53      00:25:22:33:99:4f     te0/1     dynamic   
   53      00:25:22:53:f4:86     te0/1     dynamic   
   53      00:26:18:79:12:74     gi0/2     dynamic   
   53      00:26:18:9d:35:1e     te0/1     dynamic   
   53      00:26:18:e0:34:50     gi0/2     dynamic   
   53      00:26:22:59:3f:c9     te0/1     dynamic   
   53      00:26:9e:1b:1f:15     te0/1     dynamic   
   53      00:26:9e:99:b5:50     gi0/1     dynamic   
   53      00:30:16:04:2f:cc     te0/1     dynamic   
   53      00:30:16:04:31:3d     te0/1     dynamic   
   53      00:50:8d:7e:af:51     te0/1     dynamic   
   53      00:80:48:1f:46:51     te0/1     dynamic   
   53      00:80:c8:3c:e5:2a     te0/1     dynamic   
   53      00:90:f5:64:54:f1     te0/1     dynamic   
   53      00:e0:42:fd:04:2d     gi0/2     dynamic   
   53      00:e0:4c:46:64:fb     te0/1     dynamic   
   53      00:e0:4c:51:af:92     gi0/3     dynamic   
   53      00:e0:4c:a0:db:e9     te0/1     dynamic   
   53      00:e0:50:33:05:6e     te0/1     dynamic   
   53      00:e0:50:5d:07:ca     te0/1     dynamic   
   53      00:e0:52:96:31:e9     te0/1     dynamic   
   53      00:e0:52:a2:30:49     te0/1     dynamic   
   53      00:e0:52:a6:92:2c     te0/1     dynamic   
   53      00:e0:52:a7:af:80     te0/1     dynamic   
   53      00:e0:52:a8:c1:6f     gi0/3     dynamic   
   53      00:e0:52:af:23:90     te0/1     dynamic   
   53      14:d6:4d:83:a7:5d     te0/1     dynamic   
   53      1c:6f:65:41:ed:72     te0/1     dynamic   
   53      1c:6f:65:d8:52:21     te0/1     dynamic   
   53      1c:af:f7:2d:22:3e     te0/1     dynamic   
   53      1c:af:f7:43:9c:9b     te0/1     dynamic   
   53      1c:af:f7:a3:07:0d     te0/1     dynamic   
   53      1c:bd:b9:29:f2:ed     te0/1     dynamic   
   53      1c:bd:b9:29:f3:a7     te0/1     dynamic   
   53      1c:bd:b9:bf:89:7d     te0/1     dynamic   
   53      20:cf:30:19:b7:ba     te0/1     dynamic   
   53      20:cf:30:87:e1:3d     te0/1     dynamic   
   53      20:cf:30:c2:e0:04     te0/1     dynamic   
   53      34:08:04:bb:c7:51     te0/1     dynamic   
   53      34:08:04:d2:d1:67     gi0/3     dynamic   
   53      44:87:fc:80:ad:fe     te0/1     dynamic   
   53      44:87:fc:82:5c:40     gi0/2     dynamic   
   53      4c:00:10:27:1c:c2     te0/1     dynamic   
   53      54:42:49:fd:19:e4     gi0/3     dynamic   
   53      5c:d9:98:1b:ba:0b     te0/1     dynamic   
   53      5c:d9:98:2d:ea:dd     te0/1     dynamic   
   53      6c:f0:49:77:98:6d     te0/1     dynamic   
   53      70:71:bc:50:8b:71     te0/1     dynamic   
   53      70:71:bc:bb:e3:08     te0/1     dynamic   
   53      88:ae:1d:63:01:5d     te0/1     dynamic   
   53      8c:89:a5:11:ad:a6     te0/1     dynamic   
   53      94:0c:6d:fa:78:d1     te0/1     dynamic   
   53      e0:cb:4e:e7:cf:e8     te0/1     dynamic   
   53      e0:cb:4e:e7:d0:5d     te0/1     dynamic   
  111      00:1b:21:1c:03:41     te0/1     dynamic   
  111      00:21:91:39:a9:5c     te0/1     dynamic   
  111      00:21:91:3b:49:28     te0/1     dynamic   
  111      00:21:91:3b:4b:44     te0/1     dynamic   
  111      00:21:91:3b:4b:4c     te0/1     dynamic   
  111      00:21:91:3b:4b:7a     te0/1     dynamic   
  111      00:21:91:3b:4b:8c     te0/1     dynamic   
  111      00:21:91:3b:4b:8e     te0/1     dynamic   
  111      00:21:91:3b:4b:9a     te0/1     dynamic   
  111      00:21:91:3b:4b:b8     te0/1     dynamic   
  111      00:21:91:3b:4d:6c     te0/1     dynamic   
  111      00:21:91:3b:4d:8e     te0/1     dynamic   
  111      00:21:91:3b:52:94     te0/1     dynamic   
  111      00:21:91:3b:52:aa     te0/1     dynamic   
  111      00:21:91:3b:52:b8     te0/1     dynamic   
  111      00:21:91:3b:6a:ea     te0/1     dynamic   
  111      00:21:91:3b:6a:ee     te0/1     dynamic   
  111      00:21:91:3b:6a:f6     te0/1     dynamic   
  111      00:21:91:3b:6c:88     te0/1     dynamic   
  111      00:21:91:3f:a9:ea     te0/1     dynamic   
  111      00:21:91:3f:ab:6e     te0/1     dynamic   
  111      00:21:91:40:38:d8     te0/1     dynamic   
  111      00:21:91:40:51:ec     te0/1     dynamic   
  111      00:21:91:42:63:8c     te0/1     dynamic   
  111      00:21:91:42:70:26     te0/1     dynamic   
  111      00:21:91:42:70:38     te0/1     dynamic   
  111      00:21:91:42:70:44     te0/1     dynamic   
  111      00:21:91:42:70:46     te0/1     dynamic   
  111      00:21:91:c7:d5:d0     te0/1     dynamic   
  111      00:22:b0:bc:5e:09     te0/1     dynamic   
  111      00:26:5a:ab:a3:a2     te0/1     dynamic   
  111      00:a0:c5:fb:53:ca     te0/1     dynamic   
  111      1c:bd:b9:52:e0:80     gi0/3     dynamic   
  111      1c:bd:b9:53:03:20     gi0/1     dynamic   
  111      1c:bd:b9:54:77:e0     gi0/2     dynamic   
  111      f0:7d:68:97:3f:cc     te0/1     dynamic   
""", 
}
    snmp_get = {}
    snmp_getnext = {}
