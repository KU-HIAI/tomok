import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030203_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.2.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '사질토의 무리말뚝 침하'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.2 사용한계상태의 변위와 지지력
    3.3.2.3 침하
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 침하];
    B["KDS 24 14 51 3.3.2.3 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:사질토의 무리말뚝 침하/]
		VarIn1[/입력변수:2Db/3지점에 작용하는 순 기초압력/]
		VarIn2[/입력변수:무리말뚝의 폭이나 최소치수/]
		VarIn3[/입력변수:무리말뚝의 침하/]
		VarIn4[/입력변수:무리말뚝의 유효근입깊이에 대한 영향계수/]
		VarIn5[/입력변수:유효깊이/]
		VarIn6[/입력변수:지지층에 근입된 말뚝의 길이/]
		VarIn7[/입력변수:SPT의 타격횟수로서 상재하중에 대해 보정한 대표적인 평균값/]
		VarIn8[/입력변수:침하층에서 측정된 SPT의 타격횟수/]
		VarIn9[/입력변수:유효연직응력/]
		VarIn10[/입력변수:등가확대기초아래 임의의 깊이 z에 대한 평균 정적 콘 저항값/]

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4 ~~~ VarIn5
		VarIn6 ~~~ VarIn7 ~~~ VarIn8 ~~~ VarIn9 ~~~ VarIn10


    end
		Python_Class ~~~ G(["KDS 24 14 51 3.3.2.3 (3)"])
		G --> Variable_def;

		C["<img src='https://latex.codecogs.com/svg.image?-0.125\frac{D\prime}{X}\geq&space;0.5'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?&space;SPT=\rho=\frac{30qI\sqrt{X}}{N_{corr}}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?N_{corr}=[0.77log_{10}(\frac{1.92}{\sigma_{v}^{'}})]N'>---------------------------------"]
		F([사질토에 설치된 무리말뚝의 침하])

		Variable_def ---> C & E ---> D --->F
    """

    @rule_method
    def the_sedimentation_of_sandstones(fIq,fIx,fIp,fIdp,fIdb,fIn,fIeffstr,fIqc,fIlacscA,fIlacscB) -> RuleUnitResult:
        """사질토의 무리말뚝 침하

        Args:
            fIq (float): 2Db/3 지점에 작용하는 순 기초압력
            fIx (float): 무리말뚝의 폭이나 최소치수
            fIp (float): 무리말뚝의 침하
            fIdp (float): 유효깊이
            fIdb (float): 지지층에 근입된 말뚝의 길이
            fIn (float): 침하층에서 측정된 SPT의 타격횟수
            fIeffstr (float): 유효연직응력
            fIqc (float): 등가 확대기초 아래 임의의 깊이 z에 대한 평균 정적 콘저항값
            fIlacscA (float): 사질토에 설치된 무리말뚝의 침하 (SPT의 경우)
            fIlacscB (float): 사질토에 설치된 무리말뚝의 침하 (CPT 경우)

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3 침하 (3)의 판단 결과
            fOspt (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3 침하 (3)의 값 1
            fOcpt (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3 침하 (3)의 값 2
            fONcorr (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3 침하 (3)의 값 3
            fOi (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3 침하 (3)의 값 4
        """

        assert isinstance(fIq, float)
        assert isinstance(fIx, float)
        assert isinstance(fIp, float)
        assert isinstance(fIdp, float)
        assert isinstance(fIdb, float)
        assert isinstance(fIn, float)
        assert isinstance(fIeffstr, float)
        assert isinstance(fIqc, float)
        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)


        fONcorr = (0.77 * math.log10(1.92 / fIeffstr)) * fIn
        fOi = 1 - 0.125 * fIdp / fIx

        if fIlacscA == 0 and fIlacscB != 0 :
          fOspt = 30 * fIq * fOi * fIx ** 0.5 / fONcorr
          return RuleUnitResult(
              result_variables = {
                  "fOspt": fOspt,
                  }
              )
        elif fIlacscA != 0 and fIlacscB == 0 :
          fOcpt = fIq * fIx * fOi / (24 * fIqc)
          return RuleUnitResult(
              result_variables = {
                  "fOcpt": fOcpt,
                  }
              )