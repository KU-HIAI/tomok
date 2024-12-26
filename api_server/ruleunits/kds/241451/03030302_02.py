import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030302_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '말뚝의 감가된 지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.2 말뚝의 축방향 하중
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝의 감가된 지지력];
    B["KDS 24 14 51 3.3.3.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:말뚝의 감가된 지지력/]
		VarIn1[/입력변수:외말뚝의 지지력에 대한 저항계수/]
		VarIn2[/입력변수:외말뚝의 지지력/]
		VarIn3[/입력변수:말뚝의 선단지지력/]
		VarIn4[/입력변수:말뚝의 주면마찰력/]
		VarIn5[/입력변수:말뚝의 단위 선단지지력/]
		VarIn6[/입력변수:말뚝의 단위 주면 마찰력/]
		VarIn7[/입력변수:말뚝 주면면적/]
		VarIn8[/입력변수:말뚝 선단면적/]
		VarIn9[/입력변수:말뚝의 선단지지에 대한 저항계수/]
		VarIn10[/입력변수:말뚝의 주면마찰에 대한 저항계수/]

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4 ~~~ VarIn5
		VarIn6 ~~~ VarIn7 ~~~ VarIn8 ~~~ VarIn9 ~~~ VarIn10


    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.2 (2)"])
		C --> Variable_def;

		H["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{q}Q_{ult}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{qp}Q_{p}&plus;\phi&space;_{qs}Q_{s}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?Q_{p}=q_{p}A_{p}'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?Q_{s}=q_{s}A_{s}'>---------------------------------"]
		G([말뚝의 감가된 지지력])

		Variable_def ---> E & F ----> D
		Variable_def ---> H
		D & H ---> G
    """

    @rule_method
    def the_reduced_support_of_a_stake(fIphiq,fIQult,fIqp,fIqs,fIAs,fIAp,fIphiqp,fIphiqs) -> RuleUnitResult:
        """말뚝의 감가된 지지력

        Args:
            fIphiq (float): 외말뚝의 지지력에 대한 저항계수
            fIQult (float): 외말뚝의 지지력
            fIqp (float): 말뚝의 단위 선단지지력
            fIqs (float): 말뚝의 단위 주면마찰력
            fIAs (float): 말뚝 주면면적
            fIAp (float): 말뚝 선단면적
            fIphiqp (float): 말뚝의 선단지지에 대한 저항계수
            fIphiqs (float): 말뚝의 주면마찰에 대한 저항계수

        Returns:
            fOQR (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.2 말뚝의 축방향 하중 (2)의 값 1
            fOQp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.2 말뚝의 축방향 하중 (2)의 값 2
            fOQse (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.2 말뚝의 축방향 하중 (2)의 값 3
        """

        assert isinstance(fIphiq, float)
        assert isinstance(fIQult, float)
        assert isinstance(fIqp, float)
        assert isinstance(fIqs, float)
        assert isinstance(fIAs, float)
        assert isinstance(fIAp, float)
        assert isinstance(fIphiqp, float)
        assert isinstance(fIphiqs, float)

        fOQp = fIqp * fIAp
        fOQse = fIqs * fIAs

        if fIphiq != 0 and fIphiqp == 0 :
          fOQR = fIphiq * fIQult
          return RuleUnitResult(
              result_variables = {
                  "fOQR": fOQR,
              }
          )

        if fIphiq == 0 and fIphiqp != 0 :
          fOQR = fIphiqp * fOQp + fIphiqs * fOQse
          return RuleUnitResult(
              result_variables = {
                  "fOQR": fOQR,
              }
          )