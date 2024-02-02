import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030304_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.3.4 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '볼트접합 시공 공통사항'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.3 볼트접합
    3.3.4 시공
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1)  공통사항
    ① 볼트의 나사부는 하나 이상의 나사산이 연결되는 부재 안쪽에 남아있도록 한다.
    ② 그룹볼트의 조임은 중앙의 볼트에서 단부의 볼트 방향으로 작업을 진행하며, 1차 예비조임과 본조임으로 나누어 2회 시행한다. 1차조임은 소요 토크 값의 60% 정도로 전체볼트를 조인다.
    ③ 볼트접합면의 표면처리는 블라스트 등에 의해 녹, 흑피 등을 제거하여 미끄럼계수가 0.4 이상 얻어지도록 처리한다.
    ④ 볼트 체결작업의 2차 본조임은 강우 및 결로 등 습한 상태에서 실시해서는 안 된다.
    ⑤ 토크계수값을 줄이기 위해서 표면처리를 실시한 와셔를 사용할 경우는 이것을 너트 측에만 사용하고 볼트머리 측에는 표면처리를 하지 않은 것을 사용한다.
    ⑥ 용접과 고장력볼트의 마찰접합을 병용할 때에는, 용접완료 후에 고장력볼트의 조임 시공을 실시하는 것으로 한다. 고장력볼트를 조인 후에 용접할 때에는 구속에 의한 영향을 고려한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 볼트접합 시공 공통사항];
    B["KCS 24 30 00 3.3.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.3.4 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 그룹볼트의 1차 조임 토크/];
    VarOut2[/출력변수: 볼트접합면의 표면처리/];
    VarIn1[/입력변수: 소요 토크/];
    VarIn2[/입력변수: 미끄럼계수/];
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"검토항목"}
    C --> |"그룹볼트의 1차 조임"|D["그룹볼트의 1차 조임 토크 = 소요 토크 * 0.6"]
    C --> |"볼트접합면의 표면처리"|E{"미끄럼계수 ≥ 0.4"}
    E --> |"True"|F(["Pass"])
    E --> |"False"|G(["Fail"])
    D --> J([볼트접합 시공 공통사항])
    """

    @rule_method
    def primary_tightening_torque(fIReqTor)-> float:
        """
        Args:
            fIReqTor (float): 소요 토크
        Returns:
            fOPriTor (float): 그룹볼트의 1차 조임 토크
        """
        fOPriTor = fIReqTor *0.6
        return fOPriTor

    def surface_treatment(self,fISliFac)-> str:
        """
        Args:
            fISliFac (float): 미끄럼계수
        Returns:
            sOSurTre (string): 볼트접합면의 표면처리
        """
        if fISliFac >=0.4:
            sOSurTre = "Pass"
        else:
            sOSurTre = "Fail"
        return sOSurTre