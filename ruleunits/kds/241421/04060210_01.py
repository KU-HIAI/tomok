import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060210_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.10 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '곡선 긴장재에 사용한 횡구속 철근'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.10 곡선 긴장재의 영향을 고려한 부재 상세
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
    A["곡선 긴장재의 영향을 고려한 부재 상세"];
    B["KDS 24 14 21 4.6.2.10 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:철근응력/];
		VarIn2[/입력변수:철근의 기준항복강도/];
		VarIn3[/입력변수:횡구속철근의 간격/];
		VarIn4[/입력변수: 덕트 외측지름/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

		Python_Class ~~~ Variable_def---> G & H

		G["철근응력 <img src='https://latex.codecogs.com/svg.image?\leq&space;0.6f_y'>---------------------------------"]

		H["횡구속철근간격≤덕트 외측지름X3 or 600mm"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def transverse_confinement_bars_for_curved_tension_member(fIrebstr,fIfy,fIspatcb,fIduoudi) -> bool:
        """곡선 긴장재에 사용한 횡구속 철근
        Args:
             fIrebstr (float): 철근응력
             fIfy (float): 철근의 기준항복강도
             fIspatcb (float): 횡구속철근의 간격
             fIduoudi (float): 덕트 외측지름

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.10 곡선 긴장재의 영향을 고려한 부재 상세 (1)의 통과 여부
        """

        if fIrebstr <= 0.6*fIfy and fIfy <= 420 and fIspatcb<=min(3*fIduoudi,600):
          return "Pass"
        else:
          return "Fail"


# 

