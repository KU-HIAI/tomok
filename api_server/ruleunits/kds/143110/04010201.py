import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04010201(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.3.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '총단면의 항복한계상태'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.2 단면적의 산정
    4.1.2.1 총단면적
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[총단면적] ;
		B["KDS 14 31 10 4.1.2.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 부재의 총단면적/]
    VarIn1[/입력변수: 부재축의 직각방향으로 측정된 각 요소단면/]
		end

		Python_Class ~~~ Variable_def
	  C(["부재의 총단면적 = 부재축의 직각방향으로 측정된 각 요소단면의 합"]) ;

    Variable_def --> C
    """

    @rule_method
    def Total_crosssectional_area_of_member(fOAg,fIsumsec) -> RuleUnitResult:
        """부재의 총단면적

        Args:
            fOAg (float): 부재의 총단면적
            fIsumsec (float): 부재축의 직각방향으로 측정된 각 요소단면의 합

        Returns:
            fOAg (float): 강구조부재설계기준(하중저항계수설계법)  4.1.2.1 총단면적의 값
        """

        assert isinstance(fOAg, float)
        assert isinstance(fIsumsec, float)

        fOAg = fIsumsec

        return RuleUnitResult(
            result_variables = {
                "fOAg": fOAg,
            }
        )