import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060803_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.8.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수평 철근량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.8 벽체
    4.6.8.3 수평 철근
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
    A["수평 철근"];
    B["KDS 24 14 21 4.6.8.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:수평 철근량/];
		VarIn2[/입력변수:수직철근량/];
		VarIn3[/입력변수:콘크리트 단면적/];
		VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C

		C["수평 철근량≥max(수평 철근량x25%,0.001Ac)"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def horizontal_reinforcement(fIhorent, fIverent, fIAc) ->bool:
        """수평 철근량
        Args:
             fIhorent (float): 수평 철근량
             fIverent (float): 수직철근량
             fIAc (float): 콘크리트 단면적
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.8.3 (1) 설계기준에 따른 수평 철근량 적합여부
        """
        if fIhorent >= max(fIverent/4, 0.001*fIAc):
          return "Pass"
        else:
          return "Fail"


# 

