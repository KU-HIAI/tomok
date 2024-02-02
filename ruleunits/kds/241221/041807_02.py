import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041807_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.7 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수리동적질량계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.7 선박충돌에너지
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
        A[수리동적질량계수];
        B["KDS 24 12 21 4.18.7 (2)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 수리동적질량계수/];
    VarIn1[/입력변수 : 용골과 수로바닥과의 간격/];
    VarIn2[/입력변수 : 선박의 흘수/];
    VarIn3[/입력변수 : 선박의 바닥과 수로의 바닥간의 간격/];
    end
    Python_Class~~~Variable_def
    C["용골과 수로바닥과의 간격=선박의 바닥과 수로의 바닥간의 간격"]
    K{"용골과 수로바닥과의 간격과 선박의 흘수 관계"}
    D["용골과 수로바닥과의 간격>선박의 흘수X0.5"];
    E["용골과 수로바닥과의 간격<선박의 흘수X0.1"];
    F["선박의 흘수X0.1<용골과 수로바닥과의 간격<선박의 흘수X0.5"];
    G["<img src='https://latex.codecogs.com/svg.image?C_{H}=1.05'>-------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?C_{H}=1.25'>-------------------------------"];
    I["적절히 보간"];
    J(["등가 정적선박충격하중"]);
    Variable_def--->C--->K--->D--->G--->J
    K--->E--->H--->J
    K--->F--->I--->J
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def mathematical_dynamic_mass_factor(fIdkeebw,fIdraft,fOCH,fIdbshbw) -> float:
        """수리동적질량계수

        Args:
            fIdkeebw (float): 용골과 수로바닥과의 간격
            fIdraft (float): 선박의 흘수
            fOCH (float): 수리동적질량계수
            fIdbshbw (float): 선박의 바닥과 수로의 바닥간의 간격
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.7 선박충돌에너지 (2) 의 값
        """

        fIdkeebw = fIdbshbw
        if fIdkeebw > fIdraft*0.5:
          fOCH = 1.05
        if fIdkeebw < fIdraft*0.1:
          fOCH = 1.25
        if fIdraft*0.1 <= fIdkeebw <= fIdraft*0.5:
          fOCH = 1.25 - 0.2*(fIdkeebw-fIdraft*0.1)/(fIdraft*0.5-fIdraft*0.1)

        return(fOCH)


# 

