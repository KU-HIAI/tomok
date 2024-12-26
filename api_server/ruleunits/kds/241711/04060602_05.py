import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060602_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.2 (5)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '소요 변위연성도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소요 변위연성도의 최댓값];
    B["KDS 24 17 11 4.6.6.2 (5)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 소요 변위연성도/] ;
    VarIn1[/입력변수: 고려하는 방향으로의 단면 최대 두께/] ;
    VarIn2[/입력변수: 기둥 형상비의 기준이 되는 기둥길이/];
    end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.6.2 (5)"])
		C --> Variable_def-->F -->D
    D(["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\triangle,max}'>-----------------------"]);
    F["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\triangle,max}=2(L_{s}/h)\leq&space;5.0'>----------------------------------------------------------"]
    """

    @rule_method
    def maximum_required_displacement_ductility(fIh,fILs) -> RuleUnitResult:
        """소요 변위연성도

        Args:
            fIh (float): 고려하는 방향으로의 단면 최대 두께
            fILs (float): 기둥 형상비의 기준이 되는 기둥길이

        Returns:
            fOmaxmud (float): 교량내진설계기준(한계상태설계법) 4.6.6.2 소요연성도 (5)의 값
        """

        assert isinstance(fIh, float)
        assert isinstance(fILs, float)

        if 2 * (fILs / fIh) <= 5.0 :
          fOmaxmud = 2 * (fILs / fIh)
          return RuleUnitResult(
              result_variables = {
                  "fOmaxmud": fOmaxmud,
                  }
              )