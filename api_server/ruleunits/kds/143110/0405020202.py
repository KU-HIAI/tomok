import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405020202(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '핀의 지압강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.2 핀
    4.5.2.2 강도
    4.5.2.2.2 지압
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[핀의 지압강도] ;
		B["KDS 14 31 10 4.5.2.2.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
			VarOut1[/출력변수: 핀의 지압강도/] ;
      VarIn1[/입력변수: 판의 두께/] ;
      VarIn2[/입력변수: 핀의 직경/] ;
      VarIn3[/입력변수: 지압에 댓한 강도저항계수/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.2.2.2"]) --> Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?(R_{pB})_{n}=1.5tDF_{y}>------------------------------------------"]
		F["<img src=https://latex.codecogs.com/svg.image?(R_{pB})_{r}=\phi&space;_{b}(R_{pB})_{n}>------------------------------------------"]

		Variable_def --> E --> F --> D(["<img src=https://latex.codecogs.com/svg.image?(R_{pB})_{r}>-----------------"])
    """

    @rule_method
    def Pin_bearing_strength(fIt,fID,fIphib,fIFy) -> RuleUnitResult:
        """핀의 지압강도

        Args:
            fIt (float): 판의 두께
            fID (float): 핀의 직경
            fIphib (float): 지압에 대한 강도저항계수
            fIFy (float): 핀의 항복강도

        Returns:
            fORpBr (float): 강구조부재설계기준(하중저항계수설계법) 4.5.2.2.2 지압의 값 1
            fORpBn (float): 강구조부재설계기준(하중저항계수설계법) 4.5.2.2.2 지압의 값 2
        """

        assert isinstance(fIt, float)
        assert isinstance(fID, float)
        assert isinstance(fIphib, float)
        assert isinstance(fIFy, float)

        fORpBn = 1.5 * fID * fIFy
        fORpBr = fIphib * fORpBn

        return RuleUnitResult(
          result_variables = {
          "fORpBn": fORpBn,
          "fORpBr": fORpBr,
          }
        )