import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_020206_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.6 (1)' # 건설기준문서
    ref_date = '2023-10-05'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명


    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.6 굵은 골재의 최대 치수
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.6 굵은 골재의 최대 치수
    (1) 굵은 골재의 공칭 최대 치수는 다음 값을 초과하지 않아야 한다. 그러나 이러한 제한은 콘크리트를 공극 없이 칠 수 있는 다짐 방법을 사용할 경우에는 책임기술자의 판단에 따라 적용하지 않을 수 있다.
    ① 거푸집 양 측면 사이의 최소 거리의 1/5
    ② 슬래브 두께의 1/3
    ③ 개별 철근, 다발철근, 긴장재 또는 덕트 사이 최소 순간격의 3/4
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 굵은 골재의 공칭 최대 치수"];
    B["KCS 14 31 30 2.2.6 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.6 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 굵은 골재의 공칭 최대 치수"/];


		VarIn1[/"입력변수: 거푸집 양 측면 사이의 최소 거리"/];
		VarIn2[/"입력변수: 슬래브 두께"/];
		VarIn3[/"입력변수: 개별 철근, 다발철근, 긴장재 또는 덕트 사이 최소 순간격"/];

    VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"굵은 골재의 최대 치수<\nmin((거푸집 양 측면 사이의 최소 거리)*1/5,\n(개별 철근, 다발철근, 긴장재 또는 덕트 사이 최소 순간격)*3/4)\n(슬래브 두께)*1/3"}


		D --> |True|E([PASS])
		D --> |False|K([Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def max_nominal_size_of_coarse_aggregates(fISizAgg, fIDisFor, fISlaThi, fIMinDis) -> float:
        """굵은 골재의 공칭 최대 치수
        Args:
            fISizAgg (float): 굵은 골재의 공칭 최대 치수
            fIDisFor (float): 거푸집 양 측면 사이의 최소 거리
            fISlaThi (float): 슬래브 두께
            fIMinDis (float): 개별 철근, 다발철근, 긴장재 또는 덕트 사이 최소 순간격
        Returns:
            sOSizAgg (string): 굵은 골재의 공칭 최대 치수
        """

        if fISizAgg <= min((fIDisFor)*1/5, (fISlaThi)*1/3, (fIMinDis)*3/4):
            sOSizAgg = "PASS"
        else:
            sOSizAgg = "FAIL"
        return sOSizAgg