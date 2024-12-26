import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_04_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 4 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '전단철근에 의한 공칭전단강도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 전단철근에 의한 공칭전단강도]
	  B["KDS 24 17 10 부록 4 (5)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:축력 작용에 의한 공칭전단강도/];
		VarIn2[/입력변수:콘크리트에 의한 공칭전단강도/];
		VarIn3[/입력변수:전단철근에 의한 공칭전단강도/];

		VarOut1[/출력변수:단부구역을 제외한 구역의 공칭전단강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 4 (5)"])
		C --> Variable_def

	  Variable_def--->E--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;V_n=V_c&plus;V_s&plus;V_p'>---------------------------------"]

		F(["단부구역을 제외한 구역의 공칭전단강도"])
    """

    @rule_method
    def Nominal_shear_strength_by_shear_reinforcement(fIVsA,fIVsB,fIVsC,fIAv,fIAsp,fIAct,fIDc,fIfyh,fIlct,fIs) -> RuleUnitResult:
        """전단철근에 의한 공칭전단강도

        Args:
            fIVsA (float): 전단철근에 의한 공칭전단강도 (사각형 띠철근단면)
            fIVsB (float): 전단철근에 의한 공칭전단강도 (원형단면의 나선철근 또는 원형 후프띠철근)
            fIVsC (float): 전단철근에 의한 공칭전단강도 (원형 후프띠철근에 보강띠철근이 추가된 경우)
            fIAv (float): 전단철근으로 작용하는 띠철근의 단면적
            fIAsp (float): 나선철근 또는 원형 후프띠철근의 단면적
            fIAct (float): 원형단면에 배근되는 보강띠철근의 단면적
            fIDc (float): 고려하는 방향의 심부콘크리트 단면 치수
            fIfyh (float): 띠철근 또는 나선철근의 항복강도
            fIlct (float): 원형단면에 배근되는 보강띠철근에서 갈고리 부분과 연장길이를 제외한 길이
            fIs (float): 띠철근 또는 나선철근의 수직간격

        Returns:
            fOVs (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (5)의 값
            pass_fail (bool): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (5)의 판단 결과 1
            sOnone (string): 건축물 설계하중  3.5.3 제한사항 (2)의 판단 결과 2
        """

        assert isinstance(fIAv, float)
        assert isinstance(fIAsp, float)
        assert isinstance(fIAct, float)
        assert isinstance(fIDc, float)
        assert isinstance(fIfyh, float)
        assert isinstance(fIlct, float)
        assert isinstance(fIs, float)
        assert fIs != 0

        import math

        if fIVsA != 0 and fIVsB == 0 and fIVsC == 0 :
          fOvs = fIAv * fIfyh * fIDc / fIs
          return RuleUnitResult(
              result_variables = {
                  "fOvs": fOvs,
              }
          )

        elif fIVsA == 0 and fIVsB != 0 and fIVsC == 0 :
          fOvs = (math.pi / 2) * (fIAsp * fIfyh * fIDc)
          return RuleUnitResult(
              result_variables = {
                  "fOvs": fOvs,
              }
          )

        elif fIVsA == 0 and fIVsB == 0 and fIVsC != 0 :
          fOvs = fIAct * fIfyh * fIlct / fIs
          return RuleUnitResult(
              result_variables = {
                  "fOvs": fOvs,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )