import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_08_05(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ⑧ 마'
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
    마
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ⑧ 결함 길이가 25 mm를 초과하고 깊이가 25 mm보다 큰 불연속 보수는 다음에 준하여 보수해야 한다.
    마.  용접보수의 전체길이가 모재단부 길이의 20%를 초과하는 경우 다른 재료로 대체해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ⑧ 마"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ⑧ 마"])

    subgraph Variable_def
    VarOut8[/출력변수: 용접 보수/];
    VarIn63[/입력변수: 결함 길이/];
    VarIn64[/입력변수: 결함 깊이/];
    VarIn81[/입력변수: 용접보수의 전체길이/];
    VarIn82[/입력변수: 모재단부 길이/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{결함 길이 \n 결함 깊이}
		C--> |결함 길이>25 mm & \n 결함 깊이>25 mm|D{"용접보수의 전체길이 > 모재단부 길이 * 0.2"}
		D --> |True|He[다른 재료로 대체]
		He --> End5([불연속 보수])
    """

    @rule_method
    def Secondory_Member_of_Bridge(fILenDef, fIDepDef, fILenWel, fILenEnd) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        fILenDef (float): 결함 길이
        fIDepDef (float): 결함 깊이
        fILenWel (float): 용접보수의 전체길이
        fILenEnd (float): 모재단부 길이

        Returns:
        sOWelRep (str): 용접 보수
        """
        assert isinstance(fILenDef, float)
        assert isinstance(fIDepDef, float)
        assert isinstance(fILenWel, float)
        assert isinstance(fILenEnd, float)

        if fILenDef > 25 and fIDepDef > 25:
          if fILenWel > (fILenEnd * 0.2):
            sOWelRep = "다른 재료로 대체"
          else:
            sOWelRep = None
        else:
          sOWelRep = None

        return RuleUnitResult(
           result_variables={
               "sOWelRep": sOWelRep
           }
        )