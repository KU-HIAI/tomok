import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030205_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.5 (1)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.5 단면치수의 허용오차
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.5 단면치수의 허용오차
    (1) 기둥, 보, 교각, 벽체 및 슬래브(두께만 적용)
    ① 단면치수가 300mm 미만 : ＋9mm, －6mm
    ② 단면치수가 300mm 이상 ~ 900mm 미만 : ＋13mm, －9mm
    ③ 단면치수가 900mm 이상 : ＋25mm, －19mm
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 단면치수의 허용오차"];
    B["KCS 21 50 05 3.2.5 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.5 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 단면치수의 허용오차"/];
		VarIn1[/"입력변수: 단면치수"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{단면치수}


		D --> |단면치수 < 300mm|E["+9mm, -6mm"]
		D --> |300mm <= 단면치수 < 900mm|F["+13mm, -9mm"]
		D --> |단면치수 => 900mm|G["+25mm, -19mm"]

		E --> K([단면치수의 허용오차])
		F --> K([단면치수의 허용오차])
		G --> K([단면치수의 허용오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def tolerance_for_cross_sectional_dimensions(fICroDim) -> RuleUnitResult:
        """단면치수의 허용오차

        Args:
            fICroDim (float): 단면치수

        Returns:
            sOTolCro (str): 단면치수의 허용오차
        """
        assert isinstance(fICroDim, float)

        if fICroDim < 300:
            sOTolCro = "+9mm, -6mm"
            return RuleUnitResult(
                result_variables = {
                    "sOTolCro": sOTolCro
                }
            )
        elif 300 <= fICroDim < 900:
            sOTolCro = "+13mm, -9mm"
            return RuleUnitResult(
                result_variables = {
                    "sOTolCro": sOTolCro
                }
            )
        elif fICroDim >= 900:
            sOTolCro = "+25mm, -19mm"
            return RuleUnitResult(
                result_variables = {
                    "sOTolCro": sOTolCro
                }
            )