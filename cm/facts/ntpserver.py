# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## NTP server host
##----------------------------------------------------------------------
## Copyright (C) 2007-2015 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from base import BaseFact


class NTPServer(BaseFact):
    ATTRS = ["ip"]

    def __init__(self, ip=None):
        self.ip = ip

    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, value):
        self._ip = value or None
