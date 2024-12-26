import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040302_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.2 (4)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수];
    B["KDS 14 20 54 4.3.2 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수/];
    VarIn1[/입력변수 : 인장하중을 받는 앵커 그룹에 작용하는 인장력의 합력과 앵커 그룹 도심사이의 거리/];
    VarIn2[/입력변수 : 앵커의 유효묻힘깊이/];
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.2 (4)"])
		C --> Variable_def

    D{"두 축에 대하여 편심하중이 존재하는 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,N}=\frac{1}{\left(1&plus;\frac{2e_{N}^{,}}{3h_{ef}}\right)}(\leq&space;1)'>---------------------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,N}=\frac{1}{\left(1&plus;\frac{2e_{N}^{,}}{3h_{ef}}\right)}(\leq&space;1)'>각 축에 대해 독립적으로 계산후 곱합"];
    G(["인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수"]);
    Variable_def--->D--Yes--->F--->G
    D--No --->E--->G
    """

    @rule_method
    def Modification_factor_for_anchor_group_under_eccentric_tensile(fIeprimN,fIhef) -> RuleUnitResult:
        """인장력의 편심이 작용하는 앵커 그룹에 대한 수정계수

        Args:
            fIeprimN (float): 인장하중을 받는 앵커 그룹에 작용하는 인장력의 합력과 앵커 그룹 도심 사이의 거리
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            fOpsiecN (float): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 판단 결과
        """

        assert isinstance(fIeprimN, float)
        assert 0 < fIeprimN
        assert isinstance(fIhef, float)
        assert 0 < fIhef

        fOpsiecN = 1 / (1 + (2 * fIeprimN) / (3 * fIhef))

        if fOpsiecN <= 1 :
          return RuleUnitResult(
              result_variables = {
                  "fOpsiecN": fOpsiecN,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )