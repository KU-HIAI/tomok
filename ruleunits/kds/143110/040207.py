import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040207 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.7' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-30'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭압축강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
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
		A[세장판단면을 갖는 압축부재] ;
		B["KDS 14 31 10 4.2.7"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭압축강도/]
    VarIn1[/입력변수: 좌굴응력/]
    VarIn2[/입력변수: 세장비/]
    VarIn3[/입력변수: root E/QFy/]
    VarIn4[/입력변수: QFy/Fe/]
    VarIn5[/입력변수: 모든 세장 압축요소를 고려하는 순 감도계수/]
    VarIn6[/입력변수: 탄성좌굴응력/]
    VarIn7[/입력변수: 강재의 항복강도/]
    VarOut1~~~ VarIn4
    VarIn1~~~ VarIn5
    VarIn2~~~ VarIn6
    VarIn3~~~ VarIn7
		end

		Python_Class ~~~ Variable_def
    C["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{cr}A_{g}'>------------------------------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}\leq&space;4.71\sqrt{\frac{E}{QF_{y}}}or\frac{QF_{y}}{F_{e}}\leq&space;2.25'>------------------------------------------------------"] ;
    E(["<img src='https://latex.codecogs.com/svg.image?F_{cr}=Q\left[0.658^{\frac{QF_{y}}{F_{e}}}\right]F_{y}'>---------------------------------------------------"]) ;
    F["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}>4.71\sqrt{\frac{E}{QF_{y}}}or\frac{QF_{y}}{F_{e}}>2.25'>--------------------------------------------------------------"] ;
    G(["<img src='https://latex.codecogs.com/svg.image?F_{cr}=0.877F_{e}'>-----------------------------------"]) ;

    Variable_def-->C-->D & F
    D-->E
    F-->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_Compressive_Strength(fOPn,fIFcr,fIKLr,fIsqrtEQFy,fIQFyFe,fIQ,fIFe,fIFy,fIAg) -> float:
        """공칭압축강도

        Args:
            fOPn (float): 공칭압축강도
            fIFcr (float): 좌굴응력
            fIKLr (float): 세장비
            fIsqrtEQFy (float):
            fIQFyFe (float):
            fIQ (float): 모든 세장 압축요소를 고려하는 순감소계수
            fIFe (float): 탄성좌굴응력
            fIFy (float): 강재의 항복강도
            fIAg (float):

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.2.7 세장판단면을 갖는 압축부재의 값
        """

        if fIKLr <= 4.71*fIsqrtEQFy or fIQFyFe <= 2.25:
          fIFcr = fIQ * (0.658**fIQFyFe) * fIFy
        elif fIKLr > 4.71*fIsqrtEQFy or fIQFyFe > 2.25:
          fIFcr = 0.877 * fIFe

        fOPn = fIFcr * fIAg
        return fOPn


# 

