import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030307_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.7 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '인발저항력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.7 인발
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발저항력];
    B["KDS 24 14 51 3.3.3.7 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:감가된 인발저항력/]
		VarIn1[/입력변수:저항계수/]
		VarIn2[/입력변수:무리말뚝의 공칭 인발저항력/]
		VarIn3[/입력변수:외말뚝의 인발저항력/]
		VarIn4[/입력변수:무리말뚝의 인발저항력/]
		VarIn5[/입력변수:무리말뚝의 폭/]
		VarIn6[/입력변수:무리말뚝의 길이/]
		VarIn7[/입력변수:말뚝캡 아래 블록의 깊이/]
		VarIn8[/입력변수:평균 비배수 전단강도/]
		VarIn9[/입력변수:흙, 말뚝, 그리고 말뚝캡을 포함한 블록의 중량/]

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~ VarIn3
		VarIn4 ~~~ VarIn5 ~~~ VarIn6
		VarIn7 ~~~ VarIn8 ~~~ VarIn9

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.7 (3)"])
		C --> Variable_def

		J[외말뚝의 인발 저항력]
		D[무리말뚝의 인발저항력]
		E([공칭인발저항력])
		F[인발저항력]
		G[사질토에 설치된 무리말뚝의 공칭인발 저항력]

		Variable_def ---> J & D ---> I{둘중 작은 값}
		Variable_def ---> F ---> J["<img src='https://latex.codecogs.com/svg.image?Q_{R}=\phi&space;Q_{n}=\phi&space;_{ug}Q_{ug}'>---------------------------------"]
		Variable_def ---> G ---> H["<img src='https://latex.codecogs.com/svg.image?Q_{n}=Q_{ug}=(2XZ&plus;2YZ)\overline{S_{u}}&plus;W_{g}'>---------------------------------"]
		J & H & I ---> E
    """

    @rule_method
    def pull_resistance(fIressin,fIresbul,fIX,fIY,fIZ,fIaveshe,fIWg) -> RuleUnitResult:
        """인발저항력

        Args:
            fIressin (float): 외말뚝의 인발저항력의 합
            fIresbul (float): 무리말뚝의 인발저항력
            fIX (float): 무리말뚝의 폭
            fIY (float): 무리말뚝의 길이
            fIZ (float): 말뚝캡 아래 블록의 깊이
            fIaveshe (float): 평균 비배수 전단강도
            fIWg (float): 흙, 말뚝, 그리고 말뚝캡을 포함한 블록의 중량

        Returns:
            fOresbul (float): 깊은기초 설계기준(일반설계법) 3.3.3.7 인발 (3)의 값 1
            fOQug (float): 깊은기초 설계기준(일반설계법) 3.3.3.7 인발 (3)의 값 2
            fOQr (float): 깊은기초 설계기준(일반설계법) 3.3.3.7 인발 (3)의 값 3
        """

        assert isinstance(fIressin, float)
        assert isinstance(fIresbul, float)
        assert isinstance(fIX, float)
        assert isinstance(fIY, float)
        assert isinstance(fIZ, float)
        assert isinstance(fIaveshe, float)
        assert isinstance(fIWg, float)

        fOresbul = (2 * fIX * fIZ + 2 * fIY * fIZ) * fIaveshe + fIWg
        fOQug = min(fIressin, fIresbul)
        fOQr = fOresbul * fOQug

        return RuleUnitResult(
            result_variables = {
                "fOresbul": fOresbul,
                "fOQug": fOQug,
                "fOQr": fOQr,
              }
        )