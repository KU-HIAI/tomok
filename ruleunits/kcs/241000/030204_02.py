import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS241000_030204_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 10 00 3.2.4 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-09-25'
    title = '그라우트의 시공기간'

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트교량공사
    3. 시공
    3.2 프리스트레스트 콘크리트
    3.2.4 그라우트의 시공
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.4 그라우트의 시공
    그라우트의 시공은 프리스트레싱이 끝난 후 될 수 있는 대로 빨리 하여야 한다. 강재에 대한 별도의 부식방지 대책이 없는 경우, 강재설치로부터 다음의 기간 내에 주입이 이루어져야 한다.
    (2) 습도 40% 이상 70% 이하: 20일
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 시공기간];
    B["KCS 24 10 00 3.2.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 10 00 3.2.4 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 그라우트의 시공기간/];
    VarIn1[/입력변수: 습도/];
	VarIn2[/입력변수: 별도의 부식방지 대책/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"별도의 부식방지 대책"}
    C --> |False|D{40≤습도 ≤ 70}
    D--> E["그라우트의 시공기간 = 20일"];
    E--> F(["그라우트의 시공기간"])
    """

    @rule_method
    def grouting_interval(fIHum, bICorPro):
        """
        Args:
            fIHum (float): 습도
            bICorPro (boolean): 별도의 부식방지 대책
        Returns:
            nOGroInt (integer): 그라우트의 시공기간
        """
        if bICorPro == False:
            if fIHum >= 40 and fIHum <=70:
                nOGroInt = 20
            else:
                return None
        else:
            return None
        return nOGroInt