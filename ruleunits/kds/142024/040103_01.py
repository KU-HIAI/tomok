import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040103_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jaeguk Jang'  # 작성자명
    ref_code = 'KDS 14 20 24 4.1.3 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-08-09'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '계수하중에 의한 스트럿과 타이의 단면력 검토'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준(한계상태설계법)
    4. 설계
    4.1 스트럿-타이 모델 설계 절차
    4.1.3 설계 원칙
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
    A[스트럿, 타이 그리고 절점영역의 설계];
    B["KDS 14 20 24 4.1.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수 : 계수하중에 의한 스트럿과 타이의 단면력/];
		VarIn2[/입력변수 : 절점영역의 한 면에 작용하는 단면력/];
		VarIn3[/입력변수 : 스트럿, 타이 그리고 절점영역의 공칭축강도/];
		VarIn4[/입력변수 : 스트럿의 강도감소계수/];
		VarIn5[/입력변수 : 타이의 강도감소계수/];
		VarIn1 ~~~ VarIn3
		VarIn2 ~~~ VarIn4
    end

		Python_Class ~~~ Variable_def

		D{"강도감소계수"};
		E["<img src='https://latex.codecogs.com/svg.image?\phi&space;_{c} = 0.75'>"];
		F["<img src='https://latex.codecogs.com/svg.image?\phi&space;_{t} = 0.85'>"];
		Variable_def --->D
		D--스트럿--->E
		D--타이--->F

		G["<img src='https://latex.codecogs.com/svg.image?\phi&space;F_{n}\geq&space;F_{u}'>"];
		E--->G
		F--->G
		G--->H([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Examine_the_sectional_forces_in_struts_and_ties_under_counting_loads(fISFu, fINFu, fIFn, fIpiec, fIpiet) -> bool:
        """계수하중에 의한 스트럿과 타이의 단면력 검토

        Args:
            fISFu (float): 계수하중에 의한 스트럿과  타이의 단면력.
            fINFu (float): 절점영역의 한 면에 작용하는단면력.
            fIFn (float): 공칭축강도.
            fIpiec (float): 스트럿의 강도감소계수.
            fIpiet (float): 타이의 강도감소계수.

        Returns:
            bool: 콘크리트 스트럿-타이모델 기준  4.1.3 설계원칙 (1)의 통과 여부
        """

        if fIpiec*fIFn >= fISFu and fIpiet*fIFn >= fINFu :
          return "Pass"
        else:
          return "Fail"


# 

