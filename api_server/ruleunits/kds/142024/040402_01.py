import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040402_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.4.2 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '절점영역의 공칭강도'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.4 절점영역의 강도
    4.4.2 축강도 산정
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절점영역의 공칭강도];
    B["KDS 14 20 24 4.4.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 절점영역의 공칭강도/];
    VarIn1[/입력변수 : 절점영역의 유효압축강도/];
    VarIn2[/입력변수 : 절점영역 경계면의 면적/];
    VarOut~~~ VarIn1
    VarOut~~~VarIn2
    end

    Python_Class ~~~ C(["KDS 14 20 24 4.4.2 (1)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?&space;F_{nn}=f_{ce}A_{n}'>--------------------------------------------"];
    E(["절점영역의 공칭강도"]);
    Variable_def--->D--->E
    """

    @rule_method
    def nominal_strength_of_nodalzone(fIfce,fIAn) -> RuleUnitResult:
        """타이의 공칭강도

        Args:
            fIfce (float): 스트럿 또는 절점영역의 콘크리트 유효압축강도
            fIAn (float): 절점영역 경계면의 면적

        Returns:
            fOFnn (float): 콘크리트구조 스트럿-타이모델 기준  4.4.2 축강도 산정 (1)의 값
        """

        assert isinstance(fIfce, float)
        assert isinstance(fIAn, float)

        fOFnn = fIfce * fIAn

        return RuleUnitResult(
              result_variables = {
                  "fOFnn": fOFnn,
              }
          )