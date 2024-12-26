import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030903_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.9.3 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '띠장과 접합부의 각도'

    description = """
    가설흙막이 공사
    3. 시공
    3.9 띠장, 버팀대, 중간말뚝, X-브레이싱
    3.9.3 버팀대(strut), 경사버팀대 및 경사고임대(레이커, raker)
    (2)
    """

    content = """
    #### 3.9.3. 버팀대(strut), 경사버팀대 및 경사고임대(레이커, raker)
    (2) 띠장과의 접합부는 부재축이 일치되고 수평이 유지되도록 설치하며, 수평오차가 ±30mm 이내에 있어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 띠장과 접합부의 각도];
    B["KCS 21 30 00 3.9.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.9.3 (2)"])

    subgraph Variable_def
    VarIn[/입력변수: 띠장과 접합부의 수평오차/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"|띠장과 접합부의 수평오차| <= 30"}

    C --> D([Pass or Fail])
    """

    @rule_method
    def Horizontal_Tolerance_of_Belt_and_Joint(fIHorTol) -> bool:
        """ 띠장과 접합부의 각도
        Args:
            fIHorTol (float): 띠장과 접합부의 수평 오차

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.9.3 버팀대(strut), 경사버팀대 및 경사고임대(레이커, raker) (2)의 판단 결과
        """
        assert isinstance(fIHorTol, float)

        if -30 <= fIHorTol <= 30:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )