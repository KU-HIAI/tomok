import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040303_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.3 (5)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도];
    B["KDS 14 20 54 4.3.3 (5)"];
    A ~~~ B
    end
    subgraph Variable_def
	  VarIn1[/입력변수 : 단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도/];
	  VarIn2[/입력변수 : 콘크리트의 설계기준압축강도/];
	  VarIn3[/입력변수 : J 또는 L볼트 샤프트의 안쪽면부터 J또는 L볼트의 바깥쪽 끝까지거리/];
	  VarIn4[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름/];
	  VarIn1 ~~~ VarIn3
	  VarIn2 ~~~ VarIn4

	  end

    Python_Class ~~~ C(["KDS 14 20 54 4.3.3 (5)"])
		C --> Variable_def

    E{"단일 갈고리볼트가 인장력을 받는 경우"};
	  G{"<img src='https://latex.codecogs.com/svg.image?N_{p}\leq&space;0.9f_{ck}e_{h}d_{a}'>--------------------------------"};
	  H(["Pass of Fail"]);
	  I{"<img src='https://latex.codecogs.com/svg.image?3d_{a}\leq&space;e_{h}\leq&space;4.5d_{a}'>----------------------------"};
	  Variable_def--->E--->I--->G--->H
    """

    @rule_method
    def pullout_strength_with_single_hookbolt_under_tensile_force(fINp,fIfck,fIeh,fIda) -> RuleUnitResult:
        """단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도

        Args:
            fINp (float): 단일 갈고리볼트가 인장력을 받는 경우 뽑힘강도
            fIfck (float): 콘크리트의 설계기준압축강도
            fIeh (float): J 또는 L볼트 샤프트의 안쪽면부터 J또는 L볼트의 바깥쪽끝까지 거리
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.3 인장력을 받는 선설치앵커, 후설치 확장앵커 및 언더컷앵커의 뽑힘강도 (5)의 판단 결과
        """

        assert isinstance(fINp, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIeh, float)
        assert isinstance(fIda, float)

        if 3*fIda <= fIeh <= 4.5*fIda :
          if fINp <= 0.9 * fIfck * fIeh * fIda:
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

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )