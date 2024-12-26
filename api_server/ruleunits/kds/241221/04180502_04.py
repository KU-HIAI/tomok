import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04180502_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5.2 (4)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수];
    B["KDS 24 12 21 4.18.5.2 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수/];
    VarIn1[/입력변수 : 꺽임 혹은 곡선영역의 회전각도/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.5.2 (4)"])
		C --> Variable_def

    H{"수로영역"};
    D["<img src='https://latex.codecogs.com/svg.image?R_{B}=1.0'>"];
    E["<img src='https://latex.codecogs.com/svg.image?R_{B}=1.0&plus;\frac{\theta}{90^{\circ}}'>--------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?R_{B}=1.0&plus;\frac{\theta}{45^{\circ}}'>--------------------------"];
    G(["수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수"]);
    Variable_def--->H--직선영역--->D--->G
    H--전이영역--->E--->G
    H--꺾임/곡선영역--->F--->G
    """

    @rule_method
    def correction_factor_according_to_the_bridge_position_related_to_the_relative_position_of_the_bridge_to_the_waterwqy_area(fIRbA,fIRbB,fIRbC,fIangcur) -> RuleUnitResult:
        """수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수

        Args:
            fIRbA (float): 보정계수 (직선 영역의 경우)
            fIRbB (float): 보정계수 (전이 영역의 경우)
            fIRbC (float): 보정계수 (꺾임/곡선 영역의 경우)
            fIangcur (float): 꺾임 혹은 곡선영역의 회전 각도

        Returns:
            fORb (float): 강교 설계기준(한계상태설계법)  4.18.5.2 항로이탈확률 (4)의 값
        """

        assert isinstance(fIangcur, float)

        if fIRbA != 0 and fIRbB == 0 and fIRbC == 0 :
          fORb = 1.0
          return RuleUnitResult(
              result_variables = {
                  "fORb": fORb,
              }
          )

        if fIRbA == 0 and fIRbB != 0 and fIRbC == 0 :
          fORb = 1 + fIangcur / 90
          return RuleUnitResult(
              result_variables = {
                  "fORb": fORb,
              }
          )

        if fIRbA == 0 and fIRbB == 0 and fIRbC != 0 :
          fORb = 1 + fIangcur / 45
          return RuleUnitResult(
              result_variables = {
                  "fORb": fORb,
              }
          )