import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04110304(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.11.3.4'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '설계휨강도 검토'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.3 강바닥판
    4.11.3.4 횡방향휨
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전체인장을 받는 바닥판 검토];
    B["KDS 24 14 31 4.11.3.4"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarIn1[/입력변수: 설계하중에 의해 가로보에 작용되는 모멘트/] ;
    VarIn2[/입력변수: 가로보의 설계휨강도/];
    VarIn3[/입력변수: 인접리브로부터 전달되는 축중하중에 의한 바닥판의 휨방향설계모멘트/];
    VarIn4[/입력변수: 인접리브로부터 전달되는 축중하중에 의한 바닥판의 휨방향설계휨강도/];

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
		end

		Python_Class ~~~ C(["KDS 24 14 31 4.11.3.4"])
		C --> Variable_def

		G{"<img src='https://latex.codecogs.com/svg.image?\frac{M_{fb}}{M_{rb}}&plus;\frac{M_{ft}}{M_{rt}}\leq&space;1.0'>-----------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?\frac{M_{fb}}{M_{rb}}\leq&space;1.0'>---------------------"}

		E{"가로보의 간격 &ge;종방향리브의 복부판 간격x3"}

		Variable_def --> E
		E --yes--> D
		E --No--> C

		G & D --> F([Pass or fail])
    """

    @rule_method
    def Examine_the_Design_bending_strength(fIMfb,fIMrb,fIMft,fIMrt,fIsphobe,fIspaplr) -> RuleUnitResult:
        """설계휨강도 검토

        Args:
            fIMfb (float): 설계하중에 의해 가로보에 작용되는 모멘트
            fIMrb (float): 가로보의 설계휨강도
            fIMft (float): 인접리브로부터 전달되는 축중하중에 의한 바닥판의 횡방향 설계모멘트
            fIMrt (float): 인접리브로부터 전달되는 축중하중에 의한 바닥판의 횡방향 설계휨강도
            fIsphobe (float): 가로보의 간격
            fIspaplr (float): 종방향리브의 복부판 간격

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.11.3.4 횡방향휨의 판단 결과
        """

        assert isinstance(fIMfb, float)
        assert isinstance(fIMrb, float)
        assert fIMrb != 0
        assert isinstance(fIMft, float)
        assert isinstance(fIMrt, float)
        assert fIMrt != 0
        assert isinstance(fIsphobe, float)
        assert isinstance(fIspaplr, float)

        if fIsphobe < 3*fIspaplr :
          if (fIMfb/fIMrb) + (fIMft/fIMrt) <= 1.0 :
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        else:
          if fIMfb/fIMrb <= 1.0 :
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )