import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010102_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.1.2 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소편심 및 휨모멘트'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
    (5)
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
    A["휨 및 축력이 작용하는 부재의 극한한계상태 검증"];
    B["KDS 24 14 21 4.1.1.2 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 축력/];
    VarIn2[/입력변수: 최소 편심 eo/] ;
		VarIn3[/입력변수: 단면의 깊이/] ;
		VarIn4[/입력변수: 실제 휨모멘트/] ;
		VarOut1[/출력변수: 계산한 휨모멘트/];

		VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C--->D-->E
		C["<img src='https://latex.codecogs.com/svg.image?&space;20mm\leq&space;e_{0}=h/30'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?M_{u}&space;\geq&space;e_{o}N_{u}'>---------------------------------"]
		E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_eccentricity_and_Bending_moment(fIcalbem,fIaxifor,fIminece,fIh,fIactbem) -> bool:
        """최소편심 및 휨모멘트

        Args:
             fIcalbem (float): 계산한 휨모멘트
             fIaxifor (float): 축력
             fIminece (float): 최소편심 eo
             fIh (float): 단면의 깊이
             fIactbem (float): 실제 휨모멘트(Actual bending moment)



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (5)의 통과 여부
        """

        fIminece = fIh/30
        fIcalbem = fIminece*fIaxifor
        if fIminece >= 20 and fIactbem >= fIcalbem:
          return "Pass"
        else:
          return "Fail"


# 

