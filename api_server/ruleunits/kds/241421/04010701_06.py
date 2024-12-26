import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010701_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.7.1 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '콘크리트 스트럿 최대 유효강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.1 판요소 설계
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 스트럿 최대 유효강도];
    B["KDS 24 14 21 4.1.7.1 (6)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 기준압축강도/];
		VarIn2[/입력변수: 주응력/];
		VarIn3[/입력변수: 주응력/];

		VarOut1[/출력변수: 콘크리트 스트럿의 최대 유효강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.7.1 (6)"])
		C --> Variable_def

		Variable_def--->F--->D--->E
		F{"콘크리트 기준강도 50MPa이하인경우"}
		D["<img src='https://latex.codecogs.com/svg.image?&space;f_{c2,max}=0.85f_{ck}\frac{1&plus;3.8(f_1/f_2)}{[1&plus;(f_1/f_2)]^2}'>---------------------------------"]
    E(["콘크리트 스트럿의 최대 유효강도"])
    """

    @rule_method
    def Concrete_strut_maximum_effective_strength(fIfck,fIf1,fIf2) -> RuleUnitResult:
        """콘크리트 스트럿 최대 유효강도

        Args:
            fIfck (float): 콘크리트 기준압축강도
            fIf1 (float): 주응력
            fIf2 (float): 주응력

        Returns:
            fOc2max (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (6)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (6)의 판단 결과
        """

        assert isinstance(fIfck, float)
        assert isinstance(fIf1, float)
        assert fIf1 > 0
        assert isinstance(fIf2, float)
        assert fIf2 > 0

        fOc2max = 0.85 * fIfck * (1 + 3.8 * fIf1 / fIf2) / (1 + (fIf1 / fIf2))**2

        if fIfck <= 50 and fIf1 > 0 and fIf2 > 0 :
          fOc2max = 0.85 * fIfck * (1 + 3.8 * fIf1 / fIf2) / (1 + (fIf1 / fIf2))**2
          return RuleUnitResult(
              result_variables = {
                  "fOc2max": fOc2max,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )