import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070503_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.5.2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '콘크리트의 최소 두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.3 프리캐스트 슬래브교
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트의 최소 두께];
    B["KDS 24 14 21 4.7.5.2 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:콘크리트의 최소두께/];

		VarIn1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.5.2 (5)"])
		C --> Variable_def

		Variable_def--원형 속빈부재의 중공 상부--->D
		Variable_def--다른 형태 속빈 부재의 중공 상부--->E
		D["콘크리트의 최소두께=140mm"]
		E["콘크리트의 최소두께=175mm"]
    """

    @rule_method
    def Minimum_concrete_thickness (fOminctA,fOminctB) -> RuleUnitResult:
        """콘크리트의 최소 두께

        Args:
            fOminctA (float): 콘크리트의 최소두께 (원형 속빈부재의 중공 상부)
            fOminctB (float): 콘크리트의 최소두께 (다른 형태 속빈 부재의 중공 상부)

        Returns:
            fOminctA (float): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.3 프리캐스트 슬래브교 (2)의 값 1
            fOminctB (float): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.3 프리캐스트 슬래브교 (2)의 값 2
        """

        fOminctA = 140
        fOminctB = 175

        return RuleUnitResult(
            result_variables = {
                "fOminctA": fOminctA,
                "fOminctB": fOminctB,
            }
        )