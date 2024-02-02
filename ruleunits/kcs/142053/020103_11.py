import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142053_020103_11(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 53 2.1.3 (11)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = 'PS 강재의 부식 저항성'

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (11)
    """

    # 건설기준문서내용(text)
    content = """
    ####(11) PS 강재의 부식 저항성은 일반적으로 비빌 때 그라우트 중에 함유되는 염화물의 총량으로 설정하며, KCI-PS102에 따라 측정한 전 염화물 함유량을 기준으로 사용되는 단위 시멘트량의 0.08 % 이하로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: PS 강재의 부식 저항성];
    B["KCS 14 20 53 2.1.3 (11)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (11)"])

    subgraph Variable_def
    VarOut[/출력변수: PS 강재의 부식 저항성/];
    VarIn1[/입력변수: 그라우트 중 염화물의 총량/];
    VarIn2[/입력변수: 단위 시멘트량/];

    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"염화물의 총량 <= 단위 시멘트량 * 0.8%"}
    C --> |True|Pass([Pass])
    C --> |False|Fail([Fail])
    """

    @rule_method
    def corrosion_resistance_PS_steel(fIAmoChl,fIUniCon):
        """
        Args:
            fIAmoChl (float): 그라우트 중 염화물의 총량
            fIUniCon (float): 단위 시멘트량
        Returns:
            sOCorRes (sting): PS강재의 부식 저항성
        """
        if fIAmoChl<=fIUniCon*0.0008:
            sOCorRes = "Pass"
        else:
            sOCorRes = "Fail"
        return sOCorRes