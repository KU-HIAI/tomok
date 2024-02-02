import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_0301_04(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 부록 3.1 (4)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '앵커볼트의 조임 방법'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    부록
    3. 시공
    3.1 앵커 볼트의 배치 및 설치
    3.1.3 철근의 이음
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 앵커 볼트의 조임 방법은 너트의 밀착을 확인한 후에 직경 36 mm 이하 앵커 볼트의 경우 60ﾟ, 직경 36 mm를 초과하는 앵커 볼트의 경우 30ﾟ 회전시킨다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커 볼트의 조임 방법];
    B["KCS 14 20 11 부록 3.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 부록 3.1 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 앵커 볼트의 조임 방법/];
    VarIn1[/입력변수: 앵커 볼트의 직경/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{앵커 볼트의 직경}
    C --> |"≤ 36"|D[" 너트의 밀착을 확인한 후 60ﾟ 회전시킨다"]
    C --> |"> 36"|E[" 너트의 밀착을 확인한 후 30ﾟ 회전시킨다"]
    D & E --> End(["앵커 볼트의 조임 방법"])
    """

    @rule_method
    def tightening_ahchor_bolt(fIDiaAnc):
        """
        Args:
            fIDiaAnc (float): 앵커 볼트의 직경
        Returns:
            sOTigMet (sting): 앵커 볼트의 조임 방법
        """
        if fIDiaAnc <= 36:
            sOTigMet = "너트의 밀착을 확인한 후 60ﾟ 회전시킨다"
        else:
            sOTigMet = "너트의 밀착을 확인한 후 30ﾟ 회전시킨다"
        return sOTigMet