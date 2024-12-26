import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010502_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.5.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '콘크리트 스트럿의 유효설계강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.5 스트럿-타이 모델
    4.1.5.2 스트럿
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 스트럿의 유효설계강도];
    B["KDS 24 14 21 4.1.5.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 재료계수/];
		VarIn2[/입력변수: 콘크리트 기준압축강도/];

		VarOut1[/출력변수: 콘크리트 스트럿의 유효설계강도/];

		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.5.2 (1)"])
		C --> Variable_def

		Variable_def--->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=0.85\phi&space;_cf_{ck}'>---------------------------------"]
		E(["콘크리트 스트럿의 유효설계강도"])
    """

    @rule_method
    def Effective_design_strength_of_concrete_struts(fIphic,fIfck) -> RuleUnitResult:
        """콘크리트 스트럿의 유효설계강도

        Args:
            fIphic (float): 콘크리트 재료계수
            fIfck (float): 콘크리트 기준압축강도

        Returns:
            fOfcdmax (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.5.2 스트럿 (1)의 값
            sOfcdmax (string): 콘크리트교 설계기준 (한계상태설계법) 4.1.5.2 스트럿 (1)의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIfck, float)

        fOfcdmax = 0.85 * fIphic * fIfck

        return RuleUnitResult(
            result_variables = {
                "sOfcdmax": "압축응력이 작용하는 영역에서는 더 높은 설계강도로 가정하는 것이 적절할 수 있다.",
                "fOfcdmax": fOfcdmax,
            }
        )