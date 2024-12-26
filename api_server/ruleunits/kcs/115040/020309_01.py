import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020309_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.3.9 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '동재하시험 시 시험말뚝의 두부 정리'

    description = """
    말뚝재하시험
    2. 시험
    2.3 동재하시험
    2.3.9 시험말뚝의 두부 정리
    (1)
    """
    content = """
    ####2.3.9 시험말뚝의 두부 정리
    (1) 선정된 시험말뚝은 지상 부분의 돌출길이가 3 D(D: 말뚝의 지름) 정도 되어야 하며, 말뚝 두부에 편심이 걸리지 않도록 표면에 요철이 없는 완전히 매끈한 상태를 유지하여야 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 동재하시험 시 시험말뚝의 두부 정리];
    B["KCS 11 50 40 2.3.9 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.3.9 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 시험말뚝의 두부 표면 정리/];
    VarOut2[/출력변수: 지상 부분의 돌출길이/];
    VarIn1[/입력변수: 말뚝의 지름/];
    VarOut1 & VarOut2 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D["지상 부분의 돌출길이 = \n 3*말뚝의 지름 정도"]
    Variable_def --> E["시험말뚝의 두부 표면 정리 = 말뚝 두부에 편심이 걸리지 않도록 \n 표면에 요철이 없는 완전히 매끈한 상태를 유지"]
    D & E --> End(["동재하시험 시 시험말뚝의 두부 정리"])
    """

    @rule_method
    def clearing_head_testpile(fIPilDia)-> RuleUnitResult:
        """
        Args:
            fIPilDia (float): 말뚝지름

        Returns:
            sOAboGro (str): 지상 부분의 돌출길이
            sOSurCle (str): 시험말뚝의 두부 표면 정리
        """
        assert isinstance(fIPilDia, float)
        assert fIPilDia>10

        sOSurCle = "말뚝 두부에 편심이 걸리지 않도록 표면에 요철이 없는 완전히 매끈한 상태를 유지"
        sOAboGro =  str(3*fIPilDia)+ " mm 정도"
        return RuleUnitResult(
            result_variables = {
                "sOAboGro": sOAboGro,
                "sOSurCle": sOSurCle,
                })