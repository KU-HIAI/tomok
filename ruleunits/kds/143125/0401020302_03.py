import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020302_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '플러그용접의 최소 중심간격'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
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
	  A([플러그용접의 최소 중심간격])
	  B["KDS 14 31 25 4.1.2.3.2(3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
  	VarOut[/출력변수: 플러그용접의 최소 중심간격/]
	  VarIn[/입력변수: 공칭구멍직경/]
	  VarOut ~~~ VarIn
	  end

  	Python_Class ~~~ Variable_def --> D --> F

  	D["플러그용접의 최소 중심간격 = 공칭구멍직경x4"]
	  F([플러그용접의 최소 중심간격])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_center_spacing_for_plug_welding(fOmicspw,fInohodi) -> bool:
        """플러그용접의 최소 중심간격

        Args:
            fOmicspw (float): 플러그용접의 최소 중심간격
            fInohodi (float): 공칭구멍직경

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.3.2 제한사항 (3)의 값
        """
        fOmicspw = 4*fInohodi
        return fOmicspw


# 

