import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (3)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '거푸집 및 동바리의 수평하중'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (3)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (3) 수평하중은 고정하중 및 공사 중 발생하는 활하중으로 다음의 값을 적용한다.
    ① 동바리에 작용하는 수평하중으로는 고정하중의 2% 이상 또는 동바리 상단의 수평방향 단위 길이 당 1.5 kN/m 이상 중에서 큰 쪽의 하중이 동바리 머리 부분에 수평방향으로 작용하는 것으로 가정하여 가새설치 여부를 검토한다.
    ② 벽체 거푸집의 경우에는 거푸집 측면에 대하여 0.5kN/㎡ 이상의 수평방향 하중이 작용하는 것으로 볼 수 있다.
    ③ 그 밖에 풍압, 유수압, 지진, 편심하중, 경사진 거푸집의 수직 및 수평분력, 콘크리트 내부 매설물의 양압력, 외부 진동다짐에 의한 영향하중 등의 영향을 크게 받을 때에는 별도로 이들 하중을 고려한다.
    ④ 바닷가나 강가, 고소작업에서와 같이 바람이 많이 부는 곳에서는 KDS 41 10 15 또는 KDS 24 12 21 등에 따라 풍하중 검토를 필수적으로 고려한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집 및 동바리의 수평하중];
    B["KCS 14 20 12 1.6.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (3)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 동바리에 작용하는 최소 수평하중/];
    VarIn1[/입력변수: 동바리 상단의 수평방향 길이/];
    VarIn2[/입력변수: 고정하중/];
    end
    subgraph V2
    VarOut4[/출력변수: 벽체 거푸집에 작용하는 최소 수평하중/];
    VarIn7[/입력변수: 거푸집 측면의 면적/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"동바리에 작용하는 최소 수평하중\n벽체 거푸집에 작용하는 최소 수평하중"}
    C --> |"동바리에 작용하는 최소 수평하중"|D["max(고정하중*0.02,동바리 상단의 수평방향 길이*1.5)"]
    C --> |"벽체 거푸집에 작용하는 최소 수평하중"|E["거푸집 측면의 면적*0.5"]
    D & E --> End([거푸집 및 동바리의 수평하중])
    """

    @rule_method
    def horizontal_load(fILenSho, fIDeaLoa, fIAreFor)-> RuleUnitResult:
        """
        Args:
            fILenSho (float): 동바리 상단의 수평방향 길이
            fIDeaLoa (float): 고정하중
            fIAreFor (float): 거푸집 측면의 면적

        Returns:
            fOLoaSho (float): 동바리에 작용하는 최소 수평하중
            fOHorWal (float): 벽체 거푸집에 작용하는 최소 수평하중

        """
        assert isinstance(fILenSho, float)
        assert isinstance(fIDeaLoa, float)
        assert isinstance(fIAreFor, float)

        fOLoaSho = max(fIDeaLoa * 0.02, fILenSho*1.5)
        fOHorWal = fIAreFor * 0.5

        return RuleUnitResult(
            result_variables = {
                "fOLoaSho": fOLoaSho,
                "fOHorWal": fOHorWal,
                })