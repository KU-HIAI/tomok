import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS112025_030303_12(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 20 25 3.3.3 (11)' # 건설기준문서
    ref_date = '2023-09-22'  # 디지털 건설문서 작성일
    doc_date = '2020-12-03'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '되메우기 및 뒤채움'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    되메우기 및 뒤채움
    3. 시공
    3.3 시공기준
    3.3.3 뒤채움 시공기준
    (12)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.3 뒤채움 시공기준
    (12) 보통쌓기 재료는 다져진 두께가 200 mm 이하인 연속층으로 재료를 포설하고 다짐밀도 95% 이상 다져야 한다.


    """

    # 플로우차트(mermaid)
    flowchart = """
   flowchart TD
    subgraph Python_Class
    A["Title: 뒤채움 보통쌓기 재료 시공 기준"];
    B["KCS 11 20 25 3.3.3 (12)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 25 3.3.3 (12)"])

    subgraph Variable_def
    VarOut[/"출력변수: 보통쌓기 재료"/];
    VarIn1[/"입력변수: 재료 포설 두께"/];
    VarIn2[/입력변수: 다짐 밀도/];


    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C["재료 포설 두께<=200 mm"]
		C --> |True|E[다짐 밀도 => 95%]
		C --> |False|F([FAIL])
		E --> |True|G([PASS])
		E --> |False|F([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def backfill_ordinary_stacking_material(fIMatThi, fIComDen) ->str :
        """뒤채움 시공기준_보통쌓기 재료

        Args:
            fIMatThi (float): 재료 포설 두께
            fIComDen (float): 다짐밀도

        Returns:
            sOAggMat (string): 골재쌓기 재료

        """

        if fIMatThi > 200:
            sOAggMat = "FAIL"
            return sOAggMat
        else:
            if fIComDen < 95:
                sOAggMat = "FAIL"
                return sOAggMat
            else:
                sOAggMat = "PASS"
                return sOAggMat