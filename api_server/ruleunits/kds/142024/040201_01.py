import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040201_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.2.1 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '콘크리트 스트럿의 공칭압축강도'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.2 스트럿의 축강도
    4.2.1 축강도 산정
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 스트럿의 공칭압축강도];
    B["KDS 14 20 24 4.2.1 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 콘크리트 스트럿의 공칭압축강도/];
		VarIn1[/입력변수 : 콘크리트 스트럿 양단부의 강도/];
		VarIn2[/입력변수 : 스트럿 양단부 최소 단면적/];
		VarIn3[/입력변수 : 콘크리트 스트럿의 유효압축강도/];
		VarOut ~~~VarIn1
		VarOut ~~~VarIn2
		VarOut ~~~VarIn3
    end

		Python_Class ~~~ C(["KDS 14 20 24 4.2.1 (1)"])
		C --> Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?F_{ns}='>min(<img src='https://latex.codecogs.com/svg.image?f_{ce}A_{c}'>,콘크리트 스트럿 양단부의 강도)"]
		Variable_def--->D--->E(["콘크리트 스트럿의 공칭압축강도"])
    """

    @rule_method
    def nominal_compressive_strength_of_a_concrete_strut(fIAcmin,fIfce) -> RuleUnitResult:
        """콘크리트 스트럿의 공칭압축강도

        Args:
            fIAcmin (float): 스트럿 양단부 최소 단면적
            fIfce (float): 콘크리트 스트럿의 유효압축강도

        Returns:
            fOFns (float): 콘크리트구조 스트럿-타이모델 기준  4.2.1 축강도 산정 (1)의 값
        """

        assert isinstance(fIAcmin, float)
        assert isinstance(fIfce, float)

        fOFns = fIAcmin*fIfce

        return RuleUnitResult(
              result_variables = {
                  "fOFns": fOFns,
              }
          )