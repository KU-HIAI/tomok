import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030101_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.1.1 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '압축 지강관벽의 세장비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    4.3.3.1.1 적용한계
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 압축 지강관벽의 세장비]
	  B["KDS 14 31 25 4.3.3.1.1 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 압축 지강관벽의 세장비/]
	  VarIn2[/입력변수: 강재의 탄성계수/]
	  VarIn3[/입력변수: 강재의 항복강도/]
		VarIn1 & VarIn2 & VarIn3
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.1.1 (4)"])
		C --> Variable_def

	  D{"압축 지강관벽의 세장비≤  <img src='https://latex.codecogs.com/svg.image?0.05E/F_{y}'>----------------------------------------------"} ;
		Variable_def --> D
		D-->E(["Pass or Fail"])
    """

    @rule_method
    def Slenderness_ratio_of_branch_member_wall_in_compression(fIsrcbmw,fIE,fIFy) -> RuleUnitResult:
        """압축 지강관벽의 세장비

        Args:
            fIsrcbmw (float): 압축 지강관벽의 세장비
            fIE (float): 강재의 탄성계수
            fIFy (float): 강재의 항복강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1.1 적용한계 (4)의 판단 결과
        """

        assert isinstance(fIsrcbmw, float)
        assert isinstance(fIE, float)
        assert isinstance(fIFy, float)
        assert fIFy != 0

        if fIsrcbmw <= 0.05 * fIE / fIFy:
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