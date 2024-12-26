import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_010704_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 1.7.4 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
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
		VarIn1[/"입력변수: 레디믹스트 콘크리트의 종류"/];
		VarIn2[/"입력변수: 레디믹스트 콘크리트의 설계 공기량"/];
		VarIn3[/"입력변수: 레디믹스트 콘크리트의 시공 공기량"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{레디믹스트 콘크리트의 종류}

		D --> |'보통콘크리트'|F{"레디믹스트 콘크리트의 \n설계 공기량 <= 4.5%"}
		D --> |'경량 콘크리트'|G{"레디믹스트 콘크리트의 \n설계 공기량 <= 5.5%"}
		D --> |'포장콘크리트'|H{"레디믹스트 콘크리트의 \n설계 공기량 <= 4.5%"}
		D --> |'고강도콘크리트'|I{"레디믹스트 콘크리트의 \n설계 공기량 <= 3.5%"}

		F --> J{"레디믹스트 콘크리트의 설계 공기량 \n-1.5 <= 레디믹스트 콘크리트의 시공 공기량 \n<= 레디믹스트 콘크리트의 설계 공기량 +1.5"}
		G --> K{"레디믹스트 콘크리트의 설계 공기량 \n-1.5 <= 레디믹스트 콘크리트의 시공 공기량 \n<= 레디믹스트 콘크리트의 설계 공기량 +1.5"}
		H --> L{"레디믹스트 콘크리트의 설계 공기량 \n-1.5 <= 레디믹스트 콘크리트의 시공 공기량 \n<= 레디믹스트 콘크리트의 설계 공기량 +1.5"}
		I --> M{"레디믹스트 콘크리트의 설계 공기량 \n-1.5 <= 레디믹스트 콘크리트의 시공 공기량 \n<= 레디믹스트 콘크리트의 설계 공기량 +1.5"}

		J --> O([Pass of Fail])
		K --> O
		L --> O
		M --> O

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def air_content_of_ready_mixed_concrete(sIReaCon, fIDesAir, fIConAir) -> RuleUnitResult:
        """레디믹스트 콘크리트의 공기량

        Args:
            sIReaCon (str): 레디믹스트 콘크리트의 종류
            fIDesAir (float): 레디믹스트 콘크리트의 설계 공기량
            fIConAir (float): 레디믹스트 콘크리트의 시공 공기량

        Returns:
            pass_fail (bool): 일반콘크리트 1.7.4 공기량 (1)의 판단 결과
        """
        assert isinstance(sIReaCon, str)
        assert isinstance(fIDesAir, float)
        assert isinstance(fIConAir, float)
        assert sIReaCon in ["보통콘크리트", "경량콘크리트", "포장콘크리트", "고강도콘크리트"]

        if sIReaCon == "보통콘크리트":
            if fIDesAir <= 4.5:
                if fIDesAir -1.5 <= fIConAir <= fIDesAir +1.5:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": False
                    }
                )
        elif sIReaCon == "경량콘크리트":
            if fIDesAir <= 5.5:
                if fIDesAir -1.5 <= fIConAir <= fIDesAir +1.5:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": False
                    }
                )
        elif sIReaCon == "포장콘크리트":
            if fIDesAir <= 4.5:
                if fIDesAir -1.5 <= fIConAir <= fIDesAir +1.5:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": False
                    }
                )
        elif sIReaCon == "고강도콘크리트":
            if fIDesAir <= 3.5:
                if fIDesAir -1.5 <= fIConAir <= fIDesAir +1.5:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": False
                    }
                )