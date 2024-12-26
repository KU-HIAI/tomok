import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04010202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.3.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '순단면적'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.2 단면적의 산정
    4.1.2.2 순단면적
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[순단면적] ;
		B["KDS 14 31 10 4.1.2.2(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 순단면적/]
    VarIn1[/입력변수: 부재의 총단면적/]
    VarIn2[/입력변수: 인장력에 의한 파단선상에 있는 구멍의 수/]
    VarIn3[/입력변수: 연결재 구멍의 직경/]
    VarIn4[/입력변수: 부재의 두께/]
		end

		Python_Class ~~~ Variable_def
  	C["정열배치"] ;
    D(["<img src='https://latex.codecogs.com/svg.image?A_{n}=A_{g}-ndt'>-----------------------------------"])
    Variable_def --> C -->D
    """

    @rule_method
    def net_area(fOAn,fIAg,fIn,fId,fIt) -> RuleUnitResult:
        """순단면적

        Args:
            fOAn (float): 순단면적
            fIAg (float): 부재의 총단면적
            fIn (float): 인장력에 의한 파단선상에 있는 구멍의 수
            fId (float): 연결재 구멍의 직경
            fIt (float): 부재의 두께

        Returns:
            fOAn (float): 강구조부재설계기준(하중저항계수설계법)  4.1.2.2 순단면적 (1)의 값
        """
        assert isinstance(fOAn, float)
        assert isinstance(fIAg, float)
        assert isinstance(fIn, float)
        assert isinstance(fId, float)
        assert isinstance(fIt, float)

        fOAn = fIAg - fIn*fId*fIt

        return RuleUnitResult(
            result_variables = {
                "fOAn": fOAn,
            }
        )