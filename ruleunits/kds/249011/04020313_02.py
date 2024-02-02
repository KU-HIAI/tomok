import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020313_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.13 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '이동변위에 의해 구조물에 가해지는 힘'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.13 구조물에 가해지는 힘, 모멘트, 변형
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
    A[이동변위에 의해 구조물에 가해지는 힘];
    B["KDS 24 90 11 4.2.3.13 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 받침의 총 평면적/];
		VarIn2[/입력변수: 받침의 전단계수/];
		VarIn3[/입력변수: 전단에 유효한 받침 탄성중합체의 총 두께/];
		VarOut1[/출력변수: 이동변위에 저항하는 힘의 합력/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D
		C["<img src='https://latex.codecogs.com/svg.image?R_{xy,d}=\frac{A\cdot&space;G\cdot\nu&space;_{xy,d}}{T_{e}}R_{xy,d}=\frac{A\cdot&space;G\cdot\nu&space;_{xy,d}}{T_{e}}'>--------------------------------------------------------"];


		D(["이동변위에 저항하는 힘의 합력"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def The_Sum_Of_The_Forces_Resisting_Displacement(fORxyd, fIA, fIG, fITe) -> float:
        """이동변위에 의해 구조물에 가해지는 힘

        Args:
            fORxyd (float): 이동변위에 저항하는 힘의 합력
            fIA (float): 받침의 총 평면적
            fIG (float): 받침의 전단계수
            fITe (float): 전단에 유효한 받침 탄성중합체의 총 두께


        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.12 구조물에 가해지는 힘, 모멘트, 변형 (2)의 값
        """

        fORxyd = fIA*fIG/fITe
        return fORxyd


# 

