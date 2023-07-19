import importlib.util

from .core.rule_unit import RuleUnit
from .core.decorator import rule_method

if importlib.util.find_spec("ifcopenshell"):
    from .core.rule_controller import RuleController
    from .ifc.reader import IFCReader
