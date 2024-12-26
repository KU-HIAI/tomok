import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020202_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.2 (3)'
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
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 국부항복의 한계상태]
	  B["KDS 14 31 25 4.3.2.2.2 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 전단항복뚫림의 한계상태/] ;
    VarOut2[/출력변수: 저항계수/] ;
    VarOut3[/출력변수: 유효외부뚫림변수/] ;
	  VarIn1[/입력변수: 강재의 최소인장강도/]
	  VarIn2[/입력변수: 주강관의 두께/]
	  VarIn3[/입력변수: 강관 모서리의 외부반경/]
	  VarIn4[/입력변수: 주강관벽 소성화의 한계상태/]
	  VarIn5[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/]
	  VarIn6[/입력변수: 지강관과 주강관 사이의 실제 각도/]
	  VarIn7[/입력변수: T, Y형 접합에서 측벽 국부크리플링의 한계상태/]
	  VarIn8[/입력변수: 강재의 탄성계수/]
	  VarIn9[/입력변수: 주강관 응력상관계수/]
	  VarIn10[/입력변수: X형 접합에서 측벽 국부크리플링의 한계상태/]
	  VarIn11[/입력변수: 주강관의 높이/]
	  VarIn12[/입력변수: 폭비/]

	  VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 &  VarIn2 & VarIn3 ~~~ VarIn4 &  VarIn5 & VarIn6 ~~~ VarIn7 &  VarIn8 & VarIn9 ~~~ VarIn10 &  VarIn11 & VarIn12
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.2 (3)"])
		C --> Variable_def

	  Variable_def --> H & J & L

    H-->I
    J-->K
    L-->Q

    I & K & Q-->U(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>--------------------"])

    H["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------------------"] ;
    I(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=2F_{y}t[5k&plus;N]'>-----------------------------------------------------------------------------------------------"])
    J["<img src='https://latex.codecogs.com/svg.image?\phi=0.75'>--------------------------------------------"] ;
    K(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=1.6t^2[1&plus;3N/(H-3t)](EF_{y}^{0.5}Q_{f})'>-----------------------------------------------------------------------"])
    L["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------------------------"] ;
    Q(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=[48t^{3}/(H-3t)](EF_{y})^{0.5}Q_{f}'>------------------------------------------------------------------------------------"])
    """

    @rule_method
    def Limit_state_of_local_surrender(fIPnsinA,fIPnsinB,fIPnsinC,fIFy,fIt,fIQf,fIk,fIH,fIE,fIHb,fItheta,fIbeta)  -> RuleUnitResult:
        """국부항복의 한계상태

        Args:
            fIPnsinA (float): 주강관벽 소성화의 한계상태
            fIPnsinB (float): T, Y형 접합에서 측벽 국부크리플링의 한계상태
            fIPnsinC (float): X형 접합에서 측벽 국부크리플링의 한계상태
            fIFy (float): 강재의 최소인장강도
            fIt (float): 주강관의 두께
            fIQf (float): 주강관 응력상관계수
            fIk (float): 강관 모서리의 외부반경
            fIH (float): 주강관의 높이
            fIE (float): 강재의 탄성계수
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fItheta (float): 지강관과 주강관 사이의 실제 각도
            fIbeta (float): 폭비

        Returns:
            fOPnsin (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (3)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (3)의 값 2
            fON (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (3)의 값 3
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (3)의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert fIFy > 0
        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fIQf, float)
        assert isinstance(fIk, float)
        assert isinstance(fIH, float)
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIHb, float)
        assert isinstance(fItheta, float)
        assert 0 < fItheta < 180
        assert fIH-3*fIt != 0

        import math

        fON = fIHb / (math.sin(math.radians(fItheta)))

        if fIbeta == 1 :
          if fIPnsinA != 0 and fIPnsinB == 0 and fIPnsinC == 0 :
            fOPnsin = 2*fIFy*fIt*(5*fIk+fON)
            fOphi = 1.0
            return RuleUnitResult(
                result_variables = {
                    "fOPnsin": fOPnsin,
                    "fOphi": fOphi,
                }
            )
          elif fIPnsinA == 0 and fIPnsinB != 0 and fIPnsinC == 0 :
            fOPnsin = 1.6*fIt**2*(1+3*fON/(fIH-3*fIt))*(fIE*fIFy)**0.5*fIQf
            fOphi = 0.75
            return RuleUnitResult(
                result_variables = {
                    "fOPnsin": fOPnsin,
                    "fOphi": fOphi,
                }
            )
          elif fIPnsinA == 0 and fIPnsinB == 0 and fIPnsinC != 0 :
            fOPnsin = (48*fIt**3/(fIH-3*fIt))*(fIE*fIFy)**0.5*fIQf
            fOphi = 0.9
            return RuleUnitResult(
                result_variables = {
                    "fOPnsin": fOPnsin,
                    "fOphi": fOphi,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )