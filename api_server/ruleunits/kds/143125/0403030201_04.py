import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030201_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.1 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '압축 지강관의 벽세장비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.1 적용한계
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 압축 지강관의 벽세장비]
	  B["KDS 14 31 25 4.3.3.2.1 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 압축 지강관의 벽세장비/] ;
    VarIn1[/입력변수: 벽의 폭두께비/] ;
    VarIn2[/입력변수: 강재의 탄성계수/] ;
    VarIn3[/입력변수: 지강관의 항복강도/] ;
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.1 (4)"])
		C --> Variable_def

	  C{"벽의 폭두께비 ≤ <img src='https://latex.codecogs.com/svg.image?1.25(E/F_{yb})^{0.5} or 35 '>---------------------------------------"} ;
    Variable_def-->C-->D(["PASS or Fail"])
    """

    @rule_method
    def Slenderness_ratio_of_compressive_branch_member_wall(fIsrcbmw,fIE,fIFyb) -> RuleUnitResult:
        """압축 지강관의 벽세장비

        Args:
            fIsrcbmw (float): 압축 지강관의 벽세장비
            fIE (float) : 강재의 탄성계수
            fIFyb (float) : 지강관의 항복강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.1 적용한계 (4)의 판단 결과
        """

        assert isinstance(fIsrcbmw, float)
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIFyb, float)
        assert fIFyb > 0

        if fIsrcbmw <= 1.25*(fIE/fIFyb)**0.5 and fIsrcbmw <= 35:
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