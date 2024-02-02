import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010201_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.1 (7)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '작용 전단력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
    (7)
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
    A["일반"];
    B["KDS 24 14 21 4.1.2.1 (7)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 작용전단력/];
		VarIn2[/입력변수: 설계최대전단강도/];


		VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->E

		C["<img src='https://latex.codecogs.com/svg.image?V_{u}\leq V_{dmax}'>---------------------------------"]
    E["Pass or Fail"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def acting_shear_force(fIVu,fIVdmax) -> bool:
        """작용 전단력

        Args:
             fIVu (float): 작용 전단력
             fIVdmax (float): 설계최대전단강도


        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.1 일반 (7)의 통과 여부
        """

        if fIVu <= fIVdmax:
          return "Pass"
        else:
          return "Fail"


# 

