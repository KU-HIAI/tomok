import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03080402_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.8.4.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '인발저항력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.8 앵커지지 벽체
    3.8.4 지반 파괴에 대한 안전성
    3.8.4.2 앵커의 인발저항력(pullout capacity)
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발저항력];
    B["KDS 24 14 51 3.8.4.2 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:인발저항력/]
		VarIn1[/출력변수:앵커 인발저항력 저항계수/]
		VarIn2[/출력변수:앵커의 공칭인발 저항력/]
		VarIn3[/출력변수:앵커천공의 직경/]
		VarIn4[/출력변수:앵커의 공칭 부착응력/]
		VarIn5[/출력변수:앵커의 정착길이/]

		VarOut1 ~~~
		VarIn1 ~~~ VarIn2 ~~~ VarIn3
		VarIn4 ~~~ VarIn5

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.8.4.2 (1)"])
		C --> Variable_def

		E["<img src='https://latex.codecogs.com/svg.image?Q_{R}=\phi&space;Q_{n}=\phi\pi&space;d\tau&space;_{n}L_{b}'>---------------------------------"]
		D([인발저항력])

		Variable_def ---> E ---> D
    """

    @rule_method
    def pull_out_resistance_force(fIanccoe,fIQn,fId,fInomstr,fILb) -> RuleUnitResult:
        """인발저항력

        Args:
            fIanccoe (float): 앵커 인발저항력 저항계수
            fIQn (float): 앵커의 공칭인발저항력
            fId (float): 앵커 천공의 직경
            fInomstr (float): 앵커의 공칭 부착응력
            fILb (float): 앵커의 정착길이

        Returns:
            fOQr (float): 교량 하부구조 설계기준 (한계상태설계법)  3.8.4.2 앵커의 인발저항력(pullout capacity) (1)의 값
        """

        assert isinstance(fIanccoe, float)
        assert isinstance(fIQn, float)
        assert isinstance(fId, float)
        assert isinstance(fInomstr, float)
        assert isinstance(fILb, float)

        import math

        fOQr = fIanccoe * math.pi * fId * fInomstr * fILb

        return RuleUnitResult(
            result_variables = {
                "fOQr": fOQr,
            }
        )