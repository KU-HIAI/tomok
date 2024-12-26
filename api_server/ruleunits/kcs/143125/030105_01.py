import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143125_030105_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.5 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.5 볼트조임
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.5 볼트조임
    (1) 볼트조임에 관한 일반사항
    ④ 와셔는 볼트머리와 너트에 평행하게 놓아야 한다. 볼트가 볼트축에 직각인 평면과 1/20보다 큰 경사를 갖는 경사면이나 원형면 위에 사용될 경우에는 볼트머리나 너트가 완전히 지지되도록 경사진 와셔나 원형 와셔를 갖추어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 볼트조임에 따른 와셔 타입];
    B["KCS 14 31 25 3.1.5 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.5 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 볼트축에 직각인 평면의 경사도/];
    VarIn2[/입력변수: 볼트가 사용될 경사면 또는 원형면의 경사도/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"볼트축에 직각인 평면의 경사도 +1/20\n <볼트가 사용될 경사면 또는 원형면의 경사도"}
    C --> |True|D["볼트머리나 너트가 완전히 지지되도록 경사진 와셔나 원형 와셔를 갖추어야 한다."]

		D --> End([와셔 타입])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def washer_types_based_on_gradient_of_surface(fIPlaPer, fIBolUse) -> RuleUnitResult:
        """경사면 또는 원형면의 경사도에 따른 와셔 타입
        Args:
            fIPlaPer (float): 볼트축에 직각인 평면의 경사도
            fIBolUse (float): 볼트가 사용될 경사면 또는 원형면의 경사도

        Returns:
            sOWasTyp (str): 와셔 타입
        """
        assert isinstance(fIPlaPer, float)
        assert isinstance(fIBolUse, float)

        if fIPlaPer + 1/20 < fIBolUse:
            sOWasTyp = "볼트머리나 너트가 완전히 지지되도록 경사진 와셔나 원형 와셔를 갖추어야 한다."
            return RuleUnitResult(
                result_variables = {
                    "sOWasTyp": sOWasTyp
                }
            )
        else:
            assert 1 != 1