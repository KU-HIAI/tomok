import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030203 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.2.3' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-30'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트

    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """

    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
        subgraph Python_Class
        A[Title: T, X형 접합에서 지강관의 면외 휨모멘트] ;
        B["KDS 14 31 25 4.3.3.2.3"] ;
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

        Python_Class ~~~ Variable_def
        C["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}t^{2}[0.5H_{b}(1&plus;\beta)/(1-\beta)&plus;[2BB_{b}(1&plus;\beta)/(1-\beta)]^{0.5}]Q_{f}'>-------------------------------------------------------------------------------------------------------------------------"] ;
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
    Variable_def-->E--No--->J-->C
    C-->I-->H
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

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def designed_strength(fOphiMn,fIplaion,fIswloyi,fIlocyie,fIlsrcsp,fOMn,fIFy,fIt,fIHb,fIbeta,fIB,fIBb,fIQf,fIFystar,fIFyb,fIZb,fIbeoi,fItb,fIH,fIuserdefine1,fIuserdefine2) -> float:
        """설계강도

        Args:
            fOphiMn (float): 설계강도
            fIplaion (float): 소성화
            fIswloyi (float): 측벽 국부항복
            fIlocyie (float): 국부항복
            fIlsrcsp (float): 주강관의 뒴파단의 한계상태들
            fOMn (float): 소성화의 한계상태
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fIbeta (float): 폭비
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭
            fIQf (float): 응력상관계수
            fIFystar (float): T형,X형 접합에 대한 항복강도
            fIFyb (float): 지강관의 항복강도
            fIZb (float): 휨축에 대한 지강관의 소성단면계수
            fIbeoi (float): 주강관에 용접된 지강관 면의 유효폭
            fItb (float): 지강관의 두께
            fIH (float): 주강관의 높이
            fIuserdefine1 (float): 사용자가 정의한 값
            fIuserdefine2 (float): 사용자가 정의한 값


        Returns:
            float: 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 의 값
        """
        #T형 접합의 경우 : fIuserdefine1 = 1
        #X형 접합의 경우 : fIuserdefine1 = 2
        #X형 또는 T형 접합에서 주강간 뒤틀림이 방지되어 있는 경우 : fIuserdefine2 = 1
        #주강간 뒤틀림에 대한 방지가 되어있지 않은 경우 : fIuserdefine2 = 2


        if fIuserdefine1==1:
          fIFystar = fIFy
        if fIuserdefine1==2:
          fIFystar = 0.8*fIFy

        fIbeoi = min((10/(fIB/fIt))*(fIFy*fIt/(fIFyb*fItb))*fIBb,fIBb)

        fIplaion = fIFy*fIt**2*(0.5*fIHb*(1+fIbeta)/(1-fIbeta)+((2*fIB*fIBb)*(1+fIbeta)/(1-fIbeta))**0.5)*fIQf

        fIswloyi = fIFystar*fIt*(fIB-fIt)*(fIHb+5*fIt)

        fIlocyie = 0.95*fIFyb*(fIZb-0.5*((1-(fIbeoi/fIBb)**2)*fIBb**2*fItb))

        fIlsrcsp = 2*fIFy*fIt*(fIHb*fIt+(fIB*fIH*fIt)*((fIB+fIH)**0.5))


        if fIuserdefine2 == 1:
          if fIbeta >= 0.85:
            fOphiMn = min(fIswloyi,fIlocyie)
          elif fIbeta < 0.85:
            fOphiMn = fIplaion
        elif fIuserdefine2 ==2:
          if fIbeta >= 0.85:
            fOphiMn = min(fIswloyi,fIlocyie,fIlsrcsp)
          elif fIbeta < 0.85:
            fOphiMn = min(fIplaion,fIlsrcsp)

        return(fOphiMn)


# 

