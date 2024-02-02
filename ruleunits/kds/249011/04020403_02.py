import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020403_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '회전수용능력'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.3 회전수용능력
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
    A[회전수용능력];
    B["KDS 24 90 11 4.2.4.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 피스톤과 포트벽과의 최대 마찰계수/];

		VarIn1
		end

		Python_Class ~~~ Variable_def;
		Variable_def--> C --->D

		C{"탄생패드에 발생하는 최대 구속모멘트와 피스톤과 포트벽의 마찰에 의한 모멘트 고려하여 설계 시"}
		D["피스톤과 포트벽과의 최대 마찰계수=0.2"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_Coefficient_Of_Friction_Between_Piston_And_Port_Wall (fImaxcof) -> bool:
        """회전수용능력
        Args:
            fImaxcof (float): 피스톤과 포트벽과의 최대 마찰계수

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)   4.2.4.3 회전수용능력 (2)의 값
        """


        fImaxcof = 0.2
        return fImaxcof


# 

