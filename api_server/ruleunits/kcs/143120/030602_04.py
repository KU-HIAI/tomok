import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030602_04(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.6.2 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '단일전극 서브머지드 아크용접의 용접층'

    description = """
    용접
    3. 시공
    3.6 서브머지드아크용접(SAW)
    3.6.2 단일전극 서브머지드아크용접
    """

    content = """
    #### 3.6.2 단일전극 서브머지드아크용접
    (4) 루트 및 표면층을 제외하고 용접층의 두께가 6mm를 초과하여서는 안 된다. 루트간격이 12mm 이상 또는 용접층의 폭이 16mm를 초과할 경우에는 다중패스의 층분할 기법을 적용한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 단일전극 서브머지드 아크용접의 용접층"];
    B["KCS 14 31 20 3.6.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.6.2 (4)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 단일전극 서브머지드 아크용접의 용접층"/];
    VarIn1[/입력변수: 루트 및 표면층/];
    VarIn2[/입력변수: 용접층의 두께/];
    VarIn3[/입력변수: 루트 간격/];
    VarIn4[/입력변수: 용접층의 폭/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"루트 및 표면층"}
    C --> |"False"|D{"용접층의 두께 ≤ 6 mm"}
		D --> |True|E{"루트간격 ≥ 12 mm \n or \n 용접층의 폭 > 16 mm"}
		E --> F[다중패스의 층분할 기법을 적용]

		D & E --> G([Pass or Fail])
		F --> H([단일전극 서브머지드 아크용접의 용접층])
    """

    @rule_method
    def Root_and_Surface_Layer(bIRooSur, fIThiWel, fIRooDis, fIWidWel) -> RuleUnitResult:
        """ 단일전극 서브머지드 아크용접의 용접층
        Args:
        bIRooSur (bool): 루트 및 표면층
        fIThiWel (float): 용접층의 두께
        fIRooDis (float): 루트 간격
        fIWidWel (float): 용접층의 폭

        Returns:
        sOLayWel (str): 단일전극 서브머지드 아크용접의 용접층
        pass_fail (bool): 용접 3.6.2 단일전극 서브머지드아크용접 (4)의 판단 결과
        """
        assert isinstance(bIRooSur, bool)
        assert isinstance(fIThiWel, float)
        assert isinstance(fIRooDis, float)
        assert isinstance(fIWidWel, float)

        if bIRooSur == False:
          if fIThiWel <= 6:
            if fIRooDis >= 12 or fIWidWel > 16:
              pass_fail = False
              sOLayWel = "다중패스의 층분할 기법을 적용"
            else:
              pass_fail = True
              sOLayWel = None
          elif fIThiWel > 6:
            pass_fail = False
            sOLayWel = None
        else:
          pass_fail = None
          sOLayWel = None

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "sOLayWel": sOLayWel,
                }
            )