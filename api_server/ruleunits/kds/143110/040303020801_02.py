import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020801_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.8.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '휨강도-부모멘트부 인장플랜지의 종방향 응력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.8 휨강도-부모멘트부
    4.3.3.2.8.1 일반사항
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 휨강도-부모멘트부 인장플랜지의 종방향 응력] ;
		B["KDS 14 31 10 4.3.3.2.8.1 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 플랜지 횡방향 휨이나 종방향 뒴을 고려하지 않은 플랜지 종방향응력/] ;
    VarIn2[/입력변수: 휨에 대한 강도저항계수/] ;
    VarIn3[/입력변수: 인장플랜지의 공칭휨강도/] ;
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.8.1 (2)"])
		C --> Variable_def

		D{"<img src=https://latex.codecogs.com/svg.image?f_{bu}\leq\phi&space;_{f}F_{nt}>--------------------------"}

		Variable_def --> D --> F(["PASS or Fail"])
    """

    @rule_method
    def longitudinal_stress_of_flexural_strength_negative_moment_tensile_flange(fIfbu,fIphif,fIFnt) -> RuleUnitResult:
        """휨강도-부모멘트부 인장플랜지의 종방향 응력

        Args:
            fIfbu (float): 플랜지 횡방향 휨이나 종방향 뒴을 고려하지 않은 플랜지 종방향응력
            fIphif (float): 휨에 대한 강도저항계수
            fIFnt (float): 인장플랜지의 공칭휨강도

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.8.1 일반사항 (2)의 판단 결과
        """

        assert isinstance(fIfbu, float)
        assert isinstance(fIphif, float)
        assert isinstance(fIFnt, float)

        if fIfbu <= fIphif * fIFnt:
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