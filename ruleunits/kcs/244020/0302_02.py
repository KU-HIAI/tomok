import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0302_02(RuleUnit): #KCS244020_0302_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 최정운'  # 작성자명
    ref_code = 'KCS 24 40 20 3.1 (1)' # 건설기준문서
    ref_date = '2016-06-30'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '시공할때의 기온'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.2 기상 조건
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### (2) 시공할 때의 기온은 5 ℃ 이상이어야 한다. 부득이 하여 기온이 5 ℃ 미만에서 시공할 경우는 결로에 주의하여야 하며, 보온 대책을 수립하여야 한다. 하절기와 같이 시공할 때의 온도가 30 ℃를 넘는 경우 온도에 영향을 받기 쉬운 재료, 특히 클로로프렌 고무 도막방수재는 새벽이나 야간에 시공하거나 차양을 설치하여 직사광의 영향을 받아 시공면의 온도가 올라가는 것을 막도록 하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시공할 때의 기온];
    B["KCS 24 40 20 3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.2 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 시공할 때의 기온/];
    VarIn1[/입력변수: 기온/];
    VarIn2[/입력변수: 온도에 영향을 받기 쉬운 재료/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{기온}
    C --> |"5 ℃ ≤ 기온 ≤ 30 ℃"|Pass([Pass])
    C --> |"기온 > 30 ℃"|D{온도에 영향을 받기 쉬운 재료}
    D --> |False|Pass([Pass])
    D --> |True|F[새벽이나 야간에 시공하거나 차양을 설치하여 \n 직사광의 영향을 받아 시공면의 온도가 \n 올라가는 것을 막도록 하여야 한다.]
    C --> |"기온 < 5 ℃"|G[결로에 주의하여야 하며, \n 보온 대책을 수립하여야 한다.]
    F & G --> End(["시공할 때의 기온"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def temperature(fITem,bITemMat)->str:
        """
        Args:
            fITem (float): 기온
            bITemMat (boolean): 온도에 영향을 받기 쉬운 재료
        Returns:
            sOTemCon (string): 기온에 따른 시공
        """
        if fITem < 5:
            sOTemCon = "결로에 주의하여야 하며, 보온 대책을 수립하여야 한다"
        elif fITem < 30:
            sOTemCon = "Pass"
        else:
            if bITemMat:
                sOTemCon = "새벽이나 야간에 시공하거나 차양을 설치하여 직사광의 영향을 받아 시공면의 온도가 올라가는 것을 막도록 하여야 한다."
            else:
                sOTemCon = "Pass"
        return sOTemCon