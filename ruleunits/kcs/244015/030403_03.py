import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244015_030403_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 15 3.4.3 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '리벳 및 볼트 구멍의 최종직경'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량난간
    3. 시공
    3.4 알루미늄 난간
    3.4.3 리벳 및 볼트 구멍
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####
    (3) 다음의 경우를 제외하고는 구멍의 최종직경은 조임재의 직경보다 7% 이상 커서는 안 된다.
        ① 신축을 원활하게 하기 위하여 도면에 표시한 대로 슬롯(slot)볼트 구멍을 설치할 경우
        ② 앵커용 볼트구멍을 뚫을 경우, 볼트 직경의 50% 최대 13 mm까지 크게 뚫을 수 있다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 리벳 및 볼트 구멍의 최종직경];
    B["KCS 24 40 15 3.4.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.4.3 (3)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 리벳 및 볼트 구멍의 최대 직경/];
    VarIn10[/입력변수: 슬롯볼트 구멍/];
    VarIn11[/입력변수: 조임재의 직경/];
    end
    subgraph V2
    VarOut2[/출력변수: 리벳 및 볼트 구멍의 최대 직경/];
    VarIn20[/입력변수: 앵커용 볼트구멍/];
    VarIn21[/입력변수: 조임재의 직경/];
    VarIn22[/입력변수: 볼트 직경/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{앵커용 볼트구멍\n슬롯볼트 구멍}
    C --> |슬롯볼트 구멍|D["도면에 표시한대로 설치"]
    C --> |앵커용 볼트구멍|E["리벳 및 볼트 구멍의 최대 직경 = min(볼트 직경 * 1.5, 13 mm)"]
    C --> |False|F[리벳 및 볼트 구멍의 최대 직경 = 조임재의 직경 * 1.07]
    D & E & F --> End(["리벳 및 볼트 구멍의 최대 직경"])
    """

    @rule_method
    def rivet_bolt_hole(bISloBol,bIBolAnc,fIFasDia,fIBolDia)-> str:
        """
        Args:
            bISloBol (boolean): 슬롯볼트 구멍
            bIBolAnc (boolean): 앵커용 볼트구멍
            fIFasDia (float): 조임재의 직경
            fIBolDia (float): 볼트 직경
        Returns:
            sODiaHol (string): 리벳 및 볼트 구멍의 최종 직경
        """
        if bISloBol:
            sODiaHol = "도면에 표시한대로 설치"
        else:
            if bIBolAnc:
                sODiaHol = "최대 "+ str(min(fIBolDia*1.5, 13)) + " mm"
            else:
                sODiaHol = "최대 " + str(round(fIFasDia*1.07,3))  + " mm"
        return sODiaHol