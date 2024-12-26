import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040206(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.2.6'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '이음부 공칭강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.6 이음부 강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 이음부 공칭강도] ;
		B["KDS 14 31 10 4.5.4.2.6"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 이음부 공칭강도/] ;
    VarIn2[/입력변수: 이음부 저항계수/] ;
    VarIn3[/입력변수: 설계압축력/] ;
		end

    Python_Class ~~~ C(["KDS 14 31 10 4.5.4.2.6"])
		C --> Variable_def

		Q{"<img src=https://latex.codecogs.com/svg.image?T_{f}<\phi&space;_{j}S_{s}>---------------------"}

		Variable_def --> Q --> X(["PASS or Fail"])
    """


    @rule_method
    def Nominal_joint_strength(fISs,fIphij,fITf) -> RuleUnitResult:
        """이음부 공칭강도

        Args:
            fISs (float): 이음부 공칭강도
            fIphij (float): 이음부 저항계수
            fITf (float): 설계압축력

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.6 이음부 강도의 판단 결과
        """

        assert isinstance(fISs, float)
        assert isinstance(fIphij, float)
        assert isinstance(fITf, float)

        if fITf < fIphij * fISs:
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