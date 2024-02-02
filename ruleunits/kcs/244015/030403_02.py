import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244015_030403_02(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 15 3.4.3 (2)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '예비로 천공된 리벳 및 볼트 구멍의 최소 크기'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량난간
    3. 시공
    3.4 알루미늄 난간
    3.4.3 리벳 및 볼트 구멍
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### (2) 예비로 천공된 구멍의 크기는 적어도 부재두께의 1/4 이상 되어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 예비로 천공된 리벳 및 볼트 구멍의 최소크기];
    B["KCS 24 40 15 3.4.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.4.3 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 예비로 천공된 리벳 및 볼트 구멍의 최소크기/];
    VarIn1[/입력변수: 부재두께/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C[예비로 천공된 리벳 및 볼트 구멍의 최소크기 = 부재두께/4]
    C --> F(["예비로 천공된 리벳 및 볼트 구멍의 최소크기"])
    """

    @rule_method
    def rivet_bolthole_size(fIMemThi)-> float:
        """
        Args:
            fIMemThi (float): 부재 두께
        Returns:
            fOSizHol (float): 예비로 천공된 리벳 및 볼트 구멍의 최소 크기
        """
        fOSizHol = round(fIMemThi/4,3)
        return fOSizHol