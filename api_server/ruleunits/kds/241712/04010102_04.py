import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04010102_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.1.1.2 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-15'
    title = '유효수평지반가속도'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.1 설계일반사항
    4.1.1 설계지반운동
    4.1.1.2 지진위험도 및 유효수평지반가속도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균압축강도];
    B["KDS 24 17 21 4.1.1.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지진구역계수/];
    VarIn2[/입력변수: 위험도계수/] ;
    VarIn3[/입력변수: 유효수평지반가속도/] ;
 	  VarOut1[/출력변수: 유효수평지반가속도/];

	  VarOut1~~~VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ C(["KDS 24 17 12 4.1.1.2(4)"])
		C --> Variable_def;

		D["유효수평지반가속도=지진구역계수X위험도계수"]
		Variable_def--->D--->J
		J(["유효수평지반가속도"])
    """

    @rule_method
    def effective_horizontal_ground_acceleration(fIZ,fII,fOS) -> RuleUnitResult:
        """유효수평지반가속도

        Args:
            fIZ (float): 지진구역계수
            fII (float): 위험도계수
            fOS (float): 유효수평지반가속도

        Returns:
            fOS (float): 교량내진 설계기준(케이블교량) 4.1.1.2 (4)의 값
        """

        assert isinstance(fIZ, float)
        assert isinstance(fII, float)

        fOS = fIZ * fII

        return RuleUnitResult(
            result_variables = {
                "fOS": fOS,
                }
            )