import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030206_03_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.6 (3) ①' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.6 상대오차
    (3)
    ①
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.6 상대오차
    (3) 거푸집면 또는 선의 기울기는 3m당 측정하여 다음의 오차 범위 이내이어야 한다.
    ① 노출된 기둥의 모서리 수직선, 노출 콘크리트에 있는 조절 줄눈의 홈 : 6mm
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 3m 당 거푸집면 또는 선의 기울기 허용 오차"];
    B["KCS 21 50 05 3.2.6 (3) ①"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.6 (3) ①"])

    subgraph Variable_def
    VarOut1[/"출력변수: 상대오차"/];
		VarIn1[/"입력변수: 측정 대상"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{측정 대상}


		D --> |노출된 기둥의 모서리 수직선 \n or 노출 콘크리트에 있는 조절 줄눈의 홈|E[상대오차 = 6mm]


		E --> K([상대오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def gradient_tolerance_of_surface_or_line(sIMeaSub) -> RuleUnitResult:
        """거푸집 면 또는 선의 기울기 허용 오차

        Args:
            sIMeaSub (str): 측정 대상

        Returns:
            fORelTol (float): 상대오차
        """
        assert isinstance(sIMeaSub, str)

        if sIMeaSub == "노출된 기둥의 모서리 수직선" or sIMeaSub == "노출 콘크리트에 있는 조절 줄눈의 홈":
            fORelTol = 6
            return RuleUnitResult(
                result_variables = {
                    "fORelTol": fORelTol
                }
            )
        else:
            assert 1 != 1