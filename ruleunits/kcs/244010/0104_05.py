import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244010_0104_05(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 24 40 10 1.4 (5)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2018-08-30'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '신축이음'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    신축이음
    1. 일반사항
    1.4 제출물
    (5) 제작도면
    """

    # 건설기준문서내용(text)
    content = """
    #### 1.4 제출물
    (5) 제작도면
    총 이동량이 45 mm 이상인 신축이음에 대해서는 감독자에게 제작도면을 제출하여 사전 승인을 받아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 신축이음의 제작도면];
    B["KCS 24 40 10 1.4 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 1.4 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 신축이음의 제작도면/];
    VarIn1[/입력변수: 신축이음의 총 이동량/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{신축이음의 총 이동량 => 45mm}
    C --> |True|D["감독자에게 제작도면을 제출하여 사전 승인을 받아야 한다"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def joint_drawing(fIMovJoi) ->str :
        """신축이음의 제작도면

        Args:
            fIMovJoi (float): 신축이음의 총 이동량. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당

        Returns:
            sOJoiDra (string) : 신축이음의 제작도면
        """

        if fIMovJoi >= 45:
            sOJoiDra = "감독자에게 제작도면을 제출하여 사전 승인을 받아야 한다."
            return sOJoiDra
        else:
            return None