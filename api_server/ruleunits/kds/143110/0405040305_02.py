import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040305_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.3.5 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '이음부 강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.5 이음부 강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 이음부 강도] ;
		B["KDS 14 31 10 4.5.4.3.5 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 이음부 강도/] ;
    VarIn1[/입력변수: 이음부의 휨모멘트/] ;
    VarIn2[/입력변수: 파형강판의 소성모멘트 강도/] ;
		end

		VarOut1 ~~~ VarIn1 & VarIn2

		Python_Class ~~~ C(["KDS 14 31 10 4.5.4.3.5 (2)"])
		C --> Variable_def

		E["이음부 설계 시"]

		R(["Max(이음부의 휨모멘트, <img src=https://latex.codecogs.com/svg.image?0.75M_{pf})>---------------------------------"])

		Variable_def --> E
 		E --> R
    """


    @rule_method
    def joint_strength(fIMpf,fIbemojo) -> RuleUnitResult:
        """이음부 강도

        Args:
            fIMpf (float): 파형강판의 소성모멘트 강도
            fIbemojo (float): 이음부의 휨모멘트

        Returns:
            fOS (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.5 이음부 강도 (2)의 값
        """

        assert isinstance(fIMpf, float)
        assert isinstance(fIbemojo, float)

        fOS = max(fIbemojo, 0.75 * fIMpf)

        return RuleUnitResult(
            result_variables = {
                "fOS": fOS,
            }
        )