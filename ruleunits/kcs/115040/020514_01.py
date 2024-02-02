import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020511_01(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.5.11 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '횡방향 재하시험 재하장치'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.5 횡방향재하시험
    2.5.11 가력장치
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 재하장치는 계획최대시험하중의 120% 이상의 가력능력을 가져야 하며, 예상되는 시험말뚝 등의 변형에 충분히 따를 수 있는 것으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 재하시험 재하장치];
    B["KCS 11 50 40 2.5.14 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.5.14 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 재하장치/];
    VarIn1[/입력변수: 가력능력/];
    VarIn2[/입력변수: 계획최대시험하중/];
    VarIn3[/입력변수: 예상되는 시험말뚝 등의 변형 수용/];

    VarOut  ~~~ VarIn1 & VarIn2
    VarIn1 & VarIn2  ~~~ VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"가력능력 ≥ 계획최대시험하중*1.2"}
    C --> |True|D{"예상되는 시험말뚝 등의 변형 수용"}
    C --> |False|Fail([Fail])
    D --> |True|Pass([Pass])
    D --> |False|Fail([Fail])
    """

    @rule_method
    def loading_device(fILoaCap,fIDesLoa,bIDefPil ):
        """
        Args:
            fILoaCap (float): 가력능력
            fIDesLoa (float): 계획최대시험하중
            bIDefPil (boolean): 예상되는 시험말뚝 등의 변형 수용
        Returns:
            sOLoaDev (sting): 재하장치
        """
        if fILoaCap >= fIDesLoa*1.2:
            if bIDefPil == True:
                sOLoaDev = "Pass"
            else:
                sOLoaDev = "Fail"
        else:
            sOLoaDev = "Fail"
        return sOLoaDev