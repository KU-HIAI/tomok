import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040102(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '구조용 파형강판의 최소두께'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.1 일반사항
    4.5.4.1.2 최소두께
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 구조용 파형강판의 최소두께] ;
		B["KDS 14 31 10 4.5.4.1.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/입력변수: 구조용 파형강판의 두께/] ;
			end

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.4.1.2"]) -->Variable_def

		E{"구조용 파형강판의 두께 ≥ 3.0mm"}

		Variable_def --> E --> D([PASS or Fail])
    """

    @rule_method
    def Minimum_thickness_of_structural_corrugated_steel_plate(fImtscss) -> RuleUnitResult:
        """구조용 파형강판의 최소두께

        Args:
            fImtscss (float): 구조용 파형강판의 두께

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.5.4.1.2 최소두께의 통과여부
        """

        assert isinstance(fImtscss, float)

        if fImtscss >= 3.0 :
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