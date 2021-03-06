# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Eltex.MES.get_vlans
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetvlans import IGetVlans


class Script(BaseScript):
    name = "Eltex.MES.get_vlans"
    interface = IGetVlans

    rx_vlan = re.compile(
        r"^\s*(?P<vlan_id>\d+)\s+(?P<name>.+?)\s+(\S+|)\s+\S+\s+\S+\s*$",
        re.MULTILINE)

    def execute_snmp(self, **kwargs):
        r = []
        for vlan, name in self.snmp.join_tables(
            "1.3.6.1.2.1.17.7.1.4.2.1.3",
            "1.3.6.1.2.1.17.7.1.4.3.1.1"
        ):
            r += [{"vlan_id": vlan, "name": name}]
        return r

    def execute_cli(self, **kwargs):
        r = []
        for match in self.rx_vlan.finditer(self.cli("show vlan")):
            if match.group("name") != "-":
                r += [match.groupdict()]
            else:
                r += [{"vlan_id": int(match.group("vlan_id"))}]
        return r
