import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04070702_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.7.7.2 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '탄성지진응답계수'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.2 등가정적하중법
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 등가지진력];
	  B["KDS 24 17 11 4.7.7.2 (1)"];
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 지진격리받침의 유효강성/]
	  VarIn1[/입력변수: 상부구조물의 총중량/]
	  VarIn2[/입력변수: 탄성지진응답계수/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.7.7.2 (1)"])
		C --> Variable_def

  	E["<img src='https://latex.codecogs.com/svg.image?F_e=C_sW'>"];

  	D(["<img src='https://latex.codecogs.com/svg.image?F_e'>"]);

  	Variable_def --> E --> D
    """

    @rule_method
    def equlibrious_earthquake_force(fIW,fICs) -> RuleUnitResult:
        """등가지진력

        Args:
            fIW (float): 상부구조물의 총중량
            fICs (float): 탄성지진응답계수

        Returns:
            fOFe (float): 교량내진설계기준(한계상태설계법) 4.7.7.2 등가정적하중법 (1)의 값
        """

        assert isinstance(fIW, float)
        assert isinstance(fICs, float)

        fOFe = fICs * fIW

        return RuleUnitResult(
            result_variables = {
                "fOFe": fOFe,
                }
            )