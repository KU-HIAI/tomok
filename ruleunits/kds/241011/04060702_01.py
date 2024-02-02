import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060702_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jong Hyeok'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.7.2 (1)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-09'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '플랜지 유효폭'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.7 플랜지 유효폭
    4.6.7.2 박스형 세그멘탈 콘크리트 보 및 단 격실 박스형 현장타설 콘크리트 보
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
   # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
        subgraph Python_Class
        A[플렌지 유효폭];
        B["KDS 24 10 11 4.6.7.2 (1)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 플랜지 유효폭/];
    VarIn1[/입력변수 : 복부판 어느 한쪽으로의 플랜지폭/];
    VarIn2[/입력변수 : 표 4.6-14에서 저으이된 bs와 bm을 결정하기 위해 그림 4.6.8에 규정된 지간장/];
    VarIn3[/입력변수 : 상부구조물의 높이/];
    VarIn4[/입력변수 : 특별한 지점단면의 플랜지 유효폭/];
    VarIn5[/입력변수 : 경간의 내부구간에서의 플랜지 유효폭/];
    VarIn6[/입력변수 : 내부지점 또는 캔틸레버 구간에서의 플랜지 유효폭/];
    VarIn7[/입력변수 : 그림 4.6-6에 보인 바와 같이 복부판 각면의 플랜지폭과 지간길이의 1/4중에서 작은값을 플랜지 유효폭으로 취했을 경우 유효폭이 변화되는 지간부위/];
    VarOut~~~VarIn3~~~VarIn6
    VarIn1~~~VarIn4~~~VarIn7
    VarIn2~~~VarIn5~~~VarIn7
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?b\leq&space;0.1l_{i}and&space;b\leq&space;0.3d_{o}'>-----------------------------------------"};
    E["플랜지 유효폭=실제 플랜지 폭"];
    F["표 4.6-14,그림 4.6-7~4.6-9에 규정된 폭 참고"];
    G(["플랜지 유효폭"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  effective_length_of_flange(fIWactfl,fIdo,fIb,fIbe,fIbm,fIbs,fIa,fIli,fOWefffl) -> float:
        """플랜지 유효폭
        Args:
            fIWactfl (float): 실제 플랜지의 폭
            fIdo (float): 상부구조물의 높이
            fIb (float): 복부판 어느 한쪽으로의 플랜지폭
            fIbe (float): 표 4.6-14에서 결정되어지는 경간내의 특별한 지점단면의 플랜지 유효폭
            fIbm (float): 그림 4.6-7에서 결정된 경간의 내부 구간에서의 플랜지 유효폭
            fIbs (float): 그림 4.6-7에서 결정된 내부지점 혹은 캔틸레버 구간에서의 플랜지 유효폭
            fIa (float): 그림 4.6-6에 보인 바와 같이 복부판 각면의 플랜지폭과 지간길이의 1/4 중에서 작은 값을 플랜지 유효폭으로 취하였을 경우 유효폭이 변화되는 지간 부위
            fIli (float): 표 4.6-14에서 정의된  및 을 결정하기 위해 그림 4.6.8에 규정된 지간장
            fOWefffl (float): 플랜지 유효폭
        Returns:
            float: 교량 설계 일반사항(한계상태설계법) 4.6.7.2 박스형 세그멘탈 콘크리트 보 및 단 격실 박스형 현장타설 콘크리트 보 (1)의 값
        """
        if fIb <= 0.1*fIli or fIb <= 0.3*fIdo:
          fOWefffl = fIWactfl
          return(fOWefffl)


