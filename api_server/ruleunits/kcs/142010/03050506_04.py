import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_03050506_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 3.5.5.6 (4)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    3. 시공
    3.5 현장 품질관리
    3.5.5 콘크리트 구조물 검사
    3.5.5.6 현장에서 양생한 공시체의 제작, 시험 및 강도 결과
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.5.5.6 현장에서 양생한 공시체의 제작, 시험 및 강도 결과
    (4) 구조물의 콘크리트 강도를 확인하기 위해 지정된 시험 재령일에 실시한 현장 양생된 공시체 강도가 동일 조건의 시험실에서 양생된 공시체 강도의 85%보다 작을 때는 콘크리트의 양생과 보호절차를 개선하여야 한다. 만일 현장 양생된 것의 강도가 설계기준압축강도보다 3.5MPa를 초과하여 상회하면 85 %의 한계조항은 무시할 수 있다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 양생 및 보호절차 개선 여부];
    B["KCS 14 20 10 3.5.5.6 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 10 3.5.5.6 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 현장 양생 공시체 강도/];
    VarIn2[/입력변수: 시험실 양생 공시체 강도/];
    VarIn3[/입력변수: 설계기준압축강도/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"현장 양생 공시체 강도 < \n 시험실 양생 공시체 강도* 0.85"}
    C --> |True|D{"현장 양생 공시체 강도 > \n 설계기준압축강도 + 3.5MPa"}
    C --> |False|E["양생 및 보호절차 개선해야 함"]

    D -->  |True|G["한계조항을 무시할 수 있음"]
    D -->  |False|H["한계조항을 무시할 수 있음"]

		G & H & E --> End(["양생 및 보호절차 개선 여부"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def curing_and_protection_procedures(fIFieStr, fILabStr, fISpeStr) -> RuleUnitResult:
        """양생 및 보호절차 개선 여부

        Args:
            fIFieStr (float): 현장 양생 공시체 강도
            fILabStr (float): 시험실 양생 공시체 강도
            fISpeStr (float): 설계기준압축강도

        Returns:
            sOImpCur (str): 양생 및 보호절차 개선
        """
        assert isinstance(fIFieStr, float)
        assert isinstance(fILabStr, float)
        assert isinstance(fISpeStr, float)

        if fIFieStr < 0.85*(fILabStr):
            if fIFieStr > fISpeStr + 3.5:
                sOImpCur = "한계조항을 무시할 수 있음"
                return RuleUnitResult(
                    result_variables = {
                        "sOImpCur": sOImpCur
                    }
                )
            else:
                sOImpCur = "양생 및 보호절차를 개선해야 함"
                return RuleUnitResult(
                    result_variables = {
                        "sOImpCur": sOImpCur
                    }
                )
        else:
            sOImpCur = "한계조항을 무시할 수 있음"
            return RuleUnitResult(
                result_variables = {
                    "sOImpCur": sOImpCur
                }
            )