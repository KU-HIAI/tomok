import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020405(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.5'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '하중 분산'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.5 하중분산
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 하중분산];
    B["KDS 24 90 11 4.2.4.5"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 하중 분산각/];

		VarIn1
		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.4.5"])
		C --> Variable_def;

		Variable_def--> F

		F{"포트받침의 구성요소 및 재료의 특징 고려 시"}

		F--Yes--->D["하중 분산각≤60°"]
		F--No--->E["하중 분산각=45°"]
    """

    @rule_method
    def Load_Dispersion_Angle(fIloadsa,fOloadsa) -> RuleUnitResult:
        """하중 분산
        Args:
            fIloadsa (float): 하중 분산각
            fOloadsa (float): 하중 분산각

        Returns:
            fOloadsa (float): 교량 기타시설설계기준 (한계상태설계법) 4.2.4.5 하중분산의 값
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.2.4.5 하중분산의 판단 결과
        """

        assert isinstance(fIloadsa, float)

        if fIloadsa != 0 :
          fOloadsa = fIloadsa
          if fIloadsa <= 60 :
            return RuleUnitResult(
                  result_variables = {
                      "fOloadsa": fOloadsa,
                      "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                  result_variables = {
                     "fOloadsa": fOloadsa,
                      "pass_fail": False,
                }
            )

        if fIloadsa == 0 :
          fOloadsa = 45
          return RuleUnitResult(
                result_variables = {
                      "fOloadsa": fOloadsa,
              }
          )