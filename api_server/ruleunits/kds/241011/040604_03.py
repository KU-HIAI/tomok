import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_040604_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.4 (3)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '교축방향 스트립의 등가폭'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.4 슬래브교에 대한 등가 스트립 폭
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 교축방향 스트립의 등가폭];
    B["KDS 24 10 11 4.6.4 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 등가폭/];
    VarIn1[/입력변수 : 실제 지간장/];
    VarIn2[/입력변수 : 실제 교폭/];
    VarIn3[/입력변수 : KDS 24 12 21 4.3.1.1에 규정된 재하차로 수/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.4 (3)"])
		C --> Variable_def

    D["L1=Min(실제 지간장,18,000mm)"];
    G["W1=Min(실제 교폭, 18,000mm)"];

    I["<img src='https://latex.codecogs.com/svg.image?E=1.1(2100+0.12\sqrt{L_{1}W_{1}})(\leq\frac{W}{N_{L}}'>----------------------------------------------"];
    J(["교축방향 스트립의 등가폭"]);

    Variable_def--->D

    D-->2이상--->G--->I--->J
    """

    @rule_method
    def equivalent_width_of_longitudinal_strip(fILactsp,fIW,fINL) -> RuleUnitResult:
        """교축방향 스트립의 등가폭

        Args:
            fILactsp (float): 실제 지간장
            fIW (float): 실제 교폭
            fINL (float): 재하차로 수

        Returns:
            fOE (float): 교량 설계 일반사항(한계상태설계법)  4.6.4 슬래브교에 대한 등가 스트립 폭 (3)의 값
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법)  4.6.4 슬래브교에 대한 등가 스트립 폭 (3)의 판단 결과
        """

        assert isinstance(fILactsp, float)
        assert fILactsp >= 0
        assert isinstance(fIW, float)
        assert fIW >= 0
        assert isinstance(fINL, float)
        assert fINL >= 2

        if fINL >= 2 :
          fOE = 1.1 * (2100 + 0.12 * (min(fILactsp,18000) * min(fIW,18000))**0.5)
          if fOE <= fIW / fINL:
            return RuleUnitResult(
                result_variables = {
                    "fOE": fOE,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )