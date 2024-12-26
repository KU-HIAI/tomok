import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040203(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '아치형 파형강판 구조물의 설계압축력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 설계압축력] ;
		B["KDS 14 31 10 4.5.4.2.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 설계압축력/] ;
      VarIn1[/입력변수: 고정하중에 의한 압축력/] ;
      VarIn2[/입력변수: 활하중에 의한 압축력/] ;
      VarIn3[/입력변수: 지진하중에 의한 압축력/] ;
      VarIn4[/입력변수: 고정하중 하중계수/] ;
      VarIn5[/입력변수: 활하중 하중계수/] ;
      VarIn6[/입력변수: 지진하중 하중계수/] ;
      VarIn7[/입력변수: 충격계수/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.4.2.3"]) --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?T_{f}=\alpha&space;_{D}T_{D}&plus;max\left\{\alpha&space;_{L}T_{L}(1&plus;i),\alpha&space;_{E}T_{E}\right\}>---------------------------------------------------------"]
		Variable_def --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?T_{f}>------"])
    """


    @rule_method
    def design_compression_force(fITD,fITL,fITE,fIalphaD,fIalphaL,fIalphag,fIi) -> RuleUnitResult:
        """아치형 파형강판 구조물의 설계압축력

        Args:
            fITD (float): 고정하중에 의한 압축력
            fITL (float): 활하중에 의한 압축력
            fITE (float): 지진하중에 의한 압축력
            fIalphaD (float): 고정하중 하중계수
            fIalphaL (float): 활하중 하중계수
            fIalphag (float): 지진하중 하중계수
            fIi (float): 충격계수

        Returns:
            fOTf (float): 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3 설계압축력의 값
        """

        assert isinstance(fITD, float)
        assert isinstance(fITL, float)
        assert isinstance(fITE, float)
        assert isinstance(fIalphaD, float)
        assert isinstance(fIalphaL, float)
        assert isinstance(fIalphag, float)
        assert isinstance(fIi, float)


        fOTf = fIalphaD * fITD + max(fIalphaL * fITL* (1 + fIi), fIalphag * fITE)

        return RuleUnitResult(
            result_variables = {
              "fOTf": fOTf,
            }
        )