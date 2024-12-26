import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020302_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.3.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '주요 시공단계에서 압축을 받는 비합성박스의 압축플랜지'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.3 시공성
    4.3.3.2.3.2 휨
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 주요 시공단계에서 압축을 받는 비합성박스의 압축플랜지] ;
		B["KDS 14 31 10 4.3.3.2.3.2 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 휨에 대한 강도저항계수/] ;
    VarIn2[/입력변수: 종방향 뒴을 고려하지 않고 계산된 고려중인 단면의 계수하중에 의한 종방향플랜지응력/] ;
    VarIn3[/입력변수: 웨브의 공칭휨좌굴강도/] ;
    VarIn4[/입력변수: 압축플랜지의 공칭휨강도/] ;
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.3.2 (2)"])
		C --> Variable_def

		D{"<img src=https://latex.codecogs.com/svg.image?f_{bu}\leq\phi&space;_{f}F_{nc}>-----------------------"}
		E{"<img src=https://latex.codecogs.com/svg.image?f_{bu}\leq\phi&space;_{f}F_{crw}>------------------------"}

		Variable_def --> D --> E --> F(["PASS or Fail"])
    """

    @rule_method
    def Compression_flange_of_non_composite_box(fIphif,fIfbu,fIFcrw,fIFnc) -> RuleUnitResult:
        """주요 시공단계에서 압축을 받는 비합성박스의 압축플랜지

        Args:
            fIphif (float): 휨에 대한 강도저항계수
            fIfbu (float): 종방향 뒴을 고려하지 않고 계산된 고려 중인 단면의 계수하중에 의한 종방향플랜지응력
            fIFcrw (float): 웨브의 공칭휨좌굴강도
            fIFnc (float): 압축플랜지의 공칭휨강도

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.3.2 휨 (2)의 판단 결과
        """

        assert isinstance(fIphif, float)
        assert isinstance(fIfbu, float)
        assert isinstance(fIFcrw, float)
        assert isinstance(fIFnc, float)

        if fIfbu <= fIphif * fIFnc and fIfbu <= fIphif * fIFcrw:
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