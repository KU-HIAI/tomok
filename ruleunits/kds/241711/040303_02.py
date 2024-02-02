import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_040303_02(RuleUnit): # KDS241711_040303_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.3.3 (2)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-22'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '교량의 주기'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.3 해석방법
    4.3.3 단일모드스펙트럼해석법
    (2)
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
	A([교량의 주기])
	B["KDS 24 17 11 4.3.3(2)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 교량의 주기/]
	VarIn1[/입력변수: 중력가속도/]
	VarIn2[/입력변수: 교량 상부구조와 이의 동적거동 영향을 주는 하부구조의 단위길이당 고정하중/]
	VarIn3[/입력변수: 균일한 등분포하중/]
	VarIn4[/입력변수: 설계변수/]

	VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
	end
	Python_Class ~~~ Variable_def --> E & G --> D --> H
	D["<img src='https://latex.codecogs.com/svg.image?T=2\pi\sqrt{\frac{\gamma}{\rho&space;_0g\alpha}}'>--------------------"]
	E["<img src='https://latex.codecogs.com/svg.image?\alpha=\int&space;v_s(x)dx'>--------------------"]
	G["<img src='https://latex.codecogs.com/svg.image?\gamma=\int&space;w(x)v_s(x)^2dx'>-----------------------"]
	H([교량의 주기 T])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Bridge_cycle(fOT,fIg,fIwx,fIpo,fIdesvar,fIgamma) -> float:
        """교량의 주기

        Args:
            fOT (float): 교량의 주기
            fIg (float): 중력가속도
            fIwx (float): 교량 상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중
            fIpo (float): 균일한 등분포하중
            fIdesvar (float): 설계변수 ɑ
            fIgamma (float): 설계변수 r
        Returns:
            float: fOT, 교량의 주기
        """

        from math import pi
        fOT = 2 * pi * (fIgamma / (fIpo * fIg * fIdesvar))**0.5
        return fOT