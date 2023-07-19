from enum import Enum
from dataclasses import dataclass


class RuleProcessType(Enum):
    Decision = 1  # 직접 건설기준
    Indirect = 2  # 간접 건설기준
    Unknown = 9999  # 미정의


@dataclass
class RuleInfo():
    process_type: RuleProcessType = RuleProcessType.Unknown
    execute_rule_name: str = None
    affect_property_name: str = None
    priority: int = 9999

    def __repr__(self):
        return "{0}({1})/{2}".format(self.process_type.name, self.priority, self.execute_rule_name)
