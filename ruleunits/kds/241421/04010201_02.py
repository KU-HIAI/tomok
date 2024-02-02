import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010201_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.1 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단보강철근이 없는 부재의 설계전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
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
    A["전단보강철근이 없는 부재의 설계전단강도"];
    B["KDS 24 14 21 4.1.2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 전단보강철근이 없는 부재의 설계전단강도/];
		VarIn1[/입력변수: 콘크리트 설계전단강도/];


		VarOut1~~~VarIn1

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C

		C(["<img src='https://latex.codecogs.com/svg.image?V_{d}=V_{cd}'>---------------------------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_shear_strength_of_members_without_shear_rebar(fOVd,fIVcd) -> float:
        """전단보강철근이 없는 부재의 설계전단강도

        Args:
             fOVd (float): 전단보강철근이 없는 부재의 설계전단강도
             fIVcd (float): 콘크리트 설계전단강도


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.1 일반 (2)의 값
        """

        fOVd = fIVcd
        return fOVd


# 

