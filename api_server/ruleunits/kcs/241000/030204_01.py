import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS241000_030204_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 10 00 3.2.4 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-09-24'
    title = '그라우트의 시공기간'


    description = """
    콘크리트교량공사
    3. 시공
    3.2 프리스트레스트 콘크리트
    3.2.4 그라우트의 시공
    (1)
    """
    content = """
    #### 3.2.4 그라우트의 시공
    그라우트의 시공은 프리스트레싱이 끝난 후 될 수 있는 대로 빨리 하여야 한다.
    강재에 대한 별도의 부식방지 대책이 없는 경우,
    강재설치로부터 다음의 기간 내에 주입이 이루어져야 한다.
    (1) 습한 지역 및 해상 (습도 ＞ 70%): 7일
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 시공기간];
    B["KCS 24 10 00 3.2.4 (1)"];
    B ~~~ A
    end
    KCS(["KCS 24 10 00 3.2.4 (1)"])
    subgraph Variable_def
    VarOut[/출력변수: 그라우트의 시공기간/];
    VarIn1[/입력변수: 습도/];
	VarIn2[/입력변수: 별도의 부식방지 대책/];
    VarOut ~~~ VarIn1 & VarIn2
    end
    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"별도의 부식방지 대책"}
    C --> |False|D{습도 > 70}
    D--> E["그라우트의 시공기간 = 7일"];
    E--> F(["그라우트의 시공기간"])
    """

    @rule_method

    def grouting_interval(fIHum, bICorPro) -> RuleUnitResult:
        """
        Args:
            fIHum (float): 습도
            bICorPro (bool): 별도의 부식방지 대책

        Returns:
            nOGroInt (int): 그라우트의 시공기간
        """
        assert isinstance(fIHum, float)
        assert isinstance(bICorPro, bool)
        assert fIHum > 70
        assert bICorPro == False

        if bICorPro == False:
            if fIHum > 70:
                nOGroInt = 7

        return RuleUnitResult(
            result_variables = {
                "nOGroInt": nOGroInt,
                })