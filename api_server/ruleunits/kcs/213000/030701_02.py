import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030701_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.7.1 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-22'
    title = '말뚝의 연직도'

    description = """
    가설흙막이 공사
    3. 시공
    3.7. 흙막이 벽 공법
    3.7.1. CIP공법
    (2)
    """

    content = """
    #### 3.7.1. CIP공법
    (2) 말뚝의 연직도는 말뚝 길이의 1/200 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝의 연직도];
    B["KCS 21 30 00 3.7.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.7.1 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 말뚝의 연직도/];
    VarIn1[/입력변수: 말뚝 길이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"말둑의 연직도 <= 말뚝 길이 * 1/200"}
    C1 --> D1["말뚝의 연직도"]
    D1 --> E1(["Pass/Fail"]);
    """

    @rule_method
    def Length_of_Pile(fILenPil) -> float:
        """ 슬러리의 비중
        Args:
            fILenPil (float): 말뚝 길이

        Returns:
            fOVerPil (float): 말뚝의 최대 연직도
        """
        assert isinstance(fILenPil, float)

        fOVerPil = fILenPil * 1/200

        return RuleUnitResult(
                result_variables = {
                    "fOVerPil": fOVerPil
                }
            )