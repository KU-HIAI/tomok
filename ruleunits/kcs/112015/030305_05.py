import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS112015_030305_05(RuleUnit): # 허윤아 박사님에게 확인받기 KDS241431_040303_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 20 15 3.3.5 (5)' # 건설기준문서
    ref_date = '2023-08-16'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2020-12-03'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '도랑파기 폭'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    터파기
    3. 시공
    3.3 시공기준
    3.3.5 터파기 및 도랑파기
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.5 터파기 및 도랑파기
(5) 도랑파기는 관의 상단 위 600 mm 평면 아래의 모든 측점에서 명시된 폭으로 하여야 하며, 이 평면 위의 파기는 공사감독자가 승인하면 명시된 폭을 초과할 수 있다. 폭이 명시되지 않은 경우는 폭은 관의 외측면에서 150 mm~450 mm 범위로 하여야 한다. 파기가 허용된 치수를 초과하면 공사감독자의 승인을 받아 더 높은 강도의 관을 설치하거나 관을 콘크리트로 감싸야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 도랑파기];
    B["KCS 11 20 15 3.3.5 (5)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 15 3.3.5 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 도랑파기/];
    VarIn1[/입력변수: 도랑파기 폭/];
    VarIn2[/입력변수: 명시된 폭/];
    VarIn3[/입력변수: 공사감독자 승인/];


    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{명시된 폭}

    C --> |True|D{"도랑파기 폭 <= 명시된 폭"}
    D --> |True|F(["PASS"])
    D --> |False|G{공사감독자 승인}
		G --> |True|F(["PASS"])
		G --> |False|H(["FAIL"])

    C --> |False|E{"150 <= 도랑파기 폭 <=450"}
		E --> |True|F(["PASS"])
		E --> |False|I{"공사감독자 승인"}
		I --> |True|K["더 높은 강도의 관을 설치하거나 관을 콘크리트로 감싸야"]
		I --> |False|H(["FAIL"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def excavation_width(bISpeWid, fISpeWid, bISupApp, fIExcWid) :
        """도랑파기 폭 만족 여부

        Args:
            bISpeWid (boolean): 명시된 폭
            fISpeWid (float): 명시된 폭의 길이
            bISupApp (boolean): 공사감독자 승인 여부
            fIExcWid (float): 도랑파기 폭

        Returns:
            sOExcWid (string): 터파기  3.3.5 터파기 및 도랑파기 (5)의 통과 여부 및 시공 기준 출력
        """

        if bISpeWid == True:
            if fIExcWid <= fISpeWid:
              sOExcWid = "PASS"
              return sOExcWid
            else:
              if bISupApp == True:
                sOExcWid = "PASS"
                return sOExcWid
              else:
                sOExcWid = "FAIL"
                return sOExcWid
        elif bISpeWid == False:
          if 150 <= fIExcWid <= 450:
            sOExcWid = "PASS"
            return sOExcWid
          else:
            sOExcWid = "공사감독자의 승인을 받아 더 높은 강도의 관을 설치하거나 관을 콘크리트로 감싸야 한다."
            return sOExcWid