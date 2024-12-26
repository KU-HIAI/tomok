import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030204_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.4 (3)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.4 표고오차
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.4 표고오차
    (3) 인방보, 창대, 파라펫, 수평 홈 그리고 현저히 눈에 띄는 선 : 13mm 이하
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 표고오차"];
    B["KCS 21 50 05 3.2.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.4 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 표고오차"/];
		VarIn1[/"입력변수: 측정 대상"/];

    VarOut1  ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{측정대상}


		D --> |"인방보 or 창대 or 파라펫 or 수평 홈 \n or 현저히 눈에 띄는 선"|E["표고오차 <= \n 13mm"]

		E --> G([표고오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def elevation_error(sIMeaSub) -> RuleUnitResult:
        """표고오차

        Args:
            sIMeaSub (str): 측정 대상

        Returns:
            fOEleTol (float): 표고오차
        """
        assert isinstance(sIMeaSub, str)

        if sIMeaSub == "인방보" or sIMeaSub == "창대" or sIMeaSub == "파라펫" or sIMeaSub == "수평 홈" or sIMeaSub == "현저히 눈에 띄는 선":
            fOEleTol = 13
            return RuleUnitResult(
                result_variables = {
                    "fOEleTol": fOEleTol
                }
            )
        else:
            assert 1 != 1