import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0403030210_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.10 (5)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '합성플랜지에서 전단연결재 사이의 횡방향 최대간격'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.10 전단연결재
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 합성플랜지에서 전단연결재 사이의 횡방향 최대간격] ;
		B["KDS 14 31 10 4.3.3.2.10 (5)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 전단연결재 사이의 횡방향 최대간격/] ;
      VarIn2[/입력변수: 박스플랜지의 두께/] ;
      VarIn3[/입력변수: 플랜지의 최소항복강도/] ;
      VarIn4[/입력변수: 균일분포 수직응력에 대한 판의 좌굴계수/]
      VarIn5[/입력변수: 강재의 탄성계수/] ;
      VarIn6[/입력변수: 박스플랜지의 한계세장비/]
			end

			Python_Class ~~~ C1(["KDS 24 90 11 4.2.3.9"]) --> Variable_def
			VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

			C["<img src=https://latex.codecogs.com/svg.image?\frac{s_{t}}{t_{f}}\sqrt{\frac{F_{yf}}{kE}}\leq&space;R_{1}>--------------------------"]

			Variable_def --> C --> D(["PASS or Fail"])
    """

    @rule_method
    def Maximum_transverse_spacing_between_shear_connectors(fIst,fItf,fIFyf,fIk,fIE,fIR1) -> RuleUnitResult:
        """합성플랜지에서 전단연결재 사이의 횡방향 최대간격

        Args:
            fIst (float): 전단연결재 사이의 횡방향 최대간격
            fItf (float): 박스플랜지의 두께
            fIFyf (float): 플랜지의 최소항복강도
            fIk (float): 균일분포 수직응력에 대한 판의 좌굴계수
            fIE (float): 강재의 탄성계수
            fIR1 (float): 박스플랜지의 한계세장비

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.10 전단연결재 (5)의 통과여부
        """

        assert isinstance(fIst, float)
        assert isinstance(fItf, float)
        assert fItf != 0
        assert isinstance(fIFyf, float)
        assert fIFyf > 0
        assert isinstance(fIk, float)
        assert fIk > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIR1, float)

        if (fIst / fItf) * (fIFyf / (fIk * fIE)) ** 0.5 <= fIR1:
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