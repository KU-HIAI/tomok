import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030402_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.4.2 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '볼트구멍의 엇갈림'

    description = """
    제작
    3. 시공
    3.4 구멍뚫기
    3.4.2 볼트 구멍의 치수 및 정밀도
    (4)
    """

    content = """
    #### 3.4.2 볼트 구멍의 치수 및 정밀도
    (4) 볼트구멍의 엇갈림
    마찰이음으로 부재를 조립할 경우, 구멍의 엇갈림은 1.0 mm 이하로 하고, 지압이음으로 부재를 조립할 경우, 구멍의 엇갈림은 0.5 mm 이하로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 볼트구멍의 엇갈림];
    B["KKCS 14 31 10 3.4.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.4.2 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 마찰이음/];
    VarIn2[/입력변수: 지압이음/];
    VarIn3[/입력변수: 구멍의 엇갈림/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> E{"마찰이음\n지압이음"}
		E --> |마찰이음|C{"구멍의 엇갈림 ≤ 1.0 mm"}
		E --> |지압이음|G{"구멍의 엇갈림 ≤ 0.5 mm"}
		C & G --> End([Pass or Fail])
    """

    @rule_method
    def Friction_Connection(bIFriCon, bIBeaCon, fIGapHol) -> bool:
        """ 볼트구멍의 엇갈림
        Args:
        bIFriCon (bool): 마찰이음
        bIBeaCon (bool): 지압이음
        fIGapHol (float): 구멍의 엇갈림

        Returns:
        pass_fail (bool): 제작 3.4.2 볼트 구멍의 치수 및 정밀도 (4)의 판단 결과
        """
        assert isinstance(bIFriCon, bool)
        assert isinstance(bIBeaCon, bool)
        assert bIFriCon != bIBeaCon
        assert isinstance(fIGapHol, float)

        if bIFriCon == True and bIBeaCon == False:
          if fIGapHol <= 1.0:
            pass_fail = True
          else:
            pass_fail = False

        elif bIFriCon == False and bIBeaCon == True:
          if fIGapHol <= 0.5:
            pass_fail = True

          else:
            pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )