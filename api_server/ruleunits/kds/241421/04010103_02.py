import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010103_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '2축 휨강도의 검토'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 2축 휨강도의 검토];
    B["KDS 24 14 21 4.1.1.3 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 세장비 비율/];
		VarIn2[/입력변수: 단면의 등가 폭/];
    VarIn3[/입력변수: 단면의 등가 깊이/] ;
		VarIn4[/입력변수: 단면의 y축 세장비/] ;
		VarIn5[/입력변수: 단면의 z축 세장비/];
		VarIn6[/입력변수: 단면의 y축 회전반지름/];
		VarIn7[/입력변수: 단면의 z축 회전반지름/];
		VarIn8[/입력변수: Muy/Pu/];
		VarIn9[/입력변수: Muz/Pu/];
		VarIn10[/입력변수: 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트/];
		VarIn11[/입력변수: 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트/];


		VarIn1 & VarIn2 & VarIn3~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
		VarIn5 ~~~VarIn8 & VarIn9 & VarIn10 & VarIn11
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.3 (2)"])
		C --> Variable_def

		Variable_def--->L & D
		L & D-->E
		L["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{y}=\frac{l}{r_{y}}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{z}=\frac{l}{r_{z}}'>---------------------------------"]

		E{"<img src='https://latex.codecogs.com/svg.image?\frac{\lambda&space;_{y}}{\lambda&space;_{z}}\leq&space;2,\frac{\lambda&space;_{z}}{\lambda&space;_{y}}\leq&space;2'>---------------------------------"}
		F["<img src='https://latex.codecogs.com/svg.image?b_{eq}=r_{y}\sqrt{12}'>---------------------------------"]
  	G["<img src='https://latex.codecogs.com/svg.image?h_{eq}=r_{z}\sqrt{12}'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?e_{z}=\frac{M_{uy}}{P_{u}}'>---------------------------------"]
	  I["<img src='https://latex.codecogs.com/svg.image?e_{z}=\frac{M_{uz}}{P_{u}}'>---------------------------------"]
	  J{"<img src='https://latex.codecogs.com/svg.image?\frac{e_{y}/h_{eq}}{e_{z}/b_{eq}}\leq&space;0.2\;\,or\,\,\frac{e_{z}/b_{eq}}{e_{y}/h_{eq}}\leq&space;0.2'>---------------------------------"}
	  Variable_def---> F & G & H & I--->J
  	K(["Pass or Fail"])
    E & J--->K
    """

    @rule_method
    def Review_of_biaxial_flexural_strength(fIry,fIrz,fIl,fIPu,fIMuy,fIMuz) -> RuleUnitResult:
        """2축 휨강도의 검토

        Args:
            fIry (float): 단면의 y축 회전반지름
            fIrz (float): 단면의 z축 회전반지름
            fIl (float): 길이
            fIPu (float): 축력
            fIMuy (float): 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트
            fIMuz (float): 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 판단 결과 1
            sOflestr (string): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 판단 결과 2
            fObeq (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 값 1
            fOheq (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 값 2
            fOlamy (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 값 3
            fOlamz (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 값 4
            fOez (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 값 5
            fOey (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 값 6
        """

        assert isinstance(fIry, float)
        assert fIry != 0
        assert isinstance(fIrz, float)
        assert fIrz != 0
        assert isinstance(fIl, float)
        assert fIl != 0
        assert isinstance(fIPu, float)
        assert fIPu != 0
        assert isinstance(fIMuy, float)
        assert fIMuy != 0
        assert isinstance(fIMuz, float)
        assert fIMuz != 0

        fObeq = fIry * (12**0.5)
        fOheq = fIrz * (12**0.5)
        fOlamy = fIl / fIry
        fOlamz = fIl / fIrz
        fOey = fIMuy / fIPu
        fOez = fIMuz / fIPu

        if fOlamy/fOlamz <= 2 and fOlamz/fOlamy <= 2 and ((fOey/fOheq)/(fOez/fObeq) or (fOez/fObeq)/(fOey/fOheq)) :
          return RuleUnitResult(
              result_variables = {
                  "sOflestr": "2축 휨강도 검토 생략 가능",
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )