import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041811_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.11 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '표준호퍼바지선'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.11 교각에 작용하는 바지선의 충격력
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
        A[교각에 작용하는 표준호퍼바지선의 제원];
        B["KDS 24 12 21 4.18.11 (1)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarIn1[/입력변수 : 폭/];
    VarIn2[/입력변수 : 길이/];
    VarIn3[/입력변수 : 깊이/];
    VarIn4[/입력변수 : 비적재 흘수/];
    VarIn5[/입력변수 : 적재 흘수/];
    VarIn6[/입력변수 : 질량/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3~~~VarIn6

    end
    Python_Class~~~Variable_def
    D["폭=10,700mm, 길이 =60,000mm, 깊이=3,700mm,
    비적재 흘수 =520mm, 적재 흘수=2,700mm, 질량 =1,730미터톤"];
    E{"내륙하천에서 운항되는 바지선인 경우"};
    F(["Pass or Fail"]);
    Variable_def--->E--Yes--->D--->F
    E--No--->F
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def standard_hopper_barge_ship(fIW,fIL,fIDepth,fIdraunl,fIdraloa,fIM) -> bool:
        """표준호퍼바지선

        Args:
            fIW (float): 폭
            fIL (float): 길이
            fIDepth (float): 깊이
            fIdraunl (float): 비적재 홀수
            fIdraloa (float): 적재 홀수
            fIM (float): 질량

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.11 교각에 작용하는 바지선의 충격력 (1) 의 통과여부
        """

        #Pass : 표준호퍼바지선
        #Fail : 표준호퍼바지선의 경우

        if fIW == 10700 and fIL == 60000 and fIDepth == 3700 and fIdraunl == 520 and fIdraloa == 2700 and fIM == 1730:
          return("Pass")
        else:
          return("Fail")


# 

