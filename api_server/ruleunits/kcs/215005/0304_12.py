import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_0304_12(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.4 (12)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.4 동바리
    (12)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.4 동바리
    (12) 동바리 설치높이가 4.0m를 초과하거나 콘크리트 타설 두께가 1.0m를 초과하여 파이프 서포트로 설치가 어려울 경우에는 시스템 동바리 또는 안전성을 확보할 수 있는 지지구조로 설치할 수 있다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 시스템 동바리의 설치"];
    B["KCS 21 50 05 3.4 (12)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.4 (12)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 설치 방식"/];
		VarIn1[/"입력변수: 동바리 설치높이"/];
		VarIn2[/"입력변수: 콘크리트 타설 두께"/];


    VarOut1  ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{동바리 설치높이 \n or 콘크리트 타설 두께}


		D --> |동바리 설치높이 > 4.0m|E["시스템 동바리 또는 안전성을 확보할 수 있는 지지구조로 설치"]
		D --> |콘크리트 타설 두께 > 1.0m|F["시스템 동바리 또는 안전성을 확보할 수 있는 지지구조로 설치"]

		E --> G([설치 방식])
		F --> G([설치 방식])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  prefabricated_shoring_system_installation(fIHeiSho, fIPlaThi) -> RuleUnitResult:
        """시스템 동바리의 설치

        Args:
            fIHeiSho (float): 동바리 설치높이
            fIPlaThi (float): 콘크리트 타설 두께

        Returns:
            sOInsMet (str): 설치 방식
        """
        assert isinstance(fIHeiSho, float)
        assert isinstance(fIPlaThi, float)

        if fIHeiSho > 4.0:
            sOInsMet = "시스템 동바리 또는 안전성을 확보할 수 있는 지지구조로 설치할 수 있다."
            return RuleUnitResult(
                result_variables = {
                    "sOInsMet": sOInsMet
                }
            )
        elif fIPlaThi > 1.0:
            sOInsMet = "시스템 동바리 또는 안전성을 확보할 수 있는 지지구조로 설치할 수 있다."
            return RuleUnitResult(
                result_variables = {
                    "sOInsMet": sOInsMet
                }
            )
        else:
            assert 1 != 1