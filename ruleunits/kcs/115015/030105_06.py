import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115015_030105_06(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 50 15 3.1.5 (6)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2021-05-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '기성말뚝'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    기성말뚝
    3. 시공
    3.1 일반사항
    3.1.5 시험시공말뚝
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.5 시험시공말뚝
    (6) 시험시공말뚝은 설계서에 명시된 말뚝규격으로 선정하고 말뚝길이는 소요길이보다 2m 이상 긴 말뚝으로 시공하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 시험시공말뚝 시공 조건"];
    B["KCS 11 50 15 3.1.5 (6)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 15 3.1.5 (6)"])

    subgraph Variable_def
    VarOut[/"출력변수: 시험시공말뚝 시공 조건"/];
		VarIn2[/"입력변수: 말뚝길이"/];
		VarIn3[/"입력변수: 소요길이"/];



    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"시험시공말뚝"}

		D --> E([설계서에 명시된 말뚝규격으로 선정])
		D --> F[말뚝길이 => 소요길이 + 2 m ]
		F --> |True|G([PASS])
		F --> |False|H([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def construction_conditions_for_test_piles(fIPilLen, fIReqLen) ->str :
        """시험시공말뚝 시공 조건

        Args:
            fIPilLen (float): 말뚝길이
            fIReqLen (float): 소요길이

        Returns:
            sOConTes (string) : 시험시공말뚝 시공 조건
        """

        if fIPilLen >= fIReqLen + 2:
            sOConTes = "PASS"
            return sOConTes
        else:
            sOConTes = "FAIL"
            return sOConTes