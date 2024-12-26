import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS112015_030305_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 20 15 3.3.5 (5)'
    ref_date = '2023-08-16'
    doc_date = '2020-12-03'
    title = '도랑파기 폭'

    description = """
    터파기
    3. 시공
    3.3 시공기준
    3.3.5 터파기 및 도랑파기
    (5)
    """

    content = """
    #### 3.3.5 터파기 및 도랑파기
(5) 도랑파기는 관의 상단 위 600 mm 평면 아래의 모든 측점에서 명시된 폭으로 하여야 하며, 이 평면 위의 파기는 공사감독자가 승인하면 명시된 폭을 초과할 수 있다. 폭이 명시되지 않은 경우는 폭은 관의 외측면에서 150 mm~450 mm 범위로 하여야 한다. 파기가 허용된 치수를 초과하면 공사감독자의 승인을 받아 더 높은 강도의 관을 설치하거나 관을 콘크리트로 감싸야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 도랑파기 폭];
    B["KCS 11 20 15 3.3.5 (5)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 15 3.3.5 (5)"])

    subgraph Variable_def
    VarIn1[/입력변수: 도랑파기 폭/];
    VarIn2[/입력변수: 명시된 폭/];
    VarIn3[/입력변수: 공사감독자 승인/];

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{명시된 폭}

    C --> |True|D{"도랑파기 폭 <= 명시된 폭"}
    D --> |True|F(["PASS"])
    D --> |False|G{공사감독자 승인}
		G --> |True|F(["PASS"])
		G --> |False|H(["FAIL"])

    C --> |False|E{"150 <= 도랑파기 폭 <=450"}
		E --> |True|F(["PASS"])
		E --> |False|I{"공사감독자 승인"}
		I --> |True|K["더 높은 강도의 관을 설치하거나 관을 콘크리트로 감싸야"]
		I --> |False|H(["FAIL"])
    """

    @rule_method
    def excavation_width(bISpeWid, fISpeWid, bISupApp, fIExcWid) -> bool:
        """도랑파기 폭 만족 여부

        Args:
            bISpeWid (bool): 명시된 폭
            fISpeWid (float): 명시된 폭의 길이
            bISupApp (bool): 공사감독자 승인 여부
            fIExcWid (float): 도랑파기 폭

        Returns:
            sOExcWid (str): 도랑파기 폭
            pass_fail (bool): 터파기 3.3.5 터파기 및 도랑파기 (5)의 판단 결과
        """
        assert isinstance (bISpeWid, bool)
        assert isinstance (fISpeWid, float)
        assert isinstance (bISupApp, bool)
        assert isinstance (fIExcWid, float)

        if bISpeWid == True:
            if fIExcWid <= fISpeWid:
              pass_fail = True
              sOExcWid = None
            else:
              if bISupApp == True:
                pass_fail = True
                sOExcWid = None
              else:
                pass_fail = False
                sOExcWid = None
        elif bISpeWid == False:
          if 150 <= fIExcWid <= 450:
            pass_fail = True
            sOExcWid = None
          else:
            pass_fail = None
            sOExcWid = "공사감독자의 승인을 받아 더 높은 강도의 관을 설치하거나 관을 콘크리트로 감싸야 한다."

        return RuleUnitResult(
              result_variables = {
                  "pass_fail": pass_fail,
                  "sOExcWid": sOExcWid,
              }
          )