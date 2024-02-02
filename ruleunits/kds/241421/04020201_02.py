import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020201_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.2.1 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '강재의 응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.2 응력 한계
    4.2.2.1 기본 사항
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
    A["강재의 응력"];
    B["KDS 24 14 21 4.2.2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 철근의 인장응력/];
		VarIn2[/입력변수: 철근의 기준항복강도/];
		VarIn3[/입력변수: 프리스트레스 강재의 응력/];
		VarIn4[/입력변수: 프리스트레스 강재의 인장강도/];

		VarIn1 & VarIn2  & VarIn3 & VarIn4

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C{"하중조합에 따라"}
		C--사용하중조합1 일때--->D
		D["철근의 인장응력≤<img src='https://latex.codecogs.com/svg.image?0.8f_{y}'>---------------------------------"]
		C--유효 프리스트레스와 사용한계상태 하중조합V 일때--->E
		E["프리스트레스 강재의 응력≤<img src='https://latex.codecogs.com/svg.image?0.75f_{pu}'>---------------------------------"]
		E & D-->F
		F(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Stress_in_steel(fItensrb,fIfy,fIstrpst,fIfpu,fIuserdefined) -> bool:
        """강재의 응력

        Args:
             fItensrb (float): 철근의 인장응력
             fIfy (float): 철근의 기준항복강도
             fIstrpst (float): 프리스트레스 강재의 응력
             fIfpu (float): 프리스트레스 강재의 인장강도
             fIuserdefined (float): 사용자 선택


        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.2.2.1 기본 사항 (2)의 통과 여부
        """

        #사용하중조합-I의 경우: fIuserdefined = 1
        #유효 프리스트레스와 사용한계상태 하중조합-V의 경우: fIuserdefined = 2

        if fIuserdefined == 1:
          if fItensrb <= 0.8 * fIfy:
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined == 2:
          if fIstrpst <= 0.65 * fIfpu:
            return "Pass"
          else:
            return "Fail"


# 

