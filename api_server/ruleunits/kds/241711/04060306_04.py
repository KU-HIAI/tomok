import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060306_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.6 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '축방향철근 중심각 수평간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.6 결합나선철근
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 축방향철근 중심각 수평간격];
    B["KDS 24 17 11 4.6.3.6 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 축방향철근 중심 각 수평간격/] ;
    VarIn2[/입력변수: 축방향철근/];
    end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.3.6 (4)"])
		C --> Variable_def-->D--> I

    D{" 200mm &ge; 축방향철근 중심간 수평간격 and 결합부분 축방향철근 배근 &ge; 4개"}
   	I([Pass or Fail])
    """

    @rule_method
    def axial_reinforcing_bar(fIcahsar,fIlonrei) -> RuleUnitResult:
        """축방향철근 중심각 수평간격

        Args:
            fIcahsar (float): 축방향철근 중심간 수평간격
            fIlonrei (float): 축방향철근

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.3.6 결합나선철근 (4)의 판단 결과 1
            sOfilwel (string): 교량내진설계기준(한계상태설계법) 4.6.3.6 결합나선철근 (4)의 판단 결과 2
        """

        assert isinstance(fIcahsar, float)
        assert isinstance(fIlonrei, float)

        if fIcahsar <= 200 :
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "결합부분에는 최소한 4개 이상의 축방향철근을 배근",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "결합부분에는 최소한 4개 이상의 축방향철근을 배근",
                  "pass_fail": False,
              }
          )