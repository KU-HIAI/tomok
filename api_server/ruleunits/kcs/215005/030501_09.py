import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS215005_030501_09(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 21 50 05 3.5.1 (9)' # 건설기준문서
    ref_date = '2023-01-31'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.5 시스템 동바리
    3.5.1 지주 형식 동바리
    (9)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.5.1 지주 형식 동바리
    (9) 수직재를 설치할 때에는 수평재와 수평재 사이에 수직재의 연결부위가 2개소 이상 되지 않도록 하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 수평재와 수평재 사이 수직재 연결부위 개수"];
    B["KCS 21 50 05 3.5.1 (9)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.5.1 (9)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 수평재와 수평재 사이 수직재의 연결부위 개수"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{수평재와 수평재 사이 수직재의 연결부위 개수 < 2}


		D --> G([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  prefabricated_shoring_system_installation(nINumVer) -> RuleUnitResult:
        """수평재와 수평재 사이 수직재 연결부위 개수

        Args:
            nINumVer (int): 수평재와 수평재 사이 수직재의 연결부위 개수

        Returns:
            pass_fail (bool): 거푸집 및 동사리공사 일반사항 3.5.1 지주 형식 동바리 (9)의 판단 결과
        """
        assert isinstance(nINumVer, int)

        if nINumVer >= 2:
            pass_fail = False
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )
        else:
            pass_fail = True
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )