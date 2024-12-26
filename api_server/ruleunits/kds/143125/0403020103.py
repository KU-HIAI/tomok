import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020103(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = 'K형 접합의 압축력을 받는 지강관의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.3 K형 접합의 압축력을 받는 지강관
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: K형 접합의 압축력을 받는 지강관의 설계강도]
	  B["KDS 14 31 25 4.3.2.1.3"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	 	VarOut1[/출력변수: 인장 지강관의 설계강도/] ;
	  VarOut2[/출력변수: T-및 Y-형 접합에서 주강관의 소성화의 한계상태/] ;
	  VarOut3[/출력변수: 전단항복'뚫림'의 한계상태/] ;
    VarIn1[/입력변수: 주강관의 소성화/]
	  VarIn2[/입력변수: 전단항복'뚫림'/]
	  VarIn3[/입력변수: 주강관의 항복강도/]
	  VarIn4[/입력변수: 주강관의 두께/]
	  VarIn5[/입력변수: 폭비/]
	  VarIn6[/입력변수: 주강관 세장비/]
	  VarIn7[/입력변수: 주강관 응력상관계수/]
	  VarIn8[/입력변수: 원형 지강관의 외경/]
	  VarIn9[/입력변수: 저항계수/]

		VarOut1 &	VarOut2 &	VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.3"])
		C --> Variable_def

    Variable_def -->F
	  F-->O-->K-->L
  	I--압축 지강관의 경우-->D-->C
    F-->N-->I
  	C --> M
  	L --> M
  	M --"Minimum"--> Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"])
    C["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=F_{y}t^{2}[2.0&plus;11.33D_{b}/D]Q_{g}Q_{f}'>---------------------------------------------------------------------------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?Q_{g}=\gamma^{0.2}[1&plus;\frac{0.024\gamma^{1.2}}{e^{\frac{0.5g}{t}-1.33}&plus;1}]'>---------------------------------------------------------------------------------------------------"] ;
    F["K형 접합"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=0.90'>--------------------------"]
    K["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>--------------------------"]
    L["<img src='https://latex.codecogs.com/svg.image?P_{n}=0.6F_{y}t\pi&space;D_{b}[1&plus;sin\theta/2sin^{2}\theta]'>----------------------------------------------------------------------------------"]
    M["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>-----------"] ;
	  N[주강관 소성화의 한계상태]
    O[전단항복의 한계상태]
    """

    @rule_method
    def Design_strength_of_steel_pipe_subjected_to_compressive_force_of_K_type_joint(fIlschpl,fIlsshyi) -> RuleUnitResult:
        """K형 접합의 압축력을 받는 지강관의 설계강도

        Args:
            fIlschpl (float): 주강관의 소성화의 한계상태
            fIlsshyi (float): 전단항복(뚫림)의 한계상태

        Returns:
            fOphiPn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.3 K형 접합의 압축력을 받는 지강관의 값
        """

        assert isinstance(fIlschpl, float)
        assert isinstance(fIlsshyi, float)

        fOphiPn = min(fIlschpl, fIlsshyi)

        return RuleUnitResult(
            result_variables = {
                "fOphiPn": fOphiPn,
            }
        )