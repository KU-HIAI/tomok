import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115010_010502_04(RuleUnit): # 허윤아 박사님에게 확인받기 KDS241431_040303_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 50 10 1.5.2 (4)' # 건설기준문서
    ref_date = '2023-09-06'  # 디지털 건설문서 작성일
    doc_date = '2021-05-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '현장타설 콘크리트 말뚝'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    현장타설 콘크리트 말뚝
    1. 일반사항
    1.5 일반요건
    1.5.2 허용오차
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 1.5.2 허용오차
    (4) 바닥표고 변동: ±50 ㎜ 미만
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 바닥표고 변동 허용오차"];
    B["KCS 11 50 10 1.5.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 10 1.5.2 (4)"])

    subgraph Variable_def
    VarOut[/"출력변수: 바닥표고 변동"/];
		VarIn1[/"입력변수: 바닥표고 변동"/];

    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{" -50 mm < 바닥표고 변동 < +50 mm"}
		D --> |True|E([PASS])
		D --> |False|F([FAIL])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def tolerance_of_fluctuation_in_floor_elevation(fIFluFlo) ->str :
        """바닥표고 변동

        Args:
            fIFluFlo (float): 바닥표고 변동. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당

        Returns:
            sIFluFlo (string) : 바닥표고 변동
        """

        if -50 < fIFluFlo < 50:
            sIFluFlo = "PASS"
            return sIFluFlo
        else:
            sIFluFlo = "FAIL"
            return sIFluFlo