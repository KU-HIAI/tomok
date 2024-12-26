import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060208_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.6.2.8 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-13'
    title = '단부보의 설계에 사용되는 활하중 휨모멘트'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.8 종방향 단부보
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단부보의 설계에 사용되는 활하중 휨모멘트];
    B["KDS 24 10 11 4.6.2.8 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 활하중 휨모멘트/];
    VarIn1[/입력변수 : 윤하중/];
    VarIn2[/입력변수 : 종방향 단부보의 지간/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.2.8 (2)"])
		C --> Variable_def

    E{"바닥판 구분"};
    F["활하중 휨모멘트=0.10PL"];
    G["활하중 휨모멘트=0.08PL"];
    H(["활하중 휨모멘트"]);
    Variable_def--->E--단순판--->F--->H
    E--연속판--->G--->H
    """

    @rule_method
    def Live_load_bending_moment(fIllbemA,fIllbemB,fIP,fIL) -> RuleUnitResult:
        """단부보의 설계에 사용되는 활하중 휨모멘트

        Args:
            fIllbemA (float): 활하중 휨모멘트(단순판)
            fIllbemB (float): 활하중 휨모멘트(연속판)
            fIP (float): 윤하중
            fIL (float): 종방향 단부보의 지간

        Returns:
            fOllbem (float): 교량 설계 일반사항(한계상태설계법) 4.6.2.8 종방향 단부보 (2)의 값
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법) 4.6.2.8 종방향 단부보 (2)의 판단 결과

        """

        assert isinstance(fIP, float)
        assert isinstance(fIL, float)

        if fIllbemA != 0 and fIllbemB == 0 :
          fOllbem = 0.10 * fIP * fIL
          return RuleUnitResult(
              result_variables = {
                  "fOllbem": fOllbem,
              }
          )
        elif fIllbemA == 0 and fIllbemB != 0 :
          fOllbem = 0.08 * fIP * fIL
          return RuleUnitResult(
              result_variables = {
                  "fOllbem": fOllbem,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )