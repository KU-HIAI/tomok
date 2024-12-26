import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030401_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.4.1.(2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '주틀 사이의 하중한도'

    description = """
    비계
    3. 시공
    3.4 강관틀 비계
    3.4.1 주틀
    (2)
    """

    content = """
    #### 3.4.1 주틀
    (2) 주틀의 간격이 1.8m일 경우에는 주틀 사이의 하중한도를 4.0kN으로 하고, 주틀의 간격이 1.8m 이내일 경우에는 그 역비율로 하중한도를 증가할 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 주틀 사이의 하중한도];
    B["KCS 21 60 10 3.4.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.4.1 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 주틀 사이의 하중한도/];
    VarIn1[/입력변수: 주틀의 간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"주틀의 간격 < 1.8m"}
    C1 --> |주틀의 간격 = 1.85m|D1["주틀 사이의 하중한도 = 4.0kN"]
    C1 --> |YES|D2["주틀 사이의 하중한도 = 1.8/주틀의 간격 * 4.0kN"]
    D1 & D2 --> E1(["주틀 사이의 하중한도"]);
    """

    @rule_method
    def Spacing_of_the_Main_Frame(fISpaFra) -> RuleUnitResult:
        """ 주틀 사이의 하중한도
        Args:
            fISpaFra (float): 주틀의 간격

        Returns:
            fOLimFra (float): 주틀 사이의 하중한도
        """
        assert isinstance(fISpaFra, float)
        assert 0 < fISpaFra <= 1.8

        if fISpaFra == 1.8:
          fOLimFra = 4
        elif fISpaFra < 1.8:
          fOLimFra = 4 * (1.8 / fISpaFra)

        return RuleUnitResult(
                result_variables = {
                    "fOLimFra": fOLimFra
                }
            )