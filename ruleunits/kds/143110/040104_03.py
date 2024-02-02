import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040104_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.4 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-23'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '띠판의 재축방향 길이'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.4 조립 인장부재
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
		A[조립 인장부재] ;
		B["KDS 14 31 10 4.1.4(3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 띠판의 재축방향 길이/]
    VarIn2[/입력변수: 용접/]
    VarIn3[/입력변수: 연결재 사이거리/]
    VarIn4[/입력변수: 띠판 두께/]
    VarIn5[/입력변수: 열 사이거리/]
    VarIn6[/입력변수: 단순용접/]
    VarIn7[/입력변수: 연결재의 재축방향 간격/]
    VarIn8[/입력변수: 조립부재 개별부재의 세장비/]
    VarIn1 ~~~ VarIn5
    VarIn2  ~~~ VarIn6
    VarIn3 & VarIn4 ~~~ VarIn7 & VarIn8
		end

		Python_Class ~~~ Variable_def
  	C["띠판의 재축방향 길이"]
  	D(["띠판의 재축방향 길이 ≥ 용접 or 연결재사이거리의 2/3"])
    E["띠판 두께"]
    F(["띠판 두께 ≥ 열 사이거리의 1/50"])
    G["단순용접 or 연결재의 재축방향 간격"]
    H(["단순용접 or 연결재의 재축방향 간격 ≤ 150mm"])
    I["조립부재 개별부재의 세장비"]
    J(["가급적 세장비 ≤ 300"])
    Variable_def --> C-->D
    Variable_def --> E-->F
    Variable_def --> G-->H
    Variable_def --> I-->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_length_of_the_strip_in_the_axial_direction(fIlestad,fIweldin,fIdibeco,fIbanthi,fIdibero,fIinwedw,fIspaxdc,fIamsrim) -> bool:
        """띠판의 재축방향 길이

        Args:
            fIlestad (float): 띠판의 재축방향 길이
            fIweldin (float): 용접
            fIdibeco (float): 연결재 사이거리
            fIbanthi (float): 띠판 두께
            fIdibero (float): 열 사이거리
            fIinwedw (float): 단속용접
            fIspaxdc (float): 연결재의 재축방향 간격
            fIamsrim (float): 조립부재 개별부재의 세장비

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.1.4 조립 인장부재 (3)의 통과여부
        """

        if fIlestad >= 2/3*max(fIweldin,fIdibeco) and fIbanthi >= fIdibero/50 and (fIinwedw<=150 or fIspaxdc<=150) and fIamsrim <=300:
          return 'Pass'
        else:
          return 'Fail'


# 

