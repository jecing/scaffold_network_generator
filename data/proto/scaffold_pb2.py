# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scaffold.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scaffold.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0escaffold.proto\"\x1a\n\x06LsAtom\x12\x10\n\x08idx_atom\x18\x01 \x03(\x05\"9\n\x0c\x44icMolLsatom\x12\x0f\n\x07idx_mol\x18\x01 \x01(\x05\x12\x18\n\x07ls_atom\x18\x02 \x01(\x0b\x32\x07.LsAtom\"6\n\x0eLsDicmollsatom\x12$\n\rdic_mol_atoms\x18\x01 \x03(\x0b\x32\r.DicMolLsatom\"\x8b\x01\n\rDicScaffoldLs\x12\x35\n\x0cidx_scaffold\x18\x08 \x03(\x0b\x32\x1f.DicScaffoldLs.IdxScaffoldEntry\x1a\x43\n\x10IdxScaffoldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.LsDicmollsatom:\x02\x38\x01\x62\x06proto3')
)




_LSATOM = _descriptor.Descriptor(
  name='LsAtom',
  full_name='LsAtom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_atom', full_name='LsAtom.idx_atom', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=44,
)


_DICMOLLSATOM = _descriptor.Descriptor(
  name='DicMolLsatom',
  full_name='DicMolLsatom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_mol', full_name='DicMolLsatom.idx_mol', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ls_atom', full_name='DicMolLsatom.ls_atom', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=103,
)


_LSDICMOLLSATOM = _descriptor.Descriptor(
  name='LsDicmollsatom',
  full_name='LsDicmollsatom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dic_mol_atoms', full_name='LsDicmollsatom.dic_mol_atoms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=159,
)


_DICSCAFFOLDLS_IDXSCAFFOLDENTRY = _descriptor.Descriptor(
  name='IdxScaffoldEntry',
  full_name='DicScaffoldLs.IdxScaffoldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DicScaffoldLs.IdxScaffoldEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DicScaffoldLs.IdxScaffoldEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=301,
)

_DICSCAFFOLDLS = _descriptor.Descriptor(
  name='DicScaffoldLs',
  full_name='DicScaffoldLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx_scaffold', full_name='DicScaffoldLs.idx_scaffold', index=0,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DICSCAFFOLDLS_IDXSCAFFOLDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=301,
)

_DICMOLLSATOM.fields_by_name['ls_atom'].message_type = _LSATOM
_LSDICMOLLSATOM.fields_by_name['dic_mol_atoms'].message_type = _DICMOLLSATOM
_DICSCAFFOLDLS_IDXSCAFFOLDENTRY.fields_by_name['value'].message_type = _LSDICMOLLSATOM
_DICSCAFFOLDLS_IDXSCAFFOLDENTRY.containing_type = _DICSCAFFOLDLS
_DICSCAFFOLDLS.fields_by_name['idx_scaffold'].message_type = _DICSCAFFOLDLS_IDXSCAFFOLDENTRY
DESCRIPTOR.message_types_by_name['LsAtom'] = _LSATOM
DESCRIPTOR.message_types_by_name['DicMolLsatom'] = _DICMOLLSATOM
DESCRIPTOR.message_types_by_name['LsDicmollsatom'] = _LSDICMOLLSATOM
DESCRIPTOR.message_types_by_name['DicScaffoldLs'] = _DICSCAFFOLDLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LsAtom = _reflection.GeneratedProtocolMessageType('LsAtom', (_message.Message,), dict(
  DESCRIPTOR = _LSATOM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:LsAtom)
  ))
_sym_db.RegisterMessage(LsAtom)

DicMolLsatom = _reflection.GeneratedProtocolMessageType('DicMolLsatom', (_message.Message,), dict(
  DESCRIPTOR = _DICMOLLSATOM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:DicMolLsatom)
  ))
_sym_db.RegisterMessage(DicMolLsatom)

LsDicmollsatom = _reflection.GeneratedProtocolMessageType('LsDicmollsatom', (_message.Message,), dict(
  DESCRIPTOR = _LSDICMOLLSATOM,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:LsDicmollsatom)
  ))
_sym_db.RegisterMessage(LsDicmollsatom)

DicScaffoldLs = _reflection.GeneratedProtocolMessageType('DicScaffoldLs', (_message.Message,), dict(

  IdxScaffoldEntry = _reflection.GeneratedProtocolMessageType('IdxScaffoldEntry', (_message.Message,), dict(
    DESCRIPTOR = _DICSCAFFOLDLS_IDXSCAFFOLDENTRY,
    __module__ = 'scaffold_pb2'
    # @@protoc_insertion_point(class_scope:DicScaffoldLs.IdxScaffoldEntry)
    ))
  ,
  DESCRIPTOR = _DICSCAFFOLDLS,
  __module__ = 'scaffold_pb2'
  # @@protoc_insertion_point(class_scope:DicScaffoldLs)
  ))
_sym_db.RegisterMessage(DicScaffoldLs)
_sym_db.RegisterMessage(DicScaffoldLs.IdxScaffoldEntry)


_DICSCAFFOLDLS_IDXSCAFFOLDENTRY._options = None
# @@protoc_insertion_point(module_scope)
