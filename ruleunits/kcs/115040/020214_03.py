import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020214_03(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.2.14 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '양방향 재하시험 시 가설말뚝을 기준점으로 하는 경우 기준점과 시험말뚝의 최소거리'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.2 양방향재하시험
    2.2.14 기준점 및 기준보
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####(3) 가설말뚝을 기준점으로 하는 경우 시험말뚝으로부터 그 지름의 5배 이상 혹은 2 m 이상 떨어진 위치에 설치하는 것을 원칙으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 양방향 재하시험 시 \n 가설말뚝을 기준점으로 하는 경우 \n 기준점과 시험말뚝의 최소거리\n.];
    B["KCS 11 50 40 2.2.14 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.2.14 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 기준점과 시험말뚝의 최소거리/];
    VarIn1[/입력변수: 가설말뚝/];
    VarIn2[/입력변수: 말뚝지름/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"가설말뚝"}
    C --> D["기준점과 시험말뚝의 최소거리= max(말뚝지름 * 5, 2000mm)"]
    D --> End(["기준점과 시험말뚝의 최소거리"]))
    """

    @rule_method
    def distance_reference_point(bITemPil,fIPilDia):
        """
        Args:
            bITemPil (boolean): 가설말뚝
            fIPilDia (float): 말뚝지름
        Returns:
            fODisPil (float): 기준점과 시험말뚝의 최소거리
        """
        if bITemPil:
            fODisPil = max(fIPilDia * 5, 2000)
        return fODisPil