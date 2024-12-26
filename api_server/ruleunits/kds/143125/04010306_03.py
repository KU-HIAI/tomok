import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010306_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.6 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '미끄럼 한계상태에 대한 마찰접합의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.6 마찰접합의 미끄럼강도
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 미끄럼 한계상태에 대한 마찰접합의 설계강도]
	  B["KDS 14 31 25 4.1.3.6 (3)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 마찰접합의 설계강도/]
    VarIn1[/출력변수: 미끄럼계수/]
    VarIn2[/입력변수: 끼움재계수/]
    VarIn3[/입력변수: 고장력볼트의 설계볼트장력/]
    VarIn4[/입력변수: 전단면의 수/]
  	end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.3.6 (3)"])
		C --> Variable_def

	  Variable_def --> D & E & F --> G --> H

	  D["표준구멍 또는 하중방향에 수직인 단슬롯, Φ=1.00"]
	  E["과대구멍 또는 하중방향에 평행한 단슬롯, Φ=0.85"]
    F["장슬롯, Φ=0.70"]
    G["<img src='https://latex.codecogs.com/svg.image?R_n=\mu&space;h_fT_oN_s'>---------------------------------------------"]
    H(["<img src='https://latex.codecogs.com/svg.image?R_n'>------------"])
    """

    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fImu,fIhf,fITo,iINs,fIphi) -> RuleUnitResult:
        """미끄럼 한계상태에 대한 마찰접합의 설계강도

        Args:
            fImu (float): 미끄럼계수
            fIhf (float): 끼움재계수
            fITo (float): 고장력볼트의 설계볼트장력
            iINs (int): 전단면의 수
            fIphi (float): 저항계수

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.6 마찰접합의 미끄럼강도 (3)의 값
        """

        assert isinstance(fImu, float)
        assert fImu == (0.5 or 0.45)
        assert isinstance(fIhf, float)
        assert fIhf == (1.0 or 0.85)
        assert isinstance(fITo, float)
        assert isinstance(iINs, int)
        assert isinstance(fIphi, float)
        assert fIphi == (1.0 or 0.85 or 0.7)


        fOphiRn = fIphi * fImu * fIhf * fITo * iINs

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )