# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Alcatel.AOS.get_interface_status
##----------------------------------------------------------------------
## Copyright (C) 2007-2013 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
from noc.sa.script import Script as NOCScript
from noc.sa.interfaces import IGetInterfaceStatus
import re


class Script(NOCScript):
    name = "Alcatel.AOS.get_interface_status"
    implements = [IGetInterfaceStatus]
    rx_line = re.compile(
        r"(?P<interface>\S+)\s+\S+\s+(?P<status>up|down)\s+\S+\d*\s+\d*",
        re.IGNORECASE | re.MULTILINE)

    def execute(self, interface=None):
        # Not tested. Must be identical in different vendors
        if self.snmp and self.access_profile.snmp_ro:
            try:
                # Get interface status
                r = []
                # IF-MIB::ifName, IF-MIB::ifOperStatus
                for n, s in self.snmp.join_tables("1.3.6.1.2.1.31.1.1.1.1",
                                                  "1.3.6.1.2.1.2.2.1.8",
                                                  bulk=True):
                    r += [{"interface":n, "status":int(s) == 1}]
                return r
            except self.snmp.TimeOutError:
                pass
        r = []
        for match in self.rx_line.finditer(self.cli("show interfaces port")):
            r += [{
                "interface": match.group("interface"),
                "status": match.group("status").lower() == "up"
                }]
        return r
