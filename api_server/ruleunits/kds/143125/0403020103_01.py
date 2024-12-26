import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020103_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.3 K형 접합의 압축력을 받는 지강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.2.1.3 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	 	VarOut1[/출력변수: 지강관의 설계강도/] ;

    VarIn1[/입력변수: 주강관 소성화의 한계상태/]
	  VarIn2[/입력변수: 전단항복'뚫림'의 한계상태/]
	  VarIn3[/입력변수: 주강관의 항복강도/]
	  VarIn4[/입력변수: 주강관의 두께/]
	  VarIn5[/입력변수: 원형 지강관의 외경/]
	  VarIn6[/입력변수: 바깥지름/]
	  VarIn7[/입력변수: 지강관 축방향 응력상관계수/]
	  VarIn8[/입력변수: 주강관 응력상관계수/]
	  VarIn9[/입력변수: 주강관 세장비/]
 	  VarIn10[/입력변수: 지강관에서 떨어진 거리/]
 	  VarIn11[/입력변수: 주강관의 두께/]
    VarIn12[/입력변수: 지강관과 주강관 사이의 실제 각도/]
    VarIn13[/입력변수: 용접치수를 무시한 주강관 상단부를 따라 측정된 계수/]
    VarIn14[/입력변수: 주강관 소성화의 한계상태/]
    VarIn15[/입력변수: 전단항복'뚫림'의 한계상태/]
    VarIn16[/입력변수: 웨브의 경사각/]

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
    VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
    VarIn11 ~~~ VarIn13 & VarIn14 & VarIn5 & VarIn6

		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.3 (1)"])
		C --> Variable_def

    Variable_def -->F

	  I--압축 지강관의 경우-->D-->E
	  I--인장 지강관의 경우-->E

    F-->N-->I
	  E --> M

    E["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=F_{y}t^{2}[2.0&plus;11.33D_{b}/D]Q_{g}Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?Q_{g}=\gamma^{0.2}[1&plus;\frac{0.024\gamma^{1.2}}{e^{\frac{0.5g}{t}-1.33}&plus;1}]'>---------------------------------------------------------------------------------------------------"] ;

    F["K형 접합"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]
    M["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"] ;

	  N[주강관 소성화의 한계상태]
    """

    @rule_method
    def Limit_state_of_chord_plastification(fIFy,fIt,fIDb,fID,fIQf,fIgamma,fIe,fIg,fIPn,fItheta) -> RuleUnitResult:
        """주강관 소성화의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIDb (float): 원형 지강관의 외경
            fID (float): 바깥지름
            fIQf (float): 주강관 응력상관계수
            fIgamma (float): 주강관 세장비
            fIe (float): 지강관에서 떨어진 거리
            fIg (float): 용접치수를 무시한 주강관 상단부를 따라 측정된 양수
            fIPn (float): 주강관의 소요 압축강도
            fItheta (float): 웨브의 경사각

        Returns:
            fOPnsinA (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.3 K형 접합의 압축력을 받는 지강관 (1)의 값 1
            fOPnsinB (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.3 K형 접합의 압축력을 받는 지강관 (1)의 값 2
            fOQg (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.3 K형 접합의 압축력을 받는 지강관 (1)의 값 3
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.3 K형 접합의 압축력을 받는 지강관 (1)의 값 4
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.3 K형 접합의 압축력을 받는 지강관 (1)의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIDb, float)
        assert isinstance(fID, float)
        assert fID != 0
        assert isinstance(fIQf, float)
        assert isinstance(fIgamma, float)
        assert fIgamma > 0
        assert isinstance(fIe, float)
        assert fIe > 0
        assert isinstance(fIg, float)
        assert isinstance(fIPn, float)
        assert isinstance(fItheta, float)

        import math

        fOphi = 0.9

        if fOPnsinA != 0 and fOPnsinB == 0 :
          fOQg = (fIgamma**0.2)*(1+0.024*(fIgamma**1.2)/(fIe**(0.5*fIg/fIt-1.33)+1))
          fOPnsinA = fIFy*(fIt**2)*(2+11.33*fIDb/fID)*fOQg*fIQf
          return RuleUnitResult(
                result_variables = {
                    "fOPnsinA": fOPnsinA,
                    "fOphi": fOphi,
                }
            )
        elif fOPnsinA == 0 and fOPnsinB != 0 :
          fOPnsinB = fIPn * math.sin(math.radians(fItheta))
          return RuleUnitResult(
                result_variables = {
                    "fOPnsinB": fOPnsinB,
                    "fOphi": fOphi,
                }
            )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )