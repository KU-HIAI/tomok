import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030402_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.4.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '사질토의 근입 깊이'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.4 구조설계
    3.3.4.2 말뚝의 좌굴
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 사질토의 근입 깊이];
    B["KDS 24 14 51 3.3.4.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:근입 깊이/]
		VarIn1[/입력변수:말뚝의 탄성계수/]
		VarIn2[/입력변수:말뚝의 관성모멘트/]
		VarIn3[/입력변수:점성토의 탄성계수/]

		VarOut1
		VarIn1
		VarIn2
		VarIn3

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.4.2 (2)"])
		C --> Variable_def

		E{아래 일정한 깊이에 고정되어는 것으로 가정}
		E~~~ |"KDS 24 14 21"| E
		E~~~ |"KDS 24 14 31"| E

		F["<img src='https://latex.codecogs.com/svg.image?1.8[\frac{E_{p}I_{p}}{n_{h}}]^{0.2}'>---------------------------------"]
		D([고정점까지의 근입 깊이])
		Variable_def---> E ---> I{점성토} ---> F ---> D
    """

    @rule_method
    def Penetration_depth_of_sandy_soil(fIEp,fIlp,fInh) -> RuleUnitResult:
        """사질토의 근입 깊이

        Args:
            fIEp (float): 말뚝의 탄성계수
            fIlp (float): 말뚝의 관성모멘트
            fInh (float): 사질토의 깊이에 따른 탄성계수 증가비

        Returns:
            fOpendep (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.4.2 말뚝의 좌굴 (2)의 값
        """

        assert isinstance(fIEp, float)
        assert isinstance(fIlp, float)
        assert isinstance(fInh, float)

        fOpendep=1.8 * (fIEp * fIlp / fInh)**0.2

        return RuleUnitResult(
            result_variables = {
                "fOpendep": fOpendep,
                }
            )