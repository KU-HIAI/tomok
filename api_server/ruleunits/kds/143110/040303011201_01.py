import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011201_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.12.1 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '덮개판의 길이'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.12 덮개판
    4.3.3.1.12.1 일반사항
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[덮개판의 길이] ;
		B["KDS 14 31 10 4.3.3.1.12.1 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 덮개판의 길이/] ;
      VarIn2[/입력변수: 강재 단면의 전체높이/] ;
    end
    Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.1.12.1 (1)"]) -->Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?L_{cp}\geq&space;2d&plus;900>---------------------"]
    Variable_def --> C --> D(["PASS or Fail"])
    """

    @rule_method
    def cover_plate_length(fILcp,fId) -> RuleUnitResult:
        """덮개판의 길이

        Args:
            fILcp (float): 덮개판의 길이
            fId (float): 강재 단면의 전체높이

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.12.1 일반사항 (1)의 판단 결과
        """

        assert isinstance(fILcp, float)
        assert isinstance(fId, float)


        if fILcp >= 2 * fId + 900:
          return  RuleUnitResult(
            result_variables = {
              "pass_fail": True,
            }
          )
        else:
          return  RuleUnitResult(
            result_variables = {
              "pass_fail": False,
            }
          )