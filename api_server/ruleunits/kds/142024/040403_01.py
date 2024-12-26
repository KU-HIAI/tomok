import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040403_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.4.3 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '단면력에 의한 절점영역 경계면의 유효압축강도'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.4 절점영역의 강도
    4.4.3 유효압축강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단면력에 의한 절점영역 경계면의 유효압축강도];
    B["KDS 14 20 24 4.4.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 유효묻힘깊이/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최대 연단거리/];
    VarIn2[/입력변수 : 최대 앵커 간격/];
    end

    Python_Class ~~~ C(["KDS 14 20 24 4.4.3 (1)"])
		C --> Variable_def

    D{"앵커가 세개 또는 네개의 가장자리부터 1.5hef보다 짧은 거리에 위치한 경우"};
    E{"앵커 그룹인 경우"};
    F["<img src='https://latex.codecogs.com/svg.image?h_{ef}=\frac{c_{a,max}}{1.5}'>와 최대앵커간격/3 중 큰 값"];
    G["<img src='https://latex.codecogs.com/svg.image?h_{ef}=\frac{c_{a,max}}{1.5}'>"];
    H(["<img src='https://latex.codecogs.com/svg.image?A_{Nc}'>와 식(4.3-2)~식(2.3-9)까지 적용"]);

    Variable_def--->D--->E--Yes--->F--->H
    E--No--->G--->H
    """

    @rule_method
    def effective_compressive_strength_of_the_boundary_surface_of_the_node_region_by_cross_sectional_force(fIfce,fIbetan,fIfck) -> RuleUnitResult:
        """단면력에 의한 절점영역 경계면의 유효압축강도

        Args:
            fIfce (float): 유효압축강도
            fIbetan (float): 타이의 정착영향을 고려하기 위한 계수
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            pass_fail (bool): 콘크리트구조 스트럿-타이모델 기준  4.4.3 유효압축강도 (1)의 판단 결과
        """

        assert isinstance(fIfce, float)
        assert isinstance(fIbetan, float)
        assert isinstance(fIfck, float)

        if fIfce <= 0.85 * fIbetan * fIfck:
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