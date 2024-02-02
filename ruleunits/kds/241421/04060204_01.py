import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060204_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.4 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '내측 받침부의 철근량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.4 내측 받침부 하부 철근의 정착
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
    A["내측 받침부 하부 철근의 정착"];
    B["KDS 24 14 21 4.6.2.4 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:경간 내에 배치된 철근량/];
		VarIn2[/입력변수: 철근량/];
		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def--->F--->G

		F["철근량≥경간 내에 배치된 철근량X1/4"]
		G(["Pass or fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Amount_of_reinforcement_placed_within_the_span(fIamorps,fIrebamo) ->bool:
        """내측 받침부의 철근량
        Args:
             fIamorps (float): 경간 내에 배치된 철근량
             fIrebamo (float): 철근량

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 내측 받침부의 철근량이 4.6.2.4(1)의 건설기준을 만족하는지 여부
        """
        if fIrebamo>=fIamorps/4:
          return "Pass"
        else:
          return "Fail"


# 

