import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03040506(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.4.5.6'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '확대선단부'

    description = """
    3. 설계
    3.4 현장타설말뚝
    3.4.5 현장타설말뚝의 구조세목
    3.4.5.6 확대선단부
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 확대선단부];
    B["KDS 24 14 51 3.4.5.6"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수:각도/]
		VarIn2[/입력변수:바닥면의 지름/]
		VarIn3[/입력변수:말뚝지름/]
		VarIn4[/입력변수:확대선단부의 바닥 가장자리 두께/]

		VarIn1 ~~~ VarIn2
		VarIn3 ~~~ VarIn4

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.4.5.6"])
		C --> Variable_def

		G{30° 이하의 각도}
		D{바닥면의 지름 ≤ 말뚝지름의 3배}
		F{확대 선단부의 바닥 가장자리 두께 ≥ 150mm}
		E([Pass or Fail])
		Variable_def ---> G & D & F ---> E
    """

    @rule_method
    def Enlarged_Shear(fIangle,fIdiaflo,fIdiasta,fIbotthi) -> RuleUnitResult:
        """확대선단부

        Args:
            fIangle (float): 각도
            fIdiaflo (float): 바닥면의 지름
            fIdiasta (float): 말뚝지름
            fIbotthi (float): 확대선단부의 바닥 가장자리 두께

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.4.5.6 확대선단부의 판단 결과
        """

        assert isinstance(fIangle, float)
        assert isinstance(fIdiaflo, float)
        assert isinstance(fIdiasta, float)
        assert isinstance(fIbotthi, float)

        if fIangle <= 30 and fIdiaflo<= 3*fIdiasta and fIbotthi >= 150:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )
        else :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
                  }
              )