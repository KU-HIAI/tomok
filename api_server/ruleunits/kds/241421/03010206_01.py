import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010206_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.6 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '설계압축강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.6 설계압축강도 및 설계인장강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계압축강도];
    B["KDS 24 14 21 3.1.2.6 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 기준압축강도/];
		VarIn2[/입력변수: 재료 계수/];
    VarIn3[/입력변수: 유효 계수/] ;
    VarOut1[/출력변수: 설계압축강도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.6 (1)"])
		C --> Variable_def

		Variable_def--->E--->D--->F

		E["<img src='https://latex.codecogs.com/svg.image?\alpha&space;_{cc}=0.85'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?f_{cd}=\phi&space;_c\alpha&space;_{cc}f_{ck}'>---------------------------------"]

		F(["설계압축강도"])
		D~~~ |"Table 24 14 21 1.4-1"| D
    """

    @rule_method
    def Design_compressive_strength(fImatfac,fIspecom) -> RuleUnitResult:
        """설계압축강도

        Args:
            fImatfac (float): 재료계수
            fIspecom (float): 기준압축강도

        Returns:
            fOfcd (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.6 설계압축강도 및 설계인장강도 (1)의 값
        """

        assert isinstance(fImatfac, float)
        assert isinstance(fIspecom, float)

        fOfcd = fImatfac * 0.85 * fIspecom

        return RuleUnitResult(
            result_variables = {
                "fOfcd": fOfcd,
            }
        )