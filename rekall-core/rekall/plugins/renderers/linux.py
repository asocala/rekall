# Rekall Memory Forensics
# Copyright 2014 Google Inc. All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

"""This module implements renderers specific to Linux structures."""
from rekall.ui import json_renderer
from rekall.ui import text
from rekall.plugins.addrspaces import amd64


class kuid_t_TextObjectRenderer(text.TextObjectRenderer):
    renders_type = "kuid_t"
    renderers = ["TextRenderer", "TestRenderer", "WideTextRenderer"]

    def render_row(self, target, **_):
        return text.Cell(unicode(target))

class kgid_t_TextObjectRenderer(kuid_t_TextObjectRenderer):
    renders_type = "kgid_t"


class kuid_t_JsonObjectRenderer(json_renderer.JsonObjectRenderer):
    renders_type = ["kuid_t", "kgid_t"]
    renderers = ["JsonRenderer", "DataExportRenderer"]

    def EncodeToJsonSafe(self, task, **_):
        return task.val.v()


class XenM2PMapperObjectRenderer(json_renderer.JsonObjectRenderer):
    renders_type = "XenM2PMapper"

    def EncodeToJsonSafe(self, item, **_):
        result = {}
        result["m2p_map"] = dict(item)
        result["mro"] = ":".join(self.get_mro(item))

        return result

    def DecodeFromJsonSafe(self, value, _):
        return amd64.XenM2PMapper(value["m2p_map"])
