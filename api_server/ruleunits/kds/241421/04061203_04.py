import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04061203_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.12.3 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '최소 횡철근 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.12 포스트텐션 정착부
    4.6.12.3 정착부의 검토
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소 횡철근 단면적];
    B["KDS 24 14 21 4.6.12.3 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:축방향 철근/];
		VarIn2[/입력변수:철근 사이의 순간격/];
		VarIn3[/입력변수:횡철근 단면적 보정상수/];
		VarIn4[/입력변수:재료계수/];
		VarOut1[/출력변수:최소 횡철근 단면적/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.12.3 (4)"])
		C --> Variable_def

		Variable_def--->E--->D--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\gamma&space;_{p,unfav}\geq&space;1.2'>---------------------------------"]

		D["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;A_s=0.15\frac{P_o}{\phi&space;_sf_y}\gamma&space;_{p,unfav}'>---------------------------------"]

		F(["최소 횡철근 단면적"])
    """

    @rule_method
    def Minimum_transverse_bar_cross_section(fIPO,fIfy,fIgpunfa,fIphis) -> RuleUnitResult:
        """최소 횡철근 단면적

        Args:
            fIPO (float): 축방향 철근
            fIfy (float): 철근 사이의 순간격
            fIgpunfa (float): 횡철근 단면적 보정상수
            fIphis (float): 재료계수

        Returns:
            fOAs (float): 깊은기초 설계기준(일반설계법)  4.6.12.3 정착부의 검토 (4)의 값
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.6.12.3 정착부의 검토 (4)의 판단 결과
        """

        assert isinstance(fIPO, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIgpunfa, float)
        assert isinstance(fIphis, float)

        if fIgpunfa >= 1.2 :
          fOAs = 0.15 * fIPO /(fIphis*fIfy) * fIgpunfa
          return RuleUnitResult(
              result_variables = {
                  "fOAs": fOAs,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOAs": fOAs,
                  "pass_fail": False,
              }
          )