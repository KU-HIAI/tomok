import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143130_030302_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 30 3.3.2 (1)' # 건설기준문서
    ref_date = '2023-11-29'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '조립 및 설치'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    조립 및 설치
    3. 시공
    3.3 부재조립 및 설치
    3.3.2 건축물의 현장 조립
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.2 건축물의 현장 조립
    (1) 앵커링(anchoring)
    ⑤ 구조용 앵커볼트를 사용하는 경우 앵커볼트 간의 중심선은 기둥중심선으로부터 3mm이상 벗어나지 않아야 한다. 세우기용 앵커볼트의 경우에는 앵커볼트 간의 중심선이 기둥중심선으로부터 5mm 이상 벗어나지 않아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 앵커볼트의 중심선];
    B["KCS 14 31 30 3.2.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.2.2(1)"])

    subgraph Variable_def
    VarOut[/출력변수: 앵커볼트의 중심선/];
    VarIn1[/입력변수: 앵커볼트 종류/];
    VarIn2[/입력변수: 앵커볼트 간의 중심선/];
    VarIn3[/입력변수: 기둥 중심선/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"앵커볼트 종류"}
    C --> |구조용 앵커볼트|D{"|기둥 중심선-앵커볼트 간의 중심선|\n < 3mm"}
    C --> |세우기용 앵커볼트|E{"|기둥 중심선-앵커볼트 간의 중심선|\n < 5mm"}

    D -->  |True|F(["PASS"])
    E -->  |True|G(["PASS"])

    D -->  |False|H(["FAIL"])
    E -->  |False|I(["FAIL"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def centerline_of_anchor_bolt(fICenCol, fICenAnc, sIAncTyp) ->str :
        """앵커볼트의 중심선
        Args:
            fICenCol (float): 기둥 중심선
            fICenAnc (float): 앵커볼트 간의 중심선
            sIAncTyp (string): 앵커볼트 종류
        Returns:
            sOCenAnc (string) : 앵커볼트의 중심선
        """

        if sIAncTyp == "구조용 앵커볼트":
            if -3 < fICenCol-fICenAnc < 3:
                sOCenAnc = "PASS"
            else:
                sOCenAnc = 'FAIL'
        if sIAncTyp == "세우기용 앵커볼트":
            if -5 < fICenCol-fICenAnc < 5:
                sOCenAnc = "PASS"
            else:
                sOCenAnc = 'FAIL'
        return sOCenAnc