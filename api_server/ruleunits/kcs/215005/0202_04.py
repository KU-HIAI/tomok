import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_0202_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 2.2 (4)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    2. 자재
    2.2 거푸집
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2 거푸집
    (4) 목재는 구조용 목재를 사용하여야 하며, 옹이 지름비는 40％ 이하, 모인 옹이의 지름비는 60％ 이하인 목재를 사용하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 거푸집 목재 옹이 지름비"];
    B["KCS 21 50 05 2.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 2.2 (4)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 옹이 지름비"/];
		VarIn2[/"입력변수: 모인 옹이 지름비"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E{옹이 지름비 <= 40%}
    Variable_def --> F{모인 옹이 지름비 <= 60%}

		E --> G([Pass or Fail])
		F --> G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def form_knot_diameter_ratio(fIKnoRat, fIConRat) -> RuleUnitResult:
        """거푸집 목재 옹이 지름비

        Args:
            fIKnoRat (float): 옹이 지름비
            fIConRat (float): 모인 옹이 지름비

        Returns:
            pass_fail_1 (bool): 거푸집 및 동바리공사 일반사항 2.2 거푸집 (4)의 옹이 지름비 판단 결과
            pass_fail_2 (bool): 거푸집 및 동바리공사 일반사항 2.2 거푸집 (4)의 모인 옹이의 지름비 판단 결과
        """
        assert isinstance(fIKnoRat, float)
        assert isinstance(fIConRat, float)

        if fIKnoRat <= 40:
            pass_fail_1 = True
            if fIConRat <= 60:
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
            if fIConRat <= 60:
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