import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060501_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.5.1 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '바닥판 설계'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.5 교량의 콘크리트 바닥슬래브
    4.6.5.1 일반 사항
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판 설계];
    B["KDS 24 14 21 4.6.5.1 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:홈 또는 마모 방지 층의 두께/];
		VarIn2[/입력변수:판 최소 두께/];
		VarIn3[/입력변수:프리스트레스트 콘크리트 바닥판의 최소두께/];

		VarIn1 & VarIn2 & VarIn3


		end


	  Python_Class ~~~ C(["KDS 24 14 21 4.6.5.1 (5)"])
		C --> Variable_def

		Variable_def--->F & E--->G
		F{"판 최소두께=콘크리트 바닥판 두께-흠또는 마모방지 층의 두께≥220mm"}
		E{"프리스트레스트 콘크리트 바닥판의 최소두께≥200mm"}
		G(["Pass or fail"])
    """

    @rule_method
    def thickness_of_plate(fIthigwp,fIplamth,fImintpc) -> RuleUnitResult:
        """바닥판 설계

        Args:
            fIthigwp (float): 홈 또는 마모 방지 층의 두께
            fIplamth (float): 판 최소 두께
            fImintpc (float): 프리스트레스트 콘크리트 바닥판의 최소 두께

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.5.1 일반 사항 (5)의 판단 결과
        """

        assert isinstance(fIthigwp, float)
        assert isinstance(fIplamth, float)
        assert isinstance(fImintpc, float)

        if fIplamth-fIthigwp>=220 and fImintpc>=200:
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