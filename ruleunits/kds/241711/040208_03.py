import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_040208_03(RuleUnit): # KDS241711_040208_03

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.2.8 (3)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-22'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '최소받침지지길이'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.8 설계변위
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
	A([설계변위])
	B["KDS 24 17 11 4.2.8(3)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 최소받침지지길이/]
	VarIn1[/입력변수: 인접 신축이음부까지 또는 교량단부까지의 거리/]
	VarIn2[/입력변수: 평균높이/]
	VarIn3[/입력변수: 받침선과 교축직각방향의 사잇각/]

	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	end
	Python_Class ~~~ Variable_def --> D --> E
	D["<img src='https://latex.codecogs.com/svg.image?&space;N\geq(200&plus;1.67L&plus;6.66H)(1&plus;0.000125\theta^2)(mm)'>--------------------------------------------------------------------"]
	E([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def minimum_support_length(fON,fIL,fIH,fIvarphi) -> bool:
        """최소받침지지길이

        Args:
            fON (float): 최소받침지지길이
            fIL (float): 인접 신축이음부까지 또는 교량단부까지의 거리
            fIH (float): 평균높이
            fIvarphi (float): 받침선과 교축직각방향의 사잇각

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.2.8 설계변위 (3)의 통과 여부
        """
        if fON >= (200 + 1.67 * fIL + 6.66 * fIH) * (1 + 0.000125 * fIvarphi ** 2):
          return 'Pass'
        else:
          return 'Fail'