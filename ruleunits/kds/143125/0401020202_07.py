import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020202_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (7)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '겹침이음의 최소 겹침길이'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (7)
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
  	A([최소 겹침길이])
  	B["KDS 14 31 25 4.1.2.2.2(7)"]
  	A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 최소 겹침길이/]
	  VarIn[/입력변수: 연결부의 얇은 쪽 판두께/]
	  VarOut ~~~ VarIn
	  end

	  Python_Class ~~~ Variable_def --> D --> E

	  D["최소 겹침길이= 연결부의 얇은 쪽 판 두께x5 or 25mm"]
  	E([최소 겹침길이])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_overlapped_length_of_overlap_joint(fOmiovle,fIthtspj) -> bool:
        """겹침이음의 최소 겹침길이

        Args:
            fOmiovle (float): 최소 겹침길이
            fIthtspj (float): 연결부의 앏은 쪽 판 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.2.2 제한사항 (7)의 값
        """
        if 5*fIthtspj <= 25 :
          fOmiovle = 25
          return fOmiovle

        else:
          if 5*fIthtspj > 25 :
            fOmiovle = 5*fIthtspj
            return fOmiovle


# 

