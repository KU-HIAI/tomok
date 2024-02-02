import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060602_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.6.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '비합성 기둥의 축방향 긴장재 및 철근'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.2 기둥의 축방향 철근
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
    A["기둥의 축방향 철근"];
    B["KDS 24 14 21 4.6.6.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:겹침이음 위치가 아닌 일반 단면에서의 축방향 철근 단면적/];
		VarIn2[/입력변수:기둥의 단면적/];
		VarIn3[/입력변수:프리스트레싱 강재의 단면적/];
		VarIn4[/입력변수:프리스트레싱 강재의 설계인장강도/];
		VarIn5[/입력변수:축방향 철근의 설계기준항복강도/];
		VarIn6[/입력변수:콘크리트의 설계기준압축강도/];


		VarIn1 & VarIn2 & VarIn3~~~VarIn4 & VarIn5 & VarIn6
		end

		Python_Class ~~~ Variable_def--->E

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\frac{A_sf_y}{A_gf_{ck}}&plus;\frac{A_{ps}f_{pu}}{A_gf_{ck}}\geq&space;0.135'>---------------------------------"]
		E ---> H(["Pass or Fail"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Axial_tensioners_and_reinforcement_in_non_composite_columns(fIAs,fIAg,fIAps,fIfpu,fIfy,fIfck) ->float:
        """비합성 기둥의 축방향 긴장재 및 철근
        Args:
             fIAs (float): 겹침이음 위치가 아닌 일반 단면에서의 축방향 철근 단면적
             fIAg (float): 기둥의 단면적
             fIAps (float): 프리스트레싱 강재의 단면적
             fIfpu (float): 프리스트레싱 강재의 설계인장강도
             fIfy (float): 축방향 철근의 설계기준항복강도
             fIfck (float): 콘크리트의 설계기준압축강도
        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.6.2 최소단면적 이하로 배치하는 기둥의 축방향 철근(2)의 값
        """

        if (fIAs*fIfy)/(fIAg*fIfck) + (fIAps*fIfpu)/(fIAg*fIfck) >= 0.135:
          return "Pass"
        else:
          return "Fail"


# 

