import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143130_030302_05(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 30 3.3.2 (5)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '조립 및 설치'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    조립 및 설치
    3. 시공
    3.3 부재조립 및 설치
    3.3.2 건축물의 현장 조립
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.2 건축물의 현장 조립
    (5) 현장용접
    ⑦ 용접개소에서의 풍속은 피복아크용접, 실드아크용접에서는 10 m/s, CO2반자동용접에서는 2 m/s를 넘어서지 않아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 용접개소에서의 풍속"];
    B["KCS 14 31 30 3.3.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.3.2 (5)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 풍속"/];

		VarIn1[/"입력변수: 용접의 종류"/];
		VarIn2[/"입력변수: 풍속"/];

    VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"용접의 종류"}


		D --> |"'피복아크용접' \nor '실드아크용접'"|G[풍속 <= 10 m/s]
		D --> |'CO2반자동용접'|H[풍속 <= 2 m/s]

		G --> |True|E([PASS])
		G --> |False|F([FAIL])

		H --> |True|E([PASS])
		H --> |False|F([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def wind_speed_at_welding_site(sITypWel, fIWinSpe) ->str :
        """용접개소에서의 풍속

        Args:
            sITypWel (string): 용접의 종류. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            fIWinSpe (float): 풍속

        Returns:
            sOWinSpe (string) : 용접개소에서의 풍속
        """

        if (sITypWel == "피복아크용접") or (sITypWel == "실드아크용접"):
            if fIWinSpe <= 10:
                sOWinSpe = "PASS"
                return sOWinSpe
            else:
                sOWinSpe = "FAIL"
                return sOWinSpe
        elif sITypWel == "CO2반자동용접":
            if fIWinSpe <= 2:
                sOWinSpe = "PASS"
                return sOWinSpe
            else:
                sOWinSpe = "FAIL"
                return sOWinSpe