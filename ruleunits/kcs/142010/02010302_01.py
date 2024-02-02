import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_02010302_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.3.2 (1)' # 건설기준문서
    ref_date = '2023-09-26'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 잔골재
    2.1.3.2 물리적 품질
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.3.2 물리적 품질
    (1) 잔골재의 절대건조밀도는 2.5g/㎤ 이상, 흡수율은 3.0% 이하의 값을 표준으로 한다. 다만, 잔골재의 종류에 따라 물리적 품질이 다르기 때문에 KS F 2527에서 정한 규정에 따른다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 잔골재의 물리적 품질"];
    B["KCS 14 31 30 2.1.3.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.3.2 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 잔골재의 절대건조밀도"/];
    VarOut2[/"출력변수: 잔골재의 흡수율"/];

		VarIn1[/"입력변수: 잔골재의 절대건조밀도"/];
		VarIn2[/"입력변수: 잔골재의 흡수율"/];

    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"잔골재의 절대건조밀도 => 2.5g/c㎥"}
    Variable_def --> D{"잔골재의 흡수율 <= 3.0%"}

		C --> |True|F([PASS])
		C --> |False|E([FAIL])

		D --> |True|F([PASS])
		D --> |False|E([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def physical_quality_of_aggregates(fIAbsDry, fIAbsRat) ->str :
        """잔골재의 물리적 품질

        Args:
            fIAbsDry (float): 잔골재의 절대건조밀도
            fIAbsRat (float): 잔골재의 흡수율

        Returns:
            sOAbsDry (string): 잔골재의 절대건조밀도
            sOAbsRat (string): 잔골재의 흡수율

        """

        if fIAbsDry >= 2.5:
            sOAbsDry = "PASS"
            if fIAbsRat <= 3.0:
                sOAbsRat = "PASS"
                return sOAbsDry, sOAbsRat
            else:
                sOAbsRat = "FAIL"
                return sOAbsDry, sOAbsRat
        else:
            sOAbsDry = "FAIL"
            if fIAbsRat <= 3.0:
                sOAbsRat = "PASS"
                return sOAbsDry, sOAbsRat
            else:
                sOAbsRat = "FAIL"
                return sOAbsDry, sOAbsRat