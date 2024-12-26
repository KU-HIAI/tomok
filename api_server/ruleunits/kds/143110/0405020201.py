import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405020201(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '휨과 전단의 조합'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.2 핀
    4.5.2.2 강도
    4.5.2.2.1 휨과 전단의 조합
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 휨과 전단의 조합] ;
		B["KDS 14 31 10 4.5.2.2.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 설계하중에 의한 휨모멘트/] ;
      VarIn2[/입력변수: 핀의 직경/] ;
      VarIn3[/입력변수: 핀의 항복강도/] ;
      VarIn4[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn5[/입력변수: 설계하중에 의한 전단력/] ;
      VarIn6[/입력변수: 전단에 대한 강도저항계수/] ;

			end
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.2.2.1"])--> Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?\frac{6.0M_{u}}{\phi&space;_{f}D^{3}F_{y}}&plus;\left(\frac{2.2V_{u}}{\phi&space;_{v}D^{2}F_{y}}\right)^{3}\leq&space;0.95>------------------------------------------"]

		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def combination_of_bending_and_shear(fIMu,fID,fIFy,fIphif,fIVu,fIphiv) -> RuleUnitResult:
        """휨과 전단의 조합

        Args:
            fIMu (float): 설계하중에 의한 휨모멘트
            fID (float): 핀의 직경
            fIFy (float): 핀의 항복강도
            fIphif (float): 휨에 대한 강도저항계수
            fIVu (float): 설계하중에 의한 전단력
            fIphiv (float): 전단에 대한 강도저항계수

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.5.2.2.1 휨과 전단의 조합의 통과여부
        """

        assert isinstance(fIMu, float)
        assert isinstance(fID, float) and fID != 0
        assert isinstance(fIFy, float) and fIFy != 0
        assert isinstance(fIphif, float) and fIphif != 0
        assert isinstance(fIVu, float)
        assert isinstance(fIphiv, float) and fIphiv != 0



        if (6.0 * fIMu) / (fIphif * fID ** 3 * fIFy) + ((2.2 * fIVu) / (fIphiv * fID ** 2 * fIFy)) ** 3 <= 0.95:
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