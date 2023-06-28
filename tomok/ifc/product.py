# python
from typing import Union, List
from itertools import chain
from types import SimpleNamespace
# 3rd-party
from ifcopenshell.entity_instance import entity_instance
from ifcopenshell.file import file
# framework
from .util import *
from .property_set import PropertySet
from .properties import Properties
from .entities import IfcArbitraryClosedProfile, IfcMaterial, IfcStructuralCurveAction


class Product():
    property_set_names = []

    def __init__(
        self, 
        ifc: file,
        entity: entity_instance
    ):
        self.ifc = ifc
        self.entity = entity

        self.parse()

    def __repr__(
        self
    ):
        return repr(self.entity.wrapped_data)
    
    def __getattr__(
        self,
        key
    ):
        raise AttributeError("{0} property_set is not in {1}. {2}".format(key, self, self.property_set_names))
    
    def _parse_property_set_names(
        self
    ):
        psets = get_ifc_property_set_from_entity(self.ifc, self.entity)
        if len(psets) == 0:
            self.property_set_names = []
        self.StructuralCurveAction.property_set_names = [pset.Name for pset in psets]
        self.property_set_names = self.property_set_names + [pset.Name for pset in psets]
    
    def _parse_property_set_values_and_names(
        self
    ):
        self._parse_structural_curve_action()
        self._parse_directly_connected_psets()

    def _parse_properties_values_and_names(
        self
    ):
        material = IfcMaterial(self.ifc, self.entity)
        self.__setattr__("IfcMaterial", material)

        profile = IfcArbitraryClosedProfile(self.ifc, self.entity)
        self.__setattr__("IfcProfileDef", profile)

    def _parse_structural_curve_action(
        self,
        psets_=None
    ):
        structural_curve_action = IfcStructuralCurveAction(self.ifc, self.entity)
        self.__setattr__("IfcStructuralCurveAction", structural_curve_action)

    def _parse_directly_connected_psets(
        self
    ):
        self.property_set_names = []
        psets = get_directly_connected_psets_from_entity(self.ifc, self.entity)
        self.property_set_names = [pset.Name for pset in psets]
        for pset in psets:
            key = pset.Name
            value = PropertySet(self.ifc, pset)
            self.__setattr__(key, value)

    def _parse_ifc_classification_refs(
            self):
        self.ifc_cls_refs = []
        ifc_rel_associates_clfs = [entity for entity in get_inverse(self.ifc, self.entity)
                                   if entity.is_a('IfcRelAssociatesClassification')]
        self.ifc_cls_refs = [clfs.RelatingClassification
                             for clfs in ifc_rel_associates_clfs]
    
    def parse(
        self
    ):
        self._parse_property_set_values_and_names()
        self._parse_properties_values_and_names()
        self._parse_ifc_classification_refs()
    
    def get_psets(
        self
    ) -> List[PropertySet]:
        return [
            self.__dict__[pset_name] for pset_name in self.property_set_names
        ]
    
    def get_props(
        self,
        names_only: bool = True
    ):
        def get_key(pset: PropertySet):
            if(names_only):
                return pset.entity.Name
            else:
                return pset
        return {get_key(pset): pset.get_properties() for pset in self.get_psets()}

    def _get_descriptions(
        self,
        remove_null: bool = True,
        serialize: bool = True
    ):
        """ 2022.05.21 개편사항
        IfcStructuralCurveActivity.PropertySet,
        IfcMaterial.Properties,
        IfcArbitraryClosedProfileDef
        세 곳 모두에서 description을 가져옵니다.
        06.03 추가: 직접 연결된 IfcPropertySet에서도 가져옵니다.
        """
        def filter(pset):
            if(remove_null):
                return len(pset.descriptions.values()) > 0
            else:
                return True
        every_psets = self.get_psets_from_structural_curve_action() + self.get_props_from_material() + \
                      self.get_props_from_arbitrary_closed_profile_def() + self.get_psets()
        descriptions = [list(pset.descriptions.values()) for pset in every_psets if filter(pset)]
        if(serialize):
            descriptions = list(chain.from_iterable(descriptions))
        return descriptions

    # 0923 추가
    def _get_identification(
            self,
    ):
        """ 2022.09.26 추가
        product의 ifc_cls_refs(List[RelatingClassification)에서
        각 entity_instance의 Identification 값을 가져옵니다.
        """
        identifications = [entity.Identification for entity in self.ifc_cls_refs]
        return identifications


    def get_psets_from_structural_curve_action(
        self
    ) -> List[PropertySet]:
        return self.IfcStructuralCurveAction.get_psets()

    def get_props_from_material(
        self
    ) -> List[Properties]:
        return self.IfcMaterial.get_psets()

    def get_props_from_arbitrary_closed_profile_def(
        self
    ) -> List[Properties]:
        return self.IfcProfileDef.get_psets()
