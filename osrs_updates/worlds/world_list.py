# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import array
import struct
import zlib
from enum import Enum
from pkg_resources import parse_version

from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class WorldList(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.ignored = self._io.read_u4be()
        self.world_count = self._io.read_u2be()
        self.worlds = [None] * (self.world_count)
        for i in range(self.world_count):
            self.worlds[i] = self._root.World(self._io, self, self._root)


    class World(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.id = self._io.read_u2be()
            self.mask = self._io.read_s4be()
            self.address = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.activity = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self.location = self._io.read_u1()
            self.player_count = self._io.read_u2be()



