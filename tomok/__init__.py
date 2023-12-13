import importlib.util

from .core.rule_unit import RuleUnit
from .core.decorator import rule_method
from .core.rule_unit_controller import RuleUnitController

if importlib.util.find_spec("ifcopenshell"):
    from .core.rule_ifc_controller import RuleIFCController
    from .ifc.reader import IFCReader
