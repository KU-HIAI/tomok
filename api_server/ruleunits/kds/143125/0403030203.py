import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030203_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 설계강도]
	  B["KDS 14 31 25 4.3.3.2.3"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 설계강도/] ;
    VarOut2[/출력변수: 소성화의 한계상태/] ;
    VarIn1[/입력변수: 지강관의 항복강도/] ;
    VarIn2[/입력변수: 휨축에 대한 지강관의 소성단면계수/] ;
    VarIn3[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
    VarIn4[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
    VarIn5[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
    VarIn6[/입력변수: 지강관의 두께/] ;
    VarIn7[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
    VarIn8[/입력변수: 주강관의 두께/] ;
    VarIn9[/입력변수: 주강관의 항복강도/] ;
    VarIn10[/입력변수: 폭비/] ;
    VarIn11[/입력변수: 측벽 국부항복/] ;
    VarIn12[/입력변수: 주강관의 뒴파단의 한계상태들/] ;
    VarIn13[/입력변수: 접합평면과 90를 이루는 각형 강관폭 /] ;
    VarIn14[/입력변수: 응력상관계수 /] ;
    VarIn15[/입력변수: T형 접합에 대한 항복강도 /] ;
    VarIn16[/입력변수: X형 접합에 대한 항복강도의 0.8배 /] ;
    VarIn17[/입력변수: 주강관의 높이 /] ;
    VarIn18[/입력변수: 소성화 /] ;
    end
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
    VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
    VarIn11 ~~~ VarIn13 & VarIn14 & VarIn15
    VarIn14 ~~~ VarIn16 & VarIn17 & VarIn18

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.3"])
		C --> Variable_def

	  AC["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}t^{2}[0.5H_{b}(1&plus;\beta)/(1-\beta)&plus;[2BB_{b}(1&plus;\beta)/(1-\beta)]^{0.5}]Q_{f}'>-------------------------------------------------------------------------------------------------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------"] ;
    H["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>------------------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------"]
    J["주강관벽 소성화의 한계상태"]
    E["<img src='https://latex.codecogs.com/svg.image?\beta>0.85'>--------------------"]
    F(["검토안함"]) ;
    G["측벽 국부항복의 한계상태"]
    K(["검토안함"]) ;
    L["<img src='https://latex.codecogs.com/svg.image?\beta<0.85'>--------------------"]
    M["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}^{*}t(B-t)(H_{b}&plus;5t)'>-----------------------------------------------------------------------------------"]
    N["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>--------------"] ;
    O["<img src='https://latex.codecogs.com/svg.image?\beta<0.85'>--------------------"]
    P["비균일 하중분포로 인한 국부항복의 한계상태"]
    Q["<img src='https://latex.codecogs.com/svg.image?b_{eoi}=[10/(B/t)][F_{y}t/(F_{yb}t_{b})]B_{b}\leq&space;B_{b}'>-------------------------------------------------------------------------------------------"]
    R["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{yb}[Z_{b}-0.5(1-b_{eoi}/B_{b})^{2}B_{b}^{2}t_{b}]'>-------------------------------------------------------------------------------------"]
    S["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>------------------"] ;
    T(["검토안함"]) ;
    U["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>-----------------------"]
    V["주강관 뒤틀림이 다른 조치에 의해 방지"]
    W["주강관 뒤틀림의 한계상태"]
    X["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------"]
    Y["<img src='https://latex.codecogs.com/svg.image?M_{n}=2F_{y}t[H_{b}t&plus;[BHt(B&plus;H)]^{0.5}]'>----------------------------------------------------------------------------"]
    Z(["검토안함"]) ;
    AA["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>--------------"] ;
    AB["Min(주강관벽 소성화의 한계상태일 때 설계강도, 측벽 국부항복의 한계상태일 때 설계강도, 비균일 하중분포로 인한 국부항복의 한계상태일 때 설계강도, 주강관 뒤틀림의 한계상태일 때 설계강도)"] ;
    Variable_def-->E--No--->J-->AC
    AC-->I-->H
    E--yes-->F
    Variable_def-->L--No--->G-->M
    M-->D-->N
    L--yes-->K
    Variable_def-->O--No--->P-->Q-->U
    U-->R-->S
    O--yes-->T
    Variable_def-->V--No--->W-->X-->Y-->AA
    V--yes-->Z
    H-->AB
    N-->AB
    S-->AB
    AA-->AB-->QD(["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>--------------"])
    """

    @rule_method
    def design_strength(fIplaion,fIswloyi,fIlocyie,fIlsrcsp,fIbeta) -> RuleUnitResult:
        """설계강도

        Args:
            fIplaion (float): 주강관벽 소성화의 한계상태
            fIswloyi (float): 측벽 국부항복의 한계상태
            fIlocyie (float): 비균일 하중분포로 인한 국부항복의 한계상태
            fIlsrcsp (float): 주강관 뒤틀림의 한계상태
            fIbeta (float): 폭비

        Returns:
            fOphiMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트의 값
        """

        assert isinstance(fIplaion, float)
        assert isinstance(fIswloyi, float)
        assert isinstance(fIlocyie, float)
        assert isinstance(fIlsrcsp, float)

        if fIbeta >= 0.85:
          fOphiMn = min(fIswloyi,fIlocyie,fIlsrcsp)
        elif fIbeta < 0.85:
          fOphiMn = min(fIplaion,fIlsrcsp)

        return RuleUnitResult(
            result_variables = {
                "fOphiMn": fOphiMn,
            }
        )