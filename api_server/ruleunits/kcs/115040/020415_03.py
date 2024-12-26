import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020415_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.4.15 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '인발시험 시 가설말뚝을 기준점으로 하는 경우 기준점의 위치'

    description = """
    말뚝재하시험
    2. 시험
    2.4 인발재하시험
    2.4.15 기준점 및 기준보
    (3)
    """
    content = """
    #### 2.4.15 기준점 및 기준보
    (3) 가설말뚝을 기준점으로 하는 경우 시험말뚝으로부터 그 지름의 5배 이상 또는 2 m 이상, 반력말뚝으로부터 그 지름의 3배 이상 떨어진 위치에 설치하는 것을 원칙으로 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험 시 가설말뚝을 기준점으로 하는 경우 기준점의 위치];
    B["KCS 11 50 40 2.4.15 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.4.15 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 기준점과 시험말뚝의 거리/];
    VarIn2[/입력변수: 기준점과 반력말뚝의 거리/];
    VarIn3[/입력변수: 시험말뚝 지름/];
    VarIn4[/입력변수: 반력말뚝 지름/];
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E{"기준점과 시험말뚝의 거리 >= max(시험말뚝 지름 * 5, 2000mm) \n & 기준점과 반력말뚝의 최소거리 >= 반력말뚝 지름 * 3"}
    E --> End([Pass or Fail])
    """

    @rule_method
    def distance_reference_point(fITesDia, fIReaDia, fIDisPil_1, fIDisPil_2)-> RuleUnitResult:
        """
        Args:
            fITesDia (float): 시험말뚝 지름
            fIReaDia (float): 반력말뚝 지름
            fIDisPil_1 (float): 기준점과 시험말뚝의 거리
            fIDisPil_2 (float): 기준점과 반력말뚝의 거리

        Returns:
            pass_fail (bool): 말뚝재하시험 2.4.15 기준점 및 기준보 (3)의 판단 결과
        """
        assert isinstance(fITesDia, float)
        assert isinstance(fIReaDia, float)
        assert isinstance(fIDisPil_1, float)
        assert isinstance(fIDisPil_2, float)

        if fIDisPil_1 >= max(fITesDia * 5, 2000) and fIDisPil_2 >= fIReaDia * 3:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                    })
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                    })