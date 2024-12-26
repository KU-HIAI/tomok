import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040504020503(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.2.5.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '완공 후 검토'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.5 휨모멘트와 압축력에 의한 소성힌지
    4.5.4.2.5.3 완공 후 검토
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 완공 후 검토] ;
		B["KDS 14 31 10 4.5.4.2.5.3"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 토피고 H와 Dh/2 중 작은 값/] ;
    VarOut2[/출력변수: 파형강판의 소성압축강도/] ;
    VarOut3[/출력변수: 지간 및 토피고에 따른 하중감소계수/] ;
    VarOut4[/출력변수: 상부 아치 정점부까지 고정하중에 의한 휨모멘트/] ;
    VarOut5[/출력변수: 상부 아치 정점부 위의 고정하중에 의한 휨모멘트/] ;
    VarOut6[/출력변수: 완공 후 활하중에 의한 휨모멘트/] ;
    VarOut7[/출력변수: 파형강판의 소성모멘트강도/] ;
    VarOut8[/출력변수: 완공 후 작용하는 휨모멘트/] ;
    VarIn1[/입력변수: 설계압축력/] ;
    VarIn2[/입력변수: 완공 후 소성힌지저항계수/] ;
    VarIn3[/입력변수: 파형강판의 단면적/] ;
    VarIn4[/입력변수: 파형강판의 항복강도/] ;
    VarIn5[/입력변수: 고정하중 하중계수/] ;
    VarIn6[/입력변수: 활하중 하중계수/] ;
    VarIn7[/입력변수: 충격계수/] ;
    VarIn8[/입력변수: 하중조합 규정에 명시된 하중계수/] ;
    VarIn9[/입력변수: 구조물 스프링라인 사이 거리/] ;
    VarIn10[/입력변수: 구조물과 흙의 휨강성비/] ;
    VarIn11[/입력변수: 시공 중 검토식 참조/] ;
    VarIn12[/입력변수: 차량축하중/] ;
    VarIn13[/입력변수: 등가선하중 환산계수/] ;
    VarIn14[/입력변수: 파형강판의 소성단면계수/] ;
		end

		VarOut1 & VarOut2 & VarOut3 & VarOut4 ~~~ VarOut5 & VarOut6 & VarOut7 & VarOut8 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14

		Python_Class ~~~ C(["KDS 14 31 10 4.5.4.2.5.3"])
		C --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?\left(\frac{T_{f}}{P_{pf}}\right)^{2}&plus;\left|\frac{M}{M_{pf}}\right|\leq&space;1>------------------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{f}=\alpha&space;_{D}\left|M_{1}&plus;M_{D}\right|&plus;\alpha&space;_{L}M_{L}(1&plus;i)=K_{m1}R_{B}\gamma&space;D_{h}^{3}-K_{m2}R_{B}\gamma&space;D_{h}^{2}H_{e}&plus;K_{m3}R_{U}D_{h}A_{L}/k_{4}>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?P_{pf}=\phi&space;_{h}AF_{y}>------------------------------------------"]
		S["<img src=https://latex.codecogs.com/svg.image?M_{pf}=\phi&space;_{h}ZF_{y}>------------------------------------------"]
		Z["<img src=https://latex.codecogs.com/svg.image?H_{e}=Min(H,D_{h}/2)>------------------------------------------------"]

		Variable_def --> R --> Z --> W --> S --> Q --> X(["PASS or Fail"])
    """


    @rule_method
    def Review_after_completion(fITf,fIphih,fIA,fIFy,fIalphaD,fIalphaL,fIi,fIgamma,fIDh,fINf,fIH,fIKm1,fIKm2,fIKm3,fIRB,fIAL,fIk4,fIZ) -> RuleUnitResult:
        """완공 후 검토

        Args:
            fITf (float): 설계압축력
            fIphih (float): 완공 후 소성힌지저항계수
            fIA (float): 파형강판의 단면적
            fIFy (float): 파형강판의 항복강도
            fIalphaD (float): 고정하중 하중계수
            fIalphaL (float): 활하중 하중계수
            fIi (float): 충격계수
            fIgamma (float): 하중조합 규정에 명시된 하중계수
            fIDh (float): 구조물 스프링라인 사이 거리
            fINf (float): 구조물과 흙의 휨강성비
            fIH (float): 설계토피고
            fIKm1 (float): 시공 중 검토식 참조
            fIKm2 (float): 시공 중 검토식 참조
            fIKm3 (float): 시공 중 검토식 참조
            fIRB (float): 시공 중 검토식 참조
            fIAL (float): 차량축하중
            fIk4 (float): 등가선하중 환산계수
            fIZ (float): 파형강판의 소성단면계수

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 판단 결과
            fOPpf (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 1
            fOMf (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 2
            fOM1 (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 3
            fOMD (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 4
            fOML (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 5
            fOHe (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 6
            fORU (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 7
            fOMpf (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.2.5.3 완공 후 검토의 값 8
        """

        assert isinstance(fITf, float)
        assert isinstance(fIphih, float)
        assert fIphih != 0
        assert isinstance(fIA, float)
        assert fIA != 0
        assert isinstance(fIFy, float)
        assert fIFy != 0
        assert isinstance(fIalphaD, float)
        assert isinstance(fIalphaL, float)
        assert isinstance(fIi, float)
        assert isinstance(fIgamma, float)
        assert isinstance(fIDh, float)
        assert fIDh > 0
        assert isinstance(fINf, float)
        assert fINf >= 0
        assert isinstance(fIH, float)
        assert fIH > 0
        assert isinstance(fIKm1, float)
        assert isinstance(fIKm2, float)
        assert isinstance(fIKm3, float)
        assert isinstance(fIRB, float)
        assert isinstance(fIAL, float)
        assert isinstance(fIk4, float)
        assert fIk4 != 0
        assert isinstance(fIZ, float)
        assert fIZ != 0

        import math

        if fIH > 3.0 :
          fIk4 == 4.9

        fOHe = min(fIH, fIDh / 2)
        fOPpf = fIphih * fIA * fIFy
        fORU = min((0.265 - 0.053 * math.log10(fINf)) / (fIH / fIDh)**0.75 , 1.0)
        fOM1 = fIKm1 * fIRB * fIgamma * fIDh**3
        fOMD = - 1 * fIKm2 * fIRB * fIgamma * fIDh**2 * fOHe
        fOML = fIKm3 * fORU * fIDh * fIAL / fIk4
        fOMpf = fIphih * fIZ * fIFy
        fOMf = fIalphaD * abs(fOM1 + fOMD) + fIalphaL * fOML * (1 + fIi)

        if (fITf / fOPpf) ** 2 + abs(fOMf / fOMpf) <= 1:
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