import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060201_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.1 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '극한한계상태에서 중립축의 깊이'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 극한한계상태에서 중립축의 깊이];
    B["KDS 24 14 21 4.6.2.1 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
	  VarOut1[/출력변수: 극한한계상태에서의 최대중립축 깊이/];
		VarIn1[/입력변수: 중립축의 깊이/];
		VarIn2[/입력변수: 모멘트 재분배 후의 계수휨모멘트/탄성휨모멘트 비율/];
		VarIn3[/입력변수: 단면의 유효깊이/];
		VarIn4[/입력변수: 콘크리트의 극한변형률/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.1 (3)"])
		C --> Variable_def

		Variable_def --> E --> F --> G

		E["<img src='https://latex.codecogs.com/svg.image? C_{max}=(\frac{\delta\varepsilon&space;_{cu}}{0.0033}-0.6)d'>--------------------------------------------------"];
		F{"중립축의 깊이<img src='https://latex.codecogs.com/svg.image? \leq C_{max}'>---------------------------------"};

		G(["Pass or Fail"]);
    """

    @rule_method
    def Depth_of_the_neutral_axis_in_extreme_limits(fIdepnea,fIdelta,fId,fIepscu) -> RuleUnitResult:
        """극한한계상태에서 중립축의 깊이

        Args:
            fIdepnea (float): 중립축의 깊이
            fIdelta (float): 모멘트 재분배 후의 계수휨모멘트/탄성휨모멘트 비율
            fId (float): 단면의 유효깊이
            fIepscu (float): 콘크리트의 극한변형률


        Returns:
            fOcmax (float): 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 극한한계상태에서의 중립축의 깊이 (3)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 극한한계상태에서의 중립축의 깊이 (3)의 판단 결과
        """

        assert isinstance(fIdepnea, float)
        assert isinstance(fIdelta, float)
        assert isinstance(fId, float)
        assert isinstance(fIepscu, float)

        fOcmax = ((fIdelta * fIepscu) / 0.0033 - 0.6) * fId

        if fIepscu == -9999:
          return RuleUnitResult(
              result_variables = {
                  "fOcmax": fOcmax,
                  "pass_fail": -9999, # fIepsecu를 알아야 구할 수 있음
              }
          )
        else:
          if fOcmax >= fIdepnea:
            return RuleUnitResult(
                result_variables = {
                    "fOcmax": fOcmax,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "fOcmax": fOcmax,
                    "pass_fail": False,
                }
            )