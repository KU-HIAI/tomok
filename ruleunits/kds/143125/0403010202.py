import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403010202 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.1.2.2' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '집중하중이 강관축에 직각으로 분포할 때, 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.2 축직각방향 집중하중
    4.3.1.2.2 각형강관
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
	  A[각형강관]
	  B["KDS 14 31 25 4.3.1.2.2"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 설계강도/]
	  VarIn1[/입력변수: 국부항복/]
	  VarIn2[/입력변수: 전단항복뚫림/]
	  VarIn3[/입력변수: 측벽강도/]
	  VarIn4[/입력변수: 접합평면과 90도를 이루는 판폭/]
	  VarIn5[/입력변수: 접합평면과 90도를 이루는 강판폭/]
	  VarIn6[/입력변수: 주강관의 두께/]
	  VarIn7[/입력변수: 국부항복 한계상태/]
	  VarIn8[/입력변수: 강재의 항복강도/]
	  VarIn9[/입력변수: 판재의 항복강도/]
	  VarIn10[/입력변수: 판재의 두께/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
  	VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10
	  end
	  Python_Class ~~~ Variable_def --> D & E
	  E --> O & P & Q
	  O --> F
	  P --> G & H & I & J
	  H & I & J --> R
	  F & G --> S
	  Q --> T & U & V & N
	  T --> K
	  U --> L
	  V --> M
	  K & L & M --> W
	  N --> X
	  D(["<img src='https://latex.codecogs.com/svg.image?&space;0.25<B_P/B\leq&space;1.0'>-----------------------------------------"])
	  E["하중을 받는 관벽의 두께에 대해 <img src='https://latex.codecogs.com/svg.image?B/t\leq&space;35'>------------------"]
	  F["<img src='https://latex.codecogs.com/svg.image?R_n=\left[10F_yt/(B/t)\right]B_p\leq&space;F_{yp}t_pB_p'>-----------------------------------"]
	  G["<img src='https://latex.codecogs.com/svg.image?R_n=0.6F_yt\left[2t_p&plus;2B_{ep}\right]'>---------------------------------------"]
	  H["<img src='https://latex.codecogs.com/svg.image?B_{ep}=10B_p/(B/t)\leq&space;B_p'>-----------------------------------"]
	  I["<img src='https://latex.codecogs.com/svg.image?B_p>(B-2t)'>-------------------------"]
	  J["<img src='https://latex.codecogs.com/svg.image?B_p<0.85B'>---------------------"]
	  K["<img src='https://latex.codecogs.com/svg.image?R_n=2F_yt\left[5k&plus;N\right]'>------------------------"]
	  L["<img src='https://latex.codecogs.com/svg.image?R_n=1.6t^2\left[1&plus;3N/(H-3t)\right](EF_y)^{0.5}Q_f'>--------------------"]
	  M["<img src='https://latex.codecogs.com/svg.image?R_n=\left[48t^3/(H-3t)\right](EF_y)^{0.5}Q_f'>---------------------------------"]
	  N["<img src='https://latex.codecogs.com/svg.image?L_e=2\left[10/(B/t)\right]\left\lceil(F_yt)/(F_{yp}t_p)\right\rceil&space;B_p\leq&space;2B_p'>-----------------------------------------------------"]
	  O["하중이 전달된 관내의 비균일 하중분포에 의한 관재의 국부항복 한계상태"]
	  P["전단항복의 한계상태"]
	  Q["인장력을 받는 측벽의 한계상태"]
	  R(["한계상태 검토 필요 X"])
	  S(["<img src='https://latex.codecogs.com/svg.image?R_n'>-----------------"])
	  T["측벽 국부항복의 한계상태"]
	  U["T형접합에서 측벽의 국부크리플링의 한계상태"]
	  V["X형접합에서 측벽의 국부좌굴의 한계상태"]
	  W(["<img src='https://latex.codecogs.com/svg.image?R_n'>-----------------"])
	  X(["<img src='https://latex.codecogs.com/svg.image?L_e'>-----------------"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_strength(fOphiRn,fIlocyie,fIsheyie,fIposwst,fIBp,fIB,fIt,fIRn,fIFy,fIFyp,fItp,fIBep,fIloyssw,fIlocrsw,fIlobusw,fIk,fIN,fIH,fIE,fIQf,fOLe,fIuserdefined) -> bool:
        """집중하중이 강관축에 직각으로 분포할 때, 설계강도
        Args:
            fOphiRn (float): 설계강도
            fIlocyie (float): 국부항복
            fIsheyie (float): 전단항복(뚫림)
            fIposwst (float): 측벽강도
            fIBp (float): 접합평면과 90°를 이루는 판폭
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIt (float): 주강관의 두께
            fIRn (float): 국부항복 한계상태
            fIFy (float): 강재의 항복강도
            fIFyp (float): 판재의 항복강도
            fItp (float): 판재의 두께
            fIBep (float): 보정된 판폭
            fIloyssw (float): 측벽의 국부항복응력
            fIlocrsw (float): 측벽의 국부크리플링
            fIlobusw (float): 측벽의 국부좌굴
            fIk (float): 강관 모서리의 외부반경
            fIN (float): 집중하중이 작용하는 폭
            fIH (float): 접합평면에서 측정한 각형 주강관의 높이
            fIE (float): 강재의 탄성계수
            fIQf (float): 주관-응력상관변수
            fOLe (float): 홈용접이나 필릿용접의 유효길이
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.1.2.2 각형강관의 값
        """

        fOLe = min(2 * (10 / (fIB/fIt)) * ((fIFy * fIt) / (fIFyp * fItp)) * fIBp, 2 * fIBp)

        #국부항복 한계상태
        fIlocyie = 0.95 * min((10 * fIFy * fIt / (fIB/fIt)) * fIBp, fIFyp * fItp * fIBp)

        #전단항복의 한계상태
        fIBep = min(10 * fIBp / (fIB / fIt), fIBp)
        fIsheyie = 0.95 * 0.6 * fIFy * fIt * (2 * fItp + 2 * fIBep)

        #인장력 또는 압축력을 받는 측벽의 한계상태
        # fIuserdefined == 1 : 인장력을 받는 측벽의 한계상태
        # fIuserdefined == 2 : 압축력을 받는 측벽의 한계상태

        if 0.25 < fIBp/fIB <= 1.0 :
          fIBep = 10 * fIBp / (fIB / fIt)
          if fIBep <= fIBp or fIBp > (fIB - 2 * fIt) or fIBp < 0.85 * fIB :
            if fIuserdefined == 1:
              fIRn = 2 * fIFy * fIt * (5 * fIk + fIN)
              fIloyssw = 1.0 * fIRn
              return fIloyssw, fOLe
            elif fIuserdefined == 2:
              fIloyssw = 1.0 * 2 * fIFy * fIt * (5 * fIk + fIN) # 측벽 국부항복의 한계상태
              fIlocrsw = 0.75 * 1.6 * fIt ** 2 * (1 + 3 * fIN / (fIH - 3 * fIt)) * (fIE * fIFy) ** 0.5 * fIQf # T형 접합에서 측벽의 국부크리플링의 한계상태
              fIlobusw = 0.90 * (48 * fIt ** 3 / (fIH - 3 * fIt)) * (fIE * fIFy) ** 0.5 * fIQf # X형 접합에서 측벽의 국부좌굴의 한계상태
              fIposwst = min(fIloyssw, fIlocrsw, fIlobusw)
              fOphiRn = min(fIlocyie, fIposwst)
          else:
            if fIuserdefined == 1:
              fIRn = 2 * fIFy * fIt * (5 * fIk + fIN)
              fIloyssw = 1.0 * fIRn
              return fIloyssw, fOLe
            elif fIuserdefined == 2:
              fIloyssw = 1.0 * 2 * fIFy * fIt * (5 * fIk + fIN) # 측벽 국부항복의 한계상태
              fIlocrsw = 0.75 * 1.6 * fIt ** 2 * (1 + 3 * fIN / (fIH - 3 * fIt)) * (fIE * fIFy) ** 0.5 * fIQf # T형 접합에서 측벽의 국부크리플링의 한계상태
              fIlobusw = 0.90 * (48 * fIt ** 3 / (fIH - 3 * fIt)) * (fIE * fIFy) ** 0.5 * fIQf # X형 접합에서 측벽의 국부좌굴의 한계상태
              fIposwst = min(fIloyssw, fIlocrsw, fIlobusw)
              fOphiRn = min(fIlocyie, fIsheyie, fIposwst)
          return fOphiRn, fOLe
        else:
          return "Fail"


# 

