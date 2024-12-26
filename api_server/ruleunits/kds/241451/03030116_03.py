import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030116_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.1.16 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '설계지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.16 최대 허용항타하중
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계지지력];
    B["KDS 24 14 51 3.3.1.16 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수: 설계지지력/];
		VarIn1[/입력변수: 강도 저항계수/];
		VarIn2[/입력변수: 목재의 압축강도/];
		VarIn3[/입력변수: 목재의 단면적/];

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~	VarIn3

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.3.1.16 (3)"])
		C --> Variable_def;

		Variable_def
		J[프리스트레스 콘크리트 말뚝]
		D[압축]
		E[인장]
		F["<img src='https://latex.codecogs.com/svg.image?\phi&space;\left ( 0.85f_{c}^{\prime}-f_{pe} \right )A_{c}'>---------------------------------"]
		I([Pass or Fail])
		L["<img src='https://latex.codecogs.com/svg.image?\phi&space;\left(0.25\sqrt{f_{c}^{\prime}}+f_{pe} \right)A_{c}'>---------------------------------"]
		K["<img src='https://latex.codecogs.com/svg.image?\phi&space;f_{pe} A_{ps}'>---------------------------------"]

		Variable_def ---> J ---> D & E
		D ---> F
		E --"일반적 환경"--> L
		E --"부식성이 심한 환경"--> K
		L & K ---> H(설계지지력)
		F ---> H(설계지지력) ---> I
		H~~~ |"KDS 24 14 21"| H
		H~~~ |"KDS 24 14 31"| H
    """

    @rule_method
    def design_bearing_capacity(fIDebcatA,fIDebcatB,fIDebcatC,fIphi,fIfpe,fIAc,fIfprimc,fIAps) -> RuleUnitResult:
        """설계지지력

        Args:
            fIDebcatA (float): 설계지지력(압축)
            fIDebcatB (float): 설계지지력(인장, 일반적 환경)
            fIDebcatC (float): 설계지지력(인장, 부식성이 심한 환경)
            fIphi (float): 저항계수
            fIfpe (float): 프리스트레싱 강재의 유효 긴장응력
            fIAc (float): 압축플랜지 단면적
            fIfprimc (float): 콘크리트의 회소압축강도
            fIAps (float): 긴장재타이의 단면력

        Returns:
            fODebcac (float): 교량 하부구조 설계기준 (한계상태설계법)  3.3.1.16 최대 허용항타하중 (3)의 값
            sOnone (string): 건축물 설계하중  3.5.3 제한사항 (2)의 판단 결과
        """

        assert isinstance(fIphi, float)
        assert isinstance(fIfpe, float)
        assert isinstance(fIAc, float)
        assert isinstance(fIfprimc, float)
        assert isinstance(fIAps, float)


        if fIDebcatA != 0 and fIDebcatB == 0 and fIDebcatC == 0 :
          fODebcac = fIphi * (0.85 * fIfprimc - fIfpe) * fIAc
          return RuleUnitResult(
              result_variables = {
                  "fODebcac": fODebcac,
              }
          )

        elif fIDebcatA == 0 and fIDebcatB != 0 and fIDebcatC == 0 :
          fODebcac = fIphi * (0.25 * fIfprimc**0.5 + fIfpe) * fIAc
          return RuleUnitResult(
              result_variables = {
                  "fODebcac": fODebcac,
              }
          )

        elif fIDebcatA == 0 and fIDebcatB == 0 and fIDebcatC != 0 :
          fODebcac = fIphi * fIfpe * fIAps
          return RuleUnitResult(
              result_variables = {
                  "fODebcac": fODebcac,
              }
          )
        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )