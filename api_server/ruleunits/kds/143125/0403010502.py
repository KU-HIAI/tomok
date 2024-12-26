import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010502(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.5.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '한 개의 벽체에 대한 국부 크리플링 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.5 각형강관의 단부 마구리판에 작용하는 축방향 집중하중
    4.3.1.5.2 한 개의 벽체에 대한 국부 크리플링 한계상태
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 한 개의 벽체에 대한 국부 크리플링 한계상태]
	  B["KDS 14 31 25 4.3.1.5.2"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 국부크리플링 한계상태/]
	  VarIn1[/입력변수: 저항계수/]
	  VarIn2[/입력변수: 벽체의 두께/]
	  VarIn3[/입력변수: 집중하중이 작용하는 폭/]
	  VarIn4[/입력변수: 접합평면과 90도를 이루는 각형 강관폭/]
	  VarIn5[/입력변수: 판재의 두께/]
	  VarIn6[/입력변수: 강재의 탄성계수/]
	  VarIn7[/입력변수: 강재의 항복강도/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.5.2"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?R_n=0.8t^2\left[1&plus;(6N/B)(t/t_p)^{1.5}\right]\left[EF_yt_p/t\right]^{0.5}'>-----------------------------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    @rule_method
    def Local_crippling_limit_state(fIt,fIN,fIB,fItp,fIE,fIFy) -> RuleUnitResult:
        """한 개의 벽체에 대한 국부 크리플링 한계상태

        Args:
            fIt (float): 벽체의 두께
            fIN (float): 집중하중이 작용하는 폭
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fItp (float): 판재의 두께
            fIE (float): 강재의 탄성계수
            fIFy (float): 강재의 항복강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.5.2 한 개의 벽체에 대한 국부 크리플링 한계상태의 판단 결과
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.5.2 한 개의 벽체에 대한 국부 크리플링 한계상태의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.5.2 한 개의 벽체에 대한 국부 크리플링 한계상태의 값 2
        """

        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fIN, float)
        assert fIN != 0
        assert isinstance(fIB, float)
        assert fIB != 0
        assert isinstance(fItp, float)
        assert fItp > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIFy, float)
        assert fIFy > 0

        fORn = 0.8 * fIt ** 2 * (1 + (6 * fIN / fIB) * (fIt / fItp) ** 1.5) * (fIE * fIFy * fItp / fIt) ** 0.5
        fOphi = 0.75

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
            }
        )