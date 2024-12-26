import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_0402_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.2 (3)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '인장을 받는 단일부착식 앵커'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.2 앵커 강도에 관한 일반 규정
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장을 받는 단일부착식 앵커];
    B["KDS 14 20 54 4.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 인장을 받는 단일 부착식 앵커의 기본 부착강도/];
		VarIn2[/입력변수 : 계수 지속 인장하중/];
		VarIn3[/입력변수 : 강도감소계수/];
    VarIn1
		VarIn1 ~~~ VarIn2 & VarIn3
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.2 (3)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?&space;0.55\phi N_{ba}\geq N_{ua,s}'>--------------------"};
    E([PASS or Fail]);
    Variable_def--->D
    D--->E
    """

    @rule_method
    def Attached_anchor_with_continuous_tensile_load(fINba,fINuas,fIphi) -> RuleUnitResult:
        """인장을 받는 단일부착식 앵커

        Args:
            fINba (float): 인장을 받는 단일 부착식 앵커의 기본 부착강도
            fINuas (float): 계수 지속 인장하중
            fIphi (float): 강도감소계수

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.2 앵커 상도에 관한 일반 규정 (3)의 판단 결과
        """

        assert isinstance(fINba, float)
        assert isinstance(fINuas, float)
        assert isinstance(fIphi, float)

        if 0.55 * fIphi * fINba >= fINuas :
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