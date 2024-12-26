import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.2.2 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '콘크리트 스트럿의 유효압축강도'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.2 스트럿의 축강도
    4.2.2 유효압축강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 스트럿의 유효압축강도];
    B["KDS 14 20 24 4.2.2 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 콘크리트 스트럿의 유효압축강도/];
		VarIn1[/입력변수 : 균열의 영향과 구속철근의 영향을 고려하기 위한 계수/];
		VarIn2[/입력변수 : 콘크리트의 설계기준압축강도/];
		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
    end

		Python_Class ~~~ C(["KDS 14 20 24 4.2.2 (1)"])
		C --> Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?f_{ce}=0.85\beta&space;_{s}f_{ck}'>---------------------------------------"];
		E["실험과 적절한 해석을 통해 구한 값"]
		F(["<img src='https://latex.codecogs.com/svg.image?f_{ce}'>"]);
		Variable_def--->D--->F
		Variable_def--->E--->F
    """

    @rule_method
    def effective_compressive_strength_of_a_concrete_strut(fIbetas,fIfck) -> RuleUnitResult:
        """콘크리트 스트럿의 유효압축강도

        Args:
            fIbetas (float): 균열의 영향과 구속철근의 영향을 고려하기 위한 계수
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            fOfce (float): 콘크리트구조 스트럿-타이모델 기준  4.2.2 유효압축강도 (1)의 값
        """

        assert isinstance(fIbetas, float)
        assert isinstance(fIfck, float)

        fOfce = 0.85*fIbetas*fIfck

        return RuleUnitResult(
              result_variables = {
                  "fOfce": fOfce,
              }
          )