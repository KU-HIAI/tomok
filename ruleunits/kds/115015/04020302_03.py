import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04020302_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.2.3.2 (3)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-31'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '연직하중에 의한 케이슨 상단의 총 침하량'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.2.3.2 고려사항
    (3)
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
    A[연직하중에 의한 케이슨 상단의 총 침하량];
    B["KDS 11 50 15 4.2.3.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 연직하중에 의한 케이슨 상단의 총 침하량/];
    VarIn1[/입력변수: 케이슨 본체의 탄성변위량/] ;
    VarIn2[/입력변수: 케이슨 기초지반의 침하량/];


		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["연직하중에 의한 케이슨 상단의 총 침하량= 케이슨 본체의 탄성변위량+케이슨 기초지반의 침하량"];
    D(["연직하중에 의한 케이슨 상단의 총 침하량"]);

    C--->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def total_subsidence_at_the_top_of_the_caisson(fOtsubtc,fIeldisc,fIsubcgr) -> float:
        """연직하중에 의한 케이슨 상단의 총 침하량

        Args:
            fOtsubtc (float): 케이슨 상단의 총 침하량
            fIeldisc (float): 케이슨 본체의 탄성변위량
            fIsubcgr (float): 케이슨 기초지반의 침하량

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.2.3.2 고려사항 (3)의 값
        """

        fOtsubtc = fIeldisc + fIsubcgr
        return fOtsubtc


# 

