import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_040205_01(RuleUnit): # KDS241711_040205_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.2.5 (1)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-19'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '수평지진력'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.5 단경간교의 설계규정
    (1)
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
		A[단경간교의 설계규정] ;
		B["KDS 24 17 11 4.2.5 (1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 수평지진력/] ;
		VarIn1[/입력변수: 최대지반가속도/] ;
		VarIn2[/입력변수: 유효수평지반가속도/] ;
		VarIn3[/입력변수: 단주기 지반증폭계수/] ;
		VarIn4[/입력변수: 고정하중반력/] ;
		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
		VarOut ~~~ VarIn3
		VarOut ~~~ VarIn4
		end

		Python_Class ~~~ Variable_def

		C["최대지반가속도"] ;

		D{지반 분류} ;

		E["암반지반"] ;

		F["토사지반"] ;

		G["최대지반가속도 = <img src='https://latex.codecogs.com/svg.image?S'>"] ;

		H["최대지반가속도 = <img src='https://latex.codecogs.com/svg.image?S\times&space;F_a'>"] ;

		I["수평지진력 = 고정하중반력 x 최대지반가속도"] ;

		J(["수평지진력"]) ;

		Variable_def --> C --> D

		D --> E & F

		E --> G

		F --> H

		G & H --> I --> J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def horizontal_earthquake_load(fOhorsef,fImaxgra,fIdelore,fIS,fIFa,fIuserdefined) -> float:
        """수평지진력

        Args:
            fOhorsef (float): 수평지진력
            fImaxgra (float): 최대지반가속도
            fIdelore (float): 고정하중반력
            fIS (float): 유효수평지반가속도
            fIFa (float): 단주기 지반증폭계수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량내진설계기준(한계상태설계법) 4.2.5 단경간교의 설계규정 (1)의 값
        """

        if fIuserdefined == 1: #지반분류가 암반지반인 경우
          fImaxgra = fIS
          fOhorsef = fIdelore * fImaxgra
          return(fOhorsef)
        elif fIuserdefined == 2: #지반분류가 토사지반인 경우
          fImaxgra = fIS * fIFa
          fOhorsef = fIdelore * fImaxgra
          return(fOhorsef)