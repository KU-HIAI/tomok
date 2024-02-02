import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020309_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.3.9 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '동재하시험 시 시험말뚝의 두부 정리'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.3 동재하시험
    2.3.9 시험말뚝의 두부 정리
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 선정된 시험말뚝은 지상 부분의 돌출길이가 3 D(D: 말뚝의 지름) 정도 되어야 하며, 말뚝 두부에 편심이 걸리지 않도록 표면에 요철이 없는 완전히 매끈한 상태를 유지하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 동재하시험 시 시험말뚝의 두부 정리];
    B["KCS 11 50 40 2.3.9 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.3.9 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 시험말뚝의 두부 정리/];
    VarIn1[/입력변수: 지상 부분의 돌출길이/];
    VarIn2[/입력변수: 말뚝의 지름/];
    VarIn3[/입력변수: 표면 정리/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"지상 부분의 돌출길이 \n 표면 정리\n."}
    C --> |지상 부분의 돌출길이|D["지상 부분의 돌출길이가 \n 3*말뚝의 지름 정도\n."]
    C --> |표면 정리|E["말뚝 두부에 편심이 걸리지 않도록 \n 표면에 요철이 없는 완전히 매끈한 상태를 유지\n."]
    D & E --> End(["시험말뚝의 두부 정리"])
    """

    @rule_method
    def clearing_head_testpile(bIAboGro,fIPilDia, bISurCle):
        """
        Args:
            bIAboGro (boolean): 지상 부분의 돌출길이
            fIPilDia (float): 말뚝지름
            bISurCle (boolean): 표면 정리
        Returns:
            sOCleHea (string): 시험말뚝의 두부 정리
        """
        if bIAboGro:
            sOCleHea = "지상 부분의 돌출길이가 " + str(3*fIPilDia)+ "mm 정도"
        elif bISurCle:
            sOCleHea = "말뚝 두부에 편심이 걸리지 않도록 표면에 요철이 없는 완전히 매끈한 상태를 유지"
        return sOCleHea