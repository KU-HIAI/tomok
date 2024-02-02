import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_04_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 4.5' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단철근에 의한 공칭전단강도'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(5)
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
    A["전단철근에 의한 공칭전단강도"];
    B["KDS 24 17 10 부록.4.(3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:축력 작용에 의한 공칭전단강도/];
		VarIn2[/입력변수:콘크리트에 의한 공칭전단강도/];
		VarIn3[/입력변수:전단철근에 의한 공칭전단강도/];


		VarOut1[/출력변수:단부구역을 제외한 구역의 공칭전단강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end

		Python_Class ~~~ Variable_def
		Variable_def--->E--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;V_n=V_c&plus;V_s&plus;V_p'>---------------------------------"]

		F(["단부구역을 제외한 구역의 공칭전단강도"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_shear_strength_by_shear_reinforcement(fOvs,fIav,fIasp,fIct,fIdc,fIfyh,fIlct,fIs,fIuserdefined) -> float:
        """전단철근에 의한 공칭전단강도

        Args:
            fOvs (float): 전단철근에 의한 공칭전단강도
            fIav (float): 전단철근으로 작용하는 띠철근의 단면적
            fIasp (float): 나선철근 또는 원형 후프띠철근의 단면적
            fIct (float): 원형단면에 배근되는 보강띠철근의 단면적
            fIdc (float): 고려하는 방향의 심부콘크리트 단면 치수
            fIfyh (float): 띠철근 또는 나선철근의 항복강도
            fIlct (float): 원형단면에 배근되는 보강띠철근에서 갈고리 부분과 연장길이를 제외한 길이
            fIs (float): 띠철근 또는 나선철근의 수직간격
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (5)의 값
        """

        # 사각형 띠철근단면
        fIav * fIfyh * fIdc / fIs

        # 원형단면의 나선철근 또는 원형 후프띠철근
        (math.pi / 2) * (fIasp * fIfyh * fIdc)

        # 원형 후프띠철근에 보강띠철근이 추가된 경우
        fIct * fIfyh * fIlct / fIs


        # fIuserdefined == 1 : 사각형 띠철근단면
        # fIuserdefined == 2 : 원형단면의 나선철근 또는 원형 후프띠철근
        # fIuserdefined == 3 : 원형 후프띠철근에 보강띠철근이 추가된 경우


        if fIuserdefined == 1:
          fOvs = fIav * fIfyh * fIdc / fIs
          return fOvs
        elif fIuserdefined == 2:
          fOvs = (math.pi / 2) * (fIasp * fIfyh * fIdc)
          return fOvs
        elif fIuserdefined == 3:
          fOvs = fIct * fIfyh * fIlct / fIs
          return fOvs





# 

