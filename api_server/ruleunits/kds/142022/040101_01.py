import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_040101_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.1.1 (1)'
    ref_date = '2022-01-11'
    doc_date = '2024-06-27'
    title = '전단강도'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.1 전단설계 원칙
    4.1.1 전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단강도];
    B["KDS 14 20 22 4.1.1 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 단면의 공칭전단강도/];
    VarIn1[/입력변수: 단면에서 계수전단력/];
    VarIn2[/입력변수: 비횡구속 골조의 모멘트확대계수/];
    VarIn3[/입력변수: 콘크리트에 의한 단면의 공칭전단강도/];
    VarIn4[/입력변수: 전단철근에 의한 단면의 공칭전단강도/];
    end
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

    Python_Class ~~~ C(["KDS 14 20 22 4.1.1 (1)"])
		C --> Variable_def

		Variable_def --> D --> E --> F

		D["<img src='https://latex.codecogs.com/svg.image? V_{n}=V_{c}+V_{s}'>-----------------------------"];
		E{"<img src='https://latex.codecogs.com/svg.image? V_{u}\leq \phi V_{n}'>-----------------------------"};

		F(["Pass or Fail"])
    """

    @rule_method
    def shear_strength(fIVu,fIphi,fIVc,fIVs) -> RuleUnitResult:
        """전단강도

        Args:
            fIVu (float): 단면에서 계수전단력
            fIphi (float): 강도감소계수
            fIVc (float): 콘크리트에 의한 단면의 공칭전단강도
            fIVs (float): 전단철근에 의한 단면의 공칭전단강도


        Returns:
            fOVn (float): 단면의 공칭전단강도
            pass_fail (bool): 콘크리트구조 전단 및 비틀림 설계기준  4.1.1 전단강도 (1)의 판단 결과
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIphi, float)
        assert isinstance(fIVc, float)
        assert isinstance(fIVs, float)


        fOVn = fIVc + fIVs

        if fIVu <= fIphi * fOVn:
          return RuleUnitResult(
              result_variables = {
                  "fOVn": fOVn,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOVn": fOVn,
                  "pass_fail": False,
              }
          )