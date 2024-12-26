import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040204_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.2.4 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '파형강판 구조물의 압축좌굴'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.4 압축좌굴
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 파형강판 구조물의 압축좌굴] ;
		B["KDS 14 31 10 4.5.4.2.4 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 설계압축응력/] ;
    VarIn2[/입력변수: 설계압축력/] ;
    VarIn3[/입력변수: 파형강판의 단면적/] ;
    VarIn4[/입력변수: 설계좌굴강도/] ;
		end

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

		Python_Class ~~~ C(["KDS 14 31 10 4.5.4.2.4 (1)"])
		C --> Variable_def

		Q{"<img src=https://latex.codecogs.com/svg.image?f_{c}=\frac{T_{f}}{A}\leq&space;f_{b}>--------------------------------------"}

		Variable_def --> Q --> D(["PASS or Fail"])
    """


    @rule_method
    def Design_compressive_stress(fITf,fIA,fIfb) -> RuleUnitResult:
        """파형강판 구조물의 압축좌굴

        Args:
            fITf (float): 설계압축력
            fIA (float): 파형강판의 단면적
            fIfb (float): 설계좌굴강도

        Returns:
            fOfc (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.4 압축좌굴 (1)의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.4 압축좌굴 (1)의 판단 결과
        """

        assert isinstance(fITf, float)
        assert isinstance(fIA, float)
        assert fIA != 0
        assert isinstance(fIfb, float)

        fOfc = fITf / fIA

        if fOfc <= fIfb:
          return RuleUnitResult(
              result_variables = {
                  "fOfc": fOfc,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )