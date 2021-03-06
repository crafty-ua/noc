# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# PhoneRangeProfile model
# ---------------------------------------------------------------------
# Copyright (C) 2007-2016 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from threading import Lock
import operator
# Third-party modules
from mongoengine.document import Document
from mongoengine.fields import StringField, IntField
import cachetools
# NOC modules
from noc.main.models.style import Style
from noc.lib.nosql import ForeignKeyField
from noc.core.model.decorator import on_delete_check

id_lock = Lock()


@on_delete_check(check=[
    ("phone.PhoneRange", "profile")
])
class PhoneRangeProfile(Document):
    meta = {
        "collection": "noc.phonerangeprofiles",
        "strict": False,
        "auto_create_index": False
    }

    name = StringField(unique=True)
    description = StringField()
    # Cooldown time in days
    # Time when number will be automatically transferred from C to F state
    cooldown = IntField(default=30)
    style = ForeignKeyField(Style)

    _id_cache = cachetools.TTLCache(100, ttl=60)

    def __unicode__(self):
        return self.name

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_id_cache"),
                             lock=lambda _: id_lock)
    def get_by_id(cls, id):
        return PhoneRangeProfile.objects.filter(id=id).first()
