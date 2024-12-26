import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010502_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.5.2 (2)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '말뚝간격'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.5 말뚝기초 설계
    4.1.5.2 말뚝간격과 말뚝배열
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝간격];
    B["KDS 11 50 15 4.1.5.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;

		VarIn1[/입력변수: 말뚝중심 간격/]
		VarIn2[/입력변수: 기초측면과 말뚝중심 간의 거리/]
    VarIn3[/입력변수: 최소 말뚝지름/] ;

		VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.1.5.2 (2)"])
		C --> Variable_def;

		F{"말뚝중심 간격 ≥ 최소한 말뚝지름x2.5"}
		D{"기초측면과 말뚝중심 간의 거리 ≥ 최소 말뚝지름x1.25"}
		Variable_def --> F
		Variable_def --> D
    F & D --> E([PASS or Fail]);
    """

    @rule_method
    def pile_spacing(fIminpdi) -> RuleUnitResult:
        """말뚝간격

        Args:
            fIminpdi (float): 최소 말뚝지름

        Returns:
            fOpcensp (float): 깊은기초 설계기준(일반설계법)  4.1.5.2 말뚝간격과 말뚝배열 (2)의 값 1
            fOdipspc (float): 깊은기초 설계기준(일반설계법)  4.1.5.2 말뚝간격과 말뚝배열 (2)의 값 2
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.5.2 말뚝간격과 말뚝배열 (2)의 판단 결과
        """

        assert isinstance(fIminpdi, float)

        if fOpcensp >= fIminpdi * 2.5 and fOdipspc >= fIminpdi * 1.25 :
          return RuleUnitResult(
                result_variables = {
                    "fOpcensp": fOpcensp,
                    "fOdipspc": fOdipspc,
                    "pass_fail": True,
                }
            )
        else:
            return RuleUnitResult(
                result_variables = {
                    "fOpcensp": fOpcensp,
                    "fOdipspc": fOdipspc,
                    "pass_fail": False,
                }
            )