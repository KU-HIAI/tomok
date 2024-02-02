import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_0411208_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.11.2.8 (3)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '트러스교의 연결판'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.2 트러스교
    4.11.2.8 연결판
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
	  A[연결판의 최대응력]
	  B["KDS 24 14 31 4.11.2.8(3)"]
	  A ~~~ B

	  end

	  subgraph Variable_def
	  VarOut1[/출력변수: 최대전단응력/]
	  VarIn1[/입력변수: 최대응력/]
	  VarIn2[/입력변수: 전단에 대한 강도저항계수/]
	  VarIn3[/입력변수: 강재의 설계기준항복강도/]
	  VarIn4[/입력변수: 순수전단/]
	  VarIn5[/입력변수: 강재의 최소인장강도/]
	  VarIn6[/입력변수: 휨전단응력/]

	  VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6

	  end

	  Python_Class ~~~ Variable_def

	  C["최대응력 <img src='https://latex.codecogs.com/svg.image?\dpi{10}\leq\phi&space;_{v}F_{y}'>---------------"]
	  D["최대전단응력 =\n <img src='https://latex.codecogs.com/svg.image?\phi&space;_{v}F_{u}/\sqrt{3}'>---------------"]
	  E["휨전단응력 =\n <img src='https://latex.codecogs.com/svg.image?\phi&space;0.74F_{u}/\sqrt{3}'>------------------------"]


	  Variable_def --> C --> K([Pass or Fail])
	  Variable_def --"순수전단"--> D --> I(["최대전단응력"])
	  Variable_def  --> E -->Q(["휨전단응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Connecting_plate_of_truss_bridge(fImaxstr,fIphiv,fIFy,fOmaxshs,fIpurshe,fIFu,fImomshs,fIuserdefined) -> bool:
        """트러스교의 연결판

        Args:
            fImaxstr (float): 최대응력
            fIphiv (float): 전단에 대한 강도저항계수
            fIFy (float): 강재의 설계기준항복강도
            fOmaxshs (float): 최대전단응력
            fIpurshe (float): 순수전단
            fIFu (float): 강재의 최소인장강도
            fImomshs (float): 휨전단응력
            fIuserdefined (float): 사용자 선택


        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.11.2.8 연결판 (3)의 값
        """

        if fImaxstr < fIphiv*fIFy :
          return fImaxstr, "Pass"
        else:
          return fImaxstr, "Fail"

        if fIuserdefined == 1:
          fOmaxshs = (fIphiv*fIFu)/(3**(1/2))
          return fOmaxshs

        if fIuserdefined == 2:
          fOmaxshs = (fIphiv*0.74*fIFu)/(3**(1/2))
          return fOmaxshs

        if fIuserdefined == None:
          fOmaxshs = (fIphiv*0.74*fIFu)/(3**(1/2))
          return fOmaxshs


# 

