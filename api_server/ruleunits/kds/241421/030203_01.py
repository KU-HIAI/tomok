import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_030203_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.2.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '철근의 설계항복강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.2 철근
    3.2.3 설계 가정
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근의 설계항복강도];
    B["KDS 24 14 21 3.2.3 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 철근 또는 프리스트레싱 강재의 재료계수/];
    VarIn2[/입력변수: 철근의 기준항복강도/] ;
		VarOut1[/출력변수: 철근의 설계항복강도/];

		VarOut1  ~~~ VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.2.3 (1)"])
		C --> Variable_def

		Variable_def--->D
		D--->E
		D["<img src='https://latex.codecogs.com/svg.image?f_{yd}=\phi&space;_sf_y'>---------------------------------"]
		E(["철근의 설계항복강도"])
    """

    @rule_method
    def Design_yield_strength_of_rebar(fIphis,fIfy) -> RuleUnitResult:
        """철근의 설계항복강도

        Args:
            fIphis (float): 철근 또는 프리스트레싱 강재의 재료계수
            fIfy (float): 철근의 기준항복강도

        Returns:
            fOfyd (float): 콘크리트교 설계기준(한계상태설계법)  3.2.3 설계 가정 (1)의 값
        """

        assert isinstance(fIphis, float)
        assert isinstance(fIfy, float)

        fOfyd = fIphis * fIfy

        return RuleUnitResult(
            result_variables = {
                "fOfyd": fOfyd,
            }
        )