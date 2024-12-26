import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_040105_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.5 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '볼트접합에서 끼움재의 두께'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.5 끼움재
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 볼트접합에서 끼움재의 두께]
	  B["KDS 14 31 25 4.1.5 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 끼움재의 두께/]
	  VarIn2[/입력변수: 끼움재의 전체두께/]
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.5 (4)"])
		C --> Variable_def

	  Variable_def --> F --> D --pass-->E
	  F{"6mm < 끼움재 두께 ≤ 19mm"}
	  D["Pass or Fail"]
	  E(["끼움재두께 x<img src='https://latex.codecogs.com/svg.image?\left\lceil&space;1-0.0154(t-6)\right\rceil'>--------------------------------"])
    """

    @rule_method
    def Thickness_of_filler_material_in_bolted_connections(fIthifil,fIt) -> RuleUnitResult:
        """볼트접합에서 끼움재의 두께

        Args:
            fIthifil (float): 끼움재의 두께
            fIt (float): 끼움재의 전체두께

        Returns:
            fOthifil (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.5 끼움재 (4)의 값 1
            fOresfac (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.5 끼움재 (4)의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.5 끼움재 (4)의 판단 결과
        """

        assert isinstance(fIthifil, float)
        assert isinstance(fIt, float)

        fOresfac = 1-0.0154*(fIt-6)

        if 6 < fIthifil <= 19 :
          fOthifil = fOresfac * fIthifil
          return RuleUnitResult(
              result_variables = {
                  "fOthifil": fOthifil,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )