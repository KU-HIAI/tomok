import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020402_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.4.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '플랜지 폭'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.2 직접 처짐 계산을 생략하는 경우
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
    A["직접 처짐 계산을 생략하는 경우"];
    B["KDS 24 14 21 4.2.4.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 플랜지 폭/];
		VarIn2[/입력변수: 복부폭/];
		VarIn3[/입력변수: 지간/];
		VarIn4[/입력변수: 단면의 유효깊이/];

		VarIn1 & VarIn2  & VarIn3  & VarIn4

		end
		Python_Class ~~~ Variable_def--->C--->E


		C["플랜지폭>복부폭 x3"]
		E["0.8 x l/d"]

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def flange_width(fIflawid,fIabdwid,fIl,fId) -> float:
        """플랜지 폭

        Args:
             fIflawid (float): 플랜지 폭
             fIabdwid (float): 복부폭
             fIl (float): 지간
             fId (float): 단면의 유효깊이

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.4.2 직접 처짐 계산을 생략하는 경우 (3)의 값
        """

        if fIflawid > 3*fIabdwid:
          return 0.8*fIl/fId


# 

