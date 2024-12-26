import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050305_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.3.5 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '횡방향철근의 최대수직간격'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.3 주탑 및 기둥
    4.5.3.5 단부구역의 횡방향철근상세
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향철근의 최대수직간격];
    B["KDS 24 17 12 4.5.3.5 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 횡방향철근의 최대수직간격/];
    VarIn2[/입력변수: 부재 최소 단면치수/];
		VarIn3[/입력변수: 축방향철근지름/];


	 VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.3.5 (2)"])
		C --> Variable_def--->E--->D

		E{"횡방향철근의 최대수직간격≤부재 최소 단면치수 X 1/4, 횡방향철근의 최대수직간격≤축방향철근지름 X 6 "}
		D(["Pass or Fail"])
    """

    @rule_method
    def maximum_vertical_spacing_of_transverse_steel(fImavstr,fImacsdm,fIlogrdi) -> RuleUnitResult:
        """횡방향철근의 최대수직간격

        Args:
            fImavstr (float): 횡방향철근의 최대수직간격
            fImacsdm (float): 부재 최소 단면치수
            fIlogrdi (float): 축방향철근지름

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.5.3.5 단부구역의 횡방향철근상세 (2)의 판단 결과
        """

        assert isinstance(fImavstr, float)
        assert isinstance(fImacsdm, float)
        assert isinstance(fIlogrdi, float)

        if fImavstr <= min(fImacsdm / 4, fIlogrdi * 6)  :
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