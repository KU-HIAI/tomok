import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020415_04(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.4.15 (4)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '인발시험 시 기준점과 반력판의 거리'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.4 인발재하시험
    2.4.15 기준점 및 기준보
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 기준점은 반력판으로부터 2.5 m 이상 떨어진 곳으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험 시 기준점과 반력판의 거리];
    B["KCS 11 50 40 2.4.15 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.4.15 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 기준점과 반력판의 거리/];
    VarIn1[/입력변수: 기준점과 반력판의 거리/];
    VarOut  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기준점과 반력판의 거리 ≥ 2.5 m"}
    C --> |True|Pass(["Pass"])
    C --> |False|Fail(["Fail"])
    """

    @rule_method
    def distance_reference_plate(fIDisPla):
        """
        Args:
            fIDisPla (float): 기준점과 반력판의 거리
        Returns:
            sODisPla (sting): 기준점과 반력판의 거리
        """
        if fIDisPla >= 2.5:
            sODisPla = "Pass"
        else:
            sODisPla = "Fail"
        return sODisPla