import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020503_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.5.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '극한한계상태에서 슬라이딩면'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.5 곡면의 미끄럼 면을 가진 받침
    4.2.5.3 슬라이딩 곡면의 설계검토
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 극한한계상태에서 슬라이딩면];
    B["KDS 24 90 11 4.2.5.3 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 극한한계상태에서의 설계축력/];
		VarIn2[/입력변수: PTFE 설계압축강도의 특성/];
		VarIn3[/입력변수: 슬라이딩면의 유효접촉면/];

    VarIn1 & VarIn2 & VarIn3


    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.5.3 (3)"])
		C --> Variable_def;
		Variable_def--->K


    K{"<img src='https://latex.codecogs.com/svg.image?N_{Sd}\leq\frac{f_{k}}{1.4}\times&space;A_{r}'>--------------------------------------------------------"};
		K --->M
		M(["Pass or Fail"])
    """

    @rule_method
    def Design_Axial_Forces_At_Extreme_Limits(fINsd,fIfk,fIAr) -> RuleUnitResult:
        """극한한계상태에서 슬라이딩면

        Args:
            fINsd (float): 극한한계상태에서의 설계축력
            fIfk (float): PTFE 설계압축강도의 특성
            fIAr (float): 슬라이딩면의 유효접촉면적

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.5.3 슬라이딩 곡면의 설계검토 (3)의 판단 결과
        """

        assert isinstance(fINsd, float)
        assert isinstance(fIfk, float)
        assert isinstance(fIAr, float)

        if fINsd <= (fIfk / 1.4) * fIAr:
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