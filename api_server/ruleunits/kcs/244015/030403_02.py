import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244015_030403_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 15 3.4.3 (2)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-20'
    title = '예비로 천공된 리벳 및 볼트 구멍의 크기'

    description = """
    교량난간
    3. 시공
    3.4 알루미늄 난간
    3.4.3 리벳 및 볼트 구멍
    (2)
    """
    content = """
    #### 3.4.3 리벳 및 볼트 구멍
    (2) 예비로 천공된 구멍의 크기는 적어도 부재두께의 1/4 이상 되어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 예비로 천공된 리벳 및 볼트 구멍의 크기];
    B["KCS 24 40 15 3.4.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 15 3.4.3 (2)"])

    subgraph Variable_def
    VarIn0[/입력변수: 예비로 천공된 리벳 및 볼트 구멍의 크기/];
    VarIn1[/입력변수: 부재두께/];
    VarIn0 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{예비로 천공된 리벳 및 볼트 구멍의 크기 > 부재두께/4}
    C --> End([Pass or Fail])
    """

    @rule_method

    def rivet_bolthole_size(fIMemThi,fISizHol) -> RuleUnitResult:
        """
        Args:
            fIMemThi (float): 부재 두께
            fISizHol (float): 예비로 천공된 리벳 및 볼트 구멍의 최소 크기

        Returns:
            pass_fail (bool): 교량난간 3.4.3 리벳 및 볼트 구멍 (2)의 판단 결과
        """
        assert isinstance(fIMemThi, float)
        assert isinstance(fISizHol, float)

        if fISizHol >= fIMemThi/4:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })