import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010102_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.1.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '극한한계변형률'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
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
    A["휨 및 축력이 작용하는 부재의 극한한계상태 검증"];
    B["KDS 24 14 21 4.1.1.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 극한한계변형률/];
		VarIn2[/입력변수: 콘크리트 정점변형률/];

		VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D


		C["극한한계변형률≤ 콘크리트 정점변형률"]
		D(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Ultimate_limit_strain(fIultlis,fIepsilonco) -> bool:
        """극한한계변형률

        Args:
             fIultlis (float): 극한한계변형률
             fIepsilonco (float): 콘크리트 정점변형률


        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (3)의 통과 여부
        """

        if fIultlis <= fIepsilonco:
          return "Pass"
        else:
          return "Fail"


# 

