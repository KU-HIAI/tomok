import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020205_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.2.5 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '스터드의 기계적 성질'

    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.5 스터드형 전단연결재
    (2)
    """
    content = """
    #### 2.2.5 스터드형 전단연결재
    (2) 강도는 표 2.2-4에 따른다.
    표 2.2-4 스터드의 기계적 성질
    \begin{table}[]
    \begin{tabular}{lll}
    인장강도(MPa) & 항복점 또는 0.2 % 내력(MPa) & 연신율(%) \\
    400∼550   & 235 이상               & 20 이상
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스터드의 기계적 성질];
    B["KCS 24 30 00 2.2.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.5 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 인장강도/];
    VarIn2[/입력변수: 항복점 또는 0.2% 내력/];
    VarIn3[/입력변수: 연신율/];
    VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"400<인장강도<550 \n 항복점 또는 0.2% 내력 >=235 \n 연신율>=20 \n."}
    C --> End([Pass or Fail])
    """

    @rule_method

    def mechanical_stud(fITenStr, fIYieBea,fIEloRat) -> RuleUnitResult:
        """
        Args:
            fITenStr (float): 인장강도
            fIYieBea (float): 항복점 또는 0.2% 내력
            fIEloRat (float): 연신율

        Returns:
            pass_fail (bool): 강교량공사 2.2.5 스터드형 전단연결재 (2)의 판단 결과
        """
        assert isinstance(fITenStr, float)
        assert isinstance(fIYieBea, float)
        assert isinstance(fIEloRat, float)

        if fITenStr >400 and fITenStr<550 and fIYieBea >=235 and fIEloRat >=20:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })