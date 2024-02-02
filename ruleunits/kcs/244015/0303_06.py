import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244015_0303_06(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 15 3.3 (6)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '앵커볼트 구멍의 최대 크기'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량난간
    3. 시공
    3.3 강재 난간
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### (6) 앵커볼트의 구멍은 볼트의 정상 직경보다 50%까지 크게 할 수 있으며, 최대 13 mm까지 크게 할 수 있다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커볼트 구멍의 최대 크기];
    B["KCS 24 40 15 3.3 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.3 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 앵커볼트 구멍의 최대 크기/];
    VarIn1[/입력변수: 볼트의 정상직경/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C["앵커볼트 구멍의 최대 크기 = min(볼트의 정상 직경 * 1.5, 13)"]
    C --> D(["앵커볼트 구멍의 최대 크기"])
    """

    @rule_method
    def anchor_bolt_hole(fIDiaBol)->float:
        """
        Args:
            fIDiaBol (float): 볼트의 정상직경
        Returns:
            fOAncHol (string): 앵커볼트 구멍의 최대 크기
        """
        fOAncHol = min(fIDiaBol*1.5, 13)
        return fOAncHol