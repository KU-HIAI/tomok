import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070105_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.1.5 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '바닥판에서의 횡방향 전단력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.1 프리캐스트 콘크리트 구조물의 일반사항
    4.7.1.5 바닥 시스템
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
    A["바닥판에서의 횡방향 전단력"];
    B["KDS 24 14 21 4.7.1.5 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:계수하중에 의한 전단 응력/];
		VarIn2[/입력변수:연결방향의 길이/];
		VarOut1[/출력변수:바닥판에서의 횡방향 전단력/];

		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def
		Variable_def--->E--->D

		D(["바닥판에서의 횡방향 전단력"])
		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;V_u=q_ub_e'>---------------------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Transverse_shear_forces_in_deck(fOVu, fIqu, fIbe) ->float:
        """바닥판에서의 횡방향 전단력
        Args:
             fOVu (float): 단순 받침부의 공칭길이
             fIqu (float): 지압응력을 고려한 순 지압판 길이
             fIbe (float): 받침점 반력

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.1.5 바닥 시스템 (5) 의 값
        """
        fOVu = fIqu * fIbe
        return fOVu


# 

