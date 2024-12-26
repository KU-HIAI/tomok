import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04070702_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.7.7.2 (3)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '상부구조의 총변위'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.2 등가정적하중법
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 상부구조의 총변위];
	  B["KDS 24 17 11 4.7.7.2 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 상부구조의 총변위/]
	  VarIn1[/입력변수: 유효수평지반가속도/]
	  VarIn2[/입력변수: 지진격리교량의 지반계수/]
	  VarIn3[/입력변수: 유효주기/]
	  VarIn4[/입력변수: 지진격리교량의 감쇠계수/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.7.7.2 (3)"])
		C --> Variable_def

  	E["<img src='https://latex.codecogs.com/svg.image?d=\frac{250S\cdot&space;S_iT_{eff}}{B}(mm)'>-----------------------------------"];

  	D(["<img src='https://latex.codecogs.com/svg.image?d'>"]);

  	Variable_def --> E --> D
    """

    @rule_method
    def Total_displacement_of_the_superstructure(fIS,fISi,fITeff,fIB) -> RuleUnitResult:
        """상부구조의 총변위

        Args:
            fIS (float): 유효수평지반가속도
            fISi (float): 지진격리교량의 지반계수
            fITeff (float): 유효주기
            fIB (float): 지진격리교량의 감쇠계수

        Returns:
            fOd (float): 교량내진설계기준(한계상태설계법) 4.7.7.2 등가정적하중법 (3)의 값
        """

        assert isinstance(fIS, float)
        assert isinstance(fISi, float)
        assert isinstance(fITeff, float)
        assert isinstance(fIB, float)
        assert fIB > 0

        fOd = 250 * fIS * fISi * fITeff / fIB

        return RuleUnitResult(
            result_variables = {
                "fOd": fOd,
                }
            )