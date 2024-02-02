import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020403_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.4.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '부재 전 경간에 걸친 평균 유효 변형량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.3 직접 처짐 계산에 의한 검증
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
    A["부재 전 경간에 걸친 평균 유효 변형량"];
    B["KDS 24 14 21 4.2.4.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 비균열 상태일 때의 변형량/];
		VarIn2[/입력변수: 완전균열상태일 때의 변형량/];
		VarIn3[/입력변수: 분포 계수/];
		VarIn4[/입력변수: 균열 단면을 기준으로 계산한 인장 철근 응력/];
		VarIn5[/입력변수: 첫 균열이 발생한 직후에 균열 면에서 계산한 철근 인장응력/];
		VarIn6[/입력변수: 평균 변형률에 미치는 하중의 반복 지속 기간을 반영하는 계수/];
		VarOut1[/출력변수: 부재 전 경간에 걸친 평균 유효 변형량/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5  & VarIn6
		end
		Python_Class ~~~ Variable_def--->D
		D{"평균 변형률에 미치는 하중의 반복 지속 기간을 반영하는 계수 β"}
		D--단기하중--->G
		D--반복하중--->H
		G["β=1.0"]
		H["β=0.5"]
		G & H--->C--->E--->F
		C["<img src='https://latex.codecogs.com/svg.image?\zeta=1-\beta(\frac{f_{sr}}{f_{so}})^2'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\Delta&space;e=\zeta\Delta&space;_{crack}&plus;(1-\zeta)\Delta&space;_{uncrack}'>---------------------------------"]

		F(["부재 전 경간에 걸친 평균 유효 변형량"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Average_effective_deformation_over_the_entire_span_of_the_member(fOdeltae,fIdeltauncrack,fIdeltacrack,fIfso,fIfsr,fIbeta,fIzeta) -> float:
        """부재 전 경간에 걸친 평균 유효 변형량

        Args:
             fOdeltae (float): 부재 전 경간에 걸친 평균 유효 변형량
             fIdeltauncrack (float): 비균열 상태일 때의 변형량
             fIdeltacrack (float): 완전균열상태일 때의 변형량
             fIfso (float): 균열단면을 기준으로 계산한 인장 철근응력
             fIfsr (float): 첫 균열 발생 직후에 균열면에서 계산한 철근 인장응력
             fIbeta (float): 평균 변형률에 미치는 하중의 반복 지속 기간을 반영하는 계수
             fIzeta (float): 분포 계수

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (2)의 값
        """

        fIzeta = 1-fIbeta*(fIfsr/fIfso)**2
        fOdeltae = fIzeta*fIdeltacrack + (1-fIzeta)*fIdeltauncrack
        return fOdeltae


# 

