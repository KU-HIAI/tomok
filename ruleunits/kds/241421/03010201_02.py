import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010201_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.1 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '통계자료가 없을 경우 평균압축강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
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
    A[평균압축강도];
    B["KDS 24 14 21 3.1.2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 평균압축강도와 기준압축강도의 차이/];
    VarIn2[/입력변수: 기준압축강도/] ;
 	  VarOut1[/출력변수: 평균압축강도/];


	  VarOut1~~~VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def;
		Variable_def---->D



		D{"<img src='https://latex.codecogs.com/svg.image?&space; f_{ck}'>--------------------------------------------------------"}
		D--40MPa이하--->E
		D--60MPa이상--->H
    D--그 이외--->G
		E["<img src='https://latex.codecogs.com/svg.image?&space;\Delta f=4MPa'>--------------------------------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?&space;\Delta f=6MPa'>--------------------------------------------------------"]
		G["직선보간"]
		I["<img src='https://latex.codecogs.com/svg.image?&space;f_{cm}=\Delta f+f_{ck}'>--------------------------------------------------------"]
		E & H & G--->I--->J
		J(["평균압축강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Average_compressive_strength(fOcm,fIdeltaf,fIfck) -> float:
        """통계자료가 없을 경우 평균압축강도

        Args:
             fOcm (float): 평균압축강도
             fIdeltaf (float): 평균압축강도와 기준압축강도의 차이
             fIfck (float): 기준압축강도


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.1 강도 (2)의 값
        """

        if fIfck <= 40:
          fIdeltaf = 4
        elif fIfck >= 60:
          fIdeltaf = 6
        else:
          fIdeltaf = fIfck / 10
        fOcm = fIfck + fIdeltaf
        return fOcm


# 

