import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020307(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.7'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '형상계수'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.7 형상계수
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 형상계수];
    B["KDS 24 90 11 4.2.3.7"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 내부강판과 접촉하는 받침의 유효 면적/];
		VarIn2[/입력변수: 탄성받침의 힘이 0인 둘레길이/];
		VarIn3[/입력변수: 압축상태에서 개별 탄성중합체 층의 유효두께/];
		VarOut1[/출력변수: 형상계수/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def;
		Variable_def-->E
		E{"압축상태에서 개별 탄성중합체 층의 유효두께"}
		E--적층받침의 경우--->F
		E--3mm이상 외부층의 경우--->G
		F & G--->H--->I

		F["<img src='https://latex.codecogs.com/svg.image?t_{e}=t_{i}'>-------------------------"];
		G["<img src='https://latex.codecogs.com/svg.image?t_{e}=1.4t_{i}'>------------------------------"];
		H["<img src='https://latex.codecogs.com/svg.image?S=\frac{A_{1}}{l_{p}t_{e}}'>--------------------"];
		I(["형상계수"]);
    """

    @rule_method
    def Shape_Factor(fIA1, fIlp, fIte) -> RuleUnitResult:
        """형상계수
        Args:
            fIte (float): 압축상태에서 개별 탄성중합체 층의 유효두께
            fIA1 (float): 내부강판과 접촉하는 받침의 유효 면적
            fIlp (float): 탄성받침의 힘이 0인 둘레길이

        Returns:
             fOS (float): 형상계수률
        """

        assert isinstance(fOS, float)
        assert isinstance(fIA1, float)
        assert isinstance(fIlp, float)
        assert fIlp > 0
        assert isinstance(fIte, float)
        assert fIte > 0

        fOS = fIA1/(fIte*fIlp)

        return RuleUnitResult(
              result_variables = {
                 "fOS": fOS,
                 }
        )