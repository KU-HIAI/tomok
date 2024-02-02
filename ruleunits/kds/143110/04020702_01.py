import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04020702_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.7.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '세장한 양연지지판의 저감계수'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    4.2.7.2 세장한 양연지지판
    (1)
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
		A[세장한 양연지지판] ;
		B["KDS 14 31 10 4.2.7.2(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 세장한 양연지지판의 저감계수/]
    VarIn1[/입력변수: 부재의 총단면적/]
    VarIn2[/입력변수: 감소된 유효폭 be를 고려하여 산정한 유효단면적의 합/]
    VarIn3[/입력변수: 균일한 두께를 갖는 정방형이나 장방형 단면의 플랜지를 제외하고, 균일압축을 받는 세장판단면의 감소된 유효폭/]
    VarIn4[/입력변수: 부재의 두께/]
    VarIn5[/입력변수: 강재의 탄성계수/]
    VarIn6[/입력변수: 세장판 단면의 응력/]
    VarIn7[/입력변수: 세장판 단면의 폭/]
    VarOut1~~~VarIn4
    VarIn1~~~VarIn5
    VarIn2~~~VarIn6
    VarIn3~~~VarIn7

		end

		Python_Class ~~~ Variable_def
	  C["<img src='https://latex.codecogs.com/svg.image?&space;Q_{a}=\frac{A_{e}}{A_{g}}'>-----------------------------"] ;
    D["균일한 두께를 갖는 정방형이나 장방형 단면의 플랜지를 제외하고, 균일압축을 받는 세장판 단면"] ;
    E["<img src='https://latex.codecogs.com/svg.image?\frac{b}{t}\geq&space;1.49\sqrt{\frac{E}{f}}'>-------------------------------------------"] ;
    F(["<img src='https://latex.codecogs.com/svg.image?b_{e}=1.92t\sqrt{\frac{E}{f}}\left[1-\frac{0.34}{(b/t)}\sqrt{\frac{E}{f}}\right]\leq&space;b'>------------------------------------------------------------------------------------------"]) ;


	  Variable_def-->C-->D-->E-->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Reduction_factor_of_slender_double_rib_support_plate(fOQa,fIAg,fIAe,fIbe,fIt,fIE,fIf,fIb) -> float:
        """세장한 양연지지판의 저감계수

        Args:
            fOQa (float): 세장한 양연지지판의 저감계수
            fIAg (float): 부재의 총단면적
            fIAe (float): 감소된 be를 고려하여 산정한 유효단면적의 합
            fIbe (float): 균일한 두께를 갖는 정방형이나 장방형 단면의 플랜지를 제외하고,균일압축을받는세장판단면의감소된유효폭
            fIt (float): 부재의 두께
            fIE (float): 강재의 탄성계수
            fIf (float): 세장판 단면의 응력
            fIb (float): 세장판 단면의 폭

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법) 4.2.7.2 세장한 양연지지판 (1)의 값
        """



        if fIb/fIt >= 1.49(fIE/fIf)**0.5:
          fIbe = 1.92*fIt*(fIE/fIf)**0.5(1-(0.34/(fIb/fIt))*(fIE/fIf)**0.5)

        else:
          fOQa = fIAe/fIAg

        return fOQa


# 

