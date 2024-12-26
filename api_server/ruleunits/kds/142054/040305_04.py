import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040305_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.5 (4)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '단일 부착식 앵커 또는 부착식 앵커 그룹의 가장자리 영향에 관한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title:단일 부착식 앵커 또는 부착식 앵커그룹의 가장자리영향에관한 수정계수];
    B["KDS 14 20 54 4.3.5 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 단일 부착식 앵커 또는 부착식 앵커그룹의 가장자리영향에관한 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적가장자리까지의 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.5 (4)"])
		C --> Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;c_{Na}'>-----------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}=1.0'>----------------"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}=0.7+0.3\frac{c_{a,min}}{c_{Na}}'>-----------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}'>"])
    Variable_def--->D
    D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def correction_factor_for_edge_influence_of_single_or_group_of_anchor(fIcamin,fIcNa) -> RuleUnitResult:
        """단일 부착식 앵커 또는 부착식 앵커 그룹의 가장자리 영향에 관한 수정계수

        Args:
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIcNa (float): 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리

        Returns:
            fOpsedNa (float): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 판단 결과
        """

        assert isinstance(fIcamin, float)
        assert isinstance(fIcNa, float)
        assert 0 < fIcNa

        if fIcamin >= fIcNa:
          fOpsedNa = 1.0
        else:
          fOpsedNa = 0.7 + 0.3 * fIcamin / fIcNa

        return RuleUnitResult(
            result_variables = {
                "fOpsedNa": fOpsedNa,
            }
        )