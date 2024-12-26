import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020302_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '콘크리트 인장 영역 내의 소요 최소 철근량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.2 최소철근량
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 인장 영역 내의 소요 최소 철근량];
    B["KDS 24 14 21 4.2.3.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 첫 균열 발생 직전 상태에서 계산된 콘크리트의인장영역단면적/];
		VarIn2[/입력변수: 첫 균열 발생 직후에 허용하는 철근의 인장응력/];
		VarIn3[/입력변수: 첫 균열이 발생할 때 유효한 콘크리트 인장강도/];
		VarIn4[/입력변수: 균열 발생 직전의 단면 내 응력 분포 상태를 반영하는계수/];
		VarIn5[/입력변수: 단면에 작용하는 평균 법선응력/];
		VarIn6[/입력변수: 단면에 작용하는 축력/];
		VarIn7[/입력변수: 단면 기준 깊이/];
		VarIn8[/입력변수: 단면 깊이/];
		VarIn9[/입력변수: 축력이 응력 분포에 미치는 영향을 반영하는 계수/];
		VarIn10[/입력변수: 플랜지에 균열이 처음 발생하기 직전에 부재전단면에작용하는휨모멘트와축력으로계산한플랜지의인장력/];
		VarIn11[/입력변수: 간접하중영향에 의해 부등 분포하는 응력의영향을반영하는계수/];
		VarIn12[/입력변수: 복부폭을 포함한 플랜지 너비/];
		VarOut1[/출력변수: 콘크리트 인장 영역 내의 소요 최소 철근량/]
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarIn2~~~ VarIn5 & VarIn6 & VarIn7 & VarIn8
		VarIn5~~~ VarIn9 & VarIn10 & VarIn11 & VarIn12
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.2 (2)"])
		C --> Variable_def

		Variable_def--->F
		M{"축력이 응력 분포에 미치는 영향을 반영하는 계수"}
		M--축력Nu가 압축력일때--->D
		D["철근의 인장응력≤<img src='https://latex.codecogs.com/svg.image?k_1=1.5'>---------------------------------"]
		M--축력Nu가 인장력일때--->E
		E["프리스트레스 강재의 응력≤<img src='https://latex.codecogs.com/svg.image?2h^*/3h'>---------------------------------"]
		F{단면 기준 깊이}
		G["<img src='https://latex.codecogs.com/svg.image?h^*=h'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?h^*=1.0m'>---------------------------------"]
		F--h<1.0일때--->G
		F--h≥1.0일때--->H
		G & H--->M
		I{"Kc=균열 발생 직전의 단면 내 응력 분포 상태를 반영하는 계수"}
		D -->I
		J["<img src='https://latex.codecogs.com/svg.image?K_c=1.0'>---------------------------------"]
		K["<img src='https://latex.codecogs.com/svg.image?0.4[1-\frac{f_n}{k(h/h^*)f_{ct}}]\leq&space;1'>---------------------------------"]
		L["<img src='https://latex.codecogs.com/svg.image?0.9\frac{N_{cr}}{A_{ct}f_{ct}}\geq&space;0.5'>---------------------------------"]
		I--순수인장을 받는 경우--->J
		I--휨과 축력을 받는 부재 복부--->K
		I--박스형이나 T형 단면 부재 플랜지--->L

		P{"k= 간접하중영향에 의해 부등 분포하는 응력의 영향을 반영하는 계수"}
		M["1.0"]
		N["0.65"]
		O["사이 값 보간"]
		Variable_def--->P
		P--면 깊이 또는 복부 폭을 포함한 플랜지 너비가 300mm 이하일 경우--->M
		P--단편 깊이 또는 복부 폭을 포함한 플랜지 너비가 800mm 이상일 경우--->N
		P--단편 깊이 또는 복부 폭을 포함한 플랜지 너비가 800mm 이상일 경우--->O
		E["<img src='https://latex.codecogs.com/svg.image?A_{s,min}=k_ckA_{ct}\frac{f_{ct}}{f_s}'>---------------------------------"]
		M & N & O & J & K & L--->E
		E--->Z
		Z(["콘크리트 인장 영역 내의 소요 최소 철근량"])
    """

    @rule_method
    def Minimum_amount_of_rebar_required_within_concrete_tensile_area(fIkcA,fIkcB,fIkcC,fIAct,fIfs,fIfct,fIfn,fINu,fINcr,fIh,fIflawid) -> RuleUnitResult:
        """콘크리트 인장 영역 내의 소요 최소 철근량

        Args:
            fIkcA (float): 균열 발생 직전의 단면 내 응력 분포 상태를 반영하는 계수 (순수인장을 받는 경우)
            fIkcB (float): 균열 발생 직전의 단면 내 응력 분포 상태를 반영하는 계수 (휨과 축력을 받는 부재 복부)
            fIkcC (float): 균열 발생 직전의 단면 내 응력 분포 상태를 반영하는 계수 (박스형이나 T형 단면 부재 플랜지)
            fIAct (float): 첫 균열 발생 직전 상태에서 계산된 콘크리트의 인장 영역 단면적
            fIfs (float): 첫 균열 발생 직후에 허용하는 철근의 인장응력
            fIfct (float): 첫 균열이 발생할 때 유효한 콘크리트 인장강도
            fIfn (float): 단면에 작용하는 평균 법선응력
            fINu (float): 단면에 작용하는 축력
            fINcr (float): 플랜지에 균열이 처음 발생하기 직전에 부재 전단면에 작용하는 휨모멘트와 축력으로 계산한 플랜지의 인장력
            fIh (float): 단면 깊이
            fIflawid (float): 복부폭을 포함한 플랜지 너비

        Returns:
            fOAsmin (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 값 1
            fOhstar (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 값 2
            fOk1 (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 값 3
            fOk (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 값 4
            fOkc (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 값 5
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (2)의 판단 결과
        """

        assert isinstance(fIAct, float)
        assert isinstance(fIfs, float)
        assert isinstance(fIfct, float)
        assert isinstance(fIfn, float)
        assert isinstance(fINu, float)
        assert isinstance(fINcr, float)
        assert isinstance(fIh, float)
        assert isinstance(fIflawid, float)

        if fIh < 1000:
          fOhstar = fIh
        else:
          fOhstar = 1000

        if fINu >= 0:
          fOk1 = 1.5
        else:
          fOk1 = 2 * fOhstar / ( 3 * fIh)

        if min(fIh, fIflawid) <= 300:
          fOk = 1.0
        elif max(fIh, fIflawid) >= 800:
          fOk = 0.65
        else:
          fOk = ((1.0-0.65)/(300-800)) * (min(fIh*1000, fIflawid) - 300) + 1.0

        if fIkcA != 0 and fIkcB == 0 and fIkcC == 0 :
          fOkc = 1.0
          fOAsmin = fOkc * fOk * fIAct * fIfct / fIfs
          return RuleUnitResult(
              result_variables = {
                  "fOAsmin": fOAsmin,
              }
          )

        if fIkcA == 0 and fIkcB != 0 and fIkcC == 0 :
          fOkc = 0.4 * ( 1 - fIfn/(fOk1 * fIh / fOhstar * fIfct))
          fOAsmin = fOkc * fOk * fIAct * fIfct / fIfs
          if fOkc <= 1.0 :
            return RuleUnitResult(
                result_variables = {
                    "fOAsmin": fOAsmin,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )

        if fIkcA == 0 and fIkcB == 0 and fIkcC != 0 :
          fOkc = 0.9 * fINcr / ( fIAct * fIfct )
          fOAsmin = fOkc * fOk * fIAct * fIfct / fIfs
          if fOkc >= 0.5 :
            return RuleUnitResult(
                result_variables = {
                    "fOAsmin": fOAsmin,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )