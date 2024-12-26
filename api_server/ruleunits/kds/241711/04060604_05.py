import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060604_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.4 (5)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '전단철근에 의한 공칭전단강도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.4 전단 설계
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 전단철근에 의한 공칭전단강도]
	  B["KDS 24 17 11 4.6.6.4(5)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 전단철근에 의한 공칭전단강도/]
	  VarIn1[/입력변수: 전단철근으로 작용하는 띠철근의 단면적/]
	  VarIn2[/입력변수: 나선철근 또는 원형 후프띠철근의 단면적/]
	  VarIn3[/입력변수: 원형단면에 배근되는 보강띠철근의 단면적/]
	  VarIn4[/입력변수: 심부 콘크리트 치수/]
	  VarIn5[/입력변수: 띠철근 또는 나선철근의 항복강도/]
	  VarIn6[/입력변수: 원형단면에 배근되는 보강디철근에서 갈고리 부분과 연장길이를 제외한 길이/]
	  VarIn7[/입력변수: 띠철근 또는 나선철근의 수직간격/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn2  ~~~ VarIn5 & VarIn6 & VarIn7
  	end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.6.4(5)"])
		C --> Variable_def--> H & I & J

	  H --> D
	  I --> E
	  J --> F
	  D & E & F --> G
	  D["<img src='https://latex.codecogs.com/svg.image?V_s=\frac{A_vf_{yh}D_c}{s}'>----------------------------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?V_s=\frac{\pi}{2}\frac{A_{sp}f_{yh}D_c}{s}'>---------------------------------------"]
	  F["<img src='https://latex.codecogs.com/svg.image?&space;V_s=\frac{\sum&space;A_{ct}f_{yh}l_{ct}}{s}'>------------------------------------------"]
	  G(["<img src='https://latex.codecogs.com/svg.image?&space;V_s'>------"])
	  H["사각형 띠철근 단면"]
	  I["원형단면의 나선철근 또는 원형 후프띠철근"]
	  J["원형후프띠철근에 보강띠철근이 추가된 경우"]
    """

    @rule_method
    def nominal_shear_strength_by_shear_rebar(fIAv, fIAsp, fIAct, fIDc, fIfyh, fIlct, fIs, fIlacscA, fIlacscB, fIlacscC) -> RuleUnitResult:
        """전단철근에 의한 공칭전단강도

        Args:
            fIAv (float): 전단철근으로 작용하는 띠철근의 단면적
            fIAsp (float): 나선철근 또는 원형 후프띠철근의 단면적
            fIAct (float): 원형단면에 배근되는 보강띠철근의 단면적
            fIDc (float): 심부 콘크리트 치수
            fIfyh (float): 띠철근 또는 나선철근의 항복강도
            fIlct (float): 원형단면에 배근되는 보강디철근에서 갈고리 부분과 연장길이를 제외한 길이
            fIs (float): 띠철근 또는 나선철근의 수직간격
            fIlacscA (float): 전단철근에 의한 공칭전단강도 (사각형 띠철근단면인 경우)
            fIlacscB (float): 전단철근에 의한 공칭전단강도 (원형단면의 나선철근 또는 원형 후프띠철근 경우)
            fIlacscC (float): 전단철근에 의한 공칭전단강도 (원형 후프띠철근에 보강띠철근이 추가된 경우)

        Returns:
            fOVs (float): 교량내진설계기준(한계상태설계법) 4.6.6.4 전단 설계 (5)의 값
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.6.4 전단 설계 (5)의 판단 결과
        """

        assert isinstance(fIAv, float)
        assert isinstance(fIAsp, float)
        assert isinstance(fIAct, float)
        assert isinstance(fIDc, float)
        assert isinstance(fIfyh, float)
        assert isinstance(fIlct, float)
        assert isinstance(fIs, float)
        assert fIs > 0
        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)
        assert isinstance(fIlacscC, float)

        import math

        if fIlacscA == 0 and fIlacscB != 0 and fIlacscC != 0 :
          fOVs = fIAv * fIfyh * fIDc / fIs
          return RuleUnitResult(
                  result_variables = {
                      "fOVs": fOVs,
                  }
              )

        elif fIlacscA != 0 and fIlacscB == 0 and fIlacscC != 0 :
          fOVs = math.pi / 2 * fIAsp * fIfyh * fIDc / fIs
          return RuleUnitResult(
              result_variables = {
                  "fOVs": fOVs,
                  }
              )

        elif fIlacscA != 0 and fIlacscB != 0 and fIlacscC == 0 :
          fOVs = fIAct * fIfyh * fIlct / fIs
          return RuleUnitResult(
              result_variables = {
                  "fOVs": fOVs,
                  }
              )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )