import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04050304_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '최대 허용항타응력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.3 말뚝
    4.5.3.4 최대 허용항타응력
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 최대 허용항타응력] ;
		B["KDS 14 31 10 4.5.3.4 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 최대 허용항타력/] ;
      VarIn2[/입력변수: 강재의 항복강도/] ;
      VarIn3[/입력변수: 부재의 총단면적/] ;
      VarIn4[/입력변수: 부재의 순단면적/] ;
			end

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
		Python_Class ~~~ C1(["KDS 14 31 10 4.5.3.4 (2)"]) --> Variable_def

		E["최대 허용항타력<img src=https://latex.codecogs.com/svg.image?\leq&space;0.9F_{y}A_{g}>------------------------------------------"]
		F["최대 허용항타력<img src=https://latex.codecogs.com/svg.image?\leq&space;0.9F_{y}A_{n}>------------------------------------------"]
		C["압축"]
		T["인장"]

		Variable_def --> C & T
		C --> E
		T --> F
		E & F --> Q(["PASS or Fail"])
    """

    @rule_method
    def maximum_permissible_driving_force(fImapedf,fIFy,fIAg,fIAn)-> RuleUnitResult:
        """최대 허용항타응력

        Args:
            fImapedf (float): 최대 허용항타력
            fIFy (float): 강재의 항복강도
            fIAg (float): 부재의 총단면적
            fIAn (float): 부재의 순단면적

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.5.3.4 최대 허용항타응력 (2)의 통과여부
        """

        assert isinstance(fImapedf, float)
        assert isinstance(fIFy, float)
        assert isinstance(fIAg, float)
        assert isinstance(fIAn, float)

        if fIAg != 0 and fIAn == 0:
          if fImapedf <= 0.9 * fIFy * fIAg:
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

        elif fIAg == 0 and fIAn != 0:
          if fImapedf <= 0.9 * fIFy * fIAn:
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
          if fImapedf <= 0.9 * fIFy * fIAn and fImapedf <= 0.9 * fIFy * fIAg:
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