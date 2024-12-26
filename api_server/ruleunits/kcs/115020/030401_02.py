import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_030401_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 3.4.1 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '강널말뚝 세우기'

    description = """
    널말뚝
    3. 시공
    3.4 강널말뚝
    3.4.1 세우기
    (2)
    """
    content = """
    ####3.4.1 세우기
    (2) 말뚝 세우기에 앞서 말뚝 매기를 완전히 행하고 상향 속도를 10m/min 정도로 권양하여야 하며, 세우기가 완료된 때의 말뚝의 연직에 대한 기울기 허용오차는 말뚝길이의 1/100 이내가 되어야 한다
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 강널말뚝 세우기];
    B["KCS 11 50 20 3.4.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.4.1 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 완전한 말뚝 매기/];
    VarIn2[/"입력변수: 10m/min 정도의 상향 속도"/];
    VarIn3[/"입력변수: 기울기 허용오차"/];
    VarIn4[/"입력변수: 말뚝 길이"/];
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"완전한 말뚝 매기 \n 10m/min 정도의 상향 속도 \n 기울기 허용오차 < 말뚝길이/100 \n."}
    C --> End([Pass or Fail])
    """

    @rule_method
    def pile_setup(bIPilDri, bIUpwVel,fITolGra,fIPilLen) -> RuleUnitResult:
        """
        Args:
            bIPilDri (bool): 완전한 말뚝 매기
            bIUpwVel (bool): 10m/min 정도의 상향 속도
            fITolGra (float): 기울기 허용오차
            fIPilLen (float): 말뚝 길이

        Returns:
            pass_fail (bool): 널말뚝 3.4.1 세우기 (2)의 판단 결과
        """
        assert isinstance(bIPilDri, bool)
        assert isinstance(bIUpwVel, bool)
        assert isinstance(fITolGra, float)
        assert isinstance(fIPilLen, float)
        assert fITolGra < fIPilLen

        if bIPilDri == True and bIUpwVel == True and fITolGra < fIPilLen/100:
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