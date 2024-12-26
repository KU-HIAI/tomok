import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060501_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.5.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '바닥판 처짐량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.5 교량의 콘크리트 바닥슬래브
    4.6.5.1 일반 사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판 처짐량];
    B["KDS 24 14 21 4.6.5.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:바닥판의 허용처짐량: 사람의 통행이 없는 바닥판/];
		VarIn2[/입력변수:바닥판의 허용처짐량: 제한된 수의 사람이 통행하는 바닥판/];
		VarIn3[/입력변수:바닥판의 허용처짐량: 많은 사람이 통행하는 바닥판/];
		VarIn4[/입력변수:바닥판 지지부재의 중심간 거리/];
		VarOut1[/출력변수:바닥판 처짐량/];

  	VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 ~~~ VarOut1


		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.5.1 (2)"])
		C --> Variable_def

		Variable_def--->F & E & G --> I(["Pass or fail"])
		F{"사람의 통행이 없는 바닥판; L/800"}
		E{"제한된 수의 사람이 통행하는 바닥판; L/1000"}
		G{"많은 사람이 통행하는 바닥판; L/1200"}
    """

    @rule_method
    def floor_design(fIflpadA,fIflpadB,fIflpadC,fIL) -> RuleUnitResult:
        """곡선 긴장재의 영향을 고려한 부재 상세

        Args:
            fIflpadA (float): 바닥판의 허용처짐량 (사람의 통행이 없는 바닥판)
            fIflpadB (float): 바닥판의 허용처짐량 (제한된 수의 사람이 통행하는 바닥판)
            fIflpadC (float): 바닥판의 허용처짐량 (많은 사람이 통행하는 바닥판)
            fIL (float): 바닥판 지지부재의 중심간 거리

        Returns:
            fOflpad (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.5.1 일반 사항 (2)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.5.1 일반 사항 (2)의 판단 결과
        """

        assert isinstance(fIL, float)

        if fIflpadA != 1 and fIflpadB == 0 and fIflpadC == 0 :
          fOflpad <= fIL / 800
          return RuleUnitResult(
              result_variables = {
                  "fOflpad": fOflpad,
              }
          )

        elif fIflpadA == 0 and fIflpadB != 1 and fIflpadC == 0 :
          fOflpad <= fIL / 1000
          return RuleUnitResult(
              result_variables = {
                  "fOflpad": fOflpad,
              }
          )

        elif fIflpadA == 0 and fIflpadB == 0 and fIflpadC != 1 :
          fOflpad <= fIL / 1200
          return RuleUnitResult(
              result_variables = {
                  "fOflpad": fOflpad,
              }
          )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )