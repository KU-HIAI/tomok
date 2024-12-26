import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040302_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.2 (7)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '비균열 콘크리트에 사용되는 후설치앵커의 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비균열 콘크리트에 사용되는 후설치 앵커의 수정계수];
    B["KDS 14 20 54 4.3.2 (7)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 비균열 콘크리트에 사용되는 후설치 앵커의 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 위험 연단거리/];
    VarIn3[/입력변수 : 앵커의 유효묻힘깊이/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2 & VarIn3
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.2 (7)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;c_{ac}'>--------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}=1'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}=\frac{c_{a,min}}{c_{ac}}(\geq&space;1.5\frac{h_{ef}}{c_{ac}}))'>-------------------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{cp,N}'>"]);
    Variable_def--->D
    D--Yes--->E--->G
    D--No--->F--->G

    """

    @rule_method
    def modification_factor_of_post_installation_anchor_used_for_uncracked_concrete(fIcamin,fIcac,fIhef) -> RuleUnitResult:
        """비균열 콘크리트에 사용되는 후설치앵커의 수정계수

        Args:
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIcac (float): 위험 연단거리
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            fOpsicpN (float): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (7)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (7)의 판단 결과
        """

        assert isinstance(fIcamin, float)
        assert isinstance(fIcac, float)
        assert isinstance(fIhef, float)
        assert 0 < fIcac

        if fIcamin >= fIcac:
          fOpsicpN = 1.0
        else:
          fOpsicpN = fIcamin / fIcac

        if fOpsicpN >= 1.5 * fIhef / fIcac :
          return RuleUnitResult(
              result_variables = {
                  "fOpsicpN": fOpsicpN,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )