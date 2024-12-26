import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030202_02_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.2 (2) ②' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.2 수직오차
    (2)
    ②
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.2 수직오차
    (2) 높이가 30m 초과인 경우
    ② 노출된 기둥의 모서리, 조절줄눈의 홈 : 높이의 1/2000 이하. 다만, 75mm 이하
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 수직오차(높이가 30m 초과)"];
    B["KCS 21 50 05 3.2.2 (2) ②"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.2 (2) ②"])

    subgraph Variable_def
    VarOut1[/"출력변수: 수직오차"/];
		VarIn1[/"입력변수: 측정 대상"/];
		VarIn2[/"입력변수: 높이"/];

    VarOut1  ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{높이> 30m}

		D --> K{측정대상}
		K --> |노출된 기둥의 모서리, 조절줄눈의 홈|F["수직오차 <= \n min(높이*(1/2000), 75mm)"]


		F --> G([수직오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def vertical_error_height_exceeding_30(sIMeaSub, fIHei) -> RuleUnitResult:
        """수직오차(높이가 30m 초과)

        Args:
            sIMeaSub (str): 측정 대상
            fIHei (float): 높이

        Returns:
            fOVerTol (float): 수직오차
        """
        assert isinstance(sIMeaSub, str)
        assert isinstance(fIHei, float)

        if fIHei > 30:
            if sIMeaSub == "노출된 기둥의 모서리" or sIMeaSub == "조절줄눈의 홈":
                fOVerTol = min((fIHei)*1000/2000, 75)
                return RuleUnitResult(
                    result_variables = {
                        "fOVerTol": fOVerTol
                    }
                )
            else:
                assert 1 != 1
        else:
            assert 1 != 1