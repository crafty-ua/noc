# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## ZyXEL.ZyNOS_EE highlight lexers
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class ConfigLexer(RegexLexer):
    name = "Zyxel.ZyNOS_EE"
    tokens = {"root": [
            (r"\"", String.Double, "string"),
            (r"(name)(.*?)$", bygroups(Keyword, Comment)),
            (r"^(interface\s+\S+|vlan\s+)(.*?)$",
                bygroups(Keyword, Name.Attribute)),
            (r"^(?:no\s+)?\S+", Keyword),
            (r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/\d{1,2})?",
                Number),  # IPv4 Address/Prefix
            (r"\d+", Number),
            (r".", Text),
        ],
        "string": [
            (r".*\"", String.Double, "#pop"),
        ]
    }
