import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010103_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '2축 휨강도의 검토'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 2축 휨강도의 검토];
    B["KDS 24 14 21 4.1.1.3 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트/];
		VarIn2[/입력변수: 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트/];
    VarIn3[/입력변수: y축에 대한 설계휨강도/] ;
		VarIn4[/입력변수: z축에 대한 설계휨강도/] ;
		VarIn5[/입력변수: 단면 형상과 축력비에 따른 지수/];
		VarIn6[/입력변수: 계수하중에 의한 축력/];
		VarIn7[/입력변수: 단면의 설계중심축압축강도/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarIn2 & VarIn3 & VarIn4~~~VarIn5 & VarIn6 & VarIn7
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.3 (3)"])
		C --> Variable_def

		Variable_def--->D
		D{"단면 형상과 축력비에 따른 지수"}
		D--직사각형 단면인 경우-->

		J{"<img src='https://latex.codecogs.com/svg.image?N_{u}/N_{od}'>---------------------------------"}

		J--0.7-->E[α=1.5]
		J--1.0-->F[α=2.0]
		J--0.1보다 작거나 같을때-->G[α=1.0]
		D--원형단면과 타원형 단면인 경우--> H[α=2.0]
		E & F & G & H--->I--->K
		I{"<img src='https://latex.codecogs.com/svg.image?(\frac{M_{uy}}{M_{dy}})^{\alpha}&plus;(\frac{M_{uz}}{M_{dz}})^{\alpha}\leq&space;1.0'>---------------------------------"}
		K(["Pass or Fail"])
    """

    @rule_method
    def Review_of_biaxial_flexural_strength(fIMuy,fIMuz,fIMdy,fIMdz,fIalpha) -> RuleUnitResult:
        """2축 휨강도의 검토

        Args:
            fIMuy (float): 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트
            fIMuz (float): 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트
            fIMdy (float): y축에 대한 설계휨강도
            fIMdz (float): z축에 대한 설계휨강도
            fIalpha (float): 단면 형상과 축력비에 따른 지수

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (3)의 판단 결과 1
        """

        assert isinstance(fIMuy, float)
        assert fIMuy > 0
        assert isinstance(fIMuz, float)
        assert fIMuz > 0
        assert isinstance(fIMdy, float)
        assert fIMdy > 0
        assert isinstance(fIMdz, float)
        assert fIMdz > 0
        assert isinstance(fIalpha, float)
        assert 0 < fIalpha <= 2.0

        if (fIMuy/fIMdy)**fIalpha + (fIMuz/fIMdz)**fIalpha <= 1.0:
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