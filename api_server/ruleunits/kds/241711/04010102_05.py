import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04010102_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.1.1.2 (5)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '유효수평지반가속도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.1 설계일반사항
    4.1.1 설계지반운동
    4.1.1.2 지진위험도 및 유효수평지반가속도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 지진위험도 및 유효수평지반가속도] ;
		B["KDS 24 17 11 4.1.1.2 (5)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 유효수평지반가속도/] ;
		VarIn1[/입력변수: 지진구역계수/] ;
		VarIn2[/입력변수: 평균재현주기의 위험도계수/] ;
		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
		end

		Python_Class ~~~ C(["KDS 24 17 11 4.1.1.2 (5)"])
		C --> Variable_def

		D{국가지진위험지도를 이용하여 결정하는 경우}

		F{"<img src='https://latex.codecogs.com/svg.image?&space;S\geq&space;0.8\times&space;Z\times&space;I'>--------------------------"};

		E([PASS or Fail]) ;

		Variable_def --> D --> F --> E
    """

    @rule_method
    def effective_horizontal_ground_acceleration(fIS,fIZ,fII) -> RuleUnitResult:
        """유효수평지반가속도


        Args:
            fIS (float): 유효수평지반가속도
            fIZ (float): 지진구역계수
            fII (float): 평균재현주기의 위험도계수

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.1.1.2 지진위험도 및 유효수평지반가속도 (5)의 판단 결과
        """

        assert isinstance(fIZ, float)
        assert isinstance(fII, float)
        assert isinstance(fIS, float)


        if fIS >= fIZ * fII * 0.8 :
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