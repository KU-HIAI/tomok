import importlib.util

from .tomok.core.rule_unit import RuleUnit
from .tomok.core.decorator import rule_method
from .tomok.core.rule_unit_controller import RuleUnitImporter

if importlib.util.find_spec("ifcopenshell"):
    from .tomok.core.rule_ifc_controller import RuleController
    from .tomok.ifc.reader import IFCReader
