import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_030203_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 3.2.3 (2)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '철근 용접이음 시 기온'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    3. 시공
    3.2 에폭시 도막철근
    3.1.3 철근의 이음
    3.2.3 손상된 에폭시 도막 보수
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 에폭시 도막이 손상된 경우, 300mm 길이 당 보수해야 할 표면적이 2%를 넘지 않아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 손상된 에폭시 도막];
    B["KCS 14 20 11 3.2.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.2.3 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 손상된 에폭시 도막의 보수 가능/];
    VarIn1[/입력변수: 에폭시 도막의 손상/];
    VarIn2[/입력변수: 300mm 길이 당 보수해야 할 표면적 비율/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"에폭시 도막의 손상"}
    C --> |True|D{"300mm 길이 당 보수해야 할 표면적 비율 < 2%"}
    D --> |True|Pass([Pass])
    D --> |False|Fail([Fail])
    """

    @rule_method
    def damaged_epoxy_paint(bIDamEpo,fIRatSur):
        """
        Args:
            bIDamEpo (boolean): 에폭시 도막의 손상
            fIRatSur (float): 300mm 길이 당 보수해야 할 표면적 비율
        Returns:
            sODamEpo (sting): 손상된 에폭시 도막의 보수 가능
        """
        if bIDamEpo:
            if fIRatSur <= 2:
                sODamEpo = "Pass"
            else:
                sODamEpo = "Fail"
        else:
            sODamEpo = "Pass"
        return sODamEpo