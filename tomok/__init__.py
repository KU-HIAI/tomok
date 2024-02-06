import importlib.util

from .core.rule_unit import RuleUnit
from .core.results import ResultBase, PassFailResult, SingleValueResult, MultiValueResult, RuleUnitResult
from .core.decorator import rule_method
from .core.rule_unit_controller import RuleUnitController

from .core.util import *

if importlib.util.find_spec("ifcopenshell"):
    from .core.rule_ifc_controller import RuleIFCController
    from .ifc.reader import IFCReader
    from .ifc.entity import Product
    from .core.rule_ifc import RuleIFC