# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# kb.KBEntryAttachment tests
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
# NOC modules
from .base import BaseModelTest
from noc.kb.models.kbentryattachment import KBEntryAttachment


class TestTestKbKBEntryAttachment(BaseModelTest):
    model = KBEntryAttachment
