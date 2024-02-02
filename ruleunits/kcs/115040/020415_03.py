import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020415_03(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.4.15 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '인발시험 시 가설말뚝을 기준점으로 하는 경우 기준점의 위치'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.4 인발재하시험
    2.4.15 기준점 및 기준보
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####(3) 가설말뚝을 기준점으로 하는 경우 시험말뚝으로부터 그 지름의 5배 이상 또는 2 m 이상, 반력말뚝으로부터 그 지름의 3배 이상 떨어진 위치에 설치하는 것을 원칙으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험 시 가설말뚝을 기준점으로 하는 경우 기준점의 위치];
    B["KCS 11 50 40 2.4.15 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.4.15 (3)"])

    subgraph Variable_def
    VarOut1[/출력변수: 기준점과 시험말뚝의 최소거리/];
    VarOut2[/출력변수: 기준점과 반력말뚝의 최소거리/];
    VarIn1[/입력변수: 가설말뚝/];
    VarIn2[/입력변수: 시험말뚝 지름/];
    VarIn3[/입력변수: 반력말뚝 지름/];
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기준점과 시험말뚝의 최소거리\n기준점과 반력말뚝의 최소거리"}
    C --> |기준점과 반력말뚝의 최소거리|D{가설말뚝}
    D --> E["기준점과 시험말뚝의 최소거리= max(시험말뚝 지름 * 5, 2000mm)"]
    C --> |기준점과 반력말뚝의 최소거리|F{가설말뚝}
    F --> G["기준점과 반력말뚝의 최소거리= 반력말뚝 지름 * 3"]
    E &  G--> End(["인발시험 시 가설말뚝을 기준점으로 하는 경우 기준점의 위치"])
    """

    @rule_method
    def distance_reference_point_testpile(bITemPil ,fITesDia):
        """
        Args:
            bITemPil (boolean): 가설말뚝
            fITesDia (float): 시험말뚝 지름
        Returns:
            fODisPil_1 (float): 기준점과 시험말뚝의 최소거리
        """
        if bITemPil:
            fODisPil_1 = max(fITesDia * 5, 2000)
        return fODisPil_1

    def distance_reference_reaction(self, bITemPil, fIReaDia):
        """
        Args:
            bITemPil (boolean): 가설말뚝
            fIReaDia (float): 반력말뚝 지름
        Returns:
            fODisPil_2 (float): 기준점과 반력말뚝의 최소거리
        """
        if bITemPil:
            fODisPil_2 = fIReaDia * 3
        return fODisPil_2