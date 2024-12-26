import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040304_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.4 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '공칭측면파열강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.4 인장력을 받는 앵커의 콘크리트측면파열강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 공칭측면파열강도];
    B["KDS 14 20 54 4.3.4 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수 : 앵커 그룹의 공칭측면파열강도/];
    VarIn2[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn3[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
    VarIn4[/입력변수 : 양 끝에 있는 앵커들 사이의 간격/];
    VarIn5[/입력변수 : 단일 헤드 앵커의 공칭측면파열강도/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.3.4 (2)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?h_{ef}\geq&space;2.5c_{a1}'>이며 앵커간격<6ca1인 앵커그룹인 경우"};
    E{"<img src='https://latex.codecogs.com/svg.image?N_{sbg}\leq\left(1+\frac{s}{6c_{a1}}\right)N_{sb}'>--------------------------------------------"};
    F(["Pass or Fail"]);
    Variable_def--->D--->E--->F
    """

    @rule_method
    def Nominal_lateral_tear_strength(fIhef,fIcaone,fINsbg,fINsb,fIs) -> RuleUnitResult:
        """공칭측면파열강도

        Args:
            fIhef (float): 앵커의 유효묻힘깊이
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리
            fINsbg (float): 앵커 그룹의 공칭측면파열강도
            fINsb (float): 공칭측면파열강도
            fIs (float): 양 끝에 있는 앵커들 사이의 간격

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.3.4 인장력을 받는 앵커의 콘크리트측면파열강도 (2)의 판단 결과
        """

        assert isinstance(fIhef, float)
        assert isinstance(fINsb, float)
        assert isinstance(fIcaone, float)
        assert 0 < fIcaone

        if fIhef >= 2.5 * fIcaone :

          if fINsbg <= (1 + fIs / 6 / fIcaone) * fINsb :
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        return RuleUnitResult(
            result_variables = {
                "pass_fail": False,
            }
        )