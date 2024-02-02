import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010504_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.5.4 (7)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '3축 압축 절점영역에서 3방향 스트럿의 힘의 분배를 모두 알 경우 콘크리트 스트럿의 유효설계강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.5 스트럿-타이 모델
    4.1.5.4 절점영역
    (7)
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
    A["절점영역"];
    B["KDS 24 14 21 4.1.5.4 (7)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 스트럿의 유효설계강도/];
		VarIn2[/입력변수: 콘크리트 기준압축강도/];
		VarIn3[/입력변수: 콘크리트 재료계수/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->D--->C--->E
		D{"3축 압축절점영역에서 3방향 스트럿 모두 힘 분배를 알 경우"}
		C["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}\leq&space;3(1-f_{ck}/250)\phi&space;_cf_{ck}'>---------------------------------"]
		E(["Pass or Fail"])
		C~~~ |"KDS 24 14 21 3.1-43, 44"| C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_design_strength_of_concrete_struts(fIfcdmax,fIfck,fIphic) -> bool:
        """3축 압축 절점영역에서 3방향 스트럿의 힘의 분배를 모두 알 경우 콘크리트 스트럿의 유효설계강도

        Args:
             fIfcdmax (float): 콘크리트 스트럿의 유효설계강도
             fIfck (float): 콘크리트 기준압축강도
             fIphic (float): 콘크리트 재료계수

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.5.4 절점영역 (7)의 통과 여부
        """

        if fIfcdmax <= 3*(1-fIfck/250)*fIphic*fIfck:
          return "Pass"
        else:
          return "Fail"


# 

