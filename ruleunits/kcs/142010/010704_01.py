import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_010704_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 1.7.4 (1)' # 건설기준문서
    ref_date = '2023-09-25'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    1. 일반사항
    1.7 레디믹스트 콘크리트 품질에 대한 지정
    1.7.4 공기량
    (1)

    """

    # 건설기준문서내용(text)
    content = """
    #### 1.7.4 공기량
    (1) 공기량은 보통콘크리트의 경우 4.5%, 경량 콘크리트의 경우 5.5%, 포장콘크리트 4.5%, 고강도콘크리트 3.5% 이하로 하되, 그 허용오차는 ±1.5%로 한다.

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 레디믹스트 콘크리트의 공기량"];
    B["KCS 14 31 30 1.7.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 1.7.4 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 레디믹스트 콘크리트의 공기량"/];
    VarOut2[/"출력변수: 레디믹스트 콘크리트의 공기량 허용 오차"/];

		VarIn1[/"입력변수: 레디믹스트 콘크리트의 종류"/];


    VarOut1 & VarOut2 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{레디믹스트 콘크리트의 종류}

		D --> |'보통콘크리트'|F["공기량 <= 4.5%"]
		D --> |'경량 콘크리트'|G["공기량 <= 5.5%"]
		D --> |'포장콘크리트'|H["공기량 <= 4.5%"]
		D --> |'고강도콘크리트'|I["공기량 <= 3.5%"]

		D --> |'보통콘크리트'|J["허용 오차 = ± 1.5%"]
		D --> |'경량 콘크리트'|K["허용 오차 = ± 1.5%"]
		D --> |'포장콘크리트'|L["허용 오차 = ± 1.5%"]
		D --> |'고강도콘크리트'|M["허용 오차 = ± 1.5%"]

		F --> N([레디믹스트 콘크리트의 공기량])
		G --> N([레디믹스트 콘크리트의 공기량])
		H --> N([레디믹스트 콘크리트의 공기량])
		I --> N([레디믹스트 콘크리트의 공기량])

		J --> O([레디믹스트 콘크리트의 공기량 허용 오차])
		K --> O([레디믹스트 콘크리트의 공기량 허용 오차])
		L --> O([레디믹스트 콘크리트의 공기량 허용 오차])
		M --> O([레디믹스트 콘크리트의 공기량 허용 오차])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def air_content_of_ready_mixed_concrete(sIRdmCon) ->str :
        """레디믹스트 콘크리트의 공기량

        Args:
            sIRdmCon (string): 레디믹스트 콘크리트의 종류

        Returns:
            sOAirCon (string): 레디믹스트 콘크리트의 공기량
            sOAirTol (string): 레디믹스트 콘크리트의 공기량 허용 오차

        """

        if sIRdmCon == "보통콘크리트":
            sOAirCon = "4.5 % 이하"
            sOAirTol = "±1.5 %"
            return sOAirCon, sOAirTol
        elif sIRdmCon == "경량콘크리트":
            sOAirCon = "5.5 % 이하"
            sOAirTol = "±1.5 %"
            return sOAirCon, sOAirTol
        elif sIRdmCon == "포장콘크리트":
            sOAirCon = "4.5 % 이하"
            sOAirTol = "±1.5 %"
            return sOAirCon, sOAirTol
        elif sIRdmCon == "고강도콘크리트":
            sOAirCon = "3.5 % 이하"
            sOAirTol = "±1.5 %"
            return sOAirCon, sOAirTol