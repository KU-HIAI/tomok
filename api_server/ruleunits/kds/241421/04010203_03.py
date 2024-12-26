import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계전단강도];
    B["KDS 24 14 21 4.1.2.3 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 경사 전단철근이 배치된 부재의 설계전단강도/];
		VarOut2[/출력변수: 축력이 작용하지 않는 경우의 최대설계전단강도/];
    VarIn1[/입력변수: 최대 허용 전단철근량/];
		VarIn2[/입력변수: 축방향 압축력이 작용하는 경우의 최대설계전단강도/];
		VarIn3[/입력변수: 철근의 재료저항계수/];
		VarIn4[/입력변수: 전단철근의 항복강도/];
		VarIn5[/입력변수: 전단 철근량/];
		VarIn6[/입력변수: 단면 내부 팔길이/];
		VarIn7[/입력변수: 전단철근 간격/];
		VarIn8[/입력변수: 부재 복부에 형성된 스트럿의 경사각/];
		VarIn9[/입력변수: 경사전단철근과 주인장철근 사이의 경사각/];
		VarIn10[/입력변수: 콘크리트 압축강도 유효계수/];
		VarIn11[/입력변수: 콘크리트의 재료저항계수/];
		VarIn12[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn13[/입력변수: 단면의 복부폭/];
		VarIn14[/입력변수: 철근의 기준항복강도/];


		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    VarIn2 ~~~ VarIn3 & VarIn4 & VarIn5
    VarIn4 ~~~ VarIn6 & VarIn7 & VarIn8
		VarIn7~~~ VarIn9 & VarIn10 & VarIn11
		VarIn10~~~VarIn11 & VarIn12 & VarIn13
		VarIn12~~~VarIn14

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (3)"])
		C --> Variable_def

		Variable_def--축력이 작용하지 않을때 -->H--->D--->E
		Variable_def--축방향 압축력--->F
		Variable_def--최대 허용전단철근량---> G
		E & F & G--->K
		H["<img src='https://latex.codecogs.com/svg.image?V_{sd}=\frac{\phi&space;_sf_{vy}A_vz}{s}(cot\theta&plus;cot\alpha)sin\alpha&space;'>---------------------------------"]
		D["<img src='https://quicklatex.com/cache3/2d/ql_018aa671eb116bfe4dfe1af3de9e752d_l3.png'>---------------------------------"]
		E{"<img src='https://latex.codecogs.com/svg.image?V_{sd}\leq&space;V_{d,max}'>------------------------------"}
		F{"<img src='https://latex.codecogs.com/svg.image?V_{sd}\leq&space;V_{d,max,com}'>---------------------------------"}
		G{"<img src='https://quicklatex.com/cache3/4a/ql_b9b65e664704b4e372bb1b332f544e4a_l3.png'>---------------------------------"}

		K(["설계전단강도"])
    """

    @rule_method
    def Design_shear_strength(fIVdmaxc,fIphis,fIphic,fIfvy,fIAv,fIz,fIs,fItheta,fIalpha,fInu,fIfck,fIbw,fIfy,fIAvmax) -> RuleUnitResult:
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
            fIalpha (float): 경사전단철근과 주인장철근 사이의 경사각
            fInu (float): 콘크리트 압축강도 유효계수
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도
            fIbw (float): 단면의 복부폭
            fIfy (float): 철근의 기준항복강도
            fIAvmax (float): 최대 허용 전단철근량

        Returns:
            fOVsd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (3)의 값 1
            fOVdmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (3)의 값 2
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (3)의 판단 결과
        """

        # 일단은 -9999가 ellipsis를 대체함. 나중에 수정하도록 할 것.
        assert isinstance(fIVdmaxc, float) or fIVdmaxc is ...  # 미결정된 경우 ...(ellipsis)가 입력됨을 가정
        assert isinstance(fIphis, float)
        assert isinstance(fIphic, float)
        assert isinstance(fIfvy, float)
        assert isinstance(fIAv, float)
        assert isinstance(fIz, float)
        assert isinstance(fIs, float)
        assert fIs != 0
        assert isinstance(fItheta, float)
        assert fItheta != 0
        assert isinstance(fIalpha, float)
        assert fIalpha != 0
        assert isinstance(fInu, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIbw, float)
        assert fIbw != 0
        assert isinstance(fIAvmax, float)

        import math

        fOVsd = fIphis * fIfvy * fIAv * fIz / fIs * (
            1/math.tan(math.radians(fItheta)) + 1/math.tan(math.radians(fIalpha))) * math.sin(
            math.radians(fIalpha))
        fOVdmax = fInu * fIphic * fIfck * fIbw * fIz * (
            1 / math.tan(math.radians(fItheta)) + 1 / math.tan(math.radians(fIalpha))) / (
            1 + (1 / math.tan(math.radians(fItheta))) ** 2)

        # 축력이 작용하지 않는 경우, fIVdmaxc(축방향 압축력이 작용하는 경우의 최대설계전단강도)에 0이 입력됨
        if fIVdmaxc == 0:
            if fIphis * fIfy * fIAvmax / ( fIbw * fIs) <= 0.5 * fInu * fIphic * fIfck * math.sin(math.radians(fIalpha)) / ( 1- math.cos(math.radians(fIalpha))) and fOVsd <= fOVdmax :
                return RuleUnitResult(
                    result_variables={
                        "fOVsd": fOVsd,
                        "fOVdmax": fOVdmax,
                        "pass_fail": True,
                    }
                )
            else:
                return RuleUnitResult(
                    result_variables={
                        "fOVsd": fOVsd,
                        "fOVdmax": fOVdmax,
                        "pass_fail": False,
                    }
                )

        # 축력이 작용하는 경우
        else:
            # Vdmaxc가 미정인 경우: 4.1.2.2.4에서 계산될 예정이므로, 4.1.2.2.4에게 fOVdmax 값을 넘김
            # if fIVdmaxc is ...:
            if fIVdmaxc == -9999:
                return RuleUnitResult(
                    result_variables={
                        "fOVsd": fOVsd,
                        "fOVdmax": fOVdmax,
                        "pass_fail": -9999,  # fIVdmaxc를 알아야 구할 수 있음
                    }
                )
            else:
                if (fIphis * fIfy * fIAvmax / (fIbw * fIs) <=
                    0.5 * fInu * fIphic * fIfck * math.sin(math.radians(fIalpha)) /
                    (1 - math.cos(math.radians(fIalpha))) and
                        fOVsd <= fIVdmaxc):
                    return RuleUnitResult(
                        result_variables={
                            "fOVsd": fOVsd,
                            "fOVdmax": fOVdmax,
                            "pass_fail": True,
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables={
                            "fOVsd": fOVsd,
                            "fOVdmax": fOVdmax,
                            "pass_fail": False,
                        }
                    )