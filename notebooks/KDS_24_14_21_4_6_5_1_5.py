import math
from typing import List
from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS_24_14_21_4_6_5_1_5)


class KDS_24_14_21_4_6_5_1_5(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1
    author = 'Jaewook Lee'
    ref_code = 'KDS 24 14 21 4.6.5.1 (5)'
    ref_date = '2023-06-28'
    title = '바닥판 최소두께'
    description = """
    콘크리트교 설계기준(한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.5 교량의 콘크리트 바닥슬래브
    4.6.5.1 일반 사항
    (5)
    """
    content = """
    #### 4.6.5.1 일반 사항
(5) 특별히 요구되지 않는 한, 콘크리트 바닥판은 홈 또는 마모 방지 층의 두께를 뺀 판 최소 두께는 220mm 보다 작아서는 안 된다. 프리스트레스트 콘크리트 바닥판의 최소두께는 200mm 이상이어야 한다. 바닥판의 최소 피복 두께는 4.4의 규정을 따라야 한다.
    """
    flowchart = """
    flowchart TD
    %% Nodes
    A["ProfileSectionSlabThickness(SLATHI)"]
    B["ReviewValueSlabMinThickness(SLAMINTHI)"]
    C{"SLATHI > SLAMINTHI"}
    D[True]
    E[False]

    %% Edges
    A --> C
    B --> C
    C --True--> D
    C --False--> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def slab_min_thickness(SLATHI, SLAMINTHI) -> bool:
        """홈 또는 마모 방지 층의 두께를 뺀 콘크리트 바닥판의 두께가 최소 두께를 만족하는 지의 여부

        Args:
            SLATHI (float): 교량의 콘크리트 바닥판의 홈 또는 마모 방지 층의 두께를 뺀 판의 두께. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            SLAMINTHI (float): 교량의 콘크리트 바닥판의 홈 또는 마모 방지 층의 두께를 뺀 판의 최소 두께. 건설 기준에 의해 정의된 기준 값.

        Returns:
            bool: 콘크리트교 설계기준(한계상태설계법) 4.6.5.1 일반 사항의 항목 (5)의 통과 여부
        """
        if SLATHI > SLAMINTHI:
            return True
        else:
            return False
