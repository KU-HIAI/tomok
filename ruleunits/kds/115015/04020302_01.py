import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04020302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.2.3.2 (1)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-31'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '케이슨 기초지반의 연직지반반력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.2.3.2 고려사항
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
    A[케이슨 기초지반의 연직지반반력];
    B["KDS 11 50 15 4.2.3.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 케이슨 기초지반의 연직지반반력/];
    VarIn1[/입력변수: 케이슨을 통해 전달되는 모든 연직하중/] ;
    VarIn2[/입력변수: 케이슨 저면적/];


		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["케이슨 기초지반의 연직지반반력= 케이슨을 통해 전달되는 모든 연직하중/케이슨 저면적"];
    D(["케이슨 기초지반의 연직지반반력"]);

    C--->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def vertical_ground_reaction_force_of_caisson_foundationground(fOvgrfcf,fIgldgrc,flbotarc) -> float:
        """케이슨 기초지반의 연직지반반력

        Args:
            fOvgrfcf (float): 케이슨 기초지반의 연직지반반력
            fIgldgrc (float): 케이슨을 통하여 지반에 전달되는 모든 연직하중
            flbotarc (float): 케이슨의 저면적

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.2.3.2 고려사항 (1)의 값
        """

        fOvgrfcf = fIgldgrc / flbotarc
        return fOvgrfcf


# 

