import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04030502_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.3.5.2 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '연행집중이동하중'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.5 열차횡하중 LF
    4.3.5.2 EL 표준열차하중의 열차횡하중
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
    A[EL 표준열차하중의 열차횡하중];
    B["KDS 24 12 21 4.3.5.2 (1)"];
    A ~~~ B
    end
	subgraph Variable_def
	VarOut1[/출력변수 : 열차횡하중/];
	VarIn1[/입력변수 : EL 표준열차하중/];

	end
	Python_Class~~~Variable_def
	D["Q=EL 표준열차하중 x 0.2"];
	Variable_def --> D --> E([열차횡하중]);
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def performance_concentrated_moving_load(fOQ,fILsttr) -> bool:
        """연행집중이동하중

        Args:
            fOQ (float): 열차횡하중
            fILsttr (float): 표준열차하중

        Returns:
            float: 강교 설계기준(한계상태설계법)  4.3.5.2 EL 표준열차하중의 열차횡하중 (1)의 값
        """

        fOQ = 0.2*fILsttr
        return fOQ


# 

