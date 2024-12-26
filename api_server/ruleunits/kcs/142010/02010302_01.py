import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_02010302_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.3.2 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 잔골재
    2.1.3.2 물리적 품질
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.3.2 물리적 품질
    (1) 잔골재의 절대건조밀도는 2.5g/㎤ 이상, 흡수율은 3.0% 이하의 값을 표준으로 한다. 다만, 잔골재의 종류에 따라 물리적 품질이 다르기 때문에 KS F 2527에서 정한 규정에 따른다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 잔골재의 물리적 품질"];
    B["KCS 14 31 30 2.1.3.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.3.2 (1)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 잔골재의 절대건조밀도"/];
		VarIn2[/"입력변수: 잔골재의 흡수율"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"잔골재의 절대건조밀도 => 2.5g/c㎥ \n잔골재의 흡수율 <= 3.0%"}


		C --> F([PASS or Fail])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def physical_quality_of_aggregates(fIAbsDry, fIAbsRat) -> RuleUnitResult:
        """잔골재의 물리적 품질

        Args:
            fIAbsDry (float): 잔골재의 절대건조밀도
            fIAbsRat (float): 잔골재의 흡수율

        Returns:
            pass_fail_1 (bool): 일반콘크리트 2.1.3.2 물리적 품질 (1)의 절대건조밀도 판단 결과
            pass_fail_2 (bool): 일반콘크리트 2.1.3.2 물리적 품질 (1)의 흡수율 판단 결과
        """
        assert isinstance(fIAbsDry, float)
        assert isinstance(fIAbsRat, float)

        if fIAbsDry >= 2.5:
            pass_fail_1 = True
            if fIAbsRat <= 3.0:
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
            if fIAbsRat <= 3.0:
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