import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04180502_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.5.2 (3)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '항로이탈확률'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
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
        A[항로이탈확률 근사적 방법];
        B["KDS 24 12 21 4.18.5.2 (3)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 항로이탈확률/];
    VarIn1[/입력변수 : 항로이탈의 기본율/];
    VarIn2[/입력변수 : 교량의 위치에 따른 보정계수/];
    VarIn3[/입력변수 : 선박의 통과경로에 평행한 유속에 대한 보정계수/];
    VarIn4[/입력변수 : 선박의 통과경로의 직각방향 유속에 대한 보정계수/];
    VarIn5[/입력변수 : 통행선박의 밀도에 대한 보정계수/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    end
    Python_Class~~~Variable_def
    D{"선박의 경우"};
    E{"바지선의 경우"};
    F["<img src='https://latex.codecogs.com/svg.image?BR=0.6\times10^{-4}'>--------------------------------------"];
    G["<img src='https://latex.codecogs.com/svg.image?BR=1.2\times10^{-4}'>--------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?PA=(BR)(R_{B})(R_{C})(R_{XC})(R_{D})'>------------------------------------------------------------------------------------"];
    I(["항로이탈확률"]);
    Variable_def--->D--->F--->H--->I
    Variable_def--->E--->G--->H
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def probability_of_departure_from_course(fOPA,fIBR,fIRb,fIRc,fIRxc,fIRd,fIuserdefine) -> float:
        """항로이탈확률

        Args:
            fOPA (float): 항로이탈확률
            fIBR (float): 항로이탈의 기본율
            fIRb (float): 보정계수
            fIRc (float): 통과경로에 평행한 유속에 대한 보정계수
            fIRxc (float): 통과경로에 직각방향 유속에 대한 보정계수
            fIRd (float): 통행선박의 밀도에 대한 보정계수
            fIuserdefine (float): 사용자가 정의한 값
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.5.2 항로이탈확률 (3) 의 값
        """

        #선박의 경우 : fIuserdefine = 1
        #바지선의 경우 : fIuserdefine = 2

        if fIuserdefine==1:
          fIBR = 0.6*10**-4
        if fIuserdefine==2:
          fIBR = 1.2*10**-4

        fOPA = fIBR*fIRb*fIRc*fIRxc*fIRd
        return(fOPA)


# 

