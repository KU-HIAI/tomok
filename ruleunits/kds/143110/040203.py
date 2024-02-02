import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040203 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭압축강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도
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
		A[비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도] ;
		B["KDS 14 31 10 4.2.3"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭압축강도/]
    VarIn1[/입력변수: 횡좌굴에 대한 비지지길이/]
    VarIn2[/입력변수: 단면2차반경/]
    VarIn3[/입력변수: 유효좌굴길이계수/]
    VarIn4[/입력변수: 좌굴 응력/]
    VarIn5[/입력변수: 부재의 총단면적/]
    VarIn6[/입력변수: 탄성좌굴해석을 통하여 구하는 탄성좌굴응력/]
    VarIn7[/입력변수: 강재의 항복강도/]
    VarIn8[/입력변수: 강재의 탄성계수/]
    VarIn9[/입력변수: 부재의 횡좌굴에 대한 비지지길이/]
    VarIn10[/입력변수: 좌굴축에 대한 단면2차반경/]
    VarIn1~~~ VarIn6
    VarIn2~~~ VarIn7
    VarOut1~~~ VarIn3~~~ VarIn8
    VarIn4~~~ VarIn9
    VarIn5~~~ VarIn10

		end

		Python_Class ~~~ Variable_def
	  C(["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{cr}A_{q}'>-----------------------------------"]) ;
    D["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}\leq&space;4.71\sqrt{\frac{E}{F_{y}}}or\frac{F_{y}}{F_{e}}\leq&space;2.25'>--------------------------------------------------------"] ;
    E["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}>4.71\sqrt{\frac{E}{F_{y}}}or\frac{F_{y}}{F_{e}}>2.25'>--------------------------------------------------------"] ;
    F["<img src='https://latex.codecogs.com/svg.image?F_{cr}=\left[0.658^{\frac{F_{y}}{F_{e}}}\right]F_{y}'>-----------------------------------"] ;
    G["<img src='https://latex.codecogs.com/svg.image?F_{cr}=0.877F_{e}'>-----------------------------------"] ;
    H["<img src='https://latex.codecogs.com/svg.image?F_{e}=\frac{\pi^{2}E}{\left(\frac{KL}{r}\right)^{2}}(MPa)'>----------------------------------------------"] ;
	  Variable_def-->H
    H-->D-->F
    H-->E-->G
    F & G --> C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def nominal_compressive_strength(fOPn,fIFcr,fIAg,fIFe,fIFy,fIE,fIK,fIL,fIr) -> float:
        """공칭압축강도

        Args:
            fOPn (float): 공칭압축강도
            fIFcr (float): 좌굴응력
            fIFe (float): 탄성좌굴해석을 통하여 구하는 탄성좌굴응력
            fIAg (float): 부재의 총단면적
            fIFy (float): 강재의 항복강도
            fIE (float): 강재의 탄성계수
            fIK (float): 유효좌굴길이계수
            fIL (float): 부재의 횡좌굴에 대한 비지지길이
            fIr (float): 좌굴축에 대한 단면2차반경

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도의 값
        """

        fIFe = ((math.pi)**2)*fIE/((fIK*fIL/fIr)**2)

        if fIK*fIL/fIr <= 4.71*(fIE/fIFy)**(0.5) or fIFy/fIFe <= 2.25:
          fIFcr = 0.658**(fIFy/fIFe) * fIFy
        elif fIK*fIL/fIr > 4.71*(fIE/fIFy)**(0.5) or fIFy/fIFe > 2.25:
          fIFcr = 0.877*fIFe

        fOPn = fIFcr * fIAg
        return fOPn


# 

