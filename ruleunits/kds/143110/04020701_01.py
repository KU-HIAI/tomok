import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04020701_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.7.1 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '세장한 자유돌출판의 저감계수'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    4.2.7.1 세장한 자유돌출판
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
		A[세장한 자유돌출판] ;
		B["KDS 14 31 10 4.2.7.1(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 세장한 자유돌출판의 저감계수/]
    VarIn1[/입력변수: 자유돌출판의 폭/]
    VarIn2[/입력변수: 부재의 두께/]
    VarIn3[/입력변수: 강재의 탄성계수/]
    VarIn4[/입력변수: 강재의 항복강도/]

		end

		Python_Class ~~~ Variable_def
	C["<img src='https://latex.codecogs.com/svg.image?Q_{s}'>------"] ;
  D["<img src='https://latex.codecogs.com/svg.image?b/t\leq&space;0.56\sqrt{E/F_{y}}'>------------------------------------------------------"] ;
  E["<img src='https://latex.codecogs.com/svg.image?0.56\sqrt{E/F_{y}}<b/t<1.03\sqrt{E/F_{y}}'>-----------------------------------------------------------------"] ;
  F["<img src='https://latex.codecogs.com/svg.image?b/t\geq&space;1.03\sqrt{E/F_{y}}'>------------------------------------------"] ;
  G(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.0'>-----------------"]) ;
  H(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.415-0.74\left(\frac{b}{t}\right)\sqrt{\frac{F_{y}}{E}}'>---------------------------------------------------------------"]) ;
  I(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=\frac{0.69E}{F_{y}\left(\frac{b}{t}\right)^{2}'>-----------------------------------"]) ;

	Variable_def-->C-->D & E & F
D-->G
E-->H
F-->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Reduction_factor_of_slender_free_projection_plate(fOQs,fIb,fIt,fIFy,fIE) -> float:
        """세장한 자유돌출판의 저감계수

        Args:
            fOQs (float): 세장한 자유돌출판의 저감계수
            fIb (float): 자유돌출판의 폭
            fIt (float): 부재의 두께
            fIFy (float): 강재의 항복강도
            fIE (float): 강재의 탄성계수
            fIkc (float): 자유돌출 세장판 요소의 계수

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법) 4.2.7.1 세장한 자유돌출판  (2)의 값
        """



        if fIb/fIt <= 0.56*(fIE/fIFy)**0.5:
          fOQs = 1.0

        elif 0.56*(fIb/fIt) < fIb/fIt < 1.03*(fIE/fIFy)**0.5:
          fOQs = 1.415 - 0.74*(fIb/fIt)*(fIFy/(fIE))**0.5

        else:
          fOQs = 0.69*fIE/(fIFy*(fIb/fIt)**2)

        return fOQs


# 

