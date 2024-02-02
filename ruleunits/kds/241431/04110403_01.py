import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_04110403_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.11.4.3 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '복부판 사이에 있는 플랜지의 폭-두께비'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.4 충복아치
    4.11.4.3 플랜지 좌굴
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
    A[복부판 사이에 있는 플랜지의 폭-두께비];
    B["KDS 24 14 31 4.11.4.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
    VarIn1[/입력변수: 플랜지의 폭-두께비/] ;
    VarIn2[/입력변수: 모멘트 확대계수를 고려한 설계하중에 의한 최대응력/];
    VarIn3[/입력변수: 설계하중에 의한 축방향응력/];
    VarIn4[/입력변수: 탄성계수/];
		VarIn5[/입력변수: 플랜지의 폭/];
    VarIn6[/입력변수: 플랜지의 두께/];

		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ Variable_def

		C["<img src='https://latex.codecogs.com/svg.image?\frac{b}{t}\leq&space;1.06\sqrt{\frac{E}{f_{a}&plus;f_{b}}}'>----------------------------------------"]

		Variable_def --> C
		C --> D([Pass or Fail])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def flange_between_the_rib_web_plate_width_thickness_ratio(fIfbwtra,fIfb,fIfa,fIE,fIb,fIts) -> bool:
        """복부판 사이에 있는 플랜지의 폭-두께비

        Args:
            fIfbwtra (float): 복부판 사이에 있는 플랜지의 폭-두께비
            fIfb (float): 모멘트 확대계수를 고려한 설계하중에 의한 최대응력
            fIfa (float): 설계하중에 의한 축방향응력
            fIE (float): 탄성계수
            fIb (float): 보강재의 폭
            fIts (float): 보강재의 두께

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.11.4.3 플랜지 좌굴 (1)의 통과 여부
        """

        temp=(fIE/(fIfa+fIfb))**(1/2)
        if fIb/fIts <= 1.06*temp :
           return "Pass"
        else:
           return "Fail"


# 

