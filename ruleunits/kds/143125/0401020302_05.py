import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020302_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (5)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '슬롯용접 길이에 횡방향인 최소 간격'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (5)
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
	  A([슬롯용접 길이에 횡방향인 최소 간격])
  	B["KDS 14 31 25 4.1.2.3.2(5)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarOut1[/출력변수: 슬롯용접 길이에 횡방향인 슬롯용접선의 최소간격/]
  	VarOut2[/입력변수: 길이방향의 최소 중심간격/]
  	VarIn1[/출력변수: 슬롯용접 길이방향의 최소 중심간격/]
  	VarIn2[/입력변수: 슬롯 길이/]

  	end

  	Python_Class ~~~ Variable_def --> D & E


  	D["횡뱡향인 슬롯용접선의 최소간격= 슬롯 폭x4 "]
  	E["슬롯용접선의 길이방향 최소중심간격= 슬롯길이x2"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_clearance_transverse_to_slot_weld_length(fOmsswtl,fIslowid,fOmcldsw,fIslolen) -> bool:
        """슬롯용접 길이에 횡방향인 최소 간격

        Args:
            fOmsswtl (float): 횡방향 최소간격
            fIslowid (float): 슬롯의 폭
            fOmcldsw (float): 최소 중심간격
            fIslolen (float): 슬롯 길이

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.3.2 제한사항 (5)의 값
        """
        fOmsswtl = 4*fIslowid
        fOmcldsw = 2*fIslolen
        return fOmsswtl, fOmcldsw


# 

