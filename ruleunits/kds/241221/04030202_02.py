import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04030202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.3.2.2 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '한 방향 한 차로의 일일트럭교통량의 설계수명기간동안 평균값'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.2 피로하중
    4.3.2.2 빈도
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
    A[차로 당 통행비율];
    B["KDS 24 12 21 4.3.2.2 (2)"];
    A ~~~ B
    end
	subgraph Variable_def
VarOut[/출력변수 : 한 방향 한차로의 일일트럭교통량의 설계수명기간동안 평균값/];
VarIn1[/입력변수 : 한 방향 일일트럭교통량의 설계수명기간동안 평균값/];
VarIn2[/입력변수 : p/];
VarIn3[/입력변수 : 트럭이 통행가능한 차로 수/];
end
Python_Class~~~Variable_def
C{"단일차로의 일평균 트럭교통량에 대한 확실한 정보가 없을 때"};
D{"트럭이 통행 가능한 차로 수"};
E["p=1.00"];
F["p=0.85"];
G["p=0.80"];
H["<img src='https://latex.codecogs.com/svg.image?ADTT_{SL}=p\times&space;ADTT'>-----------------------------"];
I(["한 방향 한 차로의 일일트럭교통량의 설계수명기간동안 평균값"]);
Variable_def--->C--->D--1차로--->E--->H--->I
D--2차로--->F--->H
D--3차로 이상--->G--->H
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def average_value_of_daily_truck_traffic_on_a_one_way_lane_over_the_design_life_period(fIADTT,fOADTTSL,fIp) -> bool:
        """한 방향 한 차로의 일일트럭교통량의 설계수명기간동안 평균값

        Args:
            fIADTT (float): 한 방향 일일트럭교통량의 설계수명기간동안 평균값
            fOADTTSL (float): 한 방향 한 차로의 일일트럭교통량의 설계수명기간동안 평균값
            fIp (float): 표 4.3-3의 값

        Returns:
            float: 강교 설계기준(한계상태설계법)  4.3.2.2 빈도 (2)의 값
        """

        fOADTTSL = fIp*fIADTT
        return fOADTTSL


# 

