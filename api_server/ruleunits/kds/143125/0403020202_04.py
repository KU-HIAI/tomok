import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020202_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.2 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '국부항복의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 국부항복의 한계상태]
	  B["KDS 14 31 25 4.3.2.2.2 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 비균일 하중분포로 인한 국부항복의 한계상태/] ;

	  VarIn1[/입력변수: 지강관의 항복강도/]
	  VarIn2[/입력변수: 강관 모서리의 외부반경/]
	  VarIn3[/입력변수: 주강관축에 평행한 하중지지길이/]
	  VarIn4[/입력변수: 주강관의 높이/]
	  VarIn5[/입력변수: 강재의 탄성계수/]
	  VarIn6[/입력변수: 주강관의 두께/]
	  VarIn7[/입력변수: 주강관의 항복강도/]
	  VarIn8[/입력변수: 지강관의 두께/]
	  VarIn9[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/]
	  VarIn10[/입력변수: 주강관에 용접된 지강관 면의 유효폭/]
	  VarIn11[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/]


	  VarOut1 ~~~ VarIn1 &  VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 &  VarIn5 & VarIn6
	  VarIn5 ~~~ VarIn7 &  VarIn8 & VarIn9
	  VarIn8 ~~~ VarIn10 &  VarIn11

		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.2 (4)"])
		C --> Variable_def

	  Variable_def -->N

    N-->R-->M

    M(["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{yb}t_{b}[2H_{b}&plus;2b_{eoi}-4t_{b}]'>-----------------------------------------------------------------------------------------------------------"])
	  N["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------------------------"] ;
    R["<img src='https://latex.codecogs.com/svg.image?b_{eoi}=F_{yb}t_{b}[2H_{b}&plus;2b_{eoi}-4t_{b}]'>--------------------------------------------------------------------------------------------------------------------------"]
    """

    @rule_method
    def Limit_state_of_local_surrender(fIbeta,fIFyb,fItb,fIHb,fIk,fIN,fIH,fIE,fIB,fIt,fIFy,fIBb)  -> RuleUnitResult:
        """국부항복의 한계상태

        Args:
            fIbeta (float): 폭비
            fIFyb (float): 지강관의 항복강도
            fItb (float): 지강관의 두께
            fIHb (float): 접합평면에서 측정한 각형
            fIk (float): 강관 모서리의 외부반경
            fIN (float): 주강관축에 평행한 하중지지길이
            fIH (float): 주강관의 높이
            fIE (float): 강재의 탄성계수
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIt (float): 주강관의 두께
            fIFy (float): 주강관의 항복강도
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭

        Returns:
            fOPn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (4)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (4)의 값 2
            fObeoi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (4)의 값 3
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (4)의 판단 결과
        """

        assert isinstance(fIbeta, float)
        assert isinstance(fIFyb, float)
        assert fIFyb != 0
        assert isinstance(fItb, float)
        assert fItb != 0
        assert isinstance(fIHb, float)
        assert isinstance(fIk, float)
        assert isinstance(fIN, float)
        assert isinstance(fIH, float)
        assert isinstance(fIE, float)
        assert isinstance(fIB, float)
        assert fIB != 0
        assert isinstance(fIt, float)
        assert fIt != 0
        assert isinstance(fIFy, float)
        assert isinstance(fIBb, float)

        if fIbeta >= 0.85 :
          fObeoi = (10/(fIB/fIt))*(fIFy*fIt)/(fIFyb*fItb)*fIBb
          fOPn = fIFyb*fItb*(2*fIHb+2*fObeoi-4*fItb)
          fOphi = 0.95
          if fObeoi <= fIBb:
            return RuleUnitResult(
                result_variables = {
                    "fOPn": fOPn,
                    "fOphi": fOphi,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )