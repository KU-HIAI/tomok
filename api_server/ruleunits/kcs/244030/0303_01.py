import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244030_0303_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 3.3 (1)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '출입사다리 발판'

    description = """
    교량점검시설
    3. 시공
    3.3 출입사다리
    (1)
    """

    content = """
    #### 3.3 출입사다리
    (1) 출입사다리 발판은 부재 또는 벽면에서 150 mm 떨어져 설치한다.

    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 출입사다리 발판 설치"];
    B["KCS 24 40 30 3.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 30 3.3 (1)"])

    subgraph Variable_def
    VarOut[/"출력변수: 출입사다리 발판"/];
    VarIn1[/"입력변수: 출입사다리 발판"/];

    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"출입사다리 발판"}
		D --> E["부재 또는 벽면에서 150 mm 떨어져 설치한다."]
		E --> F([출입사다리 발판])

    """

    @rule_method
    def access_ladder_steps(bILadSte) -> str :
        """출입사다리 발판

        Args:
            bILadSte (bool): 출입사다리 발판

        Returns:
            sOLadSte (str) : 출입사다리 발판
        """

        assert isinstance(bILadSte, bool)

        if bILadSte == True:
           sOLadSte = "부재 또는 벽면에서 150 mm 떨어져 설치한다."
        else:
          bILadSte = False; sOLadSte = "그냥 설치한다??"

        return RuleUnitResult(
                result_variables = {
                    "sOLadSte": sOLadSte,
                }
            )