import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_08_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ⑧ 나'
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
    나
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ⑧ 결함 길이가 25 mm를 초과하고 깊이가 25 mm보다 큰 불연속 보수는 다음에 준하여 보수해야 한다.
    나.  W, X, Z-형의 결함 허용면적은 철판면적의 4%를 초과해서는 안 된다. 또한 결함 길이나 깊이가 모재의 폭과 길이의 각각 20%를 초과해서는 안 된다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ⑧ 나"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ⑧ 나"])

    subgraph Variable_def
    VarOut6[/출력변수: 불연속 보수/];
    VarIn61[/입력변수: 결함 허용면적/];
    VarIn62[/입력변수: 철판면적/];
    VarIn63[/입력변수: 결함 길이/];
    VarIn64[/입력변수: 결함 깊이/];
    VarIn65[/입력변수: 모재 폭/];
    VarIn66[/입력변수: 모재 길이/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{결함 길이 \n 결함 깊이}
		C--> |결함 길이>25 mm & \n 결함 깊이>25 mm|D{결함허용면적\n결함 길이\n결함 깊이}

	  D --> Ha{"결함허용면적 ≤ 철판면적*0.04,\n 결함 길이 ≤ (모재의 폭)*0.2 \n 결함 깊이 ≤ (모재의 길이)*0.2"}
		Ha --> P([Pass or Fail])

    """

    @rule_method
    def Secondory_Member_of_Bridge(fILenDef, fIDepDef, fITolDef, fIAreSte, fIWidBas, fILenBas) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        fILenDef (float): 결함 길이
        fIDepDef (float): 결함 깊이
        fITolDef (float): 결함 허용면적
        fIAreSte (float): 철판면적
        fIWidBas (float): 모재 폭
        fILenBas (float): 모재 길이

        Returns:

        pass_fail (bool): 제작 3.4.2 절단면 검사 및 결함보수 (2) ⑧ 나 판단결과
        """

        assert isinstance(fILenDef, float)
        assert isinstance(fIDepDef, float)
        assert isinstance(fITolDef, float)
        assert isinstance(fIAreSte, float)
        assert isinstance(fIWidBas, float)
        assert isinstance(fILenBas, float)

        if fILenDef > 25 and fIDepDef > 25:
          if fITolDef <= (fIAreSte * 0.04) and fILenDef <= (fIWidBas * 0.2) and fIDepDef <= (fILenBas * 0.2):
            pass_fail = True
          else:
            pass_fail = False
        else:
          pass_fail = True



        return RuleUnitResult(
           result_variables={
               "pass_fail": pass_fail
               }
        )