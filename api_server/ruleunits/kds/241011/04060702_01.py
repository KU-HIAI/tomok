import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060702_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.7.2 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '플랜지 유효폭'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.7 플랜지 유효폭
    4.6.7.2 박스형 세그멘탈 콘크리트 보 및 단 격실 박스형 현장타설 콘크리트 보
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 플렌지 유효폭];
    B["KDS 24 10 11 4.6.7.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 플랜지 유효폭/];
    VarIn1[/입력변수 : 복부판 어느 한쪽으로의 플랜지폭/];
    VarIn2[/입력변수 : 표 4.6-14에서 정의된 bs와 bm을 결정하기 위해 그림 4.6.8에 규정된 지간장/];
    VarIn3[/입력변수 : 상부구조물의 높이/];
    VarIn4[/입력변수 : 특별한 지점단면의 플랜지 유효폭/];
    VarIn5[/입력변수 : 경간의 내부구간에서의 플랜지 유효폭/];
    VarIn6[/입력변수 : 내부지점 또는 캔틸레버 구간에서의 플랜지 유효폭/];
    VarIn7[/입력변수 : 그림 4.6-6에 보인 바와 같이 복부판 각면의 플랜지폭과 지간길이의 1/4중에서 작은값을 플랜지 유효폭으로 취했을 경우 유효폭이 변화되는 지간부위/];
    VarOut~~~VarIn3~~~VarIn6
    VarIn1~~~VarIn4~~~VarIn7
    VarIn2~~~VarIn5~~~VarIn7
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.7.2 (1)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?b\leq&space;0.1l_{i}and&space;b\leq&space;0.3d_{o}'>-----------------------------------------"};
    E["플랜지 유효폭=실제 플랜지 폭"];
    F["표 4.6-14,그림 4.6-7~4.6-9에 규정된 폭 참고"];
    G(["플랜지 유효폭"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def effective_length_of_flange(fIWactfl,fIdo,fIb,fIli) -> RuleUnitResult:
        """플랜지 유효폭

        Args:
            fIWactfl (float): 실제 플랜지의 폭
            fIdo (float): 상부구조물의 높이
            fIb (float): 복부판 어느 한쪽으로의 플랜지폭
            fIli (float): 표 4.6-14에서 정의된 bs와 bm을 결정하기 위해 그림 4.6.8에 규정된 지간장


        Returns:
            fOWefffl (float): 교량 설계 일반사항(한계상태설계법)  4.6.7.2 박스형 세그멘탈 콘크리트 보 및 단 격실 박스형 현장타설 콘크리트 보 (1)의 값
        """

        assert isinstance(fIWactfl, float)
        assert isinstance(fIdo, float)
        assert isinstance(fIb, float)
        assert isinstance(fIli, float)

        if fIb <= 0.1 * fIli or fIb <= 0.3 * fIdo:
          fOWefffl = fIWactfl

          return RuleUnitResult(
              result_variables = {
                  "fOWefffl": fOWefffl,
              }
          )