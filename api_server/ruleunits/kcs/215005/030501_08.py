import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030501_08(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.5.1 (8)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.5 시스템 동바리
    3.5.1 지주 형식 동바리
    (8)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.5.1 지주 형식 동바리
    (8) 콘크리트 두께가 0.5m 이상일 경우에는 시스템 동바리 수직재 상단과 하단의 경계조건 및 U헤드와 조절형 받침철물의 나사부 유격에 의한 수직재 좌굴하중의 감소를 방지하기 위하여, U헤드 밑면으로부터 최상단 수평재 윗면, 조절형 받침철물 윗면으로부터 최하단 수평재 밑면까지의 순간격이 400mm 이내가 되도록 설치하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 수평재까지의 순간격"];
    B["KCS 21 50 05 3.5.1 (8)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.5.1 (8)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 콘크리트 두께"/];
		VarIn2[/"입력변수: U헤드 밑면과 최상단 수평재 윗면의 순간격"/];
		VarIn3[/"입력변수: 조절형 받침철물 윗면과 최하단 수평재 밑면의 순간격"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{콘크리트 두께> 0.5m}


		D --> E{"U헤드 밑면과 최상단 수평재 윗면의 순간격 < 400mm"}
    D --> F{"조절형 받침철물 윗면과 최하단 수평재 밑면의 순간격 < 400mm"}

		E --> G([Pass or Fail])
		F --> G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  spacing_to_horizontal_beam(fIThiCon, fIDisUhe, fIDisAdj) -> RuleUnitResult:
        """수평재까지의 순간격

        Args:
            fIThiCon (float): 콘크리트 두께
            fIDisUhe (float): U헤드 밑면과 최상단 수평재 윗면의 순간격
            fIDisAdj (float): 조절형 받침철물 윗면과 최하단 수평재 밑면의 순간격

        Returns:
            pass_fail_1 (bool): 거푸집 및 동바리공사 일반사항 3.5.1 지주 형식 동바리 (8)의 U헤드 밑면과 최상단 수평재 윗면의 순간격의 판단 결과
            pass_fail_2 (bool): 거푸집 및 동바리공사 일반사항 3.5.1 지주 형식 동바리 (8)의 조절형 받침철물 윗면과 최하단 수평재 밑면의 순간격의 판단 결과
        """
        assert isinstance(fIThiCon, float)
        assert isinstance(fIDisUhe, float)
        assert isinstance(fIDisAdj, float)
        if fIThiCon >= 0.5:
            if fIDisUhe <= 400:
                pass_fail_1 = True
                if fIDisAdj <= 400:
                    pass_fail_2 = True
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail_1": pass_fail_1,
                            "pass_fail_2": pass_fail_2
                        }
                    )
                else:
                    pass_fail_2 = False
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail_1": pass_fail_1,
                            "pass_fail_2": pass_fail_2
                        }
                    )
            else:
                pass_fail_1 = False
                if fIDisAdj <= 400:
                    pass_fail_2 = True
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail_1": pass_fail_1,
                            "pass_fail_2": pass_fail_2
                        }
                    )
                else:
                    pass_fail_2 = False
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail_1": pass_fail_1,
                            "pass_fail_2": pass_fail_2
                        }
                    )
        else:
            assert 1 != 1