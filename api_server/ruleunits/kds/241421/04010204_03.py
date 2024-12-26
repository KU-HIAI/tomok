import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010204_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '종방향 전단응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 전단응력];
    B["KDS 24 14 21 4.1.2.4 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 종방향 전단응력/];
		VarIn2[/입력변수: 콘크리트의 재료계수/];
		VarIn3[/입력변수: 콘크리트의 포아송비/];
		VarIn4[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
	  VarIn5[/입력변수: 거더 플랜지에 형성된 스트럿의 경사각/];
		VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.4 (3)"])
		C --> Variable_def

		Variable_def--->E--->D
		E{"<img src='https://quicklatex.com/cache3/d9/ql_20a91df6403211f93a37e2b2cad18dd9_l3.png'>---------------------------------"}
		D(["Pass or Fail"])
    """

    @rule_method
    def Longitudinal_shear_stress(fIvuf,fIphic,fInu,fIfck,fIthetaf) -> RuleUnitResult:
        """종방향 전단응력

        Args:
            fIvuf (float): 종방향 전단응력
            fIphic (float): 콘크리트의 재료계수
            fInu (float): 콘크리트의 포아송비
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도
            fIthetaf (float): 거더 플랜지에 형성된 스트럿의 경사각

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단 (3)의 값
        """

        assert isinstance(fIvuf, float)
        assert isinstance(fIphic, float)
        assert isinstance(fInu, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIthetaf, float)

        import math

        if fIvuf < fIphic * fInu * fIfck * math.sin(math.radians(fIthetaf)) * math.cos(math.radians(fIthetaf)):
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