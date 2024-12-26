import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_0406_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.6 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-13'
    title = '앵커의 최소 중심 간격'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.6 쪼갬파괴를 방지하기 위한 연단거리, 앵커 간격, 두께
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커의 최소 중심 간격];
    B["KDS 14 20 54 4.6 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 앵커의 최소 중심 간격/];
    VarIn1[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트 지름/];
    VarIn2[/입력변수 : 선설치 앵커/];
    VarIn3[/입력변수 : 후설치 앵커/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.6 (2)"])
		C --> Variable_def

    D{"(5)에 의해 결정되지 않는 경우"};
    E{"비틀림이 가해지는 경우"};
    F["선설치 앵커"];
    G["선설치 앵커 and 후설치 앵커"];
    H["앵커의 최소 중심 간격 = 4da"];
    I["앵커의 최소 중심 간격 = 6da"];
    J(["앵커의 최소 중심 간격"]);
    Variable_def --->D--->E
    E--Yes--->G--->I--->J
    E--No--->F--->H--->J
    """

    @rule_method
    def minimum_center_spacing_of_anchor(fIda) -> RuleUnitResult:
        """앵커의 최소 중심 간격

        Args:
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의샤프트지름

        Returns:
            fOmincsA (float): 콘크리트용 앵커 설계기준  4.6 쪼갬파괴를 방지하기 위한 연단거리, 앵커 간격, 두께 (2)의 값 1
            fOmincsB (float): 콘크리트용 앵커 설계기준  4.6 쪼갬파괴를 방지하기 위한 연단거리, 앵커 간격, 두께 (2)의 값 2
        """

        assert isinstance(fIda, float)

        fOmincsA = 4 * fIda
        fOmincsB = 6 * fIda

        return RuleUnitResult(
            result_variables = {
                "fOmincsA": fOmincsA,
                "fOmincsB": fOmincsB,
            }
        )