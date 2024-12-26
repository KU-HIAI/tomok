import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020702_08(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.7.2 (8)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '볼트구멍 중심으로부터 연단까지의 최대거리'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.7 연결 이음부 설계
    4.2.7.2 볼트 이음부 설계
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 볼트구멍 중심으로부터 연단까지의 최대거리];
    B["KDS 24 90 11 4.2.7.2 (8)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 볼트구멍 중심으로부터 연단까지의 최대거리/];
		VarIn2[/입력변수: 표면의 판 두께/];

		VarIn1 & VarIn2

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.7.2 (8)"])
		C --> Variable_def;

		Variable_def---> F---->D--->E
		F["볼트구멍 중심으로부터 연단까지의 최대거리=표면의 판 두께x8"];
		D{"볼트구멍 중심으로부터 연단까지의 최대거리≤150mm"};
		E(["Pass or Fail"])
    """

    @rule_method
    def Maximum_Distance_From_The_Center_Of_The_Bolt_Hole_To_The_Podium(fImdfcbp,fIplthos) -> RuleUnitResult:
        """볼트구멍 중심으로부터 연단까지의 최대거리
        Args:
            fImdfcbp (float): 볼트구멍 중심으로부터 연단까지의 최대거리
            fIplthos (float): 표면의 판 두께

        Returns:
            pass_fail (bool):  교량 기타시설설계기준 (한계상태설계법) 4.2.7.2 볼트 이음부 설계 (8)의 판단 결과
        """

        assert isinstance(fImdfcbp, float)
        assert isinstance(fIplthos, float)

        if fImdfcbp == 8 * fIplthos and fImdfcbp <= 150:
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