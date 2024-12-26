import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_030203_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 3.2.3 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '안내보의 설치 높이'

    description = """
    널말뚝
    3. 시공
    3.2 시공준비
    3.2.3 안내보
    (3)
    """
    content = """
    ####3.2.3 안내보
    (3) 안내보의 설치 높이는 강널말뚝의 타입을 완료했을 때 햄머가 안내보에 닿지 않도록 강널말뚝의 타입 목표 높이보다 300mm~500mm 정도 낮은 위치에 설치하여야 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 안내보의 설치 높이];
    B["KCS 11 50 20 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.2.3 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 안내보의 설치 높이/];
    VarIn2[/입력변수: 강널말뚝의 타입 목표 높이/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강널말뚝의 타입 목표 높이 - 500mm \n < 안내보의 설치 높이 \n < 강널말뚝의 타입 목표 높이 - 300mm\n."}
    C --> End([Pass or Fail])
    """

    @rule_method
    def install_height(fIHeiGui, fIHeiPil) -> RuleUnitResult:
        """
        Args:
            fIHeiGui (float): 안내보의 설치 높이
            fIHeiPil (float): 강널말뚝의 타입 목표 높이

        Returns:
            pass_fail (bool): 널말뚝 3.2.3 안내보 (3)의 판단 결과
        """
        assert isinstance(fIHeiGui, float)
        assert isinstance(fIHeiPil, float)


        if fIHeiGui >= fIHeiPil-500 and fIHeiGui <= fIHeiPil-300:
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