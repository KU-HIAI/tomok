import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020415_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.4.15 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '인발시험 시 사용말뚝을 기준점으로 하는 경우 기준점의 위치'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.4 인발재하시험
    2.4.15 기준점 및 기준보
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 사용말뚝을 기준점으로 하는 경우 시험말뚝 및 반력말뚝으로부터 각 말뚝지름의 2.5배 이상 떨어진 위치의 것을 이용하는 것을 원칙으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험 시 사용말뚝을 기준점으로 하는 경우 기준점의 위치];
    B["KCS 11 50 40 2.4.15 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.4.15 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 기준점과 시험말뚝 및 반력말뚝의 최소거리/];
    VarIn1[/입력변수: 사용말뚝/];
    VarIn2[/입력변수: 말뚝지름/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"사용말뚝"}
    C --> D["기준점과 시험말뚝의 최소거리= 말뚝지름 * 2.5"]
    D --> End(["인발시험 시 사용말뚝을 기준점으로 하는 경우 기준점의 위치"])
    """

    @rule_method
    def distance_reference_point(bIMaiPil ,fIPilDia):
        """
        Args:
            bIMaiPil (boolean): 사용말뚝
            fIPilDia (float): 말뚝지름
        Returns:
            fODisPil (float): 기준점과 시험말뚝 및 반력말뚝의 최소거리
        """
        if bIMaiPil:
            fODisPil = fIPilDia * 2.5
        return fODisPil