import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS112015_030306_02(RuleUnit): # 허윤아 박사님에게 확인받기 KDS241431_040303_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 20 15 3.3.6 (2)' # 건설기준문서
    ref_date = '2023-08-16'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2020-12-03'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '암반기초 터파기 표면의 기울기'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    터파기
    3. 시공
    3.3 시공기준
    3.3.6 암반기초 터파기
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.6 암반기초 터파기
    (2) 터파기한 표면의 기울기가 1 : 4 이상일 경우에는 계단, 톱니형상 또는 요철처리 등의 방법으로 시공하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 암반기초 터파기 표면의 기울기];
    B["KCS 11 20 15 3.3.6 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 15 3.3.6 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 암반기초 터파기/];
    VarIn1[/입력변수: 터파기한 표면의 기울기/];

    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{터파기한 표면의 기울기 => 1/4}

    C --> D["계단, 톱니형상 또는 요철처리 등의 방법으로 시공"]
		D --> F([암반기초 터파기])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def rock_foundation_excavation(fISloSur) -> str:
        """암반기초 터파기 기울기가 1:4 이상일 경우의 시공 방법

        Args:
            fISloSur (float): 터파기한 표면의 기울기. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당

        Returns:
            sOFouExc : 터파기  3.3.6 암반기초 터파기 (2)의 시공 기준 출력
        """

        if fISloSur >= 1/4:
            sOFouExc = "계단, 톱니형상 또는 요철처리 등의 방법으로 시공하여야 한다."
            return sOFouExc
        else:
            sOFouExc = None
            return sOFouExc