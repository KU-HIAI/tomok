import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010402_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.4.2 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기둥 기초판의 계수뚫림전단력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.2 뚫림전단 설계
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
    A["기둥 기초판의 계수뚫림전단력"];
    B["KDS 24 14 21 4.1.4.2 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 계수기둥하중/];
		VarIn2[/입력변수: 위험단면 둘레 내의 상향 지반 반력/];
		VarOut1[/출력변수: 기둥 기초판의 계수뚫림전단력/];

		VarOut1~~~VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->E
		C["기둥 기초판의 계수뚫림전단력=계수기둥하중-위험단면 둘레 내의 상향 지반 반력"]

		E(["기둥 기초판의 계수뚫림전단력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Counter_pierce_shear_force_of_column_base_plate(fOVu,fIcoecfo,fIupsrfo) -> float:
        """기둥 기초판의 계수뚫림전단력

        Args:
             fOVu (float): 기둥 기초판의 계수뚫림전단력
             fIcoecfo (float): 계수기둥하중
             fIupsrfo (float): 위험단면 둘레 내의 상향 지반 반력



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.4.2 뚫림전단 설계 (5)의 값
        """

        fOVu = fIcoecfo - fIupsrfo
        return fOVu


# 

