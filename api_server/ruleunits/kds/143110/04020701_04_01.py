import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04020701_04_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.7.1 (4) ①'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '세장한 자유돌출판의 저감계수'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    4.2.7.1 세장한 자유돌출판
    (4)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 세장한 자유돌출판의 저감계수] ;
		B["KDS 14 31 10 4.2.7.1 (4) ①"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 세장한 자유돌출판의 저감계수/]
    VarIn1[/입력변수: ㄱ형강의 가장 긴 다리의 폭/]
    VarIn2[/입력변수: 부재의 두께/]
    VarIn3[/입력변수: 강재의 항복강도/]
    VarIn4[/입력변수: 강재의 탄성계수/]
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.2.7.1 (4) ①"])
		C --> Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?Q_{s}'>------"] ;
	  E{"<img src='https://latex.codecogs.com/svg.image?d/t\leq&space;0.75\sqrt{E/F_{y}}'>---------------------------------------------"} ;
	  F["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.0'>-----------------------"] ;

		Variable_def-->D-->E-->F-->G(["세장한 자유돌출판의 저감계수"])
    """

    @rule_method
    def Reduction_factor_of_slender_free_projection_plate(fId,fIt,fIE,fIFy)-> RuleUnitResult:
        """세장한 자유돌출판의 저감계수

        Args:
            fId (float): T형강의 공칭높이
            fIt (float): 부재의 두께
            fIE (float): 강재의 탄성계수
            fIFy (float): 강재의 항복강도


        Returns:
            fOQs (float): 강구조부재설계기준(하중저항계수설계법) 4.2.7.1 세장한 자유돌출판 (4) ①의 값
            sOnone (string): 강구조부재설계기준(하중저항계수설계법) 4.2.7.1 세장한 자유돌출판 (4) ①의 판단 결과
        """

        assert isinstance(fId, float)
        assert fId > 0
        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fIFy, float)
        assert fIFy > 0
        assert isinstance(fIE, float)
        assert fIE > 0

        if fId/fIt <= 0.75*(fIE/fIFy)**0.5:
          fOQs = 1.0

          return RuleUnitResult(
              result_variables = {
                  "fOQs": fOQs,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )