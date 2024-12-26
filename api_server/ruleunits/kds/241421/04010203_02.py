import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계전단강도];
    B["KDS 24 14 21 4.1.2.3 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 수직 스트럽이 배치된 부재의 설계전단강도/];
    VarIn1[/입력변수: 축력이 작용하지 않는 경우의 최대설계전단강도/];
    VarIn2[/입력변수: 축방향 압축력이 작용하는 경우의 최대설계전단강도/];
    VarIn3[/입력변수: 복부 철근의 항복을 기준으로 한 설계전단강도/];
    VarIn4[/입력변수: 철근의 재료저항계수/];
    VarIn5[/입력변수: 전단철근의 항복강도/];
    VarIn6[/입력변수: 전단 철근량/];
    VarIn7[/입력변수: 단면 내부 팔길이/];
		VarIn8[/입력변수: 전단철근 간격/];
		VarIn9[/입력변수: 부재 복부에 형성된 스트럿의 경사각/];
		VarIn10[/입력변수: 콘크리트 압축강도 유효계수/];
		VarIn11[/입력변수: 콘크리트의 재료저항계수/];
		VarIn12[/입력변수: 단면의 복부폭/];
		VarIn13[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn14[/입력변수: 철근의 기준항복강도/];
		VarIn15[/입력변수: 최대 허용 전단철근량/];

		VarOut1~~~
		VarIn1 & VarIn2  & VarIn3 & VarIn4 & VarIn5 ~~~
     VarIn6 & VarIn7 & VarIn8  & VarIn9 & VarIn10 ~~~
		VarIn11 & VarIn12 & VarIn13 & VarIn14 & VarIn15

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (2)"])
		C --> Variable_def

		H{"<img src='https://quicklatex.com/cache3/97/ql_4ec634d81b39d282f737e8d3e810a397_l3.png'>---------------------------------"}
		D{프리스트레스 포함하여 축방향 압축력이 작용}
		E{"<img src='https://latex.codecogs.com/svg.image?V_{sd} \leq V_{d,max,com}'>---------------------------------"}
		F["<img src='https://latex.codecogs.com/svg.image?V_{sd}=\frac{\phi&space;_{s}f_{vy}A_{v}z}{s}(cot\theta)'>---------------------------------"]
		G{축력작용}
		I{"<img src='https://quicklatex.com/cache3/d3/ql_8201491d5351607ec3116d7b81a360d3_l3.png'>---------------------------------"}
		J([Pass or Fail])
		M([Pass or Fail])
		N([Pass or Fail])

		Variable_def ---> H ---> J
		Variable_def ---> D ---> E ---> M
		Variable_def ---> G --No ---> I ---> N
		G -- yes ---> F ---> N
		E~~~ |"KDS 24 14 21 4.1.2.3 (4)"| E
    """

    @rule_method
    def Design_shear_strength(fIVdmaxc,fIphis,fIphic,fIfvy,fIAv,fIz,fIs,fItheta,fInu,fIfy,fIfck,fIbw,fIAvmax) -> RuleUnitResult:
        """설계전단강도

        Args:
            fIVdmaxc (float): 축방향 압축력이 작용하는 경우의 최대설계전단강도
            fIphis (float): 철근의 재료저항계수
            fIphic (float): 콘크리트의 재료저항계수
            fIfvy (float): 전단철근의 항복강도
            fIAv (float): 전단 철근량
            fIz (float): 단면 내부 팔길이
            fIs (float): 전단철근 간격
            fItheta (float): 부재 복부에 형성된 스트럿의 경사각
            fInu (float): 콘크리트 압축강도 유효계수
            fIfy (float): 철근의 기준항복강도
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도
            fIbw (float): 단면의 복부폭
            fIAvmax (float): 최대 허용 전단철근량

        Returns:
            fOVd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (2)의 값 1
            fOVsd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (2)의 값 2
            fOVdmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (2)의 값 3
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (2)의 판단 결과
        """

        assert isinstance(fIVdmaxc, float)
        assert isinstance(fIphis, float)
        assert isinstance(fIphic, float)
        assert isinstance(fIfvy, float)
        assert isinstance(fIAv, float)
        assert isinstance(fIz, float)
        assert isinstance(fIs, float)
        assert fIs != 0
        assert isinstance(fItheta, float)
        assert fItheta > 0
        assert isinstance(fInu, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIbw, float)
        assert isinstance(fIAvmax, float)

        import math

        fOVsd = fIphis * fIfvy * fIAv * fIz / ( fIs * math.tan(math.radians(fItheta)))
        fOVd = fOVsd
        fOVdmax = fInu * fIphic * fIfck * fIbw * fIz / (
            1 / math.tan(math.radians(fItheta)) + math.tan(math.radians(fItheta)))

        # 축력이 작용하지 않는 경우, fIVdmaxc(축방향 압축력이 작용하는 경우의 최대설계전단강도)에 0이 입력됨
        if fIVdmaxc == 0:
            if fIphis * fIfy * fIAvmax / (fIbw * fIs) <= 0.5 * fInu * fIphic * fIfck and fOVd <= fOVdmax:
                return RuleUnitResult(
                    result_variables={
                        "fOVd": fOVd,
                        "fOVsd": fOVsd,
                        "fOVdmax": fOVdmax,
                        "pass_fail": True,
                    }
                )
            else:
                return RuleUnitResult(
                    result_variables={
                        "pass_fail": False,
                    }
                )

        # 축력이 작용하는 경우
        else:
            # Vdmaxc가 미정인 경우: 4.1.2.2.4에서 계산될 예정이므로, 4.1.2.2.4에게 fOVdmax 값을 넘김
            if fIVdmaxc == -9999:
                return RuleUnitResult(
                    result_variables={
                        "fOVd": fOVd,
                        "fOVsd": fOVsd,
                        "fOVdmax": fOVdmax,
                        "pass_fail": -9999,
                    }
                )
            # Vdmaxc가 정해져 있는 경우에는 pass_fail을 결정 가능
            else:
                if fOVd <= fIVdmaxc:
                    return RuleUnitResult(
                        result_variables={
                            "fOVd": fOVd,
                            "fOVsd": fOVsd,
                            "fOVdmax": fIVdmaxc,
                            "pass_fail": True,
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables={
                            "fOVd": fOVd,
                            "fOVsd": fOVsd,
                            "fOVdmax": fIVdmaxc,
                            "pass_fail": False,
                        }
                    )