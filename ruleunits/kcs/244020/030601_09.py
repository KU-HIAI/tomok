import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030601_09(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.6.1 (9)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-17'
    title = '도막방수공사의 시공두께'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재 시공
    3.6.1 시공일반
    (9)
    """

    # 건설기준문서내용(text)
    content = """
    #### (9) 도막방수공사에 있어서 방수성능을 확보하기 위한 시공두께는 재료의 성능면에서 1.0 mm 이상이 되어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도막방수공사의 시공두께];
    B["KCS 24 40 20 3.6.1 (9)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.1 (9)"])

    subgraph Variable_def
    VarOut[/출력변수: 도막방수공사의 시공두께/];
    VarIn1[/입력변수: 도막방수공사의 시공두께/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"도막방수공사의 시공두께 ≥ 1.0 mm"}
    C --> |"True"|Pass([Pass])
    C --> |"False"|Fail([Fail])
    """

    @rule_method
    def thickness_waterproof(fIThiCoa)->str:
        """
        Args:
            fIThiCoa (float): 도막방수공사의 시공두께
        Returns:
            sOThiCoa (string): 도막방수공사의 시공두께
        """
        if fIThiCoa >=1.0:
            sOThiCoa = "Pass"
        else:
            sOThiCoa = "Fail"
        return sOThiCoa