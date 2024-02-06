import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060208_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.8 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '표피철근량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.8 표피철근
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
    A["표피철근"];
    B["KDS 24 14 21 4.6.2.8 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 인장 철근과 평행한 방향의 표피철근량/];
		VarIn2[/입력변수: 인장 철근과 수직한 방향의 표피철근량/];
		VarIn3[/입력변수: 횡방향철근 외측의 인장콘크리트 면적/];

		VarIn1
    ~~~VarIn2
    ~~~VarIn3
		end

		Python_Class ~~~ Variable_def--->F--->G--->H

		F{"평행한 방향과 수직한 방향의 양방향에 대해서"}


		G["<img src='https://latex.codecogs.com/svg.image?A_{s,surf}\geq&space;0.01A_{ct,ext}'>---------------------------------"]



		H(["Pass or fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def amount_of_skin_reinforcement(fIAssurfpar,fIAssurfper,fIActext) -> bool:
        """표피철근량
        Args:
             fIAssurfpar (float): 인장 철근과 평행한 방향의 표피철근량
             fIAssurfper (float): 인장 철근과 수직한 방향의 표피철근량
             fIActext (float): 횡방향철근 외측의 인장콘크리트 면적

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.8 표피철근 (3)의 통과 여부
        """

        if fIAssurfpar >= 0.01*fIActext and fIAssurfper >= 0.01*fIActext:
          return "Pass"
        else:
          return "Fail"


# 
