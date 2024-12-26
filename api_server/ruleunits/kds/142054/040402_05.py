import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040402_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.4.2 (5)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-13'
    title = '전단력에 대한 편심을 받는 앵커 그룹에 대한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단력에 대한 편심을 받는 앵커 그룹에 대한 수정계수];
    B["KDS 14 20 54 4.4.2 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 편심을 받는 앵커 그룹에 대한 수정계수/];
    VarIn1[/입력변수 : 앵커 그룹에 작용하는 전단력의 편심/];
    VarIn2[/입력변수 : 앵커 샤프드 중심부터 콘크리트 단부까지의 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.4.2 (5)"])
		C --> Variable_def

    D{"앵커 그룹에서 일부 앵커만이 같은 방향으로 전단력을 받는 경우"};
    E["e'와 Vcbg를 계산할 때 같은 방향으로 전단력을 받는 앵커만을 고려"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,V}=\frac{1}{1&plus;\frac{2e^{,}_{V}}{3c_{a1}}}(\leq&space;1)'>-----------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,V}'>"]);
    Variable_def--->D
    D--Yes--->E---->F
    D--No--->F--->G
    """

    @rule_method
    def Correction_factor_for_anchor_group_that_are_eccentric_to_shear_force(fIeprimV,fIcaone) -> RuleUnitResult:
        """전단력에 대한 편심을 받는 앵커 그룹에 대한 수정계수

        Args:
            fIeprimV (float): 앵커 그룹에 작용하는 전단력의 편심
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리

        Returns:
            fOpsiecV (float): 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (5)의 값
        """

        assert isinstance(fIeprimV, float)
        assert isinstance(fIcaone, float)
        assert fIcaone > 0

        fOpsiecV = min(1/(1+2*fIeprimV / (3*fIcaone)), 1.0)

        return RuleUnitResult(
            result_variables = {
                "fOpsiecV": fOpsiecV,
            }
        )