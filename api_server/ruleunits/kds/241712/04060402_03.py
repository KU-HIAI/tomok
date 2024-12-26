import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04060402_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.6.4.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '전단성능'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.4 주탑 및 교각의 내진성능검증
    4.6.4.2 전단성능 검증
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단성능];
    B["KDS 24 17 12 4.6.4.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수:전단강도 /];
		VarOut2[/출력변수: 콘크리트 전단강도/];
    VarIn1[/입력변수: 콘크리트 기준압축강도/];
		VarIn2[/입력변수:검토단면에서 최대응답시의 모멘트와 전단력의 비/];
		VarIn3[/입력변수:고려하는 방향으로의 단면의 치수/];
		VarIn4[/입력변수:β=0.6+22*ρsolid/];
		VarIn5[/입력변수:단면의 외형치수에 대한 축방향 철근비/];
		VarIn6[/입력변수:소요변위연성도로서 항복변위에 대한 최대응답변위의 비/];
		VarIn7[/입력변수:축하중/];
		VarIn8[/입력변수:콘크리트 전단면적/];
		VarIn9[/입력변수:α=1.0-0.22*a/h/];
		VarIn10[/입력변수:모멘트/];
		VarIn11[/입력변수:전단력/];
		VarOut3[/출력변수: 철근 전단강도/];
		VarIn12[/입력변수:전단철근의 단면적/];
		VarIn13[/입력변수:전단철근의 항복강도/];
		VarIn14[/입력변수:단면의 유효깊이/];
		VarIn15[/입력변수:전단철근의 배근간격/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
		VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14 & VarIn15
		end

		Python_Class ~~~ C(["KDS 24 17 12 4.6.4.2 (3)"])
		C --> Variable_def

		D(["<img src='https://latex.codecogs.com/svg.image?V_{n}=V_{c}+V_{s}'>--------------------------------------------------------"]);
		E["<img src='https://latex.codecogs.com/svg.image?&space;V_{c}=0.5\sqrt{f_{ck}}\alpha\beta\gamma\sqrt{1&plus;\frac{P}{f_{ck}A_{g}}}A_{e}'>--------------------------------------------------------"];
		Variable_def --> E & F--->D
		F["<img src='https://latex.codecogs.com/svg.image?V_{s}=\frac{A_{v}f_{y}d}{s}'>--------------------------------------------------------"];
    """

    @rule_method
    def Verification_of_shear_performance(fIfck,fIh,fIrhosol,fImu,fIP,fIAa,fOAe,fIAg,fIM,fIV,fIAv,fIfy,fId,fIs,fIVmax) -> RuleUnitResult:
        """전단성능

        Args:
            fIfck (float): 콘크리트 기준압축강도
            fIh (float): 고려하는 방향으로의 단면의 치수
            fIrhosol (float): 단면의 외형치수에 대한 축방향 철근비
            fImu (float): 소요변위연성도로서 항복변위에 대한 최대응답변위의 비
            fIP (float): 축하중
            fIAa (float): 콘크리트 전단면적
            fIAg (float): 부재의 총단면적
            fIM (float): 모멘트
            fIV (float): 전단력
            fIAv (float): 전단철근의 단면적
            fIfy (float): 전단철근의 항복강도
            fId (float): 단면의 유효깊이
            fIs (float): 전단철근의 배근간격
            fIVmax (float): 응답이력해석에서 얻은 검토단면의 최대전단력

        Returns:
            fOVn (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 1
            fOVc (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 2
            fOVs (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 3
            fOa (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 4
            fOalpha (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 5
            fObeta (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 6
            fOgamma (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 7
            fOAe (float): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 값 8
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.6.4.2 전단성능 검증 (3)의 판단 결과
        """

        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIh, float)
        assert fIh > 0
        assert isinstance(fImu, float)
        assert isinstance(fImu, float)
        assert isinstance(fIP, float)
        assert fIP > 0
        assert isinstance(fIAa, float)
        assert fIAa > 0
        assert isinstance(fIAg, float)
        assert isinstance(fIM, float)
        assert isinstance(fIV, float)
        assert fIV > 0
        assert isinstance(fIAv, float)
        assert isinstance(fIfy, float)
        assert isinstance(fId, float)
        assert isinstance(fIs, float)
        assert fIs > 0
        assert isinstance(fIVmax, float)

        fOa = fIM / fIV
        fOalpha = 1.0 - 0.22 * fOa / fIh
        fObeta = 0.6 + 22 * fIrhosol
        fOgamma = (6-fImu)/4
        fOAe = 0.8 * fIAg
        fOVc = 0.5 * (fIfck)**0.5 * fOalpha * fObeta * fOgamma * (1 + 1000 * fIP / fIfck / fIAa)**0.5 * fOAe / 1000
        fOVs = fIAv * fIfy * fId / fIs / 1000
        fOVn = fOVc + fOVs

        if fOa / fIh <= 3 and fObeta <= 1.0 and 2 <= fImu <= 6 and 0 <= fOgamma <= 1 :
          if fOVn >= fIVmax :
            return RuleUnitResult(
                result_variables = {
                    "fOVc": fOVc,
                    "fOVs": fOVs,
                    "fOVn": fOVn,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )