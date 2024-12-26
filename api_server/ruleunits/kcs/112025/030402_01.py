import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS112025_030402_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 11 20 25 3.4.2 (1)' # 건설기준문서
    ref_date = '2020-12-03'  # 고시일
    doc_date = '2024-02-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '되메우기 및 뒤채움'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    되메우기 및 뒤채움
    3. 시공
    3.4 현장 품질관리
    3.4.2 수급인의 자체검사 및 시험
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.4.2 수급인의 자체검사 및 시험
    (1) 밀도시험은 KS F 2311과 수급인의 품질관리계획에 정한 빈도에 따라 시험하고, 명시된 요건을 만족하는지 확인하여야 하며, 정하여진 빈도가 없는 경우 다음을 따라야 한다.
    ① 넓은 수평구역: 되메우기 또는 뒤채움의 100㎡마다 1회
    ② 한정된 구역과 둑쌓기: 되메우기 또는 뒤채움의 3층마다 1회


    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 밀도시험 빈도"];
    B["KCS 11 20 25 3.4.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 25 3.4.2 (1)"])

    subgraph Variable_def
    VarIn1[/"입력변수: 정해진 빈도"/];
    VarIn2[/입력변수: 넓은 수평구역/];
    VarIn3[/"입력변수: 한정된 구역"/];
    VarIn4[/입력변수: 둑쌓기/];

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"정해진 빈도가 있는 경우"}
		D --> |True|E["수급인의 품질관리계획에 정한 빈도에 따라 시험"]
		D --> |False|F{구역}
		F --> |넓은 수평구역|G["되메우기 또는 뒤채움이 100㎡ 마다 1회"]
		F --> |한정된 구역과 둑쌓기|H["되메우기 또는 뒤채움의 3층마다 1회"]

		E --> I([밀도시험 빈도])
		G --> I
		H --> I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def density_test_frequency(bISpeFre, bIWidHor, bILimAre, bIEmbCon) -> RuleUnitResult:
        """밀도시험 빈도

        Args:
            bISpeFre (bool): 정해진 빈도
            bIWidHor (bool): 넓은 수평구역
            bILimAre (bool): 한정된 구역
            bIEmbCon (bool): 둑쌓기

        Returns:
            sOTesFre (str): 밀도시험 빈도

        """
        assert isinstance(bISpeFre, bool)
        assert isinstance(bIWidHor, bool)
        assert isinstance(bILimAre, bool)
        assert isinstance(bIEmbCon, bool)

        if bISpeFre == False:
            if bIWidHor == True:
                sOTesFre = "되메우기 또는 뒤채움의 100㎡마다 1회"
                return RuleUnitResult(
                    result_variables = {
                        "sOTesFre" : sOTesFre
                    }
                )
            elif (bILimAre == True) or (bIEmbCon == True):
                sOTesFre = "되메우기 또는 뒤채움의 3층마다 1회"
                return RuleUnitResult(
                    result_variables = {
                        "sOTesFre" : sOTesFre
                    }
                )
            else:
                assert 1 != 1
        elif bISpeFre == True:
            sOTesFre = "수급인의 품질관리계획에 정한 빈도에 따라 시험"
            return RuleUnitResult(
                result_variables = {
                    "sOTesFre" : sOTesFre
                }
            )