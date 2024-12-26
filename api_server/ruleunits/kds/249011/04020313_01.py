import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020313_01(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.13 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '접촉면에서의 압력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.13 안정성
    (1)
    """
    content = """
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 접촉면에서의 압력];
    B["KDS 24 90 11 4.2.3.13 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 평균압력/];
		VarIn2[/입력변수: 지지 재료의 강도/];

		VarIn1 & VarIn2

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.3.13 (1)"]) --> Variable_def;
		Variable_def--->K--->L
		K["평균압력≤지지 재료의 강도"];

		L(["Pass or Fail"])
    """

    @rule_method
    def Mean_Pressure(fImeapre, fIstrsup) -> RuleUnitResult:
        """접촉면에서의 압력
        Args:
            fImeapre (float): 평균압력
            fIstrsup (float): 지지 재료의 강도

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.3.13 구조물에 가해지는 힘, 모멘트, 변형 (1)의 통과 여부
        """
        assert isinstance(fImeapre, float)
        assert isinstance(fIstrsup, float)

        if fImeapre <= fIstrsup:
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