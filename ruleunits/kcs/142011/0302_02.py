import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142011_0302_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 11 부록 3.2 (2)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '그라우트의 두께'

    # 건설기준문서항목 (분류체계정보)
    description = """
    철근공사
    부록
    3. 시공
    3.2 그라우트에 관한 요구 사항
    3.1.3 철근의 이음
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 그라우트의 두께는 40mm~50mm로 하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 두께];
    B["KCS 14 20 11 부록 3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 부록 3.2 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 그라우트의 두께/];
    VarIn1[/입력변수: 그라우트의 두께/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C["40 ≤ 그라우트의 두께 ≤ 50"]
    C --> D(["Pass or Fail"])
    """

    @rule_method
    def grout_thickness(fIGroThi):
        """
        Args:
            fIGroThi (float): 그라우트의 두께
        Returns:
            sOGroThi (sting): 그라우트의 두께
        """
        if fIGroThi > 40 and fIGroThi < 50:
            sOGroThi = "Pass"
        else:
            sOGroThi = "Fail"
        return sOGroThi