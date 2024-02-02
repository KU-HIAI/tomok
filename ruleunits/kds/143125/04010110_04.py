import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010110_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.1.10 (4)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-08'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '고장력볼트의 구멍중심간 거리'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
    (4)
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
	  A([이음부 설계세칙])
  	B["KDS 14 31 25 4.1.1.10(4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut1[/출력변수: 최소거리/]
	  VarOut2[/출력변수: 표준거리/]
	  VarIn[/입력변수: 공칭직경/]
	  end

	  Python_Class ~~~ Variable_def --> D --최소거리--> E
	  D--표준거리-->F
	  E --> G
	  F --> H
  	D["고장력볼트의 구멍중심간의 거리"]
	  E["공칭직경 X 2.5"]
	  F["공칭직경 X 3"]
    G([최소거리])
	  H([표준거리])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Distance_between_hole_center_of_high_strength_bolt(fInomdim,fOmindis,fOstadis) -> bool:
        """고장력볼트의 구멍중심간 거리

        Args:
            fInomdim (float): 공칭직경
            fOmindis (float): 최소거리
            fOstadis (float): 표준거리

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.1.10 이음부 설계세칙 (4)의 값
        """

        fOmindis = fInomdim*2.5
        fOstadis = fInomdim*3
        return fOmindis, fOstadis


# 

