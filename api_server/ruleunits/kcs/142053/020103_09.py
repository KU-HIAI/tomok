import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020103_09(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.1.3 (9)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '부재 콘크리트와 긴장재를 일체화시키는 부착강도'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (9)
    """
    content = """
    #### 2.1.3 프리스트레스트 콘크리트용 그라우트
    (9) 부재 콘크리트와 긴장재를 일체화시키는 부착강도는 재령 7일 또는 28일의 압축강도로 대신하여 설정할 수 있다. 압축강도는 KCI-PS102에 준하여 구하며, 7일 재령에서 27 MPa 이상 또는 28일 재령에서 30 MPa 이상을 만족하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 부재 콘크리트와 긴장재를 일체화시키는 부착강도];
    B["KCS 14 20 53 2.1.3 (9)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (9)"])

    subgraph Variable_def
    VarIn1[/입력변수: 재령/];
    VarIn2[/입력변수: 압축강도/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"재령"}
    C --> |7일|D{"압축강도 >= 27MPa"}
    C --> |28일|E{"압축강도 >= 30MPa"}
    D & E --> End([Pass or Fail])
    """

    @rule_method

    def bonding_strength(nICurPer,fIFck) -> RuleUnitResult:
        """
        Args:
            nICurPer (int): 재령
            fIFck (float): 압축강도

        Returns:
            pass_fail (bool): 프리스트레스트 콘크리트 2.1.3 프리스트레스트 콘크리트용 그라우트 (9)의 판단 결과
        """
        assert isinstance(nICurPer, int)
        assert isinstance(fIFck, float)
        assert nICurPer == 7 or nICurPer == 28

        if nICurPer == 7:
            if fIFck >=27:
                pass_fail = True
            else:
                pass_fail = False
        elif nICurPer == 28:
            if fIFck >=30:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })