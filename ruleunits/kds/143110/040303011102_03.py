import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011102_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.11.2 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지압보강재의 설계지압강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.2 하중집중점 지압보강재
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
		A[Title: 하중집중점 지압보강재] ;
		B["KDS 14 31 10 4.3.3.1.11.2 (3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut1[/출력변수: 설계지압강도/] ;
    VarIn1[/입력변수: 지압에 대한 강도 저항계수/] ;
    VarIn2[/입력변수: 지압보강재의 공칭지압강도/] ;
    VarIn3[/입력변수: 웨브 용접면으로부터 돌출된 지압 보강재의 단면적/] ;
    VarIn4[/입력변수: 지압보강재의 최소항복강도/] ;
		VarOut1 ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def

		C["<img src=https://latex.codecogs.com/svg.image?(R_{sb})_{n}=1.4A_{pn}F_{ys}>------------------------------"]
		D["<img src=https://latex.codecogs.com/svg.image?(R_{sb})_{r}=\phi&space;_{b}(R_{sb})_{n}>----------------------------"]
		Variable_def --> C --> D --> F(["<img src=https://latex.codecogs.com/svg.image?(R_{sb})_{r}>-----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_acupressure_strength(fORsbr,fIphib,fIRsbn,fIApn,fIFys) -> bool:
        """지압보강재의 설계지압강도
        Args:
            fORsbr (float): 설계지압강도
            fIphib (float): 지압에 대한 강도저항계수
            fIRsbn (float): 지압보강재의 공칭지압강도
            fIApn (float): 웨브 용접면으로부터 돌출된 지압보강재의 단면적
            fIFys (float): 지압보강재의 최소항복강도

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.2 하중집중점 지압보강재 (3)의 통과여부
        """


        fIRsbn = 1.4 * fIApn * fIFys
        fORsbr = fIphib * fIRsbn
        return fORsbr


# 

