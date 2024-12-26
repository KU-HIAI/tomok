import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011101_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.11.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '중간수직보강재의 돌출폭'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.1 중간수직보강재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 중간수직보강재의 돌출폭] ;
		B["KDS 14 31 10 4.3.3.1.11.1 (2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 중간수직보강재의 돌출폭/] ;
    VarIn2[/입력변수: 웨브의 전체높이/] ;
    VarIn3[/입력변수: 가장 넓은 압축플랜지의 전폭/] ;
    VarIn4[/입력변수: 수직보강재의 두께/] ;
		end

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.1.11.1 (2)"])
		C --> Variable_def

		D{"<img src=https://latex.codecogs.com/svg.image?b_{t}\geq&space;50&plus;\frac{D}{30}>---------------------"}
		E{"<img src=https://latex.codecogs.com/svg.image?16t_{p}\geq&space;b_{t}\geq\frac{b_{f}}{4}>------------------------"}

		Variable_def --> D --> E --> F(["PASS or Fail"])
    """

    @rule_method
    def entrapment_width_of_intermediate_vertical_stiffener(fIbt,fID,fIbf,fItp) -> RuleUnitResult:
        """중간수직보강재의 돌출폭

        Args:
            fIbt (float): 중간수직보강재의 돌출폭
            fID (float): 웨브의 전체높이
            fIbf (float): 가장 넓은 압축플랜지의 전폭
            fItp (float): 수직보강재의 두께

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.1 중간수직보강재 (2)의 판단 결과
        """

        assert isinstance(fIbt, float)
        assert isinstance(fID, float)
        assert isinstance(fIbf, float)
        assert isinstance(fItp, float)

        if fIbt >= 50 + fID / 30 and 16 * fItp >= fIbt >= fIbf / 4:
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