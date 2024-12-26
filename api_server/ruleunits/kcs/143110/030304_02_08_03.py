import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_08_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ⑧ 다'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '절단면 검사 및 결함보수'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (2)
    ⑧
    다
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ⑧ 결함 길이가 25 mm를 초과하고 깊이가 25 mm보다 큰 불연속 보수는 다음에 준하여 보수해야 한다.
    다. 나.항의 허용면적을 초과하지 않는 Z-형 결함은 용접면에서 25 mm 이상 떨어져 있을 경우에는 보수할 필요가 없으나 25 mm 이내일 경우에는 용접열영향부에서 25 mm까지 치핑, 아크에어가우징, 또는 그라인더에 의하여 가우징하고
    층당 3  mm를 초과하지 않는 최소 4개층을 가스메탈아크용접(GMAW)을 실시하고 나머지는 서브머지드 아크용접(SAW) 또는 승인된 용접방법에 의하여 용접해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ⑧ 다"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ⑧ 다"])

    subgraph Variable_def
    VarOut8[/출력변수: 불연속 보수/];
    VarIn63[/입력변수: 결함 길이/];
    VarIn64[/입력변수: 결함 깊이/];
    VarIn81[/입력변수: 용접면까지 떨어진 길이/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{결함 길이 \n 결함 깊이}
		C--> |결함 길이>25 mm & \n 결함 깊이>25 mm|D{"용접면까지 떨어진 길이"}
		D --> |"≥ 25 mm"|Hc[보수할 필요가 없다]
		D --> |"< 25 mm"|Hd["용접열영향부에서 25 mm까지 \n 치핑, 아크에어가우징, 또는 그라인더에 의하여 가우징하고 \n 층당 3  mm를 초과하지 않는 \n 최소 4개층을 가스메탈아크용접(GMAW)을 실시하고 \n 나머지는 서브머지드 아크용접(SAW) \n 또는 승인된 용접방법에 의하여 용접해야 한다\n. "]
		Hc & Hd--> End5([불연속 보수])
    """

    @rule_method
    def Secondory_Member_of_Bridge(fILenDef, fIDepDef, fIDisWel) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        fILenDef (float): 결함 길이
        fIDepDef (float): 결함 깊이
        fIDisWel (float): 용접면까지 떨어진 길이

        Returns:

        sODisRep (str): 불연속 보수
        """

        assert isinstance(fILenDef, float)
        assert isinstance(fIDepDef, float)
        assert isinstance(fIDisWel, float)

        if fILenDef > 25 and fIDepDef > 25:
          if fIDisWel >= 25:
            sODisRep = "보수할 필요가 없다."
          else:
              sODisRep = "용접열영향부에서 25 mm까지 치핑, 아크에어가우징, 또는 그라인더에 의하여 가우징하고 층당 3  mm를 초과하지 않는 최소 4개층을 가스메탈아크용접(GMAW)을 실시하고 나머지는 서브머지드 아크용접(SAW) 또는 승인된 용접방법에 의하여 용접"
        else:
          sODisRep = "보수할 필요가 없다"


        return RuleUnitResult(
           result_variables={
               "sODisRep": sODisRep
           }
        )