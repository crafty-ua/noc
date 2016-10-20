# -*- coding: utf-8 -*-
"""
##----------------------------------------------------------------------
## Link's dynamic dashboard
##----------------------------------------------------------------------
## Copyright (C) 2007-2016 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""

import string
# NOC modules
from base import BaseDashboard
from noc.inv.models.interface import Interface
from noc.inv.models.link import Link
from jinja2 import Environment, FileSystemLoader
import json


class LinkDashboard(BaseDashboard):
    name = "link"

    def resolve_object(self, object):
        try:
            return Link.objects.get(id=object)
        except Link.DoesNotExist:
            raise self.NotFound()

    def render(self):
        mos = self.object
        context = {
            "device_a": mos.managed_objects[0].name,
            "device_b": mos.managed_objects[1].name,
            "interface_a": {
                "name": mos.interfaces[0].name,
                "descr": mos.interfaces[0].description or mos.interfaces[0].name},
            "interface_b": {
                "name": mos.interfaces[1].name,
                "descr": mos.interfaces[0].description or mos.interfaces[1].name},
            "segment": mos.managed_objects[0].segment.id,
            "device_a_id": mos.managed_objects[0].id,
            "device_b_id": mos.managed_objects[0].id,
        }
        self.logger.info("Context with data: %s" % context)
        PM_TEMPLATE_PATH = "templates/ddash/"
        j2_env = Environment(loader=FileSystemLoader(PM_TEMPLATE_PATH))
        tmpl = j2_env.get_template("dash_link.j2")
        data = tmpl.render(context)

        render = json.loads(data)
        return render