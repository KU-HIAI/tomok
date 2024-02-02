import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_04110304 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.11.3.4' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '강바닥판의 설계휨강도 검토'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.3 강바닥판
    4.11.3.4 횡방향휨
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
    A[가로보와 바닥판의 설계휨강도];
    B["KDS 24 14 31 4.11.3.4"];
    A ~~~ B
    end

		subgraph Variable_def;
    VarIn1[/입력변수: 설계하중에 의해 가로보에 작용되는 모멘트/] ;
    VarIn2[/입력변수: 가로보의 설계휨강도/];
    VarIn3[/입력변수: 인접리브로부터 전달되는 축중하중에 의한 바닥판의 휨방향설계모멘트/];
    VarIn4[/입력변수: 인접리브로부터 전달되는 축중하중에 의한 바닥판의 휨방향설계휨강도/];

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
		end
		Python_Class ~~~ Variable_def;

		C["<img src='https://latex.codecogs.com/svg.image?\frac{M_{fb}}{M_{rb}}&plus;\frac{M_{ft}}{M_{rt}}\leq&space;1.0'>-----------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\frac{M_{fb}}{M_{rb}}\leq&space;1.0'>---------------------"]

		E{"가로보의 간격 &ge;종방향리브의 복부판 간격x3"}

		Variable_def --> E
		E --yes--> D
		E --No--> C

		C & D --> F([Pass or fail])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Examine_the_Design_bending_strength_of_steel_floor_plate(fIMfb,fIMrb,fIMft,fIMrt,fIsphobe,fIspaplr) -> bool:
        """강바닥판의 설계휨강도 검토

        Args:
            fIMfb (float): 설계하중에 의해 가로보에 작용되는 모멘트
            fIMrb (float): 가로보의 설계휨강도
            fIMft (float): 인접리브로부터 전달되는 축중하중에 의한 바닥판의 횡방향 설계모멘트
            fIMrt (float): 인접리브로부터 전달되는 축중하중에 의한 바닥판의 횡방향 설계휨강도
            fIsphobe (float): 가로보의 간격
            fIspaplr (float): 종방향리브의 복부판 간격

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.11.3.4 횡방향휨의 통과 여부
        """

        if fIsphobe < 3*fIspaplr :
           (fIMfb/fIMrb)+(fIMft/fIMrt) <= 1.0
           return "Pass"
        else:
           return "Fail"

        if fIsphobe >= 3*fIspaplr :
           fIMfb/fIMrb <= 1.0
           return "Pass"
        else:
           return "Fail"


# 

