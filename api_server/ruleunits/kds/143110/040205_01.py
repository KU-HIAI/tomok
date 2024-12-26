import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040205_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.5 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '유효세장비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.5 단일ㄱ형강 압축부재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 단일ㄱ형강 압축부재] ;
		B["KDS 14 31 10 4.2.5(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 유효세장비/]
    VarIn1[/입력변수: 부재길이/]
    VarIn2[/입력변수: 접합된 다리와 평행한 축에 대한 단면2차반경/]
    VarIn3[/입력변수: 다리길이의 비/]
    VarIn4[/입력변수: ㄱ형강의 긴 쪽 다리의 길이/]
    VarIn5[/입력변수: ㄱ형강의 짧은 쪽 다리의 길이/]
    VarIn6[/입력변수: 약축에 대한 단면2차반경/]
    VarIn1~~~ VarIn4
    VarOut1~~~ VarIn2~~~ VarIn5
    VarIn3~~~ VarIn6

		end

		Python_Class ~~~ C(["KDS 14 31 10 4.2.5(1)"])
		C --> Variable_def

    N["등변ㄱ형강 또는 긴 다리로 접합된 부등변ㄱ형강이 단일 부재이거나 또는 평면트러스의 웨브재로 인접한 웨브재와 거셋플레이트 또는 현재의 동일면에 접합된 경우"] ;
    D{"<img src='https://latex.codecogs.com/svg.image?0\leq\frac{L}{r_{x}}\leq&space;80'>---------------------------------------------------------"} ;
    E{"<img src='https://latex.codecogs.com/svg.image?\frac{L}{r_{x}}>80'>-----------------------------------------"} ;
    F["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=72&plus;0.75\frac{L}{r_{x}}'>-----------------------------------------------------------------------"] ;
    G["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=32&plus;1.25\frac{L}{r_{x}}\leq&space;200'>-------------------------------------------------------------------------------"] ;
    H{"부등변ㄱ형강에서 다리길이의 비가 1.7이하이고 ㄱ형가의 짧은 다리가 접합된 경우"} ;
    I["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=72&plus;0.75\frac{L}{r_{x}}&plus;4[(b_{1}/b_{2})^{2}-1]\geq&space;0.95\frac{L}{r_{z}}'>-----------------------------------------------------------------------"] ;
    J["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=32&plus;1.25\frac{L}{r_{x}}&plus;4[(b_{1}/b_{2})^{2}-1]\geq&space;0.95\frac{L}{r_{z}}'>-----------------------------------------------------------------------"] ;
    K{"<img src='https://latex.codecogs.com/svg.image?0\leq\frac{L}{r_{x}}\leq&space;80'>---------------------------------------------------------"} ;
    L{"<img src='https://latex.codecogs.com/svg.image?\frac{L}{r_{x}}>80'>-----------------------------------------"} ;
		M(["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}'>---------------------------------------------------------"]) ;
    Variable_def-->N
    N-->H-->NO
    H-->YES
    NO-->D-->F
    NO-->E-->G
    YES-->K-->I
    YES-->L-->J
		F & G & I & J --> M
    """

    @rule_method
    def effective_slender_ratio(fIKLrA,fIKLrB,fIL,fIrx,fIlelera,fIbI,fIbs,fIrz) -> RuleUnitResult:
        """유효세장비

        Args:
            fIKLrA (float): 유효세장비
            fIKLrB (float): 유효세장비 (ㄱ형강의 짧은 다리가 접합되는 경우)
            fIL (float): 부재길이
            fIrx (float): 접합된 다리와 평행한 축에 대한 단면2차반경
            fIlelera (float): 다리길이의 비
            fIbI (float): ㄱ형강의 긴 쪽 다리의 길이
            fIbs (float): ㄱ형강의 짧은 쪽 다리의 길이
            fIrz (float): 약축에 대한 단면2차반경

        Returns:
            fOKLr (float): 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (1)의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (1)의 판단 결과 1
            sOnone (string): 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (1)의 판단 결과 2
        """

        assert isinstance(fIL, float)
        assert isinstance(fIrx, float)
        assert fIrx > 0
        assert isinstance(fIlelera, float)
        assert isinstance(fIbI, float)
        assert isinstance(fIbs, float)
        assert isinstance(fIrz, float)

        if fIKLrA != 0 and fIKLrB == 0 :
          if 0 <= fIL/fIrx <= 80 :
            fOKLr = 72 + 0.75 * fIL/fIrx
          elif fIL/fIrx > 80:
            fOKLr = min(32 + 1.25 * fIL / fIrx, 200)
          return RuleUnitResult(
              result_variables = {
                  "fOKLr": fOKLr,
              }
          )

        elif fIlelera <= 1.7 and fIKLrA == 0 and fIKLrB != 0 :
          if 0 <= fIL/fIrx <= 80 :
            fOKLr = max(72 + 0.75 * fIL / fIrx + 4*((fIbI / fIbs)**2 - 1), 0.95 * fIL / fIrz)
          elif fIL/fIrx > 80 :
            fOKLr = max(min(32 + 1.25 * fIL / fIrx, 200) + 4*((fIbI/fIbs)**2 - 1), 0.95 * fIL / fIrz)
          return RuleUnitResult(
              result_variables = {
                  "fOKLr": fOKLr,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )