import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_0405_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.5 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-13'
    title = '인장력과 전단력의 동시 작용'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.5 인장력과 전단력의 동시 작용
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력과 전단력의 동시 작용];
    B["KDS 14 20 54 4.5 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 단일 앵커 또는 앵커 그룹에 작용하는 계수전단하중/];
    VarIn2[/입력변수 : 공칭전단강도/];
    VarIn3[/입력변수 : 공칭인장강도/];
    VarIn4[/입력변수 : 단일 앵커 또는 앵커 그룹에서 개별 앵커의 계수인장하중/];
    VarIn1~~~ VarIn3
    VarIn2 ~~~ VarIn4
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.5 (2)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?\frac{V_{ua}}{\phi&space;V_{n}}\leq&space;0.2'>"};
    E{"<img src='https://latex.codecogs.com/svg.image?N_{ua}\leq\phi&space;N_{n}'>"};
    F(["Pass or Fail"])
    Variable_def--->D--Yes--->E---->F
    """

    @rule_method
    def simultaneous_action_of_tensile_and_shear_forces(fIVua,fIphiVn,fIphiNn,fINua) -> RuleUnitResult:
        """인장력과 전단력의 동시 작용

        Args:
            fIVua (float): 단일 앵커 또는 앵커 그룹에 작용하는 계수전단하중
            fIphiVn (float): 공칭전단강도
            fIphiNn (float): 공칭인장강도
            fINua (float): 단일 앵커 또는 앵커 그룹에서 개별 앵커의 계수인장하중

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.5 인장력과 전단력의 동시 작용 (2)의 판단 결과
        """

        assert isinstance(fIVua, float)
        assert isinstance(fIphiVn, float)
        assert fIphiVn != 0
        assert isinstance(fIphiNn, float)
        assert isinstance(fINua, float)

        if fIVua/fIphiVn <= 0.2 :
          if fIphiNn >= fINua :
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