import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_030203_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 3.2.3 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '안내보 보조말뚝의 설치'

    description = """
    널말뚝
    3. 시공
    3.2 시공준비
    3.2.3 안내보
    (2)
    """
    content = """
    ####3.2.3 안내보
    (2) 시공법선에 따라 보조말뚝을 2열로 박고 (10m 간격) 보조말뚝 내측에 보조버팀대를 내측 간격이 강널말뚝을 꽉 물린 상태보다 20mm~50mm의 여유를 주도록 설치한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 안내보 보조말뚝의 설치];
    B["KCS 11 50 20 3.2.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.2.3 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 보조말뚝의 열/];
    VarIn2[/입력변수: 보조말뚝의 간격/];
    VarIn3[/입력변수: 보조버팀대 내측 간격/];
    VarIn4[/입력변수: 강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격/];
    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"보조말뚝의 열 = 2 & 보조말뚝의 간격 = 10 m &
    강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격 + 20 mm \n < 보조버팀대 내측 간격 \n < 강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격 + 50 mm \n."}
    C --> End([Pass or Fail])
    """

    @rule_method
    def supplementary_pile(nIRowPil, fIDisPil, fISpaStr_1, fISpaStr_2) -> RuleUnitResult:
        """
        Args:
            nIRowPil (int): 보조말뚝의 열
            fIDisPil (float): 보조말뚝의 간격
            fISpaStr_1 (float): 보조버팀대 내측 간격
            fISpaStr_2 (float): 강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격

        Returns:
            pass_fail (bool): 널말뚝 3.2.3 안내보 (2)의 판단 결과
        """
        assert isinstance(nIRowPil, int)
        assert isinstance(fIDisPil, float)
        assert isinstance(fISpaStr_1, float)
        assert isinstance(fISpaStr_2, float)


        if nIRowPil == 2 and fIDisPil == 10 and fISpaStr_1 > fISpaStr_2 + 20 and fISpaStr_1 < fISpaStr_2 + 50:
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