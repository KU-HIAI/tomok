import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_0401_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.1 (7)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-18'
    title = '콘크리트 설계기준압축강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.1 설계 일반
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 설계기준압축강도];
    B["KDS 14 20 54 4.1 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 콘크리트 설계기준압축강도/];
    VarIn1
    end
    Python_Class~~~C(["KDS 14 20 54 4.1 (7)"]) --->Variable_def --->D

    D{"앵커설치 방법"};
    E["<img src='https://latex.codecogs.com/svg.image?&space;f_{ck}\leq70MPa'>--------------------"];
    F{"<img src='https://latex.codecogs.com/svg.image?&space;f_{ck}\leq55MPa'>--------------------"};
    G([PASS or Fail]);

    D--선설치--->E
    D--후설치--->F
    E & F--->G
    """

    @rule_method
    def Design_standard_compressive_strength_of_concrete(fIfckA,fIfckB) -> RuleUnitResult:
        """콘크리트 설계기준압축강도

        Args:
            fIfckA (float): 설계기준 압축강도 "(선설치)"
            fIfckB (float): 설계기준 압축강도 "(후설치)"

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.1 설계 일반 (7)의 판단 결과
        """

        assert isinstance(fIfckA, float)
        assert isinstance(fIfckB, float)

        if fIfckA !=0 and fIfckB == 0 :
          if fIfckA <= 70:
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
          if fIfckA <= 55:
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