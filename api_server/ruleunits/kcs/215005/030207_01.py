import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030207_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.7 (1)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.7 부재를 관통하는 개구부
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.7 부재를 관통하는 개구부
    (1) 개구부의 크기 : +25mm, -6mm
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 부재를 관통하는 개구부의 크기"];
    B["KCS 21 50 05 3.2.7 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.7 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 개구부의 크기 허용오차"/];
		VarIn1[/"입력변수: 개구부의 크기 허용오차"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{개구부의 크기 허용오차}

		D --> E["+25mm, -6mm"]
		E --> F([개구부의 크기 허용오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def size_tolerance_of_openings(bITolOpe) -> RuleUnitResult:
        """개구부의 크기 허용오차

        Args:
            bITolOpe (bool): 개구부의 크기 허용오차

        Returns:
            sOTolOpe (str): 개구부의 크기 허용오차
        """
        assert isinstance(bITolOpe, bool)

        if bITolOpe == True:
            sOTolOpe = "+25mm, -6mm"
            return RuleUnitResult(
                result_variables = {
                    "sOTolOpe": sOTolOpe
                }
            )
        else:
            assert 1 != 1