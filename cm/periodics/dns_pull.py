# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
import noc.lib.periodic

class Task(noc.lib.periodic.Task):
    name="cm.dns_pull"
    description=""
    wait_for=["cm.dns_push"]
    def execute(self):
        from noc.cm.models import DNS
        DNS.global_pull()
        return True
        
