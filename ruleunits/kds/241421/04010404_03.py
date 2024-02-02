import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010404_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.4.4 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단철근이 필요하지 않은 위험단면 둘레길이'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도
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
    A["둘레길이"];
    B["KDS 24 14 21 4.1.4.4 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 전단력/];
		VarIn2[/입력변수: 콘크리트가 기여하는 설계전단강도/];
		VarIn3[/입력변수: 유효깊이/];

		VarOut1[/출력변수: 둘레길이/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->E
		C["<img src='https://latex.codecogs.com/svg.image?u_{out,ef}=\frac{V_u}{v&space;_{cd}d}'>---------------------------------"]
		E(["둘레 길이"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def perimeter_of_critical_section(fOuout,fIVu,fIVcd,fId) -> float:
        """전단철근이 필요하지 않은 위험단면 둘레길이

        Args:
             fOuout (float): 전단철근이 필요하지 않은 위험단면 둘레길이
             fIVu (float): 전단력
             fIVcd (float): 콘크리트가 기여하는 설계전단강도
             fId (float): 유효깊이




        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도 (3)의 값
        """

        fOuout = fIVu / fIVcd / fId * 1000
        return fOuout


# 

