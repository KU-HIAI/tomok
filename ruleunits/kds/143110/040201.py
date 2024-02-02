import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040201 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.1' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계압축강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.1 일반사항

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
		A[일반사항] ;
		B["KDS 14 31 10 4.2.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 설계압축강도/]
    VarIn1[/입력변수: 공칭압축강도/]
    VarIn2[/입력변수: 휨좌굴/]
    VarIn3[/입력변수: 비틀림좌굴/]
    VarIn4[/입력변수: 휨-비틀림좌굴/]
    VarIn5[/입력변수: 강도저항계수/]
		end


		Python_Class ~~~ Variable_def
    C["공칭압축강도=min(휨좌굴, 비틀림좌굴, 휨-비틀림좌굴)"] ;
    E["<img src='https://latex.codecogs.com/svg.image?\phi&space;_{c}=0.90'>---------------------"] ;
    F(["<img src='https://latex.codecogs.com/svg.image?\phi&space;_{c}P_{n}'>---------------"]) ;
    Variable_def-->C-->E-->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_compressive_strength(fOphicPn,fIPn,fIlsflbu,fIlstobu,fIlsftbu,fIphic) -> float:
        """설계압축강도

        Args:
            fOphicPn (float): 설계압축강도
            fIPn (float): 공칭압축강도
            fIlsflbu (float): 휨좌굴의 한계상태
            fIlstobu (float): 비틀림좌굴의 한계상태
            fIlsftbu (float): 휨-비틀림좌굴의 한계상태
            fIphic (float): 강도저항계수

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.2.1 일반사항의 값
        """

        fIPn = min(fIlsflbu, fIlstobu, fIlsftbu)
        fIphic = 0.90
        fOphicPn = fIphic*fIPn
        return fOphicPn


# 

