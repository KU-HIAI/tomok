import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040303_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.3 (6)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '균열 유무에 따른 앵커뽑힘강도에 대한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 균열 유무에 따른 앵커뽑힘강도에 대한 수정계수];
    B["KDS 14 20 54 4.3.3 (6)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 균열 유무에 따른 앵커뽑힘강도에 대한 수정계수/];
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.3.3 (6)"])
		C --> Variable_def

    D{"부재가 사용하중을 받을 때 균열이 발생될 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,P}=1.0'>"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,P}=1.4'>"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,P}'>"]);
    Variable_def--->D
    D--Yes-->E--->G
    D--No--->F--->G
    """

    @rule_method
    def modification_factor_for_anchor_pullout_strength_with_and_without_cracks(fOpsicPA,fOpsicPB) -> RuleUnitResult:
        """균열 유무에 따른 앵커뽑힘강도에 대한 수정계수

        Args:
            fOpsicPA (float): 균열 유무에 따른 앵커뽑힘 강도에 대한 수정계수
            fOpsicPB (float): 균열 유무에 따른 앵커뽑힘 강도에 대한 수정계수 (해석결과 사용하중을 받을 때 균열이 발생될 경우)

        Returns:
            fOpsicPA (float): 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (6)의 값 1
            fOpsicPB (float): 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (6)의 값 2
        """

        if fOpsicPA != 0 and fOpsicPB == 0 :
          fOpsicPA = 1.4
        return RuleUnitResult(
            result_variables = {
                "fOpsicPA": fOpsicPA,
            }
        )

        if fOpsicPA == 0 and fOpsicPB != 0 :
          fOpsicPB = 1.0
        return RuleUnitResult(
            result_variables = {
                "fOpsicPB": fOpsicPB,
            }
        )