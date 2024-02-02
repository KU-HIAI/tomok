import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010205_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.5 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '시공이음 계면의 전단'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.5 서로 다른 시기에 타설한 콘크리트의 계면 전단
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
    A["서로 다른 시기에 타설한 콘크리트의 계면 전단"];
    B["KDS 24 14 21 4.1.2.5 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 계수하중에 의한 계면에서 전단응력/];
		VarIn2[/입력변수: 계면의 설계전단강도/];

		VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D
		C["<img src='https://latex.codecogs.com/svg.image?v_{u}&space;\leq&space;v_{d}'>---------------------------------"]
		D(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shear_stress_at_the_interface_due_to_modulus_load(fIVu,fIVd) -> bool:
        """시공이음 계면의 전단

        Args:
             fIVu (float): 계수하중에 의한 계면에서 전단응력
             fIVd (float): 계면의 설계전단강도



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.5 서로 다른 시기에 타설한 콘크리트의 계면 전단 (1)의 통과 여부
        """

        if fIVu <= fIVd:
          return "Pass"
        else:
          return "Fail"


# 

