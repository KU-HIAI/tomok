import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_030301_11(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 3.3.1 (11)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '받침의 성질'

    description = """
    교량받침
    3. 시공
    3.3 포트받침 및 디스크받침
    3.3.1 제조 세목
    (11)
    """
    content = """
    #### 3.3.1 제조 세목
    (11) 앞에서 언급한 사항 이외에 강판으로 된 모든 받침의 표면은 0.8 mm/m 이내로 평평하게 마무리하거나 가공하여야 한다. 0.8 mm/m 보다 편평도가 크면 불합격이다.
    받침 패드에 놓이도록 설계된 하부 받침판(저판)의 하면은 편평도가 5.2 mm/m 이내가 되도록 하여야 한다. 산소용접기로 절단한 면은 조도가 25 × 103 mm를 넘지 않도록 하여야 한다.
    전체 받침의 허용치수는 -0, +3 mm 이내이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침의 성질];
    B["KCS 24 40 05 3.3.1 (11)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.3.1 (11)"])

    subgraph Variable_def
    VarOut[/출력변수: 받침의 성질/];
    VarIn1[/입력변수: 강판으로 된 모든 받침의 표면/];
    VarIn2[/"입력변수: 받침 패드에 놓이도록 설계된 하부 받침판(저판)의 하면"/];
    VarIn3[/입력변수: 산소용접기로 절단한 면/];
    VarIn4[/입력변수: 전체 받침의 허용치수/];
    VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강판으로 된 모든 받침의 표면\n받침 패드에 놓이도록 설계된 하부 받침판(저판)의 하면\n산소용접기로 절단한 면\n전체 받침의 허용치수\n."}
    C --> |강판으로 된 모든 받침의 표면|D["편평도 0.8 mm/m 이내로 마무리하거나 가공"]
    C --> |"받침 패드에 놓이도록 설계된 하부 받침판(저판)의 하면"|E["평도가 5.2 mm/m 이내가 되도록 한다."]
    C --> |"산소용접기로 절단한 면"|F["조도가 25 × 103 mm를 넘지 않도록 하여야 한다"]
    C --> |전체 받침의 허용치수|G["-0, +3 mm 이내"]
    D & E & F & G--> End([ 받침의 성질])
    """

    @rule_method

    def property_bearing(bISurSte,bIUndBas,bISurOxy,bITolEnt) -> RuleUnitResult:
        """
        Args:
            bISurSte (bool): 강판으로 된 모든 받침의 표면
            bIUndBas (bool): 받침 패드에 놓이도록 설계된 하부 받침판(저판)의 하면
            bISurOxy (bool): 산소용접기로 절단한 면
            bITolEnt (bool): 전체 받침의 허용치수

        Returns:
            sOProBea (str): 받침의 성질
        """
        assert isinstance(bISurSte, bool)
        assert isinstance(bIUndBas, bool)
        assert isinstance(bISurOxy, bool)
        assert isinstance(bITolEnt, bool)
        assert (bISurSte+bIUndBas+bISurOxy+bITolEnt) ==1

        if bISurSte:
            sOProBea = "0.8 mm/m 이내로 평평하게 마무리하거나 가공"
        elif bIUndBas:
            sOProBea = "평도가 5.2 mm/m 이내가 되도록 한다"
        elif bISurOxy:
            sOProBea = "조도가 25 × 103 mm를 넘지 않도록 하여야 한다"
        elif bITolEnt:
            sOProBea = "-0, +3 mm 이내"

        return RuleUnitResult(
            result_variables = {
                "sOProBea": sOProBea,
                })