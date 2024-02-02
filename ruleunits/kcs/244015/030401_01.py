import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244015_030401_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 15 3.4.1 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '절단 도구'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량난간
    3. 시공
    3.4 알루미늄 난간
    3.4.1 절단
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 두께가 13 mm 이하인 재료는 가위질·톱질 또는 기계로 절단하며, 그보다 두꺼울 때에는 톱 또는 기계로 절단하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단 도구];
    B["KCS 24 40 15 3.4.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.4.1 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 절단 도구/];
    VarIn1[/입력변수: 재료 두께/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{재료 두께}
    C --> |"재료 두께 ≤ 13 mm"|D[절단 도구 = 가위, 톱, 기계]
    C --> |"재료 두께 > 13 mm"|E[절단 도구 = 톱, 기계]
    D & E --> F(["절단 도구"])
    """

    @rule_method
    def cutting_tool(fIMatThi)-> str:
        """
        Args:
            fIMatThi (float): 재료 두께
        Returns:
            sOCutToo (string): 절단 도구
        """
        if fIMatThi <= 13:
            sOCutToo = "가위질·톱질 또는 기계로 절단"
        else:
            sOCutToo = "톱 또는 기계로 절단"
        return sOCutToo