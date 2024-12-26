import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143125_030104_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.4 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.4 볼트구멍의 어긋남 수정
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.4 볼트구멍의 어긋남 수정
    (1) 접합부 조립 시에는 겹쳐진 판 사이에 생긴 2 mm 이하의 볼트구멍의 어긋남은 리머로써 수정해도 된다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 볼트구멍의 어긋남 수정 방법];
    B["KCS 14 31 25 3.1.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.4 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 볼트구멍의 어긋남 수정 방법/];
    VarIn1[/입력변수: 볼트구멍의 어긋남/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"접합부 조립 시 \n 볼트구멍의 어긋남 ≤ 2mm"}
    C --> |True|D["리머로써 수정해도 된다."]

		D --> End([볼트구멍의 어긋남 수정 방법])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def method_to_fix_misaligned_bolt_holes(fIMisBol) -> RuleUnitResult:
        """볼트구멍의 어긋남 수정 방법
        Args:
            fIMisBol (float): 볼트구멍의 어긋남

        Returns:
            sOMetCor (str):볼트구멍의 어긋남 수정 방법
        """
        assert isinstance(fIMisBol, float)

        if fIMisBol <= 2:
            sOMetCor = "리머로써 수정해도 된다."
            return RuleUnitResult(
                result_variables = {
                    "sOMetCor": sOMetCor
                }
            )
        else:
            assert 1 != 1