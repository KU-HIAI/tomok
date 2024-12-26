import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010202_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계전단강도];
    B["KDS 24 14 21 4.1.2.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
    VarOut2[/출력변수: 전단길이의 시작점부터 검토하는 단면까지의 거리와 프리스트레싱 긴장재의 전달길이의 비/];
    VarOut3[/출력변수: 축응력/];
		VarIn1[/입력변수: 단면2차모멘트/];
		VarIn2[/입력변수: 도심축 위쪽 단면의 도심축에 대한 단면1차모멘트/];
		VarIn3[/입력변수: 전달길이의 시작점부터 검토하는 단면까지의거리/];
		VarIn4[/입력변수: 전단길이의 시작점부터 검토하는 단면까지의 거리와 프리스트레싱 긴장재의 전달길이의 비/];
		VarIn5[/입력변수: 프리스트레싱 긴장재의 전달길이/];
		VarIn6[/입력변수: 축력/];
		VarIn7[/입력변수: 주인장 철근량/];
		VarIn8[/입력변수: 철근의 재료계수/];
		VarIn9[/입력변수: 철근의 기준항복강도/];
		VarIn10[/입력변수: 단면적/];
    VarIn11[/입력변수: 단면의 복부 폭/];
    VarIn12[/입력변수: 콘크리트 재료계수/];
    VarIn13[/입력변수: 콘크리트 인장강도/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.2 (2)"])
		C --> Variable_def

		Variable_def--->G
		Variable_def--->D

		G & D---->E--->F
		G["<img src='https://latex.codecogs.com/svg.image?&space;f_{n}=(N_{u}-A_{s}\phi&space;_{s}f_{y})/A_{c}'>---------------------------------"]

		D["<img src='https://latex.codecogs.com/svg.image?\alpha&space;_{l}=l_{x}/l_{tp2}'>---------------------------------"]

		E["<img src='https://latex.codecogs.com/svg.image?V_{cd}=\frac{Ib_{w}}{Q}\sqrt{(\phi&space;_{c}f_{ctk})^{2}&plus;\alpha&space;_{l}f_{n}\phi&space;_{c}f_{ctk}}'>---------------------------------"]
		F(["전단강도"])
    """

    @rule_method
    def design_shear_strength(fIalphaA,fIalphaB,fII,fIQ,fIIx,fIlpt2,fINu,fIAs,fIphis,fIfy,fIAc,flbw,fIphic,fIfctk) -> RuleUnitResult:
        """설계전단강도

        Args:
            fIalphaA (float): 전단길이의 시작점부터 검토하는 단면까지의 거리와 프리스트레싱 긴장재의 전달길이의 비 (프리텐션 부재)
            fIalphaB (float): 전단길이의 시작점부터 검토하는 단면까지의 거리와 프리스트레싱 긴장재의 전달길이의 비 (기타 프리스트레스트 부재)
            fII (float): 단면2차모멘트
            fIQ (float): 도심축 위쪽 단면의 도심축에 대한 단면1차모멘트
            fIIx (float): 전달길이의 시작점부터 검토하는 단면까지의거리
            fIlpt2 (float): 프리스트레싱 긴장재의 전달길이
            fINu (float): 축력
            fIAs (float): 주인장 철근량
            fIphis (float): 철근의 재료계수
            fIfy (float): 철근의 기준항복강도
            fIAc (float): 단면적
            flbw (float): 단면의 복부 폭
            fIphic (float): 콘크리트 재료계수
            fIfctk (float): 콘크리트 인장강도

        Returns:
            fOVcd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (2)의 값 1
            fOalpha (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (2)의 값 2
            fOfn (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (2)의 값 3
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (2)의 판단 결과
        """

        assert isinstance(fII, float)
        assert isinstance(fIQ, float)
        assert fIQ != 0
        assert isinstance(fIIx, float)
        assert isinstance(fIlpt2, float)
        assert fIlpt2 != 0
        assert isinstance(fINu, float)
        assert isinstance(fIAs, float)
        assert isinstance(fIphis, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIAc, float)
        assert fIAc != 0
        assert isinstance(flbw, float)
        assert isinstance(fIphic, float)
        assert isinstance(fIfctk, float)

        fOfn = (fINu - fIAs * fIphis * fIfy) / fIAc

        if fIalphaA != 0 and fIalphaB == 0 :
          fOalpha = fIIx / fIlpt2
          fOVcd = fII * flbw / fIQ * (((fIphic * fIfctk)**2 + fOalpha * fOfn * fIphic * fIfctk)**0.5) / 1000
          if fOalpha <= 0.1 :
            return RuleUnitResult(
                result_variables = {
                    "fOVcd": fOVcd,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        if fIalphaA == 0 and fIalphaB != 0 :
          fOalpha = 1.0
          fOVcd = fII * flbw / fIQ * (((fIphic * fIfctk)**2 + fOalpha * fOfn * fIphic * fIfctk)**0.5) / 1000
          return RuleUnitResult(
              result_variables = {
                  "fOVcd": fOVcd,
              }
          )