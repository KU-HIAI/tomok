import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_030404_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 3.4.4 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새'

    description = """
    강교량공사
    3. 시공
    3.4 조립 및 설치
    3.4.4 시공
    (2)
    """
    content = """
    ####3.4.4 시공
    (2) 시공허용오차
    ① 지점부 보강재, 웨브, 다이아프램 등 하중을 지지하는 부재는 플랜지 안쪽 표면과 75% 이상의 접촉면적을 가져야 한다.
    ② 하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새는 하중을 지지하는 부재 투영 면적의 75% 이상이 0.25 mm 이내로 접촉되고, 25% 이하는 1 mm 이내로 관리되어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하부 플랜지와 솔플레이트의 틈새 및 솔플레이트와 교량 받침의 틈새];
    B["KCS 24 30 00 3.4.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.4.4 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 하중을 지지하는 부재 투영 면적/];
    VarIn2[/입력변수: 1mm 이내로 접촉되는 면적/];
    VarIn3[/입력변수: 0.25 mm 이내로 접촉되는 면적/];
    VarIn1 ~~~ VarIn2 & VarIn3
    end


    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"0.25mm 이내로 접촉되는 면적 \n ≥ 하중을 지지하는 부재 투영 면적 * 0.75
    & 1mm 이내로 접촉되는 면적 \n ≤ 하중을 지지하는 부재 투영 면적 * 0.25 \n. "}
    C --> End([Pass or Fail])
    """

    @rule_method

    def joint_aperture(fIProAre,fIAreCon_1,fIAreCon_2) -> RuleUnitResult:
        """
        Args:
            fIProAre (float): 하중을 지지하는 부재 투영 면적
            fIAreCon_1 (float): 1mm 이내로 접촉되는 면적
            fIAreCon_2 (float): 0.25mm 이내로 접촉되는 면적

        Returns:
            pass_fail (bool): 강교량공사 3.4.4 시공 (4)의 판단 결과
        """


        assert isinstance(fIProAre,float)
        assert isinstance(fIAreCon_1,float)
        assert isinstance(fIAreCon_2,float)

        if fIAreCon_1 >= fIProAre*0.75 and fIAreCon_2 <= fIProAre*0.25:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })