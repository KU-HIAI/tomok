import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060604_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.6.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '나선철근의 순간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.4 나선철근 상세
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 나선철근의 순간격];
    B["KDS 24 14 21 4.6.6.4 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:나선철근의 순간격/];
		VarIn2[/입력변수:굵은골재 최대치수/];
		VarIn3[/입력변수:나선철근 중심간의 간격/];
		VarIn4[/입력변수:축방향 철근 지름/];


		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.6.4 (3)"])
		C --> Variable_def

		Variable_def---> F & G
		F{"나선철근의 순간격≥max(25mm, 굵은골재 최대치수 X1.33)"}
		G{"나선철근 중심간의 간격≤min(축방향 철근 지름X6, 150mm)"}
		F & G ---> H(["Pass or Fail"])
    """

    @rule_method
    def Instantaneous_gap_of_spiral_reinforcement(fIIncabe,fIcoaagr,fIspabcs,fIaxibar) -> RuleUnitResult:
        """나선철근의 순간격

        Args:
            fIIncabe (float): 나선철근의 순간격
            fIcoaagr (float): 굵은골재 최대치수
            fIspabcs (float): 나선철근 중심간의 간격
            fIaxibar (float): 축방향 철근 지름

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.6.4 나선철근 상세 (3)의 판단 결과
        """

        assert isinstance(fIIncabe, float)
        assert isinstance(fIcoaagr, float)
        assert isinstance(fIspabcs, float)
        assert isinstance(fIaxibar, float)

        if fIIncabe >= max(25, fIcoaagr*1.33) and fIspabcs <= min(fIaxibar*6, 150) :
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