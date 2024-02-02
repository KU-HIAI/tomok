import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011103_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.11.3 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수평보강재의 단면2차모멘트'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.3 수평보강재
    (3)
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
		A[Title: 수평보강재] ;
		B["KDS 14 31 10 4.3.3.1.11.3 (3)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 수평보강재의 단면2차모멘트/] ;
      VarIn2[/입력변수: 수평보강재 안의 최대 웨브 높이/] ;
      VarIn3[/입력변수: 웨브두께/] ;
      VarIn4[/입력변수: 수직보강재 간격/] ;
      VarIn5[/입력변수: 수평보강재 휨강성을 위한 곡률보정계수/] ;
      VarIn6[/입력변수: 조합단면의 중립축에 대한 회전반경/] ;
      VarIn7[/입력변수: 보강재의 최소항복강도/] ;
      VarIn8[/입력변수: 압축플랜지의 최소항복강도/] ;
      VarIn9[/입력변수: 강재의 탄성계수/] ;
      VarIn10[/입력변수: 하이브리드 단면의 응력감소계수/] ;
      VarIn11[/입력변수: 곡률인자/] ;
      VarIn12[/입력변수: 해당 패널의 최소거더반경/] ;
      VarIn13[/입력변수: 수직보강재 간격/] ;
      VarIn14[/입력변수: 웨브두께/] ;
    end
    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
    VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
    VarIn11 ~~~ VarIn13 & VarIn14
    Python_Class ~~~ Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?Z=\frac{0.95d_{0}^{2}}{Rt_{w}}\leq&space;10>------------------------------"]
    D["<img src=https://latex.codecogs.com/svg.image?I_{l}=Dt_{w}^{3}[2.4(\frac{d_{0}}{D})^{2}-0.13]\beta&space;>--------------------------------------------------"]
    E["<img src=https://latex.codecogs.com/svg.image?r\geq\frac{0.16d_{0}\sqrt{\frac{F_{ys}}{E}}}{\sqrt{1-0.6\frac{F_{yc}}{R_{h}F_{ys}}}}>------------------------------------------------------------------------"]
    F{"수평보강재가 곡률중심 쪽 웨브면에 설치된 경우"}

    Variable_def --> C --> F --"yes"--> G["<img src=https://latex.codecogs.com/svg.image?\beta=\frac{Z}{12}&plus;1>-----------------------"]
    F --"No"--> H["<img src=https://latex.codecogs.com/svg.image?\beta=\frac{Z}{6}&plus;1>-----------------------"]

    G & H --> D --> E --> Q(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Moment_of_inertia_of_horizontal_stiffeners(fIIl,fID,fItw,fIdo,fIbeta,fIr,fIFys,fIFyc,fIE,fIRh,fIZ,fIR,fIuserdefined) -> bool:
        """수평보강재의 단면2차모멘트
        Args:
            fIIl (float): 수평보강재의 단면2차모멘트
            fID (float): 수평보강재 안의 최대 웨브 높이
            fItw (float): 웨브두께
            fIdo (float): 수직보강재 간격
            fIbeta (float): 수평보강재 휨강성을 위한 곡률보정계수
            fIr (float): 조합단면의 중립축에 대한 회전반경
            fIFys (float): 보강재의 최소항복강도
            fIFyc (float): 압축플랜지의 최소항복강도
            fIE (float): 강재의 탄성계수
            fIRh (float): 하이브리드 단면의 응력감소계수
            fIZ (float): 곡률인자
            fIR (float): 해당 패널의 최소 거더반경
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.3 수평보강재 (3)의 통과여부
        """

        # fIuserdefined == 1 : 수평보강재가 곡률중심의 반대편 웨브면에 설치된 경우
        # fIuserdefined == 2 : 수평보강재가 곡률중심 쪽 웨브면에 설치된 경우
        if fIuserdefined == 1:
            fIbeta = fIZ / 6 + 1
            fIIl = fID * fItw ** 3 * (2.4 * (fIdo / fID) ** 2 - 0.13) * fIbeta
            if fIr >= (0.16 * fIdo * (fIFys / fIE) ** 0.5) / (1 - 0.6 * (fIFyc / (fIRh * fIFys))) ** 0.5:
                return "Pass"
            else:
                return "Fail"
        elif fIuserdefined == 2:
            if fIZ == 0.95 * fIdo ** 2 / (fIR * fItw) <= 10:
                fIbeta = fIZ / 12 + 1
                fIIl = fID * fItw ** 3 * (2.4 * (fIdo / fID) ** 2 - 0.13) * fIbeta
                if fIr >= (0.16 * fIdo * (fIFys / fIE) ** 0.5) / (1 - 0.6 * (fIFyc / (fIRh * fIFys))) ** 0.5:
                    return "Pass"
                else:
                    return "Fail"
            else:
                return "Fail"


# 

