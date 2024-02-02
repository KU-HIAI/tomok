import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0301_04(RuleUnit): #KCS244020_0301_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 최정운'  # 작성자명
    ref_code = 'KCS 24 40 20 3.1 (1)' # 건설기준문서
    ref_date = '2016-06-30'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '콘크리트 바닥판면 방수층 시공'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.1 시공 전 준비사항
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### (4) 바닥판면의 요철부위 중 직경 10 mm 이상이며 깊이 3 mm 이상 패인부분은 이물질을 제거하고 적합한 충전재를 사용하여 공극 메움(퍼티작업)을 하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판면의 요철부위];
    B["KCS 24 40 20 3.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.1 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 바닥판면의 요철부위/];
    VarIn1[/입력변수: 패인부분의 직경/];
    VarIn2[/입력변수: 패인부분의 깊이/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{패인부분의 직경}
    C --> |"패인부분의 직경 ≥ 10 mm"|D{패인부분의 깊이}
    D --> |"패인부분의 깊이 ≥ 3 mm"|E["이물질을 제거하고 적합한 충전재를 사용하여 \n 공극 메움(퍼티작업)을 하여야 한다."]
    C --> |"패인부분의 직경 < 10 mm"|Pass([Pass])
    D --> |"패인부분의 깊이 < 3 mm"|Pass([Pass])
    E --> End([바닥판면의 요철부위])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def unevenness_deck(fIDiaInd,fIDepInd)->str:
        """
        Args:
            fIDiaInd (float): 패인부분의 직경
            fIDepInd (float): 패인부분의 깊이
        Returns:
            sOUneDec (string): 바닥판면의 요철부위 정리
        """
        if fIDiaInd >= 10:
            if fIDepInd >=3:
                sOUneDec = "이물질을 제거하고 적합한 충전재를 사용하여 공극 메움(퍼티작업)을 하여야 한다."
            else:
                sOUneDec = "Pass"
        else:
            sOUneDec = "Pass"
        return sOUneDec