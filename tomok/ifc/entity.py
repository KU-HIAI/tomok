# 3rd-party
from ifcopenshell.file import file
from ifcopenshell.entity_instance import entity_instance
# framework
from .util import *
from .parse import get_tree
from .entity_base import SupertypeIfcEntityOfPsetAndProp


class Product(SupertypeIfcEntityOfPsetAndProp):
    def __init__(
        self,
        ifc: file,
        entity: entity_instance
    ):
        self.ifc = ifc
        self.entity = entity
        self.property_set_names = []

        self.IfcMaterial = None
        self.IfcProfileDef = None
        self.IfcStructuralCurveAction = None
        self.decision_rules = []
        self.indirect_rules = []

        self.parse()
        self.set_attributes()

    def parse(
        self
    ):
        self.tree = get_tree(self.ifc, self.entity)

    def set_attributes(
        self
    ):
        
        self.set_psets(self.tree.get('pset', {}))
        self.decision_rules = self.tree.get('rule_decision', {})
        self.indirect_rules = self.tree.get('rule_indirect', {})
        self.id2rel_class = self.tree.get('id2rel_class', {})
        self.IfcStructuralCurveAction = IfcStructuralCurveAction(
            self.ifc, self.entity, self.tree)
        self.IfcMaterial = IfcMaterial(self.ifc, self.entity, self.tree)
        self.IfcProfileDef = IfcArbitraryClosedProfile(
            self.ifc, self.entity, self.tree)

    def get_guid(
        self
    ):
        return self.entity.GlobalId

    def get_subtype(
        self
    ):
        return self.entity.ObjectType

    def get_upper_subtype(
        self
    ):
        return self.get_subtype().upper() if isinstance(self.get_subtype(), str) else ''

    @property
    def identifications(self):
        return self.tree['identification']

    @property
    def descriptions(self):
        return self.get_descriptions() + self.IfcStructuralCurveAction.get_descriptions() + \
            self.IfcMaterial.get_descriptions() + self.IfcProfileDef.get_descriptions()


class IfcStructuralCurveAction(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, from_entity: entity_instance, tree: dict):
        self.ifc = ifc
        self.entity = from_entity
        if('IfcStructuralCurveAction' in tree.keys()):
            self.set_psets(tree['IfcStructuralCurveAction'].get('pset', {}))


class IfcMaterial(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, from_entity: entity_instance, tree: dict):
        self.ifc = ifc
        self.entity = from_entity
        self.set_psets(tree.get('material', {}))


class IfcArbitraryClosedProfile(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, from_entity: entity_instance, tree: dict):
        self.ifc = ifc
        self.entity = from_entity
        self.set_psets(tree.get('profile', {}))
