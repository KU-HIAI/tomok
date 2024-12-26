import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020302_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '전단특성'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.2 압축특성과 전단특성
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성받침의 수직 압축강성];
    B["KDS 24 90 11 4.2.3.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 탄성받침의 단면적/];
		VarIn2[/입력변수: 탄성중합체층의 총두께/];
		VarIn3[/입력변수: 탄성받침의 전단 탄성계수/];
		VarOut1[/출력변수: 탄성받침의 수평 전단강성/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.2 (2)"])
		C --> Variable_def;
		Variable_def--->D-->E


		E(["탄성받침의 수평 전단강성"])
		D["<img src='https://latex.codecogs.com/svg.image?K_{h}=G\frac{A}{T_{r}}'>--------------------------------------------------------"];
    """

    @rule_method
    def Horizontal_Compressive_Stiffness_Of_Elastic_Support(fIA,fIG,fITr) -> RuleUnitResult:
        """전단특성
        Args:
            fIA (float): 탄성받침의 단면적
            fIG (float): 탄성받침의 전단탄성계수
            fITr (float): 탄성중합체층의 총두께

        Returns:
            fOKh (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.3.2 전단특성 (2)의 값
        """

        assert isinstance(fIA, float)
        assert isinstance(fIG, float)
        assert isinstance(fITr, float)
        assert fITr > 0

        fOKh = fIG * fIA / fITr
        return RuleUnitResult(
            result_variables = {
                "fOKh": fOKh,
            }
        )