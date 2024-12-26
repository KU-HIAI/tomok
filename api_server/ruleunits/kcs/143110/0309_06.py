import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_0309_06(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.9 (6)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '플랜지 내·외면의 가열'

    description = """
    제작
    3. 시공
    3.9 곡선거더교의 제작
    (6)
    """

    content = """
    #### 3.9 곡선거더교의 제작
    (6) 가열방법 및 가열온도
    ④ 플랜지 내·외면의 가열은 플랜지 두께가 30 mm 이상인 경우에는 동시에 가열해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 플랜지 내·외면의 가열"];
    B["KCS 14 31 10 3.8.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.8.3 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 플랜지 내·외면의 가열"/];
    VarIn1[/입력변수: 플랜지 두께/];
		VarOut1 ~~~ VarIn1
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"플랜지 두께 ≥ 30 mm"}
    C --> |"True"|D["동시에 가열"]
		D --> End(["플랜지 내·외면의 가열"])
    """

    @rule_method
    def Thickness_of_Flange(fIThiFla) -> str:
        """ 플랜지 내·외면의 가열
        Args:
        fIThiFla (float): 플랜지 내외의 가열

        Returns:
        sOHeaFla (str): 플랜지 두께
        """
        assert isinstance(fIThiFla, float)

        if fIThiFla >= 30:
          sOHeaFla = "동시에 가열"
        else:
          sOHeaFla = "동시에 가열할 필요가 없다"

        return RuleUnitResult(
            result_variables={
                "sOHeaFla": sOHeaFla
            }
        )