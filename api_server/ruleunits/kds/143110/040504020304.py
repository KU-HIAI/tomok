import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040504020304(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.2.3.4'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '충격계수'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
    4.5.4.2.3.4 충격계수
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 충격계수] ;
		B["KDS 14 31 10 4.5.4.2.3.4"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 충격계수/] ;
      VarIn1[/입력변수: 설계토피고/] ;
			end

		VarOut1 ~~~ VarIn1

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.4.2.3.4"]) --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?i=0.4(1-0.5\times&space;H)\geq&space;0.1>--------------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?i_{min}=0.1>------------------"]

		Variable_def --> W --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?i>--"])
    """


    @rule_method
    def impact_factor(fIH) -> RuleUnitResult:
        """충격계수

        Args:
            fIH (float): 설계토피고

        Returns:
            fOi (float): 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3.4 충격계수의 값
        """

        assert isinstance(fIH, float)

        fOi = max(0.4 * (1 - 0.5 * fIH), 0.1)

        return RuleUnitResult(
            result_variables = {
              "fOi": fOi,
            }
         )