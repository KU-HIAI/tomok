import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040301_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.1 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '앵커의 공칭강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.1 인장력을 받는 앵커의 강재강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커의 공칭강도];
    B["KDS 14 20 54 4.3.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 앵커의 공칭강도/];
    VarIn1[/입력변수 : 인장에 대한 달일 앵커의 유효단면적/];
    VarIn2[/입력변수 : 앵커 강재의 설계기준인장강도/];
    VarIn3[/입력변수 : 앵커 강재의 설계기준항복강도/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    VarOut ~~~ VarIn3
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.1 (2)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?f_{uta}=min(1.9f_{ya},860MPa)'>-----------------------------------------"];
    F{"<img src='https://latex.codecogs.com/svg.image?&space;N_{sa}\leq A_{se,N}f_{uta}'>------------------------"};
    Variable_def--->D--->F
    F--->G(["Pass or Fail"])
    """

    @rule_method
    def nominal_strength_of_anchor(fINsa,fIAseN,fIfuta,fIfya) -> RuleUnitResult:
        """앵커의 공칭강도

        Args:
            fINsa (float): 앵커의 공칭강도
            fIAseN (float): 인장에 대한 단일 앵커의 유효단면적
            fIfuta (float): 앵커 강재의 설계기준인장강도
            fIfya (float): 앵커 강재의 설계기준항복강도

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.1 인장력을 받는 앵커의 강재강도 (2)의 판단 결과
        """

        assert isinstance(fINsa, float)
        assert isinstance(fIAseN, float)
        assert isinstance(fIfuta, float)
        assert isinstance(fIfya, float)

        if fIfuta <= min(1.9*fIfya, 860):
          if fINsa <= fIAseN * fIfuta:
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
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )