import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04180502_07(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5.2 (7)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '통행선박의 밀도에 대한 보정계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 통행선박의 밀도에 대한 보정계수];
    B["KDS 24 12 21 4.18.5.2 (7)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 통행선박의 밀도에 대한 보정계수/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.5.2 (7)"])
		C --> Variable_def

    H{"수로영역"};
    D["<img src='https://latex.codecogs.com/svg.image?R_{D}=1.0'>"];
    E["<img src='https://latex.codecogs.com/svg.image?R_{D}=1.3'>"];
    F["<img src='https://latex.codecogs.com/svg.image?R_{D}=1.6'>"];
    G(["통행선박의 밀도에 대한 보정계수"]);
    Variable_def--->H--직선영역--->D--->G
    H--전이영역--->E--->G
    H--꺾임/곡선영역--->F--->G
    """

    @rule_method
    def correction_factor_for_the_density_of_passing_ship(fIRDA,fIRDB,fIRDC) -> RuleUnitResult:
        """통행선박의 밀도에 대한 보정계수

        Args:
            fIRDA (float): 보정계수(저밀도)
            fIRDB (float): 보정계수(평균밀도)
            fIRDC (float): 보정계수(고밀도)

        Returns:
            fORD (float): 강교 설계기준(한계상태설계법)  4.18.5.2 항로이탈확률 (7)의 값
        """

        if fIRDA != 0 and fIRDB == 0 and fIRDC == 0 :
          fORD = 1.0
          return RuleUnitResult(
              result_variables = {
                  "fORD": fORD,
              }
          )

        if fIRDA == 0 and fIRDB != 0 and fIRDC == 0 :
          fORD = 1.3
          return RuleUnitResult(
              result_variables = {
                  "fORD": fORD,
              }
          )

        if fIRDA == 0 and fIRDB == 0 and fIRDC != 0 :
          fORD = 1.6
          return RuleUnitResult(
              result_variables = {
                  "fORD": fORD,
              }
          )