import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_010501_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 1.5.1 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '말뚝이음 설치'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    1. 일반사항
    1.5 일반요건
    1.5.1 설치허용오차
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####1.5.1 설치허용오차
    (2) 말뚝이음은 이음위치가 동일 높이에서 시공되지 않도록 하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝이음 설치];
    B["KCS 11 50 20 1.5.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 1.5.1 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 말뚝이음 설치/];
    VarIn1[/입력변수: 동일 높이의 이음위치/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"동일 높이의 이음위치"}
    C --> |True|Fail([Fail])
    C --> |False|Pass([Pass])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def pile_joint_install(bIIdeJoi):
        """
        Args:
            bIIdeJoi (boolean): 동일 높이의 이음위치
        Returns:
            sOPilJoi (string): 말뚝이음 설치
        """
        if bIIdeJoi == True:
            sOPilJoi = "Fail"
        elif bIIdeJoi == False:
            sOPilJoi = "Pass"
        return sOPilJoi