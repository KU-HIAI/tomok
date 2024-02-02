import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0401050102 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.5.1.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단파단에 대한 공칭인장강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.1.2 유효단면적에 대한 전단파단
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
		A[유효단면적에 대한 전단파단] ;
		B["KDS 14 31 10 4.1.5.1.2"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 전단파단에 대한 공칭인장강도/]
    VarIn1[/입력변수: 인장강도/]
    VarIn2[/입력변수: 유효단면적/]
    VarIn3[/입력변수: 관구멍의 연단으로부터 힘의 방향과 평행하게 측정한 부재의 연단까지 최단거리/]
    VarIn4[/입력변수: 핀직경/]
    VarIn5[/입력변수: 판재의 두께/]
		end

		Python_Class ~~~ Variable_def
	  C(["<img src='https://latex.codecogs.com/svg.image?P_{n}=0.6F_{u}A_{sf}'>-------------------------------------"]) ;
	  D["<img src='https://latex.codecogs.com/svg.image?A_{sf}=2t(a&plus;d/2)(mm^{2})'>------------------------------------------------------"] ;
	  Variable_def-->D-->C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_tensile_strength_against_shear_fracture(fOPn,fIFu,fIAsf,fIa,fId,fIt) -> float:
        """전단파단에 대한 공칭인장강도

        Args:
            fOPn (float): 전단파단에 대한 공칭인장강도
            fIFu (float): 인장강도
            fIAsf (float): 유효단면적
            fIa (float): 핀구멍의 연단으로부터 힘의 방향과 평행하게 측정한 부재의 연단까지 최단거리
            fId (float): 핀직경
            fIt (float): 판재의 두께

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.1.5.1.2 유효단면적에 대한 전단파단의 값
        """

        fIAsf = 2 * fIt * (fIa + fId/2)
        fOPn = 0.6 * fIFu * fIAsf
        return fOPn


# 

