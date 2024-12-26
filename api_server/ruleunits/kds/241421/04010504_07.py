import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010504_07(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.5.4 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '콘크리트 스트럿의 유효설계강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.5 스트럿-타이 모델
    4.1.5.4 절점영역
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 스트럿의 유효설계강도];
    B["KDS 24 14 21 4.1.5.4 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 스트럿의 유효설계강도/];
		VarIn2[/입력변수: 콘크리트 기준압축강도/];
		VarIn3[/입력변수: 콘크리트 재료계수/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.5.4 (7)"])
		C --> Variable_def

		Variable_def--->D--->F--->E
		D{"3축 압축절점영역에서 3방향 스트럿 모두 힘 분배를 알 경우"}
		F{"<img src='https://latex.codecogs.com/svg.image?f_{cd,max}\leq&space;3(1-f_{ck}/250)\phi&space;_cf_{ck}'>---------------------------------"}
		E(["Pass or Fail"])
		F~~~ |"KDS 24 14 21 3.1-43, 44"| F
    """

    @rule_method
    def Effective_design_strength_of_concrete_struts(fIfcdmax,fIfck,fIphic) -> RuleUnitResult:
        """콘크리트 스트럿의 유효설계강도

        Args:
            fIfcdmax (float): 콘크리트 스트럿의 유효설계강도
            fIfck (float): 콘크리트 기준압축강도
            fIphic (float): 콘크리트 재료계수

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.5.2 스트럿 (7)의 판단 결과
        """

        assert isinstance(fIfcdmax, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIphic, float)


        if fIfcdmax <= 3 * (1 - fIfck / 250) * fIphic * fIfck :
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