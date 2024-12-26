import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143125_0303_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 31 25 3.3 (4)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.3 핀 및 롤러
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3 핀 및 롤러
    (4) 핀과 핀구멍의 차이는 핀지름 130 mm 미만에 대해서는 0.5 mm, 핀지름 130 mm 이상의 것에 대해서는 1 mm를 표준으로 한다.


    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 핀과 핀 구멍의 차이];
    B["KCS 14 31 25 3.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.3"])

    subgraph Variable_def
    VarIn1[/입력변수: 핀지름/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{핀지름 < 130 mm}
    C --> |True|D["0.05 mm"]
    C --> |False|E["1 mm"]
    D --> F([핀과 핀 구멍의 차이])
    E --> F([핀과 핀 구멍의 차이])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def difference_between_pin_and_pin_hole(fIPinDia) -> RuleUnitResult:
        """볼트의 조임 축력

        Args:
            fIPinDia (float): 핀지름

        Returns:
            fODifPin (float): 핀과 핀 구멍의 차이


        """
        assert isinstance(fIPinDia, float)

        if fIPinDia < 130:
            fODifPin = 0.5
            return RuleUnitResult(
                result_variables = {
                    "fODifPin": fODifPin
                }
            )
        else:
            fODifPin = 1
            return RuleUnitResult(
                result_variables = {
                    "fODifPin": fODifPin
                }
            )