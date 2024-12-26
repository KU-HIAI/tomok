import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070105_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.1.5 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '바닥판에서의 횡방향 전단력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.1 프리캐스트 콘크리트 구조물의 일반사항
    4.7.1.5 바닥 시스템
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판에서의 횡방향 전단력];
    B["KDS 24 14 21 4.7.1.5 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:지압응력을 고려한 순 지압판 길이/];
		VarIn2[/입력변수:받침점 반력/];
		VarOut1[/출력변수:바닥판에서의 횡방향 전단력/];

		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.1.5 (5)"])
		C --> Variable_def

		Variable_def--->E--->D

		D(["바닥판에서의 횡방향 전단력"])
		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;V_u=q_ub_e'>---------------------------------"]
    """

    @rule_method
    def Transverse_shear_forces_in_deck(fIqu,fIbe) -> RuleUnitResult:
        """바닥판에서의 횡방향 전단력

        Args:
            fIqu (float): 지압응력을 고려한 순 지압판 길이
            fIbe (float): 받침점 반력

        Returns:
            fOVu (float):  콘크리트교 설계기준 (한계상태설계법)  4.7.1.5 바닥 시스템 (5)의 값
        """

        assert isinstance(fIqu, float)
        assert isinstance(fIbe, float)

        fOVu = fIqu * fIbe

        return RuleUnitResult(
            result_variables = {
                "fOVu": fOVu,
            }
        )