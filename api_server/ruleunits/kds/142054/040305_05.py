import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040305_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.5 (5)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '비균열 콘크리트에 사용되는 부착식 앵커의 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비균열 콘크리트에 사용되는 부착식 앵커의 수정계수];
    B["KDS 14 20 54 4.3.5 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 비균열 콘크리트에 사용되는 부착식 앵커의 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 :  위험 연단거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.5 (5)"])
		C --> Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;c_{Na}'>-----------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}=1.0'>----------------"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}=\frac{c_{a,min}}{c_{ac}}'>-----------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}'>"])
    Variable_def--->D
    D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def Modification_factors_for_bonded_anchors_used_in_uncracked_concrete(fIcamin,fIcac) -> RuleUnitResult:
        """비균열 콘크리트에 사용되는 부착식 앵커의 수정계수

        Args:
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIcac (float): 위험 연단거리

        Returns:
            fOpsedNa (float): 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (5)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (5)의 판단 결과
        """

        assert isinstance(fIcamin, float)
        assert isinstance(fIcNa, float)
        assert 0 < fIcNa

        if fIcamin >= fIcNa:
          fOpsedNa = 1.0
        else:
          fOpsedNa = fIcamin / fIcac

        return RuleUnitResult(
            result_variables = {
                "fOpsedNa": fOpsedNa,
            }
        )