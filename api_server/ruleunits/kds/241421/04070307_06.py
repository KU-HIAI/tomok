import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070307_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.3.7 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '시공 중의 응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.3 세그멘탈 공법 교량
    4.7.3.7 연속압출공법 교량
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시공 중의 응력];
    B["KDS 24 14 21 4.7.3.7 (6)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:인장응력/];
		VarIn2[/입력변수:설계기준강도/];

		VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.3.7 (6)"])
		C --> Variable_def

		Variable_def--->D
		D["인장응력≤<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;0.58\sqrt{f_{ck}}'>---------------------------------"]
		D --->E(["Pass or Fail"])
    """

    @rule_method
    def stress_during_construction(fItenstr, fIfck) -> RuleUnitResult:
        """시공 중의 응력

        Args:
            fItenstr (float): 인장응력
            fIfck (float): 설계기준강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.3.7 연속압출공법 교량 (6)의 판단 결과 1
            sOstress (string): 콘크리트교 설계기준 (한계상태설계법)  4.7.3.7 연속압출공법 교량 (6)의 판단 결과 2
        """

        assert isinstance(fItenstr, float)
        assert isinstance(fIfck, float)
        assert fIfck > 0

        if fItenstr <= 0.58 * (fIfck)**0.5:
          return RuleUnitResult(
              result_variables = {
                  "sOstress": "시공 중의 응력에 관해서 시공오차에 의한 하중영향의 1/2과 4.7.3.3에 따른 온도에 의한 하중영향의 1/2이 중력하중에 의한 하중영향에 합산되어야 한다.",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOstress": "시공 중의 응력에 관해서 시공오차에 의한 하중영향의 1/2과 4.7.3.3에 따른 온도에 의한 하중영향의 1/2이 중력하중에 의한 하중영향에 합산되어야 한다.",
                  "pass_fail": False,
              }
          )