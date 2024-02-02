import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040304_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.4 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장력을 받는 앵커의 콘크리트측면파열강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.4 인장력을 받는 앵커의 콘크리트측면파열강도
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
    A[인장력을 받는 헤드앵커의 콘크리트측면파열강도];
    B["KDS 14 20 54 4.3.4 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def
	  VarIn1[/입력변수 : 단일 헤드앵커의 공칭측면파열강도/];
  	VarIn2[/입력변수 : 앵커의 유효묻힘깊이/];
  	VarIn3[/입력변수 : 콘크리트의 설계기준압축강도/];
  	VarIn4[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
  	VarIn5[/입력변수 : 스터드 또는 앵커볼트의 헤드 지압면적/];
  	VarIn6[/입력변수 : 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수/];
  	VarIn7[/입력변수 : 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트 단부까지 거리/];
  	VarIn1 & VarIn2 ~~~ VarIn5
  	VarIn3 ~~~ VarIn6
  	VarIn4 ~~~ VarIn7

  	end
  	Python_Class~~~Variable_def
  	D["<img src='https://latex.codecogs.com/svg.image?h_{ef}\geq 2.5c_{a1}'>--------------------------------"];
  	E["<img src='https://latex.codecogs.com/svg.image?c_{a2} < 3c_{a1}'>--------------------------------"];
  	F["<img src='https://latex.codecogs.com/svg.image?N_{sb} \leq \frac{(1+c_{a2}/c_{a1})}{4}(13c_{a1}\sqrt{A_{brg}})\lambda _{a}\sqrt{f_{ck}}'>--------------------------------"];
  	G["<img src='https://latex.codecogs.com/svg.image?1.0 \leq c_{a2}/c_{a1} \leq 3.0'>--------------------------------"];
  	H["<img src='https://latex.codecogs.com/svg.image?N_{sb} \leq (13c_{a1}\sqrt{A_{brg}})\lambda _{a}\sqrt{f_{ck}}'>--------------------------------"];
  	I(["Pass of Fail"]);
  	Variable_def--->D--->E
  	E--Yes--->G--->F
  	E--No--->H
  	F & H ---> I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_lateral_tear_strength_of_anchor_under_tensile_force(fIhef,fINsb,fIcaone,fIAbrg,fIlamda,fIfck,fIcatwo) -> float:
        """인장력을 받는 앵커의 콘크리트측면파열강도

        Args:
            fIhef (float): 앵커의 유효묻힘깊이
            fINsb (float): 공칭측면파열강도
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의거리
            fIAbrg (float): 스터드 또는 앵커볼트의 헤드 지압 면적
            fIlamda (float): 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수
            fIfck (float): 콘크리트의 설계기준압축강도
            fIcatwo (float): 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트 단부까지 거리

        Returns:
            float: 4.3.4 인장력을 받는 앵커의 콘크리트측면파열강도 (1)의 통과여부
        """

        if fIhef >= 2.5 * fIcaone :
          if fIcatwo < 3 * fIcaone :
            if 1.0 <= fIcatwo / fIcaone and fINsb <= (1 + fIcatwo/fIcaone)/4 * (13 * fIcaone * ((fIAbrg)**0.5)) * fIlamda * ((fIfck)**0.5) :
              return "Pass"
            else:
              return "Fail"
          else:
            if fINsb <= (13 * fIcaone * ((fIAbrg)**0.5)) * fIlamda * ((fIfck)**0.5) :
              return "Pass"
            else:
              return "Fail"


