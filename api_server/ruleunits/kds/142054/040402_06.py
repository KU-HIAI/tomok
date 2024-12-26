import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040402_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.4.2 (6)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-13'
    title = '전단을 받는 단일 앵커 또는 앵커 그룹의 가장자리 효과에 대한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단을 받는 단일 앵커 또는 앵커 그룹의 가장자리 효과에 대한 수정계수];
    B["KDS 14 20 54 4.4.2 (6)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 가장자리 효과에 대한 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트 단부까지 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.4.2 (6)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?c_{a2}\geq&space;1.5c_{a1}'>-------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,V}=1.0'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,V}=0.7&plus;0.3\frac{c_{a2}}{1.5c_{a1}}'>------------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,V}'>"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def Correction_factor_for_edge_effect_of_a_single_anchor_or_anchor_group_receiving_shear(fIcaone,fIcatwo) -> RuleUnitResult:
        """전단을 받는 단일 앵커 또는 앵커 그룹의 가장자리 효과에 대한 수정계수

        Args:
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리
            fIcatwo (float): 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트 단부까지 거리

        Returns:
            fOpsiedV (float): 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (6)의 값
        """

        assert isinstance(fIcaone, float)
        assert fIcaone > 0
        assert isinstance(fIcatwo, float)

        if fIcatwo >= 1.5*fIcaone:
          fOpsiedV = 1.0
          return RuleUnitResult(
              result_variables = {
                  "fOpsiedV": fOpsiedV,
              }
          )

        else :
          fOpsiedV = 0.7 + 0.3 * fIcatwo / (1.5*fIcaone)
          return RuleUnitResult(
              result_variables = {
                  "fOpsiedV": fOpsiedV,
              }
          )