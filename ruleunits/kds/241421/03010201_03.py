import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010201_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.1 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트의 각 재령에서 평균압축강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
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
    A[평균압축강도];
    B["KDS 24 14 21 3.1.2.1 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 재령 28일에서 콘크리트 평균압축강도/];
    VarIn2[/입력변수: 평균압축강도/] ;
    VarIn3[/입력변수: 강도 보정 계수/] ;
    VarIn4[/입력변수: 콘크리트의 재령/] ;
    VarIn5[/입력변수: 시멘트 종류와 양생방법에 따른 상수/] ;
 	  VarOut1[/출력변수: 재령 t일에서 콘크리트 평균압축강도/];


	  VarOut1~~~VarIn1 & VarIn2 &  VarIn3 &  VarIn4 &  VarIn5
		end
		Python_Class ~~~ Variable_def;
		Variable_def---->D



		D{"<img src='https://latex.codecogs.com/svg.image?&space; \beta_{sc}'>--------------------------------------------------------"}
		D--1종 시멘트 습윤 양생--->E
		D--1종 시멘트 증기 양생--->F
    D--3종 시멘트 습윤 양생--->G
		D--3종 시멘트 증기 양생--->H
		D--2종 시멘트--->I
		E["시멘트 종류와 양생방법에 따른 상수=0.35"]
		F["시멘트 종류와 양생방법에 따른 상수=0.15"]
    G["시멘트 종류와 양생방법에 따른 상수=0.25"]
    H["시멘트 종류와 양생방법에 따른 상수=0.12"]
    I["시멘트 종류와 양생방법에 따른 상수=0.40"]
		J["<img src='https://latex.codecogs.com/svg.image?&space;\beta_{cc}=exp\left\{\beta_{sc}[1-(\frac{28}{t})^{1/2}]\right\}'>--------------------------------------------------------"]
    E & F & G & H & I---->J
    K["<img src='https://latex.codecogs.com/svg.image?f_{cm}(t)=\beta&space;_{cc}(t)f_{cm}'>--------------------------------------------------------"]
    J---->K--->L
    L(["재령 t일에서 콘크리트 평균압축강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Average_compressive_strength(fOfcmt,fIbetacc,fIfcm,fIt,fIbetasc) -> float:
        """콘크리트의 각 재령에서 평균압축강도

        Args:
             fOfcmt (float): 재령 t일에서 콘크리트 평균압축강도
             fIbetacc (float): 강도 보정 계수
             fIfcm (float): 재령 28일에서 콘크리트 평균압축강도
             fIt (float): 콘크리트의 재령
             fIbetasc (float): 시멘트 종류와 양생방법에 따른 상수


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.1 강도 (3)의 값
        """

        import numpy as np
        fIbetacc = np.exp(fIbetasc * (1 - (28/fIt)**0.5))
        fOfcmt = fIbetacc * fIfcm
        return fOfcmt


# 

