import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040304(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.3.4'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '휨강도 검토'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.4 휨강도 검토
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 휨강도 검토] ;
		B["KDS 14 31 10 4.5.4.3.4"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 한계상태에서 정점부 설계휨모멘트/] ;
    VarOut2[/출력변수: 한계상태에서 어깨부 설계휨모멘트/] ;
    VarOut3[/출력변수: 소성설계모멘트/] ;
    VarIn1[/입력변수: 소성힌지 저항계수/] ;
    VarIn2[/입력변수: 파형강판의 소성단면계수/] ;
    VarIn3[/입력변수: 파형강판의 항복강도/] ;
		end

		VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3

    Python_Class ~~~ C(["KDS 14 31 10 4.5.4.3.4"])
		C --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?M_{pf}=\phi&space;_{h}ZF_{y}>-----------------------------------"]
		W{"<img src=https://latex.codecogs.com/svg.image?M_{cf}\leq&space;M_{pf}>--------------------------------"}
		R{"<img src=https://latex.codecogs.com/svg.image?M_{hf}\leq&space;M_{pf}>---------------------------------"}

		Variable_def --> Q --> W & R
		W & R --> S(["PASS or Fail"])
    """


    @rule_method
    def bending_moment_evaluation(fIMcf,fIMhf,fIphih,fIZ,fIFy) -> RuleUnitResult:
        """휨강도 검토

        Args:
            fIMcf (float): 한계상태에서 정점부 설계휨모멘트
            fIMhf (float): 한계상태에서 어깨부 설계휨모멘트
            fIphih (float): 소성힌지 저항계수
            fIZ (float): 파형강판의 소성단면계수
            fIFy (float): 파형강판의 항복강도

        Returns:
            fOMpf (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.4 휨강도 검토의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.4 휨강도 검토의 판단 결과
        """

        assert isinstance(fIMcf, float)
        assert isinstance(fIMhf, float)
        assert isinstance(fIphih, float)
        assert isinstance(fIZ, float)
        assert isinstance(fIFy, float)

        fOMpf = fIphih * fIZ * fIFy

        if fIMcf <= fOMpf and fIMhf <= fOMpf:
          return RuleUnitResult(
              result_variables = {
                  "fOMpf": fOMpf,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOMpf": fOMpf,
                  "pass_fail": False,
              }
          )