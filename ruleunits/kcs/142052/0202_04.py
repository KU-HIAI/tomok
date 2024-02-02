import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142052_0202_04(RuleUnit): # 허윤아 박사님에게 확인받기 KDS241431_040303_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 52 2.2 (4)' # 건설기준문서
    ref_date = '2023-08-16'  # 디지털 건설문서 작성일
    doc_date = '2021-02-18'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '콘크리트의 배합'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리캐스트 콘크리트
    2. 자재
    2.2 배합
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2 배합
    (4) 슬럼프가 20 mm 이상인 콘크리트의 배합은 슬럼프 시험을 원칙으로 하며, 슬럼프 20 mm 미만인 콘크리트의 배합은 제조 방법에 적합한 시험 방법에 의한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트의 배합];
    B["KCS 14 20 52 2.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 52 2.2"])

    subgraph Variable_def
    VarOut[/출력변수: 콘크리트의 배합/];
    VarIn1[/입력변수: 슬럼프/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{슬럼프 => 20 mm}
    C --> |True|D["슬럼프 시험"]
    C --> |False|E["제조 방법에 적합한 시험 방법"]
    D --> F(["콘크리트의 배합"])
    E --> F(["콘크리트의 배합"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def concrete_mix(fISlu) ->str :
        """슬럼프에 따른 콘크리트 배합 시험 방법

        Args:
            fISlu (float): 슬럼프. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당

        Returns:
            sOConMix (string) : 프리캐스트 콘크리트 2.2 배합
        """

        if fISlu >= 20:
            sOConMix = "슬럼프 시험"
            return sOConMix
        else:
            sOConMix = "제조 방법에 적합한 시험 방법"
            return sOConMix