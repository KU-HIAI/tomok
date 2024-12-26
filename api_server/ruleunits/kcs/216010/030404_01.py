import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030404_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.4.4.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '버팀기둥의 설치'

    description = """
    비계
    3. 시공
    3.4. 강관틀 비계
    3.4.4. 보강재
    (1)
    """

    content = """
    #### 3.4.4. 보강재
    (1) 띠장방향으로 길이 4m 이하이고, 높이 10m를 초과할 때는 높이 10m 이내마다 띠장방향으로 버팀기둥을 설치한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 버팀기둥의 설치];
    B["KCS 21 60 10 3.4.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.4.4 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 버팀기둥의 설치/];
    VarIn1[/입력변수: 띠장방향으로의 길이/];
    VarIn2[/입력변수: 띠장방향으로의 높이/];
    end
    VarOut1 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"띠장방향으로의 길이 <= 4m and 띠장방향으로의 높이 > 10m"}
    C1 --> D1["높이 10m 이내마다 띠장방향으로 버팀기둥을 설치한다"]
    D1 --> E1(["버팀기둥의 설치"]);

    """

    @rule_method
    def Length_in_the_Wale_direction(fILenWal, fIHeiWal) -> str:
        """ 버팀기둥의 설치
        Args:
            fILenWal (float): 띠장방향으로의 길이
            fIHeiWal (float): 띠장방향으로의 높이

        Returns:
            sOInsSup (str): 버팀기둥의 설치
        """
        assert isinstance(fILenWal, float)
        assert isinstance(fIHeiWal, float)

        if fILenWal <= 4 and fIHeiWal > 10:
          sOInsSup = "높이 10m 이내마다 띠장방향으로 버팀기둥을 설치한다"
        else:
          sOInsSup = "버팀기둥을 설치하지 않는다"

        return RuleUnitResult(
                result_variables = {
                    "sOInsSup": sOInsSup
                }
            )