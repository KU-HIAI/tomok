import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_0306_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 3.6 (2)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.6 가새재
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.6 가새재
    (2) 단일부재 가새재 사용이 가능할 경우 기울기는 60°이내로 사용하는 것을 원칙으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 단윌부재 가새재의 기울기"];
    B["KCS 21 50 05 3.6 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.6 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 가새재의 기울기"/];


		VarIn1[/"입력변수: 가새재의 기울기"/];


    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"가새재의 기울기 < 60°"}


		D --> |True|G([PASS])
		D --> |False|H([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  slope_of_cantilever_beam_to_supporting_beam(fISloBra) -> str:
        """단윌부재 가새재의 기울기

        Args:
            fISloBra (float): 가새재의 기울기

        Returns:
            sOSloBra (string): 가새재의 기울기
        """

        if fISloBra <= 60:
            sOSloBra = "PASS"
        else:
            sOSloBra = "FAIL"
        return sOSloBra


