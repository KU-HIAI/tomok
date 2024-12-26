import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_0305_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.5.(2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '비계의 높이'

    description = """
    비계
    3. 시공
    3.5 이동식 비계
    (2)
    """

    content = """
    #### 3.5. 이동식 비계
    (2) 비계의 높이는 밑면 최소폭의 4배 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비계의 높이];
    B["KCS 21 60 10 3.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.5 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 비계의 최대 높이/];
    VarIn1[/입력변수: 밑면 최소폭/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"비계의 최대높이 <= 밑면 최소폭 * 4"}
    C1 --> D1["비계의 최대 높이"]
    D1 --> E1(["비계의 최대 높이"]);
    """

    @rule_method
    def Minimum_Width_of_the_Bottom_Surface(fIWidBot) -> float:
        """ 비계의 높이
        Args:
            fIWidBot (float): 밑면 최소폭

        Returns:
            fOHeiSca (float): 비계의 최대 높이
        """
        assert isinstance(fIWidBot, float)

        fOHeiSca = 4 * fIWidBot

        return RuleUnitResult(
                result_variables = {
                    "fOHeiSca": fOHeiSca
                }
            )