# python
from typing import Union, List
from functools import lru_cache
# 3rd-party
from ifcopenshell.entity_instance import entity_instance
from ifcopenshell.file import file
# framework
from .util import _entity_to_list
from .type_conv import ifc_single_value_to_python, python_to_ifc_single_value, _recognize_value_type


class PropertySet():
    _STAGE = ['init', 'writable', 'freeze']
    _state = _STAGE.index('init')
    _protected_keys = []
    property_names = []
    descriptions = {}

    def __init__(
        self,
        ifc: file,
        entity: entity_instance,
        access: str = 'HasProperties'
    ):
        self.ifc = ifc
        self.entity = entity
        self.access = access

        self._protected_keys = [k for k in vars(
            self).keys()] + [k for k in vars(type(self)).keys()]

        self.parse()

        self._state = self._STAGE.index('writable')

    def __repr__(
        self
    ):
        return repr(self.entity.wrapped_data)

    def __getattr__(
        self,
        key
    ):
        raise AttributeError("{0} property is not in {1}. {2}".format(
            key, self, self.property_names))

    def __setattr__(
        self,
        key,
        value
    ):
        self.write_property(key, value)

    def _get_props(
        self
    ):
        if type(self.entity.__getattr__(self.access)) is entity_instance:
            return [self.entity.__getattr__(self.access)]
        else:
            return self.entity.__getattr__(self.access)

    def _parse_property_names(
        self
    ):
        if self.entity.__getattr__(self.access) is None:
            self.property_names = []
        else:
            self.property_names = [prop.Name for prop in self._get_props()]
            self.descriptions = {
                prop.Name: prop.Description for prop in self._get_props() if hasattr(prop, 'Description')}

    def _parse_property_values(
        self
    ):
        if self.entity.__getattr__(self.access) is None:
            return
        for prop in self._get_props():
            if prop.NominalValue is not None:
                value_type = prop.NominalValue.get_info()['type']
                wrapped_value = prop.NominalValue.wrappedValue
                value = ifc_single_value_to_python(value_type, wrapped_value)
            else:
                value = None
            self.__setattr__(prop.Name, value)

    @property
    def Name(self):
        return self.entity.Name

    def parse(
        self
    ):
        self._parse_property_names()
        self._parse_property_values()

    def write_property(
        self,
        name: str,
        value,
        description: str = None
    ):
        if self._state == self._STAGE.index('writable') and name not in self._protected_keys:
            if self.has_property(name):
                if description is None:
                    description = self.get_entity(name).Description
                self.modify_entity(name, value, description)
            else:
                self.make_entity(name, value, description)
                self._parse_property_names()
        super().__setattr__(name, value)

    def get_values(
        self
    ):
        return {pname: self.__getattribute__(pname) for pname in self.property_names}

    def get_descriptions(
        self
    ):
        return {pname: self.descriptions[pname] if pname in self.descriptions.keys() else None for pname in self.property_names}

    def get_description(
        self,
        name: str
    ):
        return self.descriptions[name]

    def get_value(
        self,
        name: str
    ):
        return self.__getattribute__(name)

    def get_properties(
        self
    ):
        return {pname: {
            'value': self.__getattribute__(pname),
            'descriptions': self.descriptions[pname] if pname in self.descriptions.keys() else None
        }
            for pname in self.property_names}

    def has_property(
        self,
        key: str
    ) -> bool:
        return key in self.property_names

    def get_entity(
        self,
        key: str
    ) -> entity_instance:
        if self.has_property(key):
            return [prop for prop in self._get_props() if prop.Name == key][0]
        raise AttributeError("{0} property is not in {1}. {2}".format(
            key, self, self.property_names))

    def make_entity(
        self,
        key: str,
        value: Union[str, int, float],
        description: str = None
    ) -> entity_instance:
        new_entity = python_to_ifc_single_value(
            ifc=self.ifc,
            name=key,
            value=value,
            description=description)
        if self.entity.__getattr__(self.access) is None:
            self.entity.__setattr__(self.access, [new_entity])
        else:
            self.entity.__setattr__(self.access, _entity_to_list(
                self.entity.__getattr__(self.access)) + [new_entity])
        return new_entity

    def modify_entity(
        self,
        key: str,
        value: Union[str, int, float],
        description: str = None
    ) -> entity_instance:
        entity = self.get_entity(key)
        if entity.NominalValue is None:
            value_type = _recognize_value_type(value)
            entity.NominalValue = self.ifc.create_entity(value_type, value)
        else:
            entity.NominalValue.wrappedValue = value
        entity.Description = description
        if description is not None:
            self.descriptions[key] = description
        elif key in self.descriptions.keys():
            del(self.descriptions[key])
        return entity
