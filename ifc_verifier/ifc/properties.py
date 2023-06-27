# python
from typing import Union
# 3rd-party
from ifcopenshell.file import file
from ifcopenshell.entity_instance import entity_instance
# framework
from .util import entity_to_list
from .property_set import PropertySet
from .type_conv import ifc_single_value_to_python, python_to_ifc_single_value


class Properties(PropertySet):
    """
    PropertySet 클래스를 IfcPropertySet이 아닌
    IfcMaterialProperties, IfcProfileProperties에
    그대로 적용 시 문제가 발생해서
    Properties 클래스를 새로 만들었습니다.
    """
    def __init__(
            self, ifc: file,
            entity: entity_instance
    ):
        super().__init__(ifc, entity)

    def _get_props(
        self
    ):
        """
        @override
        """
        if type(self.entity.Properties) is entity_instance:
            return [self.entity.Properties]
        else:
            return self.entity.Properties

    def parse(
        self
    ):
        """
        @override
        """
        self._parse_property_names()
        self._parse_property_values()

    def _parse_property_names(
        self
    ):
        """
        @override
        """
        if self.entity.Properties is None:
            self.property_names = []
        else:
            self.__dict__["property_names"] = [prop.Name for prop in self._get_props()]  # __setattr__ triggers infinite call
            self.__dict__["descriptions"] = {prop.Name: prop.Description for prop in self._get_props() if prop.Description}

    def _parse_property_values(
        self
    ):
        """
        @override
        for문 부분에서 코드 중복이 발생하는데, 어떻게 하는 게 좋을 지 모르겠어요.
        + override annotation도 더 나은 방법이…?
        """
        if self.entity.Properties is None:
            return
        for prop in self._get_props():
            if prop.NominalValue is not None:
                value_type = prop.NominalValue.get_info()['type']
                wrapped_value = prop.NominalValue.wrappedValue
                value = ifc_single_value_to_python(value_type, wrapped_value)
            else:
                value = None
            self.__setattr__(prop.Name, value)

    def make_entity(
        self,
        key: str,
        value: Union[str, int, float],
        description: str = None
    ) -> entity_instance:
        """
        @Override
        """
        new_entity = python_to_ifc_single_value(
            ifc = self.ifc,
            name = key,
            value = value,
            description = description)
        if self.entity.Properties is None:
            self.entity.Properties = [new_entity]
        else:
            self.entity.Properties = entity_to_list(self.entity.Properties) + [new_entity]
        return new_entity