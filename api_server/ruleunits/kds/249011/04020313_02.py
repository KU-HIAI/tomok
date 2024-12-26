import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020313_02(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.13 (2)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '이동변위에 의해 구조물에 가해지는 힘'

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
    A[Title: 이동변위에 의해 구조물에 가해지는 힘];
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
		Python_Class ~~~ C1(["KDS 24 90 11 4.2.3.13 (2)"]) -->Variable_def;
		Variable_def--->C--->D
		C["<img src='https://latex.codecogs.com/svg.image?R_{xy,d}=\frac{AG nu_{xy,d}}{T_{e}}'>--------------------------------------------------------"];


		D(["이동변위에 저항하는 힘의 합력"]);
    """

    @rule_method
    def The_Sum_Of_The_Forces_Resisting_Displacement(fIA, fIG, fITe) -> RuleUnitResult:
        """이동변위에 저항하는 힘의 합력

        Args:
            fIA (float): 받침의 총 평면적
            fIG (float): 전단탄성계수
            fITe (float): 전단에 유효한 받침 탄성중합체의 총 두께

        Returns:
           fORxyd (float): 이동변위에 저항하는 힘의 합력
        """
        assert isinstance(fORxyd, float)
        assert isinstance(fIA, float)
        assert isinstance(fIG, float)
        assert isinstance(fITe, float)
        assert fITe != 0

        fORxyd = fIA*fIG/fITe

        return RuleUnitResult(
            result_variables = {
                 "fORxyd": fORxyd,
             }
        )