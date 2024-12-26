import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020203_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '접합평면과 90를 이루는 각형 지강관의 폭'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 접합평면과 90를 이루는 각형 지강관의 폭]
	  B["KDS 14 31 25 4.3.2.2.3 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarIn1[/입력변수: 접합평면과 90º를 이루는 각형 지강관의 폭/] ;
		VarIn2[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
		VarIn3[/입력변수: 주강관 세장비/] ;
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.3 (1)"])
		C --> Variable_def

	  E{"<img src='https://latex.codecogs.com/svg.image?B_{b}/B\geq&space;0.1&plus;\gamma/50'>-----------------------------------------------------------------------"} ;

		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def The_width_of_the_rectangular_branch_pipe_making_90_degrees_with_the_joint_plane(fIBb,fIB,fIgamma) -> RuleUnitResult:
        """접합평면과 90를 이루는 각형 지강관의 폭

        Args:
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIgamma (float): 주강관 세장비

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관 (1)의 판단 결과
        """

        assert isinstance(fIBb, float)
        assert isinstance(fIB, float)
        assert fIB != 0
        assert isinstance(fIgamma, float)

        if fIBb/fIB >= 0.1+fIgamma/50 :
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