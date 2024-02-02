import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_030202_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 3.2.2 (1)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.2 시공 허용오차
    3.2.2 수직오차
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.2 수직오차
    (1) 높이가 30m 이하인 경우
    ① 선, 면, 그리고 모서리 : 25mm 이하
    ② 노출된 기둥의 모서리, 조절줄눈의 홈 : 13mm 이하
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 수직오차(높이가 30m 이하)"];
    B["KCS 21 50 05 3.2.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.2.2 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 수직오차"/];
		VarIn1[/"입력변수: 측정 대상"/];
		VarIn2[/"입력변수: 높이"/];

    VarOut1  ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{높이 <= 30m}

		D --> K{측정대상}
		K --> |'선, 면, 그리고 모서리'|E[수직오차 <= 25 mm]
		K --> |'노출된 기둥의 모서리, 조절줄눈의 홈'|F[수직오차 <= 13 mm]


		E --> G([수직오차])
		F --> G([수직오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def vertical_error_height_less_than_30(sIMeaSub, fIHei) -> str:

        """수직오차(높이가 30m 이하)

        Args:
            sIMeaSub (string): 측정 대상
            fIHei (float): 높이

        Returns:
            fOVerTol (float): 수직오차
        """
        if fIHei <=30:
            if sIMeaSub == "선" or sIMeaSub == "면" or sIMeaSub ==  "모서리":
                fOVerTol = 25
            elif sIMeaSub == "노출된 기둥의 모서리" or sIMeaSub == "조절줄눈의 홈":
                fOVerTol = 13
        return fOVerTol