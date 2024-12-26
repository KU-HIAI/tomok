import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041102_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.11.2 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '수직온도경사'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 온도변화
    4.11.2 온도경사(TG)
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 수직온도경사];
    B["KDS 24 12 21 4.11.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : A/];
    VarIn1[/입력변수 : 두께/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.11.2 (1)"])
		C --> Variable_def

    D{"두께 &ge; 400mm 인 콘크리트 상부구조물의 경우"};
    E{"강재로 된 상부구조물인 경우"};
    F["A=300mm"];
    G["A = 실제 두께 - 100mm"];
    H["A=300mm"]
    I(["A"]);
    Variable_def--->D--Yes--->F--->I
    D--No--->G--->I
    Variable_def--->E--->H--->I
    """

    @rule_method
    def vertical_temperature_slope(fIAA,fIAB,fIt) -> RuleUnitResult:
        """수직온도경사

        Args:
            fIAA (float): 수직온도경사 (콘크리트 상부구조물)
            fIAB (float): 수직온도경사 (강재로 된 상부구조물)
            fIt (float): 두께

        Returns:
            fOA (float): 강교 설계기준(한계상태설계법)  4.11.2 온도경사(TG) (1)의 값
        """

        assert isinstance(fIt, float)

        if fIAA != 0 and fIAB == 0 :
          if fIt >= 400 :
            fOA = 300
          else:
            fOA = fIt - 100
            return RuleUnitResult(
                result_variables = {
                    "fOA": fOA,
                }
            )

        if fIAA == 0 and fIAB != 0 :
          fOA = 300
          return RuleUnitResult(
              result_variables = {
                  "fOA": fOA,
              }
          )