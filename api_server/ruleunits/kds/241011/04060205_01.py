import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060205_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.6.2.5 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-13'
    title = '캔틸레버 바닥판'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.5 캔틸레버 바닥판
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 캔틸레버 바닥판];
    B["KDS 24 10 11 4.6.2.5 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수: 폭 1m당의 휨모멘트/];
    VarIn1[/입력변수: 하중점에서 지지점까지의 거리/];
    VarIn2[/입력변수: 설계차량활하중의 1후륜하중/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.2.5 (1)"])
		C --> Variable_def

    D{"주철근이 차량진행방향에 직각인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?E=0.8X+1.14'>------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?M=\frac{P}{E}X'>"];
    G(["휨모멘트"]);
    Variable_def--->D--->E--->F--->G
    """

    @rule_method
    def cantilever_floor(fIX,fIP) -> RuleUnitResult:
        """캔틸레버 바닥판

        Args:
            fIX (float): 하중점에서 지지점까지의 거리
            fIP (float): 설계차량활하중의 1후륜하중


        Returns:
            fOM (float): 교량 설계 일반사항(한계상태설계법) 4.6.2.5 캔틸레버 바닥판 (1)의 값
        """

        assert isinstance(fIX, float)
        assert fIX > 0
        assert isinstance(fIP, float)

        fOM = fIP * fIX / (0.8 * fIX + 1.14)

        return RuleUnitResult(
            result_variables = {
                "fOM": fOM,
            }
        )