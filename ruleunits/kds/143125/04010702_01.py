import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010702_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.7.2' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭지압강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.7 지압강도
    4.1.7.2 확장롤러 및 확장록커
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
  	A([Title: 확장룰러 및 확장록커])
  	B["KDS 14 31 25 4.1.7.2(1)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
    VarOut[/출력변수: 공칭지압강도/]
  	VarIn1[/입력변수: 항복강도/]
  	VarIn2[/입력변수: 투영된 지압면적/]
  	VarOut ~~~ VarIn1 & VarIn2
  	end

  	Python_Class ~~~ Variable_def --> C --> D --Pass--> E --> F
  	C["<img src='https://latex.codecogs.com/svg.image?d\leq&space;635mm'>---------------"]
  	D["Pass or Fail"]
  	E["<img src='https://latex.codecogs.com/svg.image?R_n=1.2(F_y-90)ld/20'>------------------------------------"]
  	F(["<img src='https://latex.codecogs.com/svg.image?R_n'>---------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def nominal_bearing_strength(fORn,fIFy,fId,fIl) -> bool:
        """공칭지압강도

        Args:
            fORn (float): 공칭지압강도
            fIFy (float): 항복강도
            fId (float): 직경
            fIl (float): 지압길이

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.7.2 확장롤러 및 확장록커의 공칭지압강도 (2)의 값
        """

        if fId <= 635 :
          fORn = (1.2)*(fIFy-90)*fIl*fId/20
          return fORn


# 

