import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030204(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.4'
    ref_date = '2017-12-20'
    doc_date = '2024-02-15'
    title = '조합력을 받는 접합부'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.4 T, X형 접합에서 지강관의 휨모멘트와 압축력의 조합
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 조합력을 받는 접합부]
	  B["KDS 14 31 25 4.1.4.4(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarIn1[/입력변수: 지강관의 항복강도/] ;
    VarIn2[/입력변수: 휨축에 대한 지강관의 소성단면계수/] ;
    VarIn3[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
    VarIn4[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
    VarIn5[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
    VarIn6[/입력변수: 지강관의 두께/] ;
    end

    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

    Python_Class ~~~ C(["KDS 14 31 25 4.1.4.4(1)"])
		C --> Variable_def

	  E{"<img src='https://latex.codecogs.com/svg.image?(P_{u}/\phi&space;P_{n})&plus;(M_{u-ip}/\phi&space;M_{n-ip})^{2}&plus;(M_{u-op}/\phi&space;M_{n-op})\leq&space;1.0'>------------------------------------------------------------------------------------------------------------------------------------------------"} ;
    Variable_def-->E-->D(["PASS or Fail"])
    """

    @rule_method
    def connection_that_receives_load_combination(fIPu,fIphiPn,fIMuip,fIphiMni,fIMuop,fIphiMno) -> RuleUnitResult:
        """조합력을 받는 접합부

        Args:
            fIPu (float): 주강관의 소요축강도
            fIphiPn (float): 설계강도
            fIMuip (float): 지강관의 소요 면내 휨강도
            fIphiMni (float): 면내 설계휨강도
            fIMuop (float): 지강관의 소요 면외 휨강도
            fIphiMno (float): 면외 설계휨강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.4 T, X형 접합에서 지강관의 휨모멘트와 압축력의 조합의 판단 결과
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIphiPn, float)
        assert fIphiPn != 0
        assert isinstance(fIMuip, float)
        assert isinstance(fIphiMni, float)
        assert fIphiMni != 0
        assert isinstance(fIMuop, float)
        assert isinstance(fIphiMno, float)
        assert fIphiMno != 0

        if fIPu/fIphiPn + (fIMuip/fIphiMni)**2 + (fIMuop/fIphiMno) <=1.0:
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