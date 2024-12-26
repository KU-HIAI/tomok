import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04030202_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관 응력 상관계수'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관 응력 상관계수]
	  B["KDS 14 31 25 4.3.2.2 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarOut1[/출력변수: 주강관 응력상관계수/] ;
	  VarIn1[/입력변수: 유요성비/]
		VarIn2[/입력변수: 폭비/]
		VarOut1 ~~~ VarIn1 & VarIn2
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2 (3)"])
		C --> Variable_def

    E(["<img src='https://latex.codecogs.com/svg.image?Q_{f}=1.3-0.4U/\beta_{eff}\leq&space;1'>----------------------------------------------------------"]) ;
    D[간격 k형 접합에서 주장관이 압축인 경우]

		Variable_def --> D --> E
    """

    @rule_method
    def Cast_steel_pipe_stress_correlation_coefficient(fIbetaef,fIPu,fIMu,fIAg,fIFc,fIS) -> RuleUnitResult:
        """주강관 응력 상관계수

        Args:
            fIbetaef (float): 유효폭 비
            fIPu (float): 주강관의 소요압축강도
            fIMu (float): 주강관의 소요휨강도
            fIAg (float): 주강관의 총단면적
            fIFc (float): 설계응력
            fIS (float): 주강관의 탄성단면계수

        Returns:
            fOQf (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2 각형강관 (3)의 값 1
            fOU (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2 각형강관 (3)의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2 각형강관 (3)의 판단 결과
        """

        assert isinstance(fIbetaef, float)
        assert fIbetaef != 0
        assert isinstance(fIPu, float)
        assert isinstance(fIMu, float)
        assert isinstance(fIAg, float)
        assert fIAg != 0
        assert isinstance(fIFc, float)
        assert fIFc != 0
        assert isinstance(fIS, float)
        assert fIS != 0

        fOU = abs(fIPu / (fIAg * fIFc) + fIMu / (fIS * fIFc))
        fOQf = 1.3 - 0.4 * fOU / fIbetaef

        if fOQf <= 1:
          return RuleUnitResult(
              result_variables = {
                  "fOQf": fOQf,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )