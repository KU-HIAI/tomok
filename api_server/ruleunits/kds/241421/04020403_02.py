import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020403_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.4.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '부재 전 경간에 걸친 평균 유효 변형량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.3 직접 처짐 계산에 의한 검증
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 부재 전 경간에 걸친 평균 유효 변형량];
    B["KDS 24 14 21 4.2.4.3 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 비균열 상태일 때의 변형량/];
		VarIn2[/입력변수: 완전균열상태일 때의 변형량/];
		VarIn3[/입력변수: 균열 단면을 기준으로 계산한 인장 철근 응력/];
		VarIn4[/입력변수: 첫 균열이 발생한 직후에 균열 면에서 계산한 철근 인장응력/];
		VarIn5[/입력변수: 평균 변형률에 미치는 하중의 반복 지속 기간을 반영하는 계수/];
		VarOut1[/출력변수: 부재 전 경간에 걸친 평균 유효 변형량/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.4.3 (2)"])
		C --> Variable_def

		Variable_def--->D
		D{"평균 변형률에 미치는 하중의 반복 지속 기간을 반영하는 계수 β"}
		D--단기하중--->G
		D--반복하중--->H
		G["β=1.0"]
		H["β=0.5"]
		G & H--->C--->E--->F
		C["<img src='https://latex.codecogs.com/svg.image?\zeta=1-\beta(\frac{f_{sr}}{f_{so}})^2'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\Delta&space;e=\zeta\Delta&space;_{crack}&plus;(1-\zeta)\Delta&space;_{uncrack}'>---------------------------------"]

		F(["부재 전 경간에 걸친 평균 유효 변형량"])
    """

    @rule_method
    def Average_effective_deformation_over_the_entire_span_of_the_member(fIdelunc,fIdelcra,fIfso,fIfsr,fIbeta) -> RuleUnitResult:
        """부재 전 경간에 걸친 평균 유효 변형량

        Args:
            fIdelunc (float): 비균열 상태일 때의 변형량
            fIdelcra (float): 완전균열상태일 때의 변형량
            fIfso (float): 균열단면을 기준으로 계산한 인장 철근응력
            fIfsr (float): 첫 균열 발생 직후에 균열면에서 계산한 철근 인장응력
            fIbeta (float): 평균 변형률에 미치는 하중의 반복 지속 기간을 반영하는 계수

        Returns:
            fOdeltae (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (2)의 값 1
            fOzeta (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (2)의 값 2
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (2)의 판단 결과
        """

        assert isinstance(fIdelunc, float)
        assert isinstance(fIdelcra, float)
        assert isinstance(fIfso, float)
        assert fIfso > 0
        assert isinstance(fIfsr, float)
        assert fIfsr > 0
        assert isinstance(fIbeta, float)

        fOzeta = 1 - fIbeta * (fIfsr / fIfso)**2
        fOdeltae = fOzeta * fIdelcra + (1 - fOzeta) * fIdelunc

        if 0 <= fOzeta <= 1.0 and fIbeta == (1.0 or 0.5) :
          return RuleUnitResult(
              result_variables = {
                  "fOdeltae": fOdeltae,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )