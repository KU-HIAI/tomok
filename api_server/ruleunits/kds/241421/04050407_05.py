import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04050407_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.4.7 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '최대 지름 12mm의 용접된 횡철근의 정착력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.4 철근의 정착
    4.5.4.7 용접철근에 의한 정착
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대 지름 12mm의 용접된 횡철근의 정착력];
    B["KDS 24 14 21 4.5.4.7 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 설계압축강도/];
		VarIn2[/입력변수: 철근 단면적/];
		VarIn3[/입력변수: 용접의 설계전단강도/];
		VarIn4[/입력변수: 횡방향 철근의 지름/];
		VarIn5[/입력변수: 정착철근의 지름/];


		VarOut1[/출력변수: 용접의 설계전단강도/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.4.7 (5)"])
		C --> Variable_def

		Variable_def--->G--->D--->E--->F

		G{"<img src='https://latex.codecogs.com/svg.image?f_{yd}=500MPa'>---------------------------------"}
		D{"최대 지름=12mm"}

		E["<img src='https://latex.codecogs.com/svg.image?F_{btd}=F_{wd}\leq&space;12A_sf_{cd}d_{b,t}/d_b'>---------------------------------"]
		F(["용접의 설계전단강도"])
    """

    @rule_method
    def Anchorage_capacity_of_welded_transverse_bars_up_to_12mm_in_diameter(fIfcd,fIAs,fIFwd,fIdbt,fIdb) -> RuleUnitResult:
        """최대 지름 12mm의 용접된 횡철근의 정착력

        Args:
            fIfcd (float): 콘크리트 설계압축강도
            fIAs (float): 철근 단면적
            fIFwd (float): 용접의 설계전단강도
            fIdbt (float): 횡방향 철근의 지름
            fIdb (float): 정착철근의 지름

        Returns:
            fOFbtd (float): 콘크리트교 설계기준 (한계상태설계법)  4.5.4.4 기본정착길이 (4)의 값
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.1.1 말뚝기초의 축방향 허용지지력과 허용변위 (2)의 판단 결과
        """

        assert isinstance(fIfcd, float)
        assert isinstance(fIAs, float)
        assert isinstance(fIdbt, float)
        assert isinstance(fIdb, float)
        assert fIdb != 0

        fOFbtd = fIFwd

        if fIdbt <= 12 and fIdb <= 12 and fOFbtd <= 12*fIAs*fIfcd*fIdbt/fIdb :
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