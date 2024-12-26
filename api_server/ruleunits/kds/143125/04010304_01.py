import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010304_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.4 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '볼트의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.4 지압접합에서 인장과 전단의 조합
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 볼트의 설계강도]
    B["KDS 14 31 25 4.1.3.4 (1)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
  	VarOut1[/출력변수: 볼트의 설계강도/]
    VarOut2[/출력변수: 전단응력의 효과를 고려한 공칭 인장강도/]
  	VarIn1[/입력변수: 저항계수/]
  	VarIn2[/입력변수: 공칭인장강도/]
  	VarIn3[/입력변수: 공칭전단강도/]
    VarIn4[/입력변수: 소요전단응력/]
  	VarOut1 & VarOut2 ~~~ VarIn2 & VarIn3 & VarIn4
  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.3.4 (1)"])
		C --> Variable_def

	  Variable_def --> D --> E

	  D["<img src='https://latex.codecogs.com/svg.image?F_{nt}`=1.3F_{nt}-\frac{F_{nt}}{\phi&space;F_{nv}}f_v\leq&space;F_{nt}'>-----------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?R_n=F_{nt}`A_b'>--------------------"])
    """

    @rule_method
    def design_strength_of_bolt(fIphi,fIFnt,fIFnv,fIfv,fIAb) -> RuleUnitResult:
        """볼트의 설계강도

        Args:
            fIphi (float): 저항계수
            fIFnt (float): 공칭인장강도
            fIFnv (float): 공칭전단강도
            fIfv (float): 소요전단응력
            fIAb (float): 볼트, 또는 나사 강봉의 나사가 없는 부분의 공칭단면적 (mm^2)

        Returns:
            fORn (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.4 지압접합에서 인장과 전단의 조합 (1)의 값 1
            fOFntpri (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.4 지압접합에서 인장과 전단의 조합 (1)의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.4 지압접합에서 인장과 전단의 조합 (1)의 판단 결과
        """

        assert isinstance(fIphi, float)
        assert fIphi != 0
        assert isinstance(fIFnt, float)
        assert isinstance(fIFnv, float)
        assert fIFnv != 0
        assert isinstance(fIfv, float)
        assert isinstance(fIAb, float)

        fOFntpri = (1.3)*fIFnt-fIFnt/(fIphi*fIFnv)*fIfv
        fORn = fOFntpri*fIAb

        if fOFntpri <= fIFnt:
          return RuleUnitResult(
              result_variables = {
                  "fORn": fORn,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )