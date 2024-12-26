import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030501_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.5.1 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '열차횡하중'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.5 열차횡하중 LF
    4.3.5.1 KRL-2012 표준열차하중의 열차횡하중
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: KRL-2012 표준열차하중의 열차횡하중];
    B["KDS 24 12 21 4.3.5.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
	  VarOut1[/출력변수 : 열차횡하중/];

	  end

  	Python_Class ~~~ C(["KDS 24 12 21 4.3.5.1 (2)"])
		C --> Variable_def

	  D["충격계수 및 원심력 감소계수 고려하지 않는다"];
	  E{"복선 이상의 선로를 지지하는 구조물인 경우"};
	  F["열차횡하중 = 100kN (1궤도에만 적용)"];
	  G["열차횡하중 = 100kN"];
	  Variable_def --> D --> E
	  E --Yes--> F -->H([열차횡하중]);
	  E --No--> G -->H([열차횡하중]);
    """

    @rule_method
    def lateral_train_load(fOQ) -> RuleUnitResult:
        """열차횡하중

        Args:
            fOQ (float): 열차횡하중

        Returns:
            fOQ (float): 강교 설계기준(한계상태설계법)  4.3.5.1 KRL-2012 표준열차하중의 열차횡하중 (2)의 값
        """

        fOQ = 100

        return RuleUnitResult(
            result_variables = {
                "fOQ": fOQ,
            }
        )