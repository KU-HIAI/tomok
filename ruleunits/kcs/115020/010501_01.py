import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_010501_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 1.5.1 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '최대 연직도'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    1. 일반사항
    1.5 일반요건
    1.5.1 설치허용오차
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####1.5.1 설치허용오차
    (1) 연직도는 말뚝길이의 1/100 이내가 되도록 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대 연직도];
    B["KCS 11 50 20 1.5.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 1.5.1 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 최대 연직도/];
    VarIn1[/입력변수: 말뚝길이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C["최대 연직도 = 말뚝길이/100"]
    C --> End([최대 연직도])
    """

    @rule_method
    def verticality(fIPilLen):
        """
        Args:
            fIPilLen (float): 말뚝 길이
        Returns:
            fOMaxVer (float): 최대 연직도
        """
        fOMaxVer = fIPilLen/100
        return fOMaxVer