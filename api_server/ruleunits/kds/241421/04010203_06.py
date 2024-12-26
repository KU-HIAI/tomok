import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '공칭복부폭'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 공칭복부폭];
    B["KDS 24 14 21 4.1.2.3 (6)"];
    A ~~~ B
    end
	  subgraph Variable_def;
    VarOut1[/출력변수: 공칭복부폭/];
    VarIn1[/입력변수: 프리스트레싱 덕트의 지름/];
    VarIn2[/입력변수: 단면의 복부폭/];
    VarIn3[/입력변수: 덕트의 외측 지름/];
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (6)"])
		C --> Variable_def

		Variable_def--->H--yes-->I
    I--yes-->L
    I--No-->J
    L & J--->K
    H["프리스트레싱 덕트의 지름 <img src='https://latex.codecogs.com/svg.image?\dpi{10}\leq\;\frac{b_{w}}{8}'>---------------"]
    I{"그라우트 된 덕트"}
    L["<img src='https://latex.codecogs.com/svg.image?b_{w,nom}=b_w-0.5\sum\phi&space;'>---------------------------------"]
    J["<img src='https://latex.codecogs.com/svg.image?b_{w,nom}=b_w-1.2\sum\phi&space;'>---------------------------------"]
    K(["공칭복부폭"])
    """

    @rule_method
    def Nominal_abdomen_width(fIbwnomA,fIbwnomB,fIdiprdu,fIbw,fIphi) -> RuleUnitResult:
        """공칭복부폭

        Args:
            fIbwnomA (float): 공칭복부폭 (그라우트 된 덕트)
            fIbwnomB (float): 공칭복부폭 (그라우트 안된 덕트)
            fIdiprdu (float): 프리스트레싱 덕트의 지름
            fIbw (float): 단면의 복부폭
            fIphi (float): 덕트의 외측 지름

        Returns:
            fObwnom (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (6)의 값
            sOnone (string): 건축물 설계하중  3.5.3 제한사항 (2)의 판단 결과
        """

        assert isinstance(fIdiprdu, float)
        assert isinstance(fIbw, float)
        assert isinstance(fIphi, float)

        temp = sum(fIphi[j] for j in range(i))

        if fIdiprdu >= fIbw / 8:
          if fIbwnomA != 0 and fIbwnomB == 0 :
            fObwnom = fIbw - 0.5 * temp
            return RuleUnitResult(
                result_variables = {
                    "fObwnom": fObwnom,
                }
            )

          if fObwnomA == 0 and fIbwnomB != 0 :
            fObwnom = fIbw - 1.2 * temp
            return RuleUnitResult(
                result_variables = {
                    "fObwnom": fObwnom,
                }
            )
        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )