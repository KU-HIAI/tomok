import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_030501_09(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 3.5.1 (9)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
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
    VarOut1[/"출력변수: 수평재와 수평재 사이 수직재의 연결부위 개수"/];


		VarIn1[/"입력변수: 수평재와 수평재 사이 수직재의 연결부위 개수"/];


    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{수평재와 수평재 사이 수직재의 연결부위 개수 < 2}


		D --> |True|G([PASS])
		D --> |False|H([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  prefabricated_shoring_system_installation(nINumVer) -> str:
        """수평재와 수평재 사이 수직재 연결부위 개수

        Args:
            nINumVer (integer): 수평재와 수평재 사이 수직재의 연결부위 개수

        Returns:
            sONumVer (string): 수평재와 수평재 사이 수직재의 연결부위 개수
        """

        if nINumVer >= 2:
            sONumVer = "FAIL"
        else:
            sONumVer = "PASS"
        return sONumVer


