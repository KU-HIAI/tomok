import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143130_030302_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 30 3.3.2 (1)'
    ref_date = '2023-11-29'
    doc_date = '2019-05-20'
    title = '앵커볼트의 중심선'

    description = """
    조립 및 설치
    3. 시공
    3.3 부재조립 및 설치
    3.3.2 건축물의 현장 조립
    (1)
    """

    content = """
    #### 3.3.2 건축물의 현장 조립
    (1) 앵커링(anchoring)
    ⑤ 구조용 앵커볼트를 사용하는 경우 앵커볼트 간의 중심선은 기둥중심선으로부터 3mm이상 벗어나지 않아야 한다. 세우기용 앵커볼트의 경우에는 앵커볼트 간의 중심선이 기둥중심선으로부터 5mm 이상 벗어나지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커볼트의 중심선];
    B["KCS 14 31 30 3.2.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.2.2(1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 앵커볼트 종류/];
    VarIn2[/입력변수: 앵커볼트 간의 중심선/];
    VarIn3[/입력변수: 기둥 중심선/];

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"앵커볼트 종류"}
    C --> |구조용 앵커볼트|D{"|기둥 중심선-앵커볼트 간의 중심선|\n < 3mm"}
    C --> |세우기용 앵커볼트|E{"|기둥 중심선-앵커볼트 간의 중심선|\n < 5mm"}

    D & E --> F(["Pass or Fail"])

    """

    @rule_method
    def centerline_of_anchor_bolt(sIAncTyp, fICenCol, fICenAnc) -> bool :
        """앵커볼트의 중심선
        Args:
            sIAncTyp (str): 앵커볼트 종류
            fICenCol (float): 기둥 중심선
            fICenAnc (float): 앵커볼트 간의 중심선

        Returns:
            pass_fail (bool) : 조립 및 설치 3.3.2 건축물의 현장 조립 (1)의 판단 결과
        """
        assert isinstance(sIAncTyp, str)
        assert isinstance(fICenCol, float)
        assert isinstance(fICenAnc, float)

        pass_fail = False

        if sIAncTyp == "구조용 앵커볼트":
            if -3 < fICenCol-fICenAnc < 3:
                pass_fail = True

        if sIAncTyp == "세우기용 앵커볼트":
            if -5 < fICenCol-fICenAnc < 5:
                pass_fail = True

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )