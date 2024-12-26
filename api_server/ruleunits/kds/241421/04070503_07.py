import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070503_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.5.3 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '종방향 시공이음'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.3 프리캐스트 슬래브교
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 시공이음];
    B["KDS 24 14 21 4.7.5.3 (7)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:무수축 모르터 압축강도/];
		VarIn2[/입력변수:키의 깊이/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.5.3 (7)"])
		C --> Variable_def

		Variable_def--->D--->E

		D["무수축 모르터 압축강도>=35MPa"]
		E["165mm≤키의 깊이"]
    """

    @rule_method
    def longitudinal_construction_joint(fIcssfmo, fIkeydep) -> RuleUnitResult:
        """종방향 시공이음
        Args:
            fIcssfmo (float): 24시간 내의 무수축 모르터 압축강도
            fIkeydep (float): 키의 깊이

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.3 프리캐스트 슬래브교 (7)의 판단 결과
        """

        assert isinstance(fIcssfmo, float)
        assert isinstance(fIkeydep, float)

        if fIcssfmo >= 35 and fIkeydep >= 165:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )