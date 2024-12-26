import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04020701_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.2.7.1 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '연결부분의 설계지진력'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.7 설계지진력
    4.2.7.1 구조부재 및 연결부의 설계지진력
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 구조부재 및 연결부의 설계지진력];
		B["KDS 24 17 11 4.2.7.1 (4)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 설계지진력/];
		VarIn1[/입력변수: 교각의 최대소성힌지력/];
		VarIn2[/입력변수: 응답수정계수를 적용하지 않은 탄성지진력/];
		VarOut ~~~ VarIn1 & VarIn2
		end

		Python_Class ~~~ E(["KDS 24 17 11 4.2.7.1 (4)"])
		E --> Variable_def

		E["연결부분의 설계지진력 = \n min (교각의 최대소성힌지력, 응답수정계수를 설정하지 않은 탄성지진력)"];

		D([연결부분의 설계지진력]);

		Variable_def --> E --> D
    """

    @rule_method
    def design_earthquake_load(fImaphfp,fIebcwoR) -> RuleUnitResult:
        """연결부분의 설계지진력

        Args:
            fImaphfp (float): 교각의 최대소성 힌지력
            fIebcwoR (float): 응답수정계수를 적용하지 않은 탄성지지력

        Returns:
            fOdesefo (float): 교량내진설계기준(한계상태설계법) 4.2.7.1 구조부재 및 연결부의 설계지진력 (4)의 값
        """

        assert isinstance(fImaphfp, float)
        assert isinstance(fIebcwoR, float)

        fOdesefo = min(fImaphfp, fIebcwoR)
        return RuleUnitResult(
            result_variables = {
                "fOdesefo": fOdesefo,
                }
            )