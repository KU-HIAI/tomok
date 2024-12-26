import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_03090301_01_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 3.9.3.1 (1) ①' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명


    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    3. 시공
    3.9 설비 및 장비
    3.9.3 혼합설비
    3.9.3.1 믹서
    (1)
    ①
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.9.3.1 믹서
    (1) 믹서는 고정식 믹서를 원칙으로 하며, KS F 2455에 의해 혼합 성능시험을 실시하여 아래에 제시한 규정을 만족하면 소요의 혼합 성능을 가지고 있는 것으로 한다.
    ① 콘크리트 중 모르타르의 단위질량의 차는 0.8% 이하일 것
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 믹서의 혼합성능"];
    B["KCS 14 31 30 3.9.3.1 (1) ①"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.9.3.1 (1) ①"])

    subgraph Variable_def
		VarIn1[/"입력변수: 콘크리트 중 모르타르의 단위질량의 차"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"콘크리트 중 \n모르타르의 단위질량의 차 < 0.8%"}

		D --> E([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def mixer_blending_capability(fIDifMor) -> RuleUnitResult:
        """믹서의 혼합성능

        Args:
            fIDifMor (float): 콘크리트 중 모르타르의 단위질량의 차

        Returns:
            pass_fail (bool): 일반콘크리트 3.9.3.1 믹서 (1) ①의 콘크리트 중 모르타르의 단위질량 차이의 판단 결과

                    """
        assert isinstance(fIDifMor, float)

        if fIDifMor <= 0.8:
            pass_fail = True
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    }
            )
        else:
            pass_fail = False
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )