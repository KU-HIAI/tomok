# 3rd-party
from ifcopenshell.file import file
from ifcopenshell.entity_instance import entity_instance

# framework
from .util import *
from .parse import get_tree
from .entity_base import SupertypeIfcEntityOfPsetAndProp


class Product(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, entity: entity_instance):
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

    def parse(self):
        self.tree = get_tree(self.ifc, self.entity)

    def set_attributes(self):

        self.set_psets(self.tree.get("pset", {}))
        self.decision_rules = self.tree.get("rule_decision", {})
        self.indirect_rules = self.tree.get("rule_indirect", {})
        self.id2rel_class = self.tree.get("id2rel_class", {})
        self.IfcStructuralCurveAction = IfcStructuralCurveAction(
            self.ifc, self.entity, self.tree
        )
        self.IfcMaterial = IfcMaterial(self.ifc, self.entity, self.tree)
        self.IfcProfileDef = IfcArbitraryClosedProfile(self.ifc, self.entity, self.tree)

    def get_guid(self):
        return self.entity.GlobalId

    def get_subtype(self):
        # test
        valid_obj_types_bridge = [
            "SEISMIC_GRADE_SETTING",
            "SEISMIC_ANALYSIS_METHOD",
            "PSC_I_GIRDER",
            "CONTINUOUS_DECK",
            "SUBSTRUCTURE_CHECK",
            "SHOE_DESIGN",
            "STEEL_PLATE_GIRDER",
            "JOINT",
            "STEEL_CROSSBEAM",
            "SERVICEABILITY_CHECK",
            "STIFFENING_GIRDER",
        ]
        valid_obj_type_building = [
            "SEISMIC_CATEGORY",
            "EARTHQUAKE_RESISTANCE_SYSTEM",
            "BASEMENT_STRUCTURE_SEISMIC_DESIGN",
            "RC_JOINT",
            "DECKPLATE_SLAB",
            "STEEL_BEAM",
            "STEEL_COLUMN",
            "STEEL_JOINT",
            "GENERAL_CONCEPT",
            "SIMPLE_METHOD",
            "STRUCTURAL_STABILITY",
            "STRUCTURAL_PERFORMANCE_EVALUATION",
            "JOINT",
        ]
        valid_obj_type = valid_obj_type_building + valid_obj_types_bridge

        if self.entity.ObjectType in valid_obj_type:
            return self.entity.ObjectType
        else:
            if "PredefinedType" in self.entity.__dict__:
                return self.entity.PredefinedType
            else:
                return self.entity.ObjectType

    def get_upper_subtype(self):
        return self.get_subtype().upper() if isinstance(self.get_subtype(), str) else ""

    @property
    def identifications(self):
        return self.tree["identification"]

    @property
    def descriptions(self):
        return (
            self.get_descriptions()
            + self.IfcStructuralCurveAction.get_descriptions()
            + self.IfcMaterial.get_descriptions()
            + self.IfcProfileDef.get_descriptions()
        )


class IfcStructuralCurveAction(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, from_entity: entity_instance, tree: dict):
        self.ifc = ifc
        self.entity = from_entity
        if "IfcStructuralCurveAction" in tree.keys():
            self.set_psets(tree["IfcStructuralCurveAction"].get("pset", {}))


class IfcMaterial(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, from_entity: entity_instance, tree: dict):
        self.ifc = ifc
        self.entity = from_entity
        self.set_psets(tree.get("material", {}))


class IfcArbitraryClosedProfile(SupertypeIfcEntityOfPsetAndProp):
    def __init__(self, ifc: file, from_entity: entity_instance, tree: dict):
        self.ifc = ifc
        self.entity = from_entity
        self.set_psets(tree.get("profile", {}))
