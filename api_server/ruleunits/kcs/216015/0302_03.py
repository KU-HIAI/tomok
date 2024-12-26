import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0302_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.2 (3)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-05'
    title = '계단참의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.2 작업계단
    (3)
    """

    content = """
    #### 3.2. 작업계단
    (3) 높이가 3m를 초과하는 계단에는 높이 3m 이내마다 너비 1.2m 이상의 계단참을 설치하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 계단참의 설치];
    B["KCS 21 60 15 3.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.5 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 계단참의 설치/];
    VarIn1[/입력변수: 계단의 높이/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"계단의 높이 > 3m"}
    C1 --> |YES|D1["3m 이내마다 너비 1.2m이상의 계단 참을 설치"]
    D1 --> E1(["계단참의 설치"]);
    """

    @rule_method
    def Height_of_Stairs(fIHeiSta) -> str:
        """ 계단참의 설치
        Args:
            fIHeiSta (float): 계단의 높이

        Returns:
            sOInsLan (str): 계단참의 설치
        """
        assert isinstance(fIHeiSta, float)

        if fIHeiSta > 3:
            sOInsLan = "높이 3m 이내마다 너비 1.2m 이상의 계단참을 설치하여야 한다"
        else:
            sOInsLan = "계단참을 설치하지 않는다"

        return RuleUnitResult(
                result_variables = {
                    "sOInsLan": sOInsLan
                }
            )