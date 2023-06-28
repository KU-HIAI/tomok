# 3rd-party
from ifcopenshell.entity_instance import entity_instance
# framework
from .util import *
from .property_set import PropertySet
from .properties import Properties


class SupertypeIfcEntityOfPsetAndProp:
    """
    Variables:
        property_set_names: PropertySet 또는 Properties의 이름을 모은 집합
    """
    property_set_names = []

    def __getattr__(self, key):
        raise AttributeError("{0} property_set is not in {1}. {2}".format(key, self, self.property_set_names))

    def __repr__(self):
        return repr(self.entity.wrapped_data)

    def get_psets(self):
        return [
            self.__getattribute__(name) for name in self.property_set_names
        ]


class IfcStructuralCurveAction(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc, from_entity):
        self.ifc = ifc
        pset_names = []
        for property_set_entity in get_structural_curve_action_psets_from_entity(self.ifc, from_entity):
            key = property_set_entity.Name
            value = PropertySet(self.ifc, property_set_entity)
            self.__setattr__(key, value)
            pset_names.append(key)
        self.property_set_names = pset_names
        ifc_structural_curve_actions = [e for e in get_inverse(ifc, from_entity) if e.is_a("IfcStructuralCurveAction")]
        if len(ifc_structural_curve_actions) > 1:
            raise ValueError("{from_entity}를 참조하는 IfcStructuralCurveAction이 두 개 이상입니다. 개발자에게 문의하세요.")
        elif len(ifc_structural_curve_actions) == 1:
            self.entity = ifc_structural_curve_actions[0]
        else:
            self.entity = None


class IfcMaterial(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc, from_entity):
        self.ifc = ifc
        pset_names = []
        for properties_entity in get_ifc_material_properties_from_entity(self.ifc, from_entity):
            key = properties_entity.Name
            value = Properties(self.ifc, properties_entity)
            self.__setattr__(key, value)
            pset_names.append(key)
        self.property_set_names = pset_names


class IfcArbitraryClosedProfile(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc, from_entity):
        # print("#", from_entity, get_ifc_profile_properties_from_entity(ifc, from_entity))
        self.ifc = ifc
        pset_names = []
        for properties_entity in get_ifc_profile_properties_from_entity(self.ifc, from_entity):
            key = properties_entity.Name
            value = Properties(self.ifc, properties_entity)
            self.__setattr__(key, value)
            pset_names.append(key)
        # print(pset_names)
        self.property_set_names = pset_names

