import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040302_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.2 (5)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '인장력을 받는 단일 앵커 또는 앵커 그룹의 가장자리 영향에 관한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력을 받는 단일 앵커 또는 앵커 그룹의 가장자리 영향에 관한 수정계수];
    B["KDS 14 20 54 4.3.2 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 인장력을 받는 단일 앵커 또는 앵커 그룹의 가장자리 영향에 관한 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘ㄴ크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 앵커의 유효묻힘깊이/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.2 (5)"]);
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;1.5h_{ef}'>--------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,N}=1'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,N}=0.7&plus;0.3(\frac{c_{a,min}}{1.5h_{ef}})'>-------------------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,N}'>"]);
    Variable_def--->D
    D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def modification_factor_of_the_effect_of_anchor(fIcamin,fIhef) -> RuleUnitResult:
        """인장력을 받는 단일 앵커 또는 앵커 그룹의 가장자리 영향에 관한 수정계수

        Args:
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            fOpsiedN (float): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (5)의 값
        """

        assert isinstance(fIcamin, float)
        assert isinstance(fIhef, float)
        assert 0 < fIhef

        if fIcamin >= 1.5 * fIhef:
          fOpsiedN = 1
        else:
          fOpsiedN = 0.7 + 0.3 * (fIcamin / (1.5 * fIhef))

        return RuleUnitResult(
            result_variables = {
                "fOpsiedN": fOpsiedN,
            }
        )