import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04030305(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.3.3.5'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '최대압축응력'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.3 적층고무형 지진격리받침
    4.3.3 설계 요구조건
    4.3.3.5 최대압축응력
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대압축응력];
    B["KDS 24 90 11 4.3.3.5"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/입력변수: 최대압축응력/];
		VarIn1[/입력변수: 자가격리받침면적/];
		VarIn2[/입력변수: 최대하중/];
		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.3.3.5"])
		C --> Variable_def
;
		Variable_def-->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?\sigma&space;_{max}=\frac{P_{max}}{A_e}'>--------------------------------------------------------"];
		D~~~ |"Table 24 90 11 4.3-2"| D
		E(["최대압축응력"])
    """

    @rule_method
    def Maximum_Compressive_Stress(fIAe,fIPmax) -> RuleUnitResult:
        """최대압축응력

        Args:
            fIAe (float): 자가격리받침면적
            fIPmax (float): 최대하중

        Returns:
            fOsigmamax (float): 교량 기타시설설계기준 (한계상태설계법) 4.3.3.5 최대압축응력의 값
        """

        assert isinstance(fIAe, float)
        assert fIAe > 0
        assert isinstance(fIPmax, float)

        fOsigmamax = fIPmax / fIAe

        return RuleUnitResult(
                result_variables = {
                    "fOsigmamax": fOsigmamax,
                }
            )