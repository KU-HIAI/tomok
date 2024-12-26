import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010502_02_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.5.2 (2) ②'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '콘크리트 스트럿의 유효설계강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.5 스트럿-타이 모델
    4.1.5.2 스트럿
    (2)
    ②
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 스트럿의 유효설계강도];
    B["KDS 24 14 21 4.1.5.2 (2) ②"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 콘크리트 스트럿의 유효설계강도/];
		VarIn1[/입력변수: 콘크리트 재료계수/];
		VarIn2[/입력변수: 콘크리트 기준압축강도/];
		VarIn3[/입력변수: 횡방향 인장철근/];
    VarIn4[/입력변수: 종방향 축에 대한 스트럿의 경사각/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.5.2 (2) ②"])
		C --> Variable_def

		Variable_def--->D
		D{"횡방향 인장철근 ≥ 0.4%"}

		D ---> E & F & G
		E{"\n <img src='https://latex.codecogs.com/svg.image? \theta > 75^{\circ}'>-----------------------------"};
		F{"\n <img src='https://latex.codecogs.com/svg.image? 75^{\circ}\geq \theta > 60^{\circ}'>-----------------------------"};
		G{"\n <img src='https://latex.codecogs.com/svg.image?  60^{\circ}\geq \theta '>-----------------------------"};

		E ---> H
		F ---> I
		G ---> J
		H["\n <img src='https://latex.codecogs.com/svg.image? f_{cd,max} = 0.85\left ( 1-f_{ck}/250 \right )\phi _{c}f_{ck}'>-----------------------------"];
		I["\n <img src='https://latex.codecogs.com/svg.image? f_{cd,max} = 0.70\left ( 1-f_{ck}/250 \right )\phi _{c}f_{ck}'>-----------------------------"];
		J["\n <img src='https://latex.codecogs.com/svg.image? f_{cd,max} = 0.60\left ( 1-f_{ck}/250 \right )\phi _{c}f_{ck}'>-----------------------------"];
		H & I & J ---> M(["콘크리트 스트럿의 유효설계강도"])
    """

    @rule_method
    def Effective_design_strength_of_concrete_struts(fIphic,fIfck,fItrtere,fItheta) -> RuleUnitResult:
        """콘크리트 스트럿의 유효설계강도

        Args:
            fIphic (float): 콘크리트 재료계수
            fIfck (float): 콘크리트 기준압축강도
            fItrtere (float): 횡방향 인장철근
            fItheta (float): 종방향 축에 대한 스트럿의 경사각

        Returns:
            fOfcdmax (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.5.2 스트럿 (2) ②의 값
            sOnone (string): 콘크리트교 설계기준 (한계상태설계법) 4.1.5.2 스트럿 (2) ②의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIfck, float)
        assert isinstance(fItrtere, float)
        assert isinstance(fItheta, float)

        if fItrtere >= 0.4:
          if fItheta > 75:
            fOfcdmax = 0.85 * (1 - fIfck/250) * fIphic * fIfck
          elif 75 >= fItheta > 60:
            fOfcdmax = 0.70 * (1 - fIfck/250) * fIphic * fIfck
          else:
            fOfcdmax = 0.6 * (1 - fIfck/250) * fIphic * fIfck

          return RuleUnitResult(
              result_variables = {
                  "fOfcdmax": fOfcdmax,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )