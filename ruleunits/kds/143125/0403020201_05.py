import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020201_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.2.1 (5)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축 지강관벽 세장비'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.1 적용한계
    (5)
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
		A[Title: 적용한계] ;
		B["KDS 14 31 25 4.3.2.2.1 (5)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut1[/출력변수: 압축 지강관벽의 세장비/] ;
	  VarIn1[/입력변수: 벽의 폭두께비/]
	  VarIn2[/입력변수: 강재의 탄성계수/]
	  VarIn3[/입력변수: 지강관 항복강도/]
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ Variable_def

   	C["벽의 폭두께비 ≤ <img src='https://latex.codecogs.com/svg.image?&space;1.1(E/F_{yb})^{0.5}'>----------------------------------- "] ;
   	D["벽의 폭두께비 ≤ 35"] ;
    E["벽의 폭두께비 ≤ <img src='https://latex.codecogs.com/svg.image?&space;1.25(E/F_{yb})^{0.5}'>-----------------------------------"] ;
  	Variable_def --> E
    E--간격 K형 접합과 T,Y,X형 접합-->D
    E--겹침 K형 접합-->C
		C & D -->Q["압축 지강관벽 세장비 = 벽의 폭두께비"] --> R(["압축 지강관벽 세장비"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Slenderness_ratio_of_compressed_steel_pipe_wall(fIsrcspw,fIE,fIFyb,fIuserdefined) -> bool:
        """압축 지강관벽 세장비
        Args:
            fIsrcspw (float): 압축 지강관벽 세장비
            fIE (float): 강재의 탄성계수
            fIFyb (float): 지강관의 항복강도
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.2.2.1 적용한계 (5)의 통과여부
        """

        # 간격 K형 접합과 T, Y, X형 접합 : fIuserdefined == 1
        # 겹침 K형 접합 : fIuserdefined == 2

        if fIuserdefined == 1:
          if fIsrcspw <= 1.25*((fIE/fIFyb)**0.5) and fIsrcspw <= 35:
            return "Pass"
          else:
            return "Fail"

        if fIuserdefined == 2:
          if fIsrcspw <= 1.1*((fIE/fIFyb)**0.5) :
            return "Pass"
          else:
            return "Fail"


# 

