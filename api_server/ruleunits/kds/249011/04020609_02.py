import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020609_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.9 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '압축응력'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.9 설계검증
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 압축응력];
    B["KDS 24 90 11 4.2.6.9 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 극한한계상태에서의 작용 축력/];
		VarIn2[/입력변수: 압축강도/];
		VarIn3[/입력변수: 미끄럼면의 유효 접촉면적/];
    VarIn4[/입력변수: 직경/];
		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.6.9 (2)"])
		C --> Variable_def;
		Variable_def--->K


		K{"<img src='https://latex.codecogs.com/svg.image?N_{Sd}\leq\frac{f_{k}}{1.4}\times&space;A_{r}'>--------------------------------------------------------"};
		K --->M
		M(["Pass or Fail"])
    """

    @rule_method
    def Actuated_Axial_Force_At_Extreme_Limits(fINsd,fIfk,fIAr,fID) -> RuleUnitResult:
        """압축응력

        Args:
            fINsd (float): 극한한계상태에서의 작용 축력
            fIfk (float): 압축강도
            fIAr (float): 미끄럼면의 유효 접촉면적
            fID (float) : 직경

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.2.6.9 설계검증 (2)의 판단 결과 1
            sOfID (string): 교량 기타시설설계기준 (한계상태설계법) 4.2.6.9 설계검증 (2)의 판단 결과 2
        """

        assert isinstance(fINsd, float)
        assert isinstance(fIfk, float)
        assert isinstance(fIAr, float)
        assert isinstance(fID, float)


        if fINsd <= fIAr * fIfk / 1.4 :
          if fID >= 100 :
            return RuleUnitResult(
                result_variables = {
                    "sOfID": "접촉면적, 유효접촉면적은 딤플 면적을 포함",
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "sOfID": "접촉면적, 유효접촉면적은 딤플 면적을 제외함",
                    "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )