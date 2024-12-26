import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04010202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.2.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '순단면적'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.2 단면적의 산정
    4.1.2.2 순단면적
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[순단면적] ;
		B["KDS 14 31 10 4.1.2.2 (2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 순단면적/]
    VarIn1[/입력변수: 부재의 총단면적/]
    VarIn2[/입력변수: 인장력에 의한 파단선상에 있는 구멍의 수/]
    VarIn3[/입력변수: 연결재 구멍의 직경/]
    VarIn4[/입력변수: 연결재 게이지선 사이의 응력 수직 방향 중심간격/]
    VarIn5[/입력변수: 식 4.1-2의 시그마 값/]
		end

		Python_Class ~~~ Variable_def
  	C["불규칙배치(엇모배치)인 경우"] ;
    D(["<img src='https://latex.codecogs.com/svg.image?&space;A_{n}=A_{g}-ndt&plus;\Sigma\frac{s^{2}}{4g}t&space;'>------------------------------------------------------"])
    Variable_def --> C -->D
    """

    @rule_method
    def net_area(fIAg,fIn,fId,fIt,fIsumstg) -> RuleUnitResult:
        """순단면적

        Args:
            fIAg (float): 부재의 총단면적
            fIn (float): 인장력에 의한 파단선상에 있는 구멍의 수
            fId (float): 연결재 구멍의 직경
            fIt (float): 연결재 게이지선 사이의 응력 수직방향 중심간격
            fIsumstg (float): 식 4.1-2의 시그마 값

        Returns:
            fOAn (float): 강구조부재설계기준(하중저항계수설계법)  4.1.2.2 순단면적 (1)의 값
        """

        assert isinstance(fIAg, float)
        assert isinstance(fIn, float)
        assert isinstance(fId, float)
        assert isinstance(fIt, float)
        assert isinstance(fIsumstg, float)

        fOAn = fIAg - fIn*fId*fIt + fIsumstg

        return RuleUnitResult(
            result_variables = {
                "fOAn": fOAn,
            }
        )