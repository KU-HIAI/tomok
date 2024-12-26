import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040305_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.5 (3)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '인장력의 편심이 작용하는 부착식앵커 그룹에 대한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력의 편심이 작용하는 부착식앵커 그룹에 대한 수정계수];
    B["KDS 14 20 54 4.3.5 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 인장력의 편심이 작용하는 부착식 앵커그룹에대한수정계수/];
    VarIn1[/입력변수 : 인장하중을 받는 앵커그룹에 작용하는 인장력의 합력과 앵커그룹도심사이의 거리/];
    VarIn2[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적가장자리까지의 거리 /];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.3.5 (3)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,Na}=\frac{1}{(1&plus;\frac{e^{,}_{N}}{c_{Na}})}(\leq&space;1)'>-------------------------------------------"];
    E(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,Na}'>"]);
    Variable_def--->D--->E
    """

    @rule_method
    def correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force(fIeprimN,fIcNa) -> RuleUnitResult:
        """인장력의 편심이 작용하는 부착식앵커 그룹에 대한 수정계수

        Args:
            fIeprimN (float): 인장하중을 받는 앵커 그룹에 작용하는 인장력의합력과 앵커그룹 도심사이의 거리
            fIcNa (float): 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리

        Returns:
            fOpsecNa (float): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (3)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (3)의 판단 결과
        """

        assert isinstance(fIeprimN, float)
        assert 0 < fIeprimN
        assert isinstance(fIcNa, float)
        assert 0 < fIcNa

        fOpsecNa = 1 / (1+(fIeprimN/fIcNa))

        if fOpsecNa <= 1 :
          return RuleUnitResult(
              result_variables = {
                  "fOpsecNa": fOpsecNa,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )