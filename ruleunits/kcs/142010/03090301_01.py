import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_03090301_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 3.9.3.1 (1)' # 건설기준문서
    ref_date = '2023-10-05'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    3. 시공
    3.9 설비 및 장비
    3.9.3 혼합설비
    3.9.3.1 믹서
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.9.3.1 믹서
    (1) 믹서는 고정식 믹서를 원칙으로 하며, KS F 2455에 의해 혼합 성능시험을 실시하여 아래에 제시한 규정을 만족하면 소요의 혼합 성능을 가지고 있는 것으로 한다.
    ① 콘크리트 중 모르타르의 단위질량의 차는 0.8% 이하일 것
    ② 콘크리트 중 단위굵은골재량의 차는 5% 이하일 것
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 믹서의 혼합성능"];
    B["KCS 14 31 30 3.9.3.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.9.3.1 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 콘크리트 중 모르타르의 단위질량의 차"/];
    VarOut2[/"출력변수: 콘크리트 중 단위굵은골재량의 차"/];

		VarIn1[/"입력변수: 콘크리트 중 모르타르의 단위질량의 차"/];
		VarIn2[/"입력변수: 콘크리트 중 단위굵은골재량의 차"/];


    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"콘크리트 중 \n모르타르의 단위질량의 차 < 0.8%"}
    Variable_def --> G{"콘크리트 중 \n단위굵은골재량의 차 < 5%"}

		D --> |True|E([PASS])
		D --> |False|F([FAIL])

		G --> |True|E([PASS])
		G --> |False|F([FAIL])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def mixer_blending_capability(fIDifMor, fIDifCoa) -> str:
        """믹서의 혼합성능

        Args:
            fIDifMor (float): 콘크리트 중 모르타르의 단위질량의 차
            fIDifCoa (float): 콘크리트 중 단위굵은골재량의 차

        Returns:
            sODifMor (string): 콘크리트 중 모르타르의 단위질량의 차
            sODifCoa (string): 콘크리트 중 단위굵은골재량의 차
        """

        if fIDifMor <= 0.8:
            sODifMor = "PASS"
            if fIDifCoa <= 5:
                sODifCoa = "PASS"
            else:
                sODifCoa = "FAIL"

        else:
            sODifMor = "FAIL"
            if fIDifCoa <= 5:
                sODifCoa = "PASS"
            else:
                sODifCoa = "FAIL"
        return sODifMor, sODifCoa