from typing import List
import math
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tomok.core.decorator import rule_method
from tomok.core.rule_unit import RuleUnit

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS142054_040305_04)
class KDS142054_040305_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.5 (4)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 부착식 앵커 또는 부착식 앵커 그룹의 가장자리 영향에 관한 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (4)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####   4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (4) 인장력을 받는 단일 부착식 앵커 또는 부착식 앵커 그룹의 가장자리 영향에 관한 수정계수 $$\psi _{ed,Na}$$는 다음과 같이 구하여야 한다.
    $$c_{a,min}\geq c_{Na}$$인 경우

		      $$\psi _{ed,Na}=1.0$$     (4.3-24)

    $$c_{a,min}<c_{Na}$$인 경우

		      $$\psi _{ed,Na}=0.7+0.3\frac{c_{a,min}}{c_{Na}}$$     (4.3-25)
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[단일 부착식 앵커 또는 부착식 앵커그룹의 가장자리영향에관한 수정계수];
    B["KDS 14 20 54 4.3.5 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 단일 부착식 앵커 또는 부착식 앵커그룹의 가장자리영향에관한 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적가장자리까지의 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?c_{a,min}\geq&space;c_{Na}'>-----------------"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}=1.0'>----------------"];
    F["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}=0.7+0.3\frac{c_{a,min}}{c_{Na}}'>-----------------------------"];
    G(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,Na}'>"])
    Variable_def--->D
    D--Yes--->E--->G
    D—No--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor_for_edge_influence_of_single_or_group_of_anchor(fOpsedNa,fIcamin,fIcNa) -> float:
        """단일 부착식 앵커 또는 부착식 앵커 그룹의 가장자리 영향에 관한 수정계수

        Args:
            fOpsedNa (float): 단일 부착식 앵커 또는 부착식 앵커 그룹의 가장자리영향에 관한 수정계수
            fIcamin (float): 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리
            fIcNa (float): 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (4)의 값
        """

        if fIcamin >= fIcNa:
          fOpsedNa = 1.0

        else:
          fOpsedNa = 0.7 + 0.3 * fIcamin / fIcNa

        return fOpsedNa

# """작성한 룰 유닛은 아래의 코드 블럭과 같이 생성하여, 작성자가 임의로 검증을 수행할 수 있습니다."""

# my_RuleUnit = KDS142054_040305_04()

# fOpsedNa = None
# fIcamin = 100
# fIcNa = 90

# Rule_Review_Result = my_RuleUnit.correction_factor_for_edge_influence_of_single_or_group_of_anchor(fOpsedNa,fIcamin,fIcNa)
# # 해당건설기준 항목 의 결과는?

# print("RuleUnit Review Result: {}".format(Rule_Review_Result))

# """<br><br>
# 아래의 코드를 통해, 룰 유닛의 content(건설기준 항목의 실제 내용)의 markdown 렌더링 결과를 확인할 수 있습니다.
# """

# my_RuleUnit.render_markdown()