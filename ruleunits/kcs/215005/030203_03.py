import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_030203_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.3 (3)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.3 수평오차
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.3 수평오차
    (3) 슬래브에서 쇠톱자름(sawcuts)이나 줄눈, 그리고 매설물로 인해 약화된 면 : 19mm 이하
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 수평오차"];
    B["KCS 21 50 05 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.3 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 수평오차"/];
		VarIn1[/"입력변수: 측정 대상"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{측정대상}


		D --> |"'슬래브에서 쇠톱자름(sawcuts)' \n or '슬래브에서 줄눈' \n or '매설물로 인해 약화된 면'"|E["수평오차 <= \n 19mm"]


		E --> G([수평오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def horizontal_error(sIMeaSub) -> str:
        """수평오차

        Args:
            sIMeaSub (string): 측정 대상

        Returns:
            fOHorTol (float): 수평오차
        """

        if sIMeaSub == "슬래브에서 쇠톱자름" or sIMeaSub == "슬래브에서 줄눈" or sIMeaSub == "매설물로 인해 약화된 면":
            fOHorTol = 19
        return fOHorTol