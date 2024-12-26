import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040504020303(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.2.3.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '지진하중에 의한 압축력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
    4.5.4.2.3.3 지진하중에 의한 압축력
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 지진하중에 의한 압축력] ;
		B["KDS 14 31 10 4.5.4.2.3.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 지진하중에 의한 압축력/] ;
      VarIn1[/입력변수: 고정하중에 의한 압축력/] ;
      VarIn2[/입력변수: 수직가속도계수/] ;
      VarIn3[/입력변수: 수평가속도계수/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.4.2.3.3"]) --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?T_{E}=T_{D}A_{V}>-----------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?A_{V}=\frac{2}{3}A_{H}>-----------------------------------"]

		Variable_def --> W --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?T_{E}>---------"])
    """


    @rule_method
    def Compressive_force_due_to_seismic_load(fITD,fIAV,fIAH) -> RuleUnitResult:
        """지진하중에 의한 압축력

        Args:
            fITD (float): 고정하중에 의한 압축력
            fIAV (float): 수직가속도계수
            fIAH (float): 수평가속도계수

        Returns:
            fOTE (float): 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3.3 지진하중에 의한 압축력의 값
        """

        assert isinstance(fITD, float)
        assert isinstance(fIAV, float)
        assert isinstance(fIAH, float)


        if fIAV == 0:
          fIAV = (2 / 3) * fIAH
        else:
          fIAV = fIAV

        fOTE = fITD * fIAV

        return RuleUnitResult(
            result_variables = {
              "fOTE": fOTE,
            }
         )