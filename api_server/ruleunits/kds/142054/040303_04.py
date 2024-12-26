import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040303_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.3 (4)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '인장을 받는 단일 헤드스터드 또는 헤드볼트의 뽑힘강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장을 받는 단일 헤드스터드 또는 헤드볼트의 뽑힘강도];
    B["KDS 14 20 54 4.3.3 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 인장을 받는 단일 헤드스터드 또는 헤드볼트의 뽑힘강도/];
    VarIn2[/입력변수 : 스터드 또는 앵커볼트의 헤드 지압면적/];
    VarIn3[/입력변수 : 콘크리트의 설계기준압축강도/];
    VarIn1
    VarIn1 ~~~ VarIn2 & VarIn3
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.3.3 (4)"])
		C --> Variable_def

    D{"인장을 받는 단일 헤드스터드 또는 헤드볼트의 경우"};
    E{"<img src='https://latex.codecogs.com/svg.image?N_{p}\leq&space;8A_{brg}f_{ck}'>-------------------------------"};
    F(["Pass of Fail"]);
    Variable_def--->D--->E--->F
    """

    @rule_method
    def pullout_strength_of_a_single_head_stud_or_head_bolt_under_tension(fINp,fIAbrg,fIfck) -> RuleUnitResult:
        """인장을 받는 단일 헤드스터드 또는 헤드볼트의 뽑힘강도

        Args:
            fINp (float): 단일 헤드스터드 또는 헤드볼트의 뽑힘강도
            fIAbrg (float): 스터드 또는 앵커볼트의 헤드 지압 면적
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (4)의 판단 결과
        """

        assert isinstance(fINp, float)
        assert isinstance(fIAbrg, float)
        assert isinstance(fIfck, float)

        if fINp <= 8 * fIAbrg * fIfck :
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