import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_030203_03(RuleUnit):


    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 3.2.3 (3)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '에폭시 도막철근의 보수'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    3. 시공
    3.2 에폭시 도막철근
    3.1.3 철근의 이음
    3.2.3 손상된 에폭시 도막 보수
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####(3) 300mm 길이 당 보수해야 할 표면적이 2%를 초과하는 에폭시 도막철근은 사용할 수 없다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 에폭시 도막철근의 보수];
    B["KCS 14 20 11 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.2.3 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 보수해야 하는 에폭시 도막철근/];
    VarIn2[/입력변수: 300mm 길이 당 보수해야 할 표면적 비율/];
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"300mm 길이 당 보수해야 할 표면적 비율 > 2%"}
    C --> |True|D[사용할 수 없다]
    D --> End([에폭시 도막철근의 보수])
    C --> |False|Pass([Pass])
    """

    @rule_method
    def maintenance_epoxy(fIRatSur):
        """
        Args:
            fIRatSur (float): 300mm 길이 당 보수해야 할 표면적 비율
        Returns:
            sOMaiEpo (sting): 보수해야 하는 에폭시 도막철근
        """
        if fIRatSur > 2:
            sOMaiEpo = "Fail"
        elif fIRatSur <= 2:
            sOMaiEpo = "Pass"
        return sOMaiEpo