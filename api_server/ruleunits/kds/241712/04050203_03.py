import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050203_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.2.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '캔틸레버 교각의 2차모멘트'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.3 주탑 및 교각의 P-Δ효과
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 캔틸레버 교각의 2차모멘트];
    B["KDS 24 17 12 4.5.2.3 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
	  VarOut1[/출력변수: 2차 모멘트/];
    VarIn1[/입력변수: 기둥 상단과 하단의 횡방향 최대상대변위/];
		VarIn2[/입력변수: 축력/];

		VarOut1~~~~ VarIn1 & VarIn2

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.2.3 (3)"])
		C --> Variable_def

		D{"휨강성으로 탄성 지진해석 수행하는 경우"}

		E["2차모멘트=기둥 상단과 하단의 횡방향 최대상대변위X1.5X축력"]
	  Variable_def--->D---> E

    E--->F

		F(["2차모멘트"]);
    """

    @rule_method
    def P_delta_Effects_of_pylons_and_cantilever_piers(fImdtdtc,fIaxifor) -> RuleUnitResult:
        """캔틸레버 교각의 2차모멘트

        Args:
            fImdtdtc (float): 기둥 상단과 하단의 횡방향 최대상대변위
            fIaxifor (float): 축력

        Returns:
            fOsecmom (bool): 교량내진 설계기준(케이블교량) 4.5.2.3 주탑 및 교각의 P-Δ효과 (3)의 값
        """

        assert isinstance(fImdtdtc, float)
        assert isinstance(fIaxifor, float)

        fOsecmom = fImdtdtc * 1.5 * fIaxifor
        return RuleUnitResult(
              result_variables = {
                  "fOsecmom": fOsecmom,
                  }
              )