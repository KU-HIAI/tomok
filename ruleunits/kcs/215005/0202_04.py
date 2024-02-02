import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_0202_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 2.2 (4)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    2. 자재
    2.2 거푸집
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2 거푸집
    (4) 목재는 구조용 목재를 사용하여야 하며, 옹이 지름비는 40％ 이하, 모인 옹이의 지름비는 60％ 이하인 목재를 사용하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 거푸집 목재 옹이 지름비"];
    B["KCS 21 50 05 2.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 2.2 (4)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 옹이 지름비"/];
    VarOut2[/"출력변수: 모인 옹이 지름비"/];
		VarIn1[/"입력변수: 옹이 지름비"/];
		VarIn2[/"입력변수: 모인 옹이 지름비"/];

    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"옹이 지름비 or \n 모인 옹이 지름비"}

		D --> |옹이 지름비|E[옹이 지름비 <= 40% ]
		D --> |모인 옹이 지름비|F[모인 옹이 지름비 <= 60%]


		E --> |True|G([PASS])
		E --> |False|H([FAIL])

		F --> |True|G([PASS])
		F --> |False|H([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def form_knot_diameter_ratio(fIKnoRat, fIConRat) -> str:
        """거푸집 목재 옹이 지름비

        Args:
            fIKnoRat (float): 옹이 지름비
            fIConRat (float): 모인 옹이 지름비

        Returns:
            sOKnoRat (string): 옹이 지름비
            sOConRat (string): 모인 옹이 지름비
        """

        if fIKnoRat <= 40:
            sOKnoRat = "PASS"
            if fIConRat <= 60:
                sOConRat = "PASS"
            else:
                sOConRat = "FAIL"

        else:
            sOKnoRat = "FAIL"
            if fIConRat <= 60:
                sOConRat = "PASS"
            else:
                sOConRat = "FAIL"
        return "옹이 지름비: " + sOKnoRat,"모인 옹이 지름비: " + sOConRat