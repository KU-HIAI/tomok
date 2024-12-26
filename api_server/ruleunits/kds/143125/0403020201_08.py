import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020201_08(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.1 (8)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '겹침접합'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.1 적용한계
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 겹침접합]
	  B["KDS 14 31 25 4.3.2.2.1 (8)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 형상비/] ;
	  VarIn1[/입력변수: 높이와 폭의 비/]
		VarOut1 ~~~ VarIn1
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.1 (8)"])
		C --> Variable_def

	  D{"<img src='https://latex.codecogs.com/svg.image?O_{v}=(q/p)\times&space;100%'>-----------------------------------"} ;
    E{"<img src='https://latex.codecogs.com/svg.image?25%\leq&space;O_{v}\leq&space;100%'>-----------------------------------"} ;
    Variable_def -->D-->E-->Q(["PASS or Fail"])
    """

    @rule_method
    def overlap_junction(fIp,fIq) -> RuleUnitResult:
        """겹침접합

        Args:
            fIp (float): 주강관에 대한 겹치는 지강관의 투영길이
            fIq (float): 주강관의 접촉면에서 측정한 겹친 길이

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.1 적용한계 (8)의 판단 결과
            fOOv (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.1 적용한계 (8)의 값
        """

        assert isinstance(fIp, float)
        assert fIp != 0
        assert isinstance(fIq, float)

        fOOv = (fIq/fIp)*100

        if 25 <= fOOv <= 100:
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