import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020406_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.6 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '탄성패드 설계'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.6 탄성패드 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성패드 설계];
    B["KDS 24 90 11 4.2.4.6 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 탄성패드의 설계강도/];
		VarIn2[/입력변수: 탄성중합체의 허용압축응력/];
		VarIn3[/입력변수: 직경/];
		VarIn4[/입력변수: 수평력/];

    VarOut1 ~~~  VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.4.6 (2)"])
		C --> Variable_def;
		Variable_def--->K--->L--->M

		K["<img src='https://latex.codecogs.com/svg.image?N_{Rd}=\frac{1}{1.3}\times\frac{\pi}{4}\times&space;d^{2}\times&space;f_{e,k}'>--------------------------------------------------------"];
		L{"<img src='https://latex.codecogs.com/svg.image?N_{Sd}\leq&space;N_{Rd}'>--------------------------------------------------------"};
		M(["Pass or Fail"])
    """

    @rule_method
    def Design_Strength_Of_Elastic_Pads(fId, fINsd, fIfek) -> RuleUnitResult:
        """탄성패드 설계
        Args:
            fId (float): 직경
            fINsd (float): 수평력
            fIfek (float): 탄성중합체의 허용압축응력

        Returns:
            fONRd (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.4.6 탄성패드 설계 (2)의 값
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.4.6 탄성패드 설계 (2)의 판단 결과
        """

        assert isinstance(fId, float)
        assert isinstance(fINsd, float)
        assert isinstance(fIfek, float)

        import math
        if fONRd <= fINsd:
          fONRd = (math.pi * (fId ** 2) * fIfek) / (1.3 * 4)
          return RuleUnitResult(
                  result_variables = {
                      "fONRd": fONRd,
                      "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
                  result_variables = {
                      "fONRd": fONRd,
                      "pass_fail": False,
                }
            )