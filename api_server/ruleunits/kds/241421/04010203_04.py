import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '최대설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대설계전단강도];
    B["KDS 24 14 21 4.1.2.3 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 축방향 압축력이 작용하는 경우의 최대설계전단강도/];
    VarOut2[/출력변수: 최대 설계전단강도 계산 보정계수/];
		VarIn1[/입력변수: 수직 스터럽 또는 경사 스터럽이 배치된 부재의 설계전단강도/];
		VarIn2[/입력변수: 축력이 작용하지 않을 경우의 최대설계전단강도/];
		VarIn3[/입력변수: 계수하중에 의해 단면에 유발된 평균압축응력/];
		VarIn4[/입력변수: 콘크리트의 재료저항계수/];
		VarIn5[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (4)"])
		C --> Variable_def

		Variable_def--->L--->F
		Variable_def--->D--->G
		Variable_def--->E--->H
		F & G & H--->I--->J
		L{"<img src='https://latex.codecogs.com/svg.image?&space;0<f_{n}\leq&space;0.25\phi&space;_cf_{ck};'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?0.25\phi&space;_cf_{ck}<f_n\leq&space;0.5\phi&space;_{c}f_{ck}'>---------------------------------"}
		E{"<img src='https://latex.codecogs.com/svg.image?0.5\phi&space;_{c}f_{ck}<f_{n}\leq&space;1.0\phi&space;_cf_{ck}'>------------------------------"}
		F["<img src='https://latex.codecogs.com/svg.image?\alpha_{cw}=(1&plus;f_n/\phi&space;_cf_{ck})'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?\alpha_{cw}=1.25'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?\alpha_{cw}=2.5(1-f_n/\phi&space;_cf_{ck})'>---------------------------------"]
		I["<img src='https://latex.codecogs.com/svg.image?V_{d,max,com}=\alpha&space;_{cw}V_{d,max}'>---------------------------------"]
		J(["<img src='https://latex.codecogs.com/svg.image?V_{d,max,com}'>---------------------------------"])
    """

    @rule_method
    def maximum_design_shear_strength(fIVsd, fIVdmax, fIfn, fIphic, fIfck) -> RuleUnitResult:
        """최대설계전단강도

        Args:
            fIVsd (float): 수직 스터럽 또는 경사 스터럽이 배치된 부재의 설계전단강도
            fIVdmax (float): 축력이 작용하지 않을 경우의 최대설계전단강도
            fIfn (float):  계수하중에 의해 단면에 유발된 평균압축응력
            fIphic (float): 콘크리트의 재료저항계수
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도

        Returns:
            fOVdmaxc (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (4)의 값 1
            fOalphcw (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (4)의 값 2
        """

        # assert isinstance(fIVsd, float)
        assert isinstance(fIVdmax, float)
        assert isinstance(fIfn, float)
        assert isinstance(fIphic, float)
        assert fIphic != 0
        assert isinstance(fIfck, float)
        assert fIfck != 0

        if 0.25 * fIphic * fIfck < fIfn <= 0.5 * fIphic * fIfck:
            fOalphcw = 1.25
        elif 0.5 * fIphic * fIfck < fIfn <= 1.0 * fIphic * fIfck:
            fOalphcw = 2.5 * (1 - fIfn / (fIphic * fIfck))
        else:  # (컴퓨터학과 김정욱) 이렇게 예외 처리 안하고 구현해도 논리적으로 괜찮은지 의문임.
            fOalphcw = 1 + fIfn / (fIphic * fIfck)

        # fIVdmax가 미정일 경우 alpha만 계산 가능
        if fIVdmax == -9999:
            return RuleUnitResult(
                result_variables={
                    "fOVdmaxc": -9999,
                    "fOalphcw": -fOalphcw
                }
            )

        else:
            fOVdmaxc = fOalphcw * fIVdmax
            return RuleUnitResult(
                result_variables={
                    "fOVdmaxc": fOVdmaxc,
                    "fOalphcw": fOalphcw
                }
            )