import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_030206_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.6 (2)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.6 상대오차
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.6 상대오차
    (2) 홈
    ① 폭이 50mm 이하인 경우 : 3mm
    ② 폭이 50mm 초과 ~ 300mm 이하인 경우 : 6mm
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 홈의 상대오차"];
    B["KCS 21 50 05 3.2.6 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.6 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 상대오차"/];
		VarIn1[/"입력변수: 홈의 폭"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{홈의 폭}


		D --> |홈의 폭 <= 50mm|E[상대오차 = 3mm]
		D --> |50mm < 홈의 폭 <= 300mm|F[상대오차 = 6mm]


		E --> K([상대오차])
		F --> K([상대오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def relative_error_of_groove(fIWidGro) -> str:
        """홈의 상대오차

        Args:
            fIWidGro (float): 홈의 폭

        Returns:
            fORelTol (float): 상대오차
        """

        if fIWidGro <= 50:
            fORelTol = 3
        elif 50 < fIWidGro <= 300:
            fORelTol = 6
        return fORelTol