import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.3 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '공칭뽑힘강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 공칭뽑힘강도];
    B["KDS 14 20 54 4.3.3 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 공칭뽑힘강도/];
    VarIn2[/입력변수 : 균열 유무에 따른 앵커뽑힘강도에 대한수정계수/];
    VarIn3[/입력변수 : 균열 콘크리트에서 인장을 받는 단일앵커의 뽑힘강도/];
    VarIn1~~~VarIn3
    VarIn2~~~VarIn3
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.3 (1)"])
		C --> Variable_def

    D{"인장력을 받는 단일 선설치앵커, 후설치 확장앵커 및 언더컷앵커인 경우"}
    E{"<img src='https://latex.codecogs.com/svg.image?N_{pn}\leq\psi&space;_{c,P}N_{p}'>-------------------------"};
    Variable_def--->D--->E--->F(["Pass or Fail"]);
    """

    @rule_method
    def nominal_pullout_strength(fINpn,fIpsicP,fINp) -> RuleUnitResult:
        """공칭뽑힘강도

        Args:
            fINpn (float): 공칭뽑힘강도
            fIpsicP (float): 균열 유무에 따른 앵커뽑힘강도에 대한 수정계수
            fINp (float): 균열 콘크리트에서 인장을 받는 단일앵커의 뽑힘강도

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (1)의 판단 결과
        """

        assert isinstance(fINpn, float)
        assert isinstance(fIpsicP, float)
        assert isinstance(fINp, float)

        if fINpn <= fIpsicP * fINp:
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