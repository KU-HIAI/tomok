import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030203_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.3 (2)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.3 수평오차
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.3 수평오차
    (2) 슬래브에 300mm 이하인 개구부의 중심선 또는 300mm 이상인 개구부의 외곽선 : 13mm 이하
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 수평오차"];
    B["KCS 21 50 05 3.2.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.3 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 수평오차"/];
		VarIn1[/"입력변수: 측정 대상"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{측정대상}


		D --> |"'부슬래브에 300mm 이하인 개구부의 중심선' \n or '300mm 이상인 개구부의 외곽선'"|E["수평오차 <= \n 13mm"]


		E --> G([수평오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def horizontal_error(sIMeaSub) -> RuleUnitResult:
        """수평오차

        Args:
            sIMeaSub (str): 측정 대상

        Returns:
            fOHorTol (float): 수평오차
        """
        assert isinstance(sIMeaSub, str)

        if sIMeaSub == "슬래브에 300mm 이하인 개구부의 중심선" or sIMeaSub == "슬래브에 300mm 이상인 개구부의 외곽선":
            fOHorTol = 13
            return RuleUnitResult(
                result_variables = {
                    "fOHorTol": fOHorTol
                }
            )
        else:
            assert 1 != 1