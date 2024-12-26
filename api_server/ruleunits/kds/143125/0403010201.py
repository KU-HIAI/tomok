import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010201(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.2.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '국부항복 한계상태에 관한 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.2 축직각방향 집중하중
    4.3.1.2.1 원형강관
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 국부항복 한계상태에 관한 설계강도]
	  B["KDS 14 31 25 4.3.1.2.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 국부항복한계상태에 관한 설계강도/]
	  VarIn2[/입력변수: 강재의 항복강도/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 접합평면과 90도를 이루는 판폭/]
	  VarIn5[/입력변수: 원형 강관의 외경/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
	  VarIn7[/입력변수: 원형 강관의 외경/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.2.1"])
		C --> Variable_def

	  Variable_def --> H --> D
	  H["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n=F_yt^2[5.5/(1-0.81B_p/D)]Q_f'>------------------------------------------------------------------------------------"]
	  D(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>------------------------"])
    """

    @rule_method
    def Design_strength_for_local_yield_limit_state(fIFy,fIt,fIBp,fID,fIQf) -> RuleUnitResult:
        """국부항복 한계상태에 관한 설계강도

        Args:
            fIFy (float): 강재의 항복강도
            fIt (float): 주강관의 두께
            fIBp (float): 접합평면과 90°를 이루는 판폭
            fID (float): 원형 강관의 외경
            fIQf (float): 주관-응력상관변수

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.2.1 원형강관의 값
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIBp, float)
        assert isinstance(fID, float)
        assert fID != 0
        assert isinstance(fIQf, float)

        fOphiRn = fIFy * (fIt ** 2) * (5.5 / (1 - 0.81 * (fIBp / fID))) * fIQf

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )