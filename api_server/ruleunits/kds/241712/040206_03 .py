import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_040206_03 (RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.2.6 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-15'
    title = '거더의 이동변위'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계에 대한 규정
    4.2.6 설계변위
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거더의 이동변위];
    B["KDS 24 17 12 4.2.6 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 행정구역에 의해 결정한 값/];
		VarIn1[/입력변수: 설계지진 발생시 지반에 대한 거더의 총 변위/];
    VarIn2[/입력변수: 설계지진 발생 시 거더의 응답변위/];
		VarIn3[/입력변수: 설계지진 발생 시 하부구조의 변위/];
		VarIn4[/입력변수: 콘크리트의 건조숙축에 의한 거더의 이동량/];
    VarIn5[/입력변수: 콘크리트의 크리프에 의한 거더의 이동량/];
		VarIn6[/입력변수: 온도변화로 인한 거더의 이동량/];

		VarOut ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2~~~~  VarIn4 &  VarIn5 &  VarIn6
		end

		Python_Class ~~~ C(["KDS 24 17 12 4.2.6 (3)"])
		C --> Variable_def;

		D["<img src='https://latex.codecogs.com/svg.image?d=d_{i}+d_{sub}'>--------------------------------------------------------"];
		Variable_def --> D---->E["KDS 24 17 12 4 6"]--->	F["<img src='https://latex.codecogs.com/svg.image?Delta \l_{i}=d+Delta \l_{s}+Delta \l_{c}+Delta \l_{t}'>--------------------------------------------------------"];
		F--->G(["헹정구역에 의해 결정한 값"])
    """

    @rule_method
    def displacement_of_girder(fId,fIdi,fIdsub,fIdeltats,fIdeltalc,fIdeltalt) -> RuleUnitResult:
        """거더의 이동변위

        Args:
            fId (float): 설계지진 발생 시 지반에 대한 거더의 총 변위
            fIdi (float): 설계지진 발생 시 거더의 응답변위
            fIdsub (float): 설계지진 발생 시 하부 구조의 변위
            fIdeltats (float): 콘크리트의 건조수축에 의한 거더의 이동량
            fIdeltalc (float): 콘크리트의 크리프에 의한 거더의 이동량
            fIdeltalt (float): 온도변화로 인한 거더의 이동량

        Returns:
            fOdeltali (float): 교량내진 설계기준(케이블교량) 4.2.6 (3)의 값
        """

        assert isinstance(fId, float)
        assert isinstance(fIdi, float)
        assert isinstance(fIdsub, float)
        assert isinstance(fIdeltats, float)
        assert isinstance(fIdeltalc, float)
        assert isinstance(fIdeltalt, float)

        fId = fIdi + fIdsub
        fOdeltali = fId + fIdeltats + fIdeltalc + 0.4 * fIdeltalt

        return RuleUnitResult(
            result_variables = {
                "fOdeltali": fOdeltali,
                }
            )