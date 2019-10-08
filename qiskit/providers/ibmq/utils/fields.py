# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Custom fields for validation."""

from qiskit.validation import ModelTypeValidator


class Enum(ModelTypeValidator):
    """Field for enums."""

    default_error_messages = {
        'invalid': '"{input}" cannot be parsed as a {enum_cls}.',
        'format': '"{input}" cannot be formatted as a {enum_cls}.',
    }

    def __init__(self, enum_cls, *args, **kwargs):
        self.valid_types = (enum_cls,)
        self.valid_strs = [elem.value for elem in enum_cls]
        self.enum_cls = enum_cls

        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj):
        try:
            return value.value
        except AttributeError:
            self.fail('format', input=value, enum_cls=self.enum_cls)

    def _deserialize(self, value, attr, data):
        try:
            return self.enum_cls(value)
        except ValueError:
            self.fail('invalid', input=value, enum_cls=self.enum_cls)