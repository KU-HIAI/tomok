import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010403(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.4.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '블록전단강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.3 블록전단강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 블록전단강도]
	  B["KDS 14 31 25 4.1.4.3"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 설계강도/]
	  VarIn2[/입력변수: 공칭강도/]
	  VarIn3[/입력변수: 저항계수/]
	  VarIn4[/입력변수: 피접합체의 공칭인장강도/]
	  VarIn5[/입력변수: 유효전단단면적/]
	  VarIn6[/"입력변수: <img src='https://latex.codecogs.com/svg.image?U_{bs}'>--------"/]
	  VarIn7[/입력변수: 인장저항순단면적/]
	  VarIn8[/입력변수: 핀의항복강도/]
	  VarIn9[/입력변수: 전단력을 받는 총단면적/]
	  VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	  VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.4.3"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?R_n=\left\lceil0.6F_uA_{nv}&plus;U_{bs}F_uA_{nt}\right\rceil\leq\left\lceil&space;0.6F_yA_{gv}&plus;U_{bs}F_uA_{nt}\right\rceil'>------------------------------------------------------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>-----------"])
    """

    @rule_method
    def Block_shear_strength(fIFu,fIAnv,fIUbs,fIAnt,fIFy,fIAgv) -> RuleUnitResult:
        """블록전단강도

        Args:
            fIFu (float): 피접합재의 공칭인장강도
            fIAnv (float): 전단저항 순단면적
            fIUbs (float): 블록전단파단 계수
            fIAnt (float): 인장저항 순단면적
            fIFy (float): 핀의 항복강도
            fIAgv (float): 전단저항 총단면적

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.3 블록전단강도의 값 1
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.3 블록전단강도의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.3 블록전단강도의 판단 결과
        """

        assert isinstance(fIFu, float)
        assert isinstance(fIAnv, float)
        assert isinstance(fIUbs, float)
        assert isinstance(fIAnt, float)
        assert isinstance(fIFy, float)
        assert isinstance(fIAgv, float)

        fORn = 0.6 * fIFu * fIAnv + fIUbs * fIFu * fIAnt
        fOphiRn = fORn * 0.75

        if fORn <= 0.6 * fIFy * fIAgv + fIUbs * fIFu * fIAnt :
          return RuleUnitResult(
              result_variables = {
                  "fOphiRn": fOphiRn,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )