import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_030203_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.2.3 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근의 평균 탄성계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.2 철근
    3.2.3 설계 가정
    (4)
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
    A["평균밀도"];
    B["KDS 24 14 21 3.3.3 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 평균밀도/];
		VarOut1

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D

		C["평균밀도=7850kg/m³"]

		D(["평균밀도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Average_modulus_of_elasticity_of_reinforcing_bars(fOEs) -> float:
        """철근의 평균 탄성계수

        Args:
             fOEs (float): 철근의 평균 탄성계수




        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.2.3 설계 가정 (4)의 값
        """

        fOEs = 200
        return fOEs


# 

