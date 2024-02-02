import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030404_02(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.4.4 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.4 조립 및 설치
    3.4.4 시공
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 시공허용오차
    ① 지점부 보강재, 웨브, 다이아프램 등 하중을 지지하는 부재는 플랜지 안쪽 표면과 75% 이상의 접촉면적을 가져야 한다.
    ② 하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새는 하중을 지지하는 부재 투영 면적의 75% 이상이 0.25 mm 이내로 접촉되고, 25% 이하는 1 mm 이내로 관리되어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새];
    B["KCS 24 30 00 3.4.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.4.4 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새/];
    VarIn1[/입력변수: 하중을 지지하는 부재 투영 면적/];
    VarIn2[/입력변수: 1mm 이내로 접촉되는 면적/];
    VarIn3[/입력변수: 0.25 mm 이내로 접촉되는 면적/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end


    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"0.25mm 이내로 접촉되는 면적 \n ≥ 하중을 지지하는 부재 투영 면적 * 0.75"}
    C --> |"True"|D{"1mm 이내로 접촉되는 면적 \n ≤ 하중을 지지하는 부재 투영 면적 * 0.25"}
    C --> |"False"|Fail([Fail])
    D --> |"False"|Fail([Fail])
    D --> |"True"|Pass([Pass])
    """

    @rule_method
    def joint_aperture(fIProAre,fIAreCon_1,fIAreCon_2)-> str:
        """
        Args:
            fIProAre (float): 하중을 지지하는 부재 투영 면적
            fIAreCon_1 (float): 1mm 이내로 접촉되는 면적
            fIAreCon_2 (float): 0.25mm 이내로 접촉되는 면적
        Returns:
            sOJoiApe (string): 하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새
        """
        if fIAreCon_1 >= fIProAre*0.75 and fIAreCon_2 <= fIProAre*0.25:
            sOJoiApe = "Pass"
        else:
            sOJoiApe = "Fail"
        return sOJoiApe