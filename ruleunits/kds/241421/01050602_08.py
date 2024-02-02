import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050602_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.6.2 (8)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '모멘트 확대계수를 계산할 때의 탄성계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.6 장주 효과
    1.5.6.2 모멘트 확대계수법의 적용
    (8)
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
    A[모멘트 확대계수를 계산할 때의 탄성계수];
    B["KDS 24 14 21 1.5.6.2 (8)"];
    A ~~~ B
    end
	subgraph Variable_def
	VarOut1[/출력변수 : 휨강성/];
	VarIn1[/입력변수 : 콘크리트의 탄성계수/];
	VarIn2[/입력변수 : 도심축에 대한 콘크리트 총단면의 단면2차모멘트/];
	VarIn3[/입력변수 : 종방향 철근의 탄성계수/];
	VarIn4[/입력변수 : 도심축에 대한 종방향 철근의 단면2차모멘트/];
	VarIn5[/입력변수 : 횡구속 골조에서 최대 계수축력에 대한 최대계수지속축력의 비/];

	VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
	VarIn2 ~~~ VarIn4 & VarIn5

	end
	Python_Class~~~Variable_def
	D["<img src='https://latex.codecogs.com/png.image?max\left ( EI=\frac{\left ( 0.2E_{c}I{g} + E_{s}I{s} \right ))}{1+\ beta _{d}}, EI=\frac{0.4E_{c}I{g}}{1+\beta _{d}} \right )'>-------------------"];
	Variable_def --> D --> E["휨강성"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Elasticity_modulus_when_calculating_moment_magnification_coefficient(fOEI,fIEc,fIIg,fIEs,fIls,fIbetad) -> bool:
        """모멘트 확대계수를 계산할 때의 탄성계수

        Args:
            fOEI (float) : 휨강성
            fIEc (float) : 콘크리트의 탄성계수
            fIIg (float) : 도심축에 대한 콘크리트 총단면의 단면2차모멘트
            fIEs (float) : 종방향 철근의 탄성계수
            fIls (float) : 도심축에 대한 종방향 철근의 단면2차모멘트
            fIbetad (float) : 횡구속 골조에서 최대 계수축력에 대한 최대계수지속축력의 비

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 1.5.6.2 모멘트 확대계수법의 적용 (8)의 통과여부
        """

        fOEI = max((0.2*fIEc*fIIg + fIEs*fIls)/(1+fIbetad), 0.4*fIEc*fIIg/(1+fIbetad))

        return fOEI


# 

