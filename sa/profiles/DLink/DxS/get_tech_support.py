# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# DLink.DxS.get_tech_support
# ---------------------------------------------------------------------
# Copyright (C) 2007-2016 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
import re
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igettechsupport import IGetTechSupport


class Script(BaseScript):
    name = "DLink.DxS.get_tech_support"
    interface = IGetTechSupport

    def execute(self):
        try:
            c = self.cli("show tech_support")
        except self.CLISyntaxError:
            raise self.NotSupportedError()
        return unicode(c, "utf8", "ignore").encode("utf8")
