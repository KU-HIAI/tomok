import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04030501_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.3.5.1 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '열차횡하중'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.5 열차횡하중 LF
    4.3.5.1 KRL-2012 표준열차하중의 열차횡하중
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
    A[KRL-2012 표준열차하중의 열차횡하중];
    B["KDS 24 12 21 4.3.5.1 (2)"];
    A ~~~ B
    end
	subgraph Variable_def
	VarOut1[/출력변수 : 열차횡하중/];

	end
	Python_Class~~~Variable_def
	D["충격계수 및 원심력 감소계수 고려하지 않는다"];
	E{"복선 이상의 선로를 지지하는 구조물인 경우"};
	F["열차횡하중 = 100kN (1궤도에만 적용)"];
	G["열차횡하중 = 100kN"];
	Variable_def --> D --> E
	E --Yes--> F -->H([열차횡하중]);
	E --No--> G -->H([열차횡하중]);
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def lateral_train_load(fOQ) -> bool:
        """열차횡하중

        Args:
            fOQ (float): 열차횡하중

        Returns:
            float: 강교 설계기준(한계상태설계법)  4.3.5.1 KRL-2012 표준열차하중의 열차횡하중 (2)의 값
        """

        fOQ = 100
        return fOQ


# 

