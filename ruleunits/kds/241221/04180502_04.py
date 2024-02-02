import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04180502_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.5.2 (4)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '보정계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
    (4)
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
        A[수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수];
        B["KDS 24 12 21 4.18.5.2 (4)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수/];
    VarIn1[/입력변수 : 꺽임 혹은 곡선영역의 회전각도/];
    end
    Python_Class~~~Variable_def
    C{"수로영역"};
    D["<img src='https://latex.codecogs.com/svg.image?R_{B}=1.0'>"];
    E["<img src='https://latex.codecogs.com/svg.image?R_{B}=1.0&plus;\frac{\theta}{90^{\circ}}'>--------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?R_{B}=1.0&plus;\frac{\theta}{45^{\circ}}'>--------------------------"];
    G(["수로영역에 대한 교량의 상대적인 위치에 관련된 교량위치에 따른 보정계수"]);
    Variable_def--->C--직선영역--->D--->G
    C--전이영역--->E--->G
    C--꺾임/곡선영역--->F--->G
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor(fORb,fIangcur,fIuserdefine) -> float:
        """보정계수

        Args:
            fORb (float): 보정계수
            fIangcur (float): 꺾임 혹은 곡선영역의 회전 각도
            fIuserdefine (float): 사용자가 정의한 값
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.5.2 항로이탈확률 (4) 의 값
        """

        #직선 영역의 경우 : fIuserdefine = 1
        #전이 영역의 경우 : fIuserdefine = 2
        #꺾임/곡선 영역의 경우 : fIuserdefine = 3

        if fIuserdefine==1:
          fORb = 1.0
        if fIuserdefine==2:
          fORb = 1+fIangcur/90
        if fIuserdefine==3:
          fORb = 1+fIangcur/45

        return(fORb)


# 

