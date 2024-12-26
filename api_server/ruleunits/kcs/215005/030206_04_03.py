import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030206_04_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.6 (4) ③' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.6 상대오차
    (4)
    ③
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.6 상대오차
    (4) 인접한 거푸집의 어긋남은 표면 평탄하기 등급에 따라 다음의 오차 범위 이내이어야 한다.
    ③ C급 : 13mm
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 인접한 거푸집의 어긋남 허용오차"];
    B["KCS 21 50 05 3.2.6 (4) ③"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.6 (4) ③"])

    subgraph Variable_def
    VarOut1[/"출력변수: 상대오차"/];
		VarIn1[/"입력변수: 표면 평탄하기 등급"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{표면 평탄하기 등급}

		D --> |C|G[상대오차 = 13mm]
		G --> K([상대오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def allowable_deviation_between_adjacent_forms(sISurGra) -> RuleUnitResult:
        """인접한 거푸집의 어긋남 허용오차

        Args:
            sISurGra (str): 표면 평탄하기 등급

        Returns:
            fORelTol (float): 상대오차
        """
        assert isinstance(sISurGra, str)

        if sISurGra == "C급":
            fORelTol = 13
            return RuleUnitResult(
                result_variables = {
                    "fORelTol": fORelTol
                }
            )
        else:
            assert 1 != 1