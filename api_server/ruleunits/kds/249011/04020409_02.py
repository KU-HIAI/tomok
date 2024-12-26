import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020409_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.9 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '피스톤과 포트 접촉부 검토'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.9 피스톤과 포트 접촉부 검토
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 피스톤과 포트 접촉부 검토];
    B["KDS 24 90 11 4.2.4.9 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 포트의 내부 직경/];
		VarIn2[/입력변수: 재료의 항복 강도/];
		VarIn3[/입력변수: 피스톤 면의 폭/];
		VarIn4[/입력변수: 접촉면의 반경/];
		VarIn5[/입력변수: 재료의 항복 강도/];
		VarIn6[/입력변수: 포트의 탄성계수/];
		VarIn7[/입력변수: 포트의 내부 직경/];
		VarIn8[/입력변수: 수평력/];
		VarIn9[/입력변수: 포트의 설계강도/];
		VarIn10[/입력변수: 포트의 설계강도/];
		VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
    VarIn4 ~~~ VarIn5 & VarIn6 & VarIn7
		VarIn5 ~~~ VarIn8 & VarIn9 & VarIn10
		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.4.9(2)"])
		C --> Variable_def;

		Variable_def--->K
		Variable_def--->L

		K["<img src='https://latex.codecogs.com/svg.image?&space;V_{Rd}=\frac{f_{y}Dw}{1.95}'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?&space;V_{Rd}=\frac{8.8f_{y}^{2}RD}{E_{d}}'>--------------------------------------------------------"];
		K & L--->M--->N
		M{"<img src='https://latex.codecogs.com/svg.image?V_{Sd}\leq V_{Rd}'>---------------"};
    N(["Pass or Fail"])
    """

    @rule_method
    def Design_Strength_Of_Pot(fIVSd, fIDprime, fIwidsop, fIR, fIfy, fIEd, fIindipt, fIlacscA, fIlacscB) -> RuleUnitResult:
        """피스톤과 포트 접촉부 검토

        Args:
            fIVSd (float): 수평력
            fIDprime (float): 포트의 내부 직경
            fIwidsop (float): 피스톤 면의 폭
            fIR (float): 접촉면의 반경
            fIfy (float): 재료의 항복 강도
            fIEd (float): 포트의 탄성계수
            fIindipt (float): 포트의 내부 직경
            fIlacscA (float): 포트의 설계강도 (평면 접촉면일 경우)
            fIlacscB (float): 포트의 설계강도 (곡면 접촉면일 경우)

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.4.9 피스톤과 포트 접촉부 검토 (2)의 판단 결과
            fOVRd (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.4.9 피스톤과 포트 접촉부 검토 (2)의 값
        """

        assert isinstance(fIVSd, float)
        assert isinstance(fIDprime, float)
        assert isinstance(fIwidsop, float)
        assert isinstance(fIR, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIEd, float)
        assert fIEd > 0
        assert isinstance(fIindipt, float)
        assert isinstance(fIEd, float)
        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)

        if fIlacscA != 0 and fIlacscB == 0 :
          fOVRd = fIfy * fIDprime * fIwidsop / 1.95
          if fIVSd <= fOVRd:
            return RuleUnitResult(
                  result_variables = {
                      "pass_fail": True,
                  }
              )
          else:
            return RuleUnitResult(
                  result_variables = {
                      "pass_fail": False,
                  }
              )

        elif fIlacscA == 0 and fIlacscB != 0 :
          fOVRd = 8.8 * fIfy ** 2 * fIR * fIindipt / fIEd
          if fIVSd <= fOVRd:
            return RuleUnitResult(
                  result_variables = {
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