import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_030203_04(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 3.2.3 (4)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '손상된 에폭시 도막에 덧댄 보수재의 면적'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    3. 시공
    3.2 에폭시 도막철근
    3.1.3 철근의 이음
    3.2.3 손상된 에폭시 도막 보수
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 손상된 에폭시 도막에 덧댄 보수재의 면적은 300mm 길이 당 5%를 넘지 않아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 손상된 에폭시 도막에 덧댄 보수재의 면적];
    B["KCS 14 20 11 3.2.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.2.3 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 손상된 에폭시 도막에 덧댄 보수재의 면적/];
    VarIn2[/입력변수: 300mm 길이 당 보수재 면적의 비율/];
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"300mm 길이 당 보수재 면적의 비율 < 5%"}
    C --> |True|Pass([Pass])
    C --> |False|Fail([Fail])
    """

    @rule_method
    def repair_material_epoxy(fIRatRep):
        """
        Args:
            fIRatRep (float): 300mm 길이 당 보수재 면적의 비율
        Returns:
            sORepMat (sting): 손상된 에폭시 도막에 덧댄 보수재의 면적
        """
        if fIRatRep <= 5:
            sORepMat = "Pass"
        else:
            sORepMat = "Fail"
        return sORepMat