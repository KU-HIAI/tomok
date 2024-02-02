import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030603_04(RuleUnit): #KCS244020_030603_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 최정운'  # 작성자명
    ref_code = 'KCS 24 40 20 3.6.3 (4)' # 건설기준문서
    ref_date = '2016-06-30'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '고무아스팔트계 도포시 기포'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재 시공
    3.6.3 고무아스팔트계의 도포
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### (4) 직경 3 mm 이상의 큰 기포는 터트린 후에 다음 층의 도포를 시행한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 고무아스팔트계 도포시 기포];
    B["KCS 24 40 20 3.6.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.3 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 도포 시 기포/];
    VarIn1[/입력변수: 기포 직경/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"기포 직경 ≥ 3mm"}
    C --> |"True"|D[기포는 터트려 제거한 뒤에 다음 층의 도포 시행]
    D --> End([도포 시 기포])
    C --> |"False"|Pass([Pass])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def bubble_spreading(fIBubDia)->str:
        """
        Args:
            fIBubDia (float): 기포 직경
        Returns:
            sOBubSpr (string): 도포 시 기포
        """
        if fIBubDia >= 3.0:
            sOBubSpr = "기포를 터트려 제거한 후에 다음 층의 도포를 시행"
        else:
            sOBubSpr = "Pass"
        return sOBubSpr