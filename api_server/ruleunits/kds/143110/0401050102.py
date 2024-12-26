import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0401050102(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.5.1.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '전단파단에 대한 공칭인장강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.1.2 유효단면적에 대한 전단파단
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 전단파단에 대한 공칭인장강도] ;
		B["KDS 14 31 10 4.1.5.1.2"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 전단파단에 대한 공칭인장강도/]
    VarIn1[/입력변수: 인장강도/]
    VarIn2[/입력변수: 유효단면적/]
    VarIn3[/입력변수: 관구멍의 연단으로부터 힘의 방향과 평행하게 측정한 부재의 연단까지 최단거리/]
    VarIn4[/입력변수: 핀직경/]
    VarIn5[/입력변수: 판재의 두께/]
		end

		Python_Class ~~~ C1(["KDS 14 31 10 4.1.5.1.2"])---> Variable_def
	  C(["<img src='https://latex.codecogs.com/svg.image?P_{n}=0.6F_{u}A_{sf}'>-------------------------------------"]) ;
	  D["<img src='https://latex.codecogs.com/svg.image?A_{sf}=2t(a&plus;d/2)(mm^{2})'>------------------------------------------------------"] ;
	  Variable_def-->D-->C
    """

    @rule_method
    def Nominal_tensile_strength_against_shear_fracture(fIFu,fIAsf,fIa,fId,fIt) -> RuleUnitResult:
        """전단파단에 대한 공칭인장강도

        Args:
            fIFu (float): 인장강도
            fIAsf (float): 유효단면적
            fIa (float): 핀구멍의 연단으로부터 힘의 방향과 평행하게 측정한 부재의 연단까지 최단거리
            fId (float): 핀직경
            fIt (float): 판재의 두께

        Returns:
            fOPn (float): 강구조부재설계기준(하중저항계수설계법)  4.1.5.1.2 유효단면적에 대한 전단파단의 값
        """

        assert isinstance(fIFu, float)
        assert isinstance(fIAsf, float)
        assert isinstance(fIa, float)
        assert isinstance(fId, float)
        assert isinstance(fIt, float)

        fIAsf = 2 * fIt * (fIa + fId/2)
        fOPn = 0.6 * fIFu * fIAsf

        return RuleUnitResult(
            result_variables = {
              "fOPn": fOPn,
            }
        )