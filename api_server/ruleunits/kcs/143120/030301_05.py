import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030301_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.3.1 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '피복아크 용접의 용접봉'

    description = """
    용접
    3. 시공
    3.3 용접준비
    3.3.1 용접재료 선택 및 주의사항
    """

    content = """
    #### 3.3.1 용접재료 선택 및 주의사항
    (5) 피복아크용접의 용접봉에 대해 다음 규정을 적용한다.
    ② 응력을 전달하는 피복아크용접봉은 직경이 4~6 mm인 것을 표준으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 피복아크용접의 용접봉];
    B["KCS 14 31 20 3.3.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.3.1 (5)"])

    subgraph Variable_def
    VarIn[/입력변수: 피복아크용접봉 직경/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"4 < 피복아크용접봉 직경 < 6"}
		C --> D([Pass or fail])
    """

    @rule_method
    def Diameter_of_Shield_Metal_Arc_Welding(fIDiaShi) -> bool:
        """ 피복아크용접의 용접봉
        Args:
        fIDiaShi (float): 피복아크용접봉 직경

        Returns:
        pass_fail (bool): 용접 3.3.1 용접재료 선택 및 주의사항 (5)의 판단 결과
        """
        assert isinstance(fIDiaShi, float)

        if 4 <= fIDiaShi <= 6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )