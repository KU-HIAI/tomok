import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244015_030403_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 15 3.4.3 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '리벳 및 볼트 구멍의 최종직경'

    description = """
    교량난간
    3. 시공
    3.4 알루미늄 난간
    3.4.3 리벳 및 볼트 구멍
    (3)
    """
    content = """
    #### 3.4.3 리벳 및 볼트 구멍
    (3) 다음의 경우를 제외하고는 구멍의 최종직경은 조임재의 직경보다 7% 이상 커서는 안 된다.
        ① 신축을 원활하게 하기 위하여 도면에 표시한 대로 슬롯(slot)볼트 구멍을 설치할 경우
        ② 앵커용 볼트구멍을 뚫을 경우, 볼트 직경의 50% 최대 13 mm까지 크게 뚫을 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 리벳 및 볼트 구멍의 최종직경];
    B["KCS 24 40 15 3.4.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.4.3 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 리벳 및 볼트 구멍의 직경/];
    VarIn2[/입력변수: 슬롯볼트 구멍/];
    VarIn3[/입력변수: 앵커용 볼트구멍/];
    VarIn4[/입력변수: 조임재의 직경/];
    VarIn5[/입력변수: 볼트 직경/];
    VarIn1 & VarIn2 ~~~ VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{슬롯볼트 구멍}
    C --> |False|D{앵커용 볼트구멍}
    D --> |False|E{"리벳 및 볼트 구멍의 직경 < 조임재의 직경 * 1.07"}
    D --> |True|F{"리벳 및 볼트 구멍의 직경 < min(볼트 직경 * 1.5, 13 mm)"}
    E & F --> End([Pass or Fail])
    """

    @rule_method

    def rivet_bolt_hole(bISloBol,bIBolAnc,fIFasDia,fIBolDia,fIDiaHol) -> RuleUnitResult:
        """
        Args:
            bISloBol (bool): 슬롯볼트 구멍
            bIBolAnc (bool): 앵커용 볼트구멍
            fIFasDia (float): 조임재의 직경
            fIBolDia (float): 볼트 직경
            fIDiaHol (float): 리벳 및 볼트 구멍의 직경

        Returns:
            pass_fail (bool): 교량난간 3.4.3 리벳 및 볼트 구멍 (3)의 판단 결과
        """
        assert isinstance(bISloBol, bool)
        assert bISloBol == False
        assert isinstance(bIBolAnc, bool)
        assert isinstance(fIFasDia, float)
        assert isinstance(fIBolDia, float)
        assert isinstance(fIDiaHol, float)

        if bISloBol == False:
            if bIBolAnc == True:
                if fIDiaHol <= min(fIBolDia*0.5, 13):
                    pass_fail = True
                else:
                    pass_fail = False
            else:
                if fIDiaHol <= fIFasDia * 0.07:
                    pass_fail = True
                else:
                    pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })