import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010504_05_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.5.4 (5) ①'
    ref_date = '2021-04-12'
    doc_date = '2024-05-14'
    title = '절점영역내의 압축응력의 최대설계유효강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.5 스트럿-타이 모델
    4.1.5.4 절점영역
    (5)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절점영역내의 압축응력의 최대설계유효강도];
    B["KDS 24 14 21 4.1.5.4 (5) ①"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 절점영역내의 압축응력의 최대설계유효강도/];
		VarIn1[/입력변수: 콘크리트 기준압축강도/];
		VarIn2[/입력변수: 콘크리트 재료계수/];

		VarOut1 ~~~~ VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.5.4 (5) ①"])
		C --> Variable_def

		Variable_def --타이가 정착되지 않은 압축 절점--> D ----> E
		D["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=(1-f_{ck}/250)\phi&space;_{c}f_{ck}'>---------------------------------"]
		E(["절점영역내의 압축응력의 최대설계유효강도"])
    """

    @rule_method
    def Effective_design_strength_of_compressive_stress_at_node_area(fIfck,fIphic) -> RuleUnitResult:
        """절점영역내의 압축응력의 최대설계유효강도

        Args:
            fIfck (float): 콘크리트 기준압축강도
            fIphic (float): 콘크리트 재료계수

        Returns:
            fOfcdmax (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.5.4 절점영역 (5) ①의 값
        """

        assert isinstance(fIfck, float)
        assert isinstance(fIphic, float)

        fOfcdmax = (1 - fIfck/250) * fIphic * fIfck

        return RuleUnitResult(
            result_variables = {
                "fOfcdmax": fOfcdmax,
            }
        )