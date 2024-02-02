import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04011005 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.10.5' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '무보강 웨브의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.5 웨브 압축좌굴강도
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
	A([무보강 웨브의 설계강도])
	B["KDS 14 31 25 4.1.10.5"]
	A ~~~ B
	end

	subgraph Variable_def
  VarOut[/출력변수: 무보강 웨브의 설계강도/]
	VarIn1[/입력변수: 집중하중에 저항하는 거리/]
	VarIn2[/입력변수: 부재깊이/]
	VarIn3[/입력변수: 웨브두께/]
	VarIn4[/입력변수: 강재의 탄성계수/]
	VarIn5[/입력변수: 압연강재의 경우 필릿 또는 코너반경을 제외한 플랜지 간 순거리, 조립단면의 경우 연결재선 사이의 거리 또는 용접한 경우에는 플랜지 간 순거리/]
	VarIn6[/입력변수: 웨브의 최소항복강도/]

	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	VarIn2 ~~~ VarIn4 & VarIn6
	VarIn6 ~~~ VarIn5
	end

	Python_Class ~~~ Variable_def --> C --> D --> E
	E --Pass--> F
	E --Fail--> G
	G --> F
	C["<img src='https://latex.codecogs.com/svg.image?&space;R_n=\frac{24t_w^3\sqrt{EF_{yw}}}{h}'>--------------------------------"]
	D["부재 단부로부터 한쌍의 집중하중에 저항하는 거리 ≥ d/2"]
	E["Pass or Fail"]
	F(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
	G["<img src='https://latex.codecogs.com/svg.image?&space;R_n\times&space;0.5'>----------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_of_unreinforced_web(fOphiRn,fIdirecl,fId,fItw,fIE,fIh,fIFyw) -> bool:
        """무보강 웨브의 설계강도
        Args:
            fOphiRn (float): 무보강 웨브의 설계강도
            fIdirecl (float): 집중하중에 저항하는 거리
            fId (float): 부재깊이
            fItw (float): 웨브두께
            fIE (float): 강재의 탄성계수
            fIh (float): 압연강재의 경우 필릿 또는 코너반경을 제외한 플랜지 간 순거리, 조립단면의 경우 연결재선 사이의 거리 또는 용접한 경우에는 플랜지 간 순거리
            fIFyw (float): 웨브의 최소항복강도

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.5 웨브 압축좌굴강도의 값
        """

        if fIdirecl < fId/2 :
          fOphiRn = (24 * (fItw**3) * ((fIE * fIFyw)**0.5)) / fIh * 0.5
        else :
          fOphiRn = (24 * (fItw**3) * ((fIE * fIFyw)**0.5)) / fIh

        return fOphiRn


# 

