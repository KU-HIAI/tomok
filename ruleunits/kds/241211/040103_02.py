import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241211_040103_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 12 11 4.1.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '침인상과 포스트텐션힘을 위한 하중계수'    # 건설기준명

    #
    description = """
    교량 설계하중조합(한계상태설계법)
    4. 설계
    4.1 하중의 종류와 하중조합
    4.1.3 받침인상과 포스트텐션힘을 위한 하중계수
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
    A[포스트텐션의 정착부에 대한 설계력];
    B["KDS24 12 11 4.1.3 (2)"];
    A ~~~ B
    end
	subgraph Variable_def
	VarOut1[/출력변수 : 포스트텐션의 정착부에 대한 설계력/];
	VarIn1[/입력변수 : 최대 긴장력/];

	end
	Python_Class~~~Variable_def
	D{"포스트텐션의 정착부에 대한 설계력 = 최대긴장력 x 1.2"};
	E{"포스트텐션의 정착부에 대한 설계력"};
	Variable_def --> D --> E

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_power(fOdespow,fImaxten) -> float:
        """침인상과 포스트텐션힘을 위한 하중계수

        Args:
            fOdespow (float): 설계력
            fImaxten (float): 최대 긴장력

        Returns:
            float: 교량 설계하중조합(한계상태설계법)  건설기준 4.1.3(2)의 침인상과 포스트텐션힘을 위한 하중계수
        """

        fOdespow=1.2*fImaxten
        return fOdespow


# 

# 

