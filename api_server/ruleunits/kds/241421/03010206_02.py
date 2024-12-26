import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010206_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.6 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '설계인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.6 설계압축강도 및 설계인장강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계인장강도];
    B["KDS 24 14 21 3.1.2.6 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 기준인장강도/];
		VarIn2[/입력변수: 콘크리트의 재료계수/];
    VarIn3[/입력변수: 인장강도 유효계수/] ;
    VarOut1[/출력변수: 설계인장강도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.6 (2)"])
		C --> Variable_def

		Variable_def--->D--->F

		D["<img src='https://latex.codecogs.com/svg.image?f_{ctd}=\phi&space;_c\alpha&space;_{ct}f_{ctk}'>---------------------------------"]
		F(["설계인장강도"])
		D~~~ |"Table 24 14 21 1.4-1"| D
    """

    @rule_method
    def Design_tensile_strength(fIphic,fIalphact,fIfctk) -> RuleUnitResult:
        """설계인장강도

        Args:
            fIphic (float): 콘크리트의 재료계수
            fIalphact (float): 인장강도 유효계수
            fIfctk (float): 기준인장강도

        Returns:
            fOfctd (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.6 설계압축강도 및 설계인장강도 (2)의 값
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIfctk, float)
        assert isinstance(fIalphact, float)

        fOfctd = fIphic * fIalphact * fIfctk

        return RuleUnitResult(
            result_variables = {
                "fOfctd": fOfctd,
            }
        )