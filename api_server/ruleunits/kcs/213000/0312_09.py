import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_0312_09(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.12.(9)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '주동토압의 고려'

    description = """
    가설흙막이 공사
    3. 시공
    3.12. 타이 로드와 케이블
    (9)
    """

    content = """
    #### 3.12. 타이 로드와 케이블
    (9) 저항체(dead man) 높이가 지표면에서 앵커판 하단까지 깊이의 1/2보다 크면, 이 앵커는 앵커판 하단 깊이에서 주동토압을 발생시키는 것으로 보고 주동토압을 고려하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 주동토압의 고려];
    B["KCS 21 30 00 3.12 (9)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.12 (9)"])

    subgraph Variable_def
    VarOut1[/출력변수: 주동토압의 고려/];
    VarIn1[/입력변수: 저항체 높이/];
    VarIn2[/입력변수: 앵커판 하단까지 깊이/];
    end
    VarOut1 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"저항체 높이 >= 앵커판 하단까지 깊이 * 0.5"}
    C1 --> |YES|D1["주동토압 고려"]
    C1 --> |NO|D2["주동토압 미고려"]

    D1 & D2 --> E1(["주동토압의 고려"]);
    """

    @rule_method
    def Height_of_Retaining_Structure(fIHeiRet, fIDepAnc) -> str:
        """ 주동토압의 고려
        Args:
            fIHeiRet (float): 저항체의 높이
            fIDepAnc (float): 앵커판 하단까지 깊이

        Returns:
            sOActEar (str): 주동토압의 고려
        """
        assert isinstance(fIHeiRet, float)
        assert isinstance(fIDepAnc, float)

        if fIHeiRet >= 0.5 * fIDepAnc:
          sOActEar = "주동토압을 고려하여야 한다"
        else:
          sOActEar = "주동토압을 고려하지 않아도 된다"

        return RuleUnitResult(
                result_variables = {
                    "sOActEar": sOActEar
                }
            )