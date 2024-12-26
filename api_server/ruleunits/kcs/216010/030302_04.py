import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030302_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.3.2.(4)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '비계기둥 사이의 하중한도'

    description = """
    비계
    3. 시공
    3.3. 강관 비계
    3.3.2. 띠장
    (4)
    """

    content = """
    #### 3.3.2. 띠장
    (4) 띠장은 비계기둥의 간격이 1.85m일 때는 비계기둥 사이의 하중한도를 4.0kN으로 하고, 비계기둥의 간격이 1.85m 미만일 때는 그 역비율로 하중한도를 증가할 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비계기둥 사이의 하중한도];
    B["KCS 21 60 10 3.3.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.3.2 (4)"])

    subgraph Variable_def
    VarOut1[/출력변수: 비계기둥 사이의 하중한도/];
    VarIn1[/입력변수: 비계기둥의 간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"비계기둥의 간격 < 1.85m"}
    C1 --> |비계기둥의 간격 = 1.85m|D1["비계기둥 사이의 하중한도 = 4.0kN"]
    C1 --> |YES|D2["비계기둥 사이의 하중한도 = 1.85/비계기둥의 간격 * 4.0kN"]
    D1 & D2 --> E1(["비계기둥 사이의 하중한도"]);
    """

    @rule_method
    def Spacing_between_Scaffolding_Columns(fISpaSca) -> RuleUnitResult:
        """ 비계기둥 사이의 하중한도
        Args:
            fISpaSca (float): 비계기둥의 간격

        Returns:
            fOLimSca (float): 비계기둥 사이의 하중한도
        """
        assert isinstance(fISpaSca, float)
        assert 0 < fISpaSca <= 1.85

        if fISpaSca == 1.85:
          fOLimSca = 4
        elif fISpaSca < 1.85:
          fOLimSca = 4 * (1.85 / fISpaSca)

        return RuleUnitResult(
                result_variables = {
                    "fOLimSca": fOLimSca
                }
            )