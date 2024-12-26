import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_0401_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.1 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-18'
    title = '인장력과 전단력의 동시 작용'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.1 설계 일반
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력과 전단력의 동시 작용];
    B["KDS 14 20 54 4.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 앵커의 강도/];
    VarIn2[/입력변수 : 최대 소요강도/];
    end
    Python_Class~~~ C(["KDS 14 20 54 4.1 (2)"])--> Variable_def
    D["앵커의 강도 &ge; KDS 14 20 10(3.2)의 적용 가능한 하중조합에 의해 결정되는 최대소요강도"];
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    @rule_method
    def anchor_strength(fIstranc,fIstrmax) -> RuleUnitResult:
        """인장력과 전단력의 동시 작용

        Args:
            fIstranc (float): 앵커의 강도
            fIstrmax (float): 최대 소요강도

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.5 인장력과 전단력의 동시 작용 (2)의 판단 결과
        """

        assert isinstance(fIstranc, float)
        assert isinstance(fIstrmax, float)


        if fIstranc >= fIstrmax :
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
               }
          )