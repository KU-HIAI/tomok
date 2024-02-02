import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142053_020103_06(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 53 2.1.3 (6)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '프리스트레스트 콘크리트용 그라우트의 충전성'

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    ####
    (6) 그라우트의 덕트 내 충전성은 그라우트의 유동성, 블리딩률, 체적변화율로 판단한다.
    ① 유동성은 KCI-PS102에 따라 유하시간 또는 플로를 측정하고 기준값과 비교하여 적절성을 판단하도록 한다.
    ② 블리딩률은 KCI-PS102에 따라 강연선이 배치된 수직관 또는 경사관 시험을 통해 측정하고 기준값과 비교하여 적절성을 판단하도록 한다. 기준값은 3시간 경과 시 0.3 % 이하로 한다.
    ③ 체적변화율은 KCI-PS102에 따라 수직관 시험을 통해 측정하고 기준값과 비교하여 적절성을 판단하도록 한다. 기준값은 24시간 경과 시 (–1 ∼ 5) %의 범위이다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리스트레스트 콘크리트용 그라우트의 충전성];
    B["KCS 14 20 53 2.1.3 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (6)"])

    subgraph Variable_def
    VarOut1[/출력변수: 그라우트 덕트 내 충전성/];
    VarIn1[/"입력변수: 블리딩률(3시간 경과)"/];
    VarIn2[/"체적변화율(24시간 경과)"/];

    VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"블리딩률<=0.3 \n -1<=체적변화율<=5 \n."}
    C --> |True|Pass([Pass])
    C --> |False|Fail([Fail])
    """

    @rule_method
    def fillability_grout_duct(fIBleRat,fIVolCha):
        """
        Args:
            fIBleRat (float): 블리딩률(3시간 경과)
            fIVolCha (float)
        Returns:
            sOFilGro (sting): 그라우트 덕트 내 충전성
        """
        if fIBleRat <=0.3 and fIVolCha>=-1 and fIVolCha<=5:
            sOFilGro = "Pass"
        else:
            sOFilGro = "Fail"
        return sOFilGro