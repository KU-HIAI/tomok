import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04061301_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.13.1 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '프리텐션 정착영역의 파열저항력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.13 프리텐션 정착부
    4.6.13.1 계수파열저항력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리텐션 정착영역의 파열저항력];
    B["KDS 24 14 21 4.6.13.1 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:철근의 설계 항복강도/];
		VarIn2[/입력변수:보의 단부에서 h/4 이내에 배치되는 횡방향 철근의 총면적/];
		VarOut1[/출력변수:프리텐션 정착영역의 파열저항력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.13.1 (1)"])
		C --> Variable_def

		Variable_def--->E--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;P_r=f_{yd}A_s'>---------------------------------"]

		F(["프리텐션 정착영역의 파열저항력"])
    """

    @rule_method
    def upture_resistance_of_the_pretension_fixing_area(fIfyd,fIAs) -> RuleUnitResult:
        """프리텐션 정착영역의 파열저항력

        Args:
            fIfyd (float): 철근의 설계 항복강도
            fIAs (float): 보의 단부에서 h/4 이내에 배치되는 횡방향 철근의 총면적

        Returns:
            fOPr (float):  콘크리트교 설계기준 (한계상태설계법)  4.6.10.5 현장 타설 말뚝 (4)의 값
        """

        assert isinstance(fIfyd, float)
        assert isinstance(fIAs, float)

        fOPr = fIfyd * fIAs

        return RuleUnitResult(
            result_variables = {
                "fOPr": fOPr,
            }
        )