import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축부재 세장비'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.2 유효좌굴길이와 세장비 제한
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
		A[유효좌굴길이와 세장비제한] ;
		B["KDS 14 31 10 4.2.2(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 주부재의 세장비/]
    VarIn2[/입력변수: 횡좌굴에 대한 비지지길이/]
    VarIn3[/입력변수: 단면2차반경/]
    VarIn4[/입력변수: 유효좌굴길이계수/]
		end

		Python_Class ~~~ Variable_def
	  C["주부재"] ;
    D(["KL/r ≤ 120"]) ;
    E["가새"] ;
    F(["KL/r ≤ 140"])  ;
	  Variable_def-->C-->D-->G([PASS or Fail]);
	  Variable_def-->E-->F-->H([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def slenderness_ratio_of_compression_member(fIL,fIr,fIK,fIuserdefined) -> bool:
        """압축부재 세장비

        Args:
            fIL (float): 횡좌굴에 대한 비지지길이
            fIr (float): 단면2차반경
            fIK (float): 유효좌굴길이계수
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.2.2 유효좌굴길이와 세장비 제한 (2)의 통과여부
        """

        #주부재 : fIuserdefined == 1
        #가새 : fIuserdefined == 2

        if fIuserdefined == 1:
          if fIL*fIK/fIr <= 120:
            return 'Pass'
          else:
            return 'Fail'

        if fIuserdefined == 2:
          if fIL*fIK/fIr <= 140:
            return 'Pass'
          else:
            return 'Fail'


# 

