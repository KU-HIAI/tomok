import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04020701_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.7.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '세장한 자유돌출판의 저감계수'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    4.2.7.1 세장한 자유돌출판
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[세장한 자유돌출판] ;
		B["KDS 14 31 10 4.2.7.1(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 세장한 자유돌출판의 저감계수/]
    VarIn1[/입력변수: 자유돌출판의 폭/]
    VarIn2[/입력변수: 부재의 두께/]
    VarIn3[/입력변수: 강재의 항복강도/]
    VarIn4[/입력변수: 강재의 탄성계수/]
    VarIn5[/입력변수: 자유돌출 세장판요소의 계수/]
		end

		Python_Class ~~~ Variable_def
	C["<img src='https://latex.codecogs.com/svg.image?Q_{s}'>------"] ;
  D["<img src='https://latex.codecogs.com/svg.image?b/t\leq&space;0.64\sqrt{EK_{c}/F_{y}}'>---------------------------------------------"] ;
  E["<img src='https://latex.codecogs.com/svg.image?0.64\sqrt{EK_{c}/F_{y}}<b/t\leq&space;1.17\sqrt{EK_{c}/F_{y}}'>----------------------------------------------------------------------------"] ;
  F["<img src='https://latex.codecogs.com/svg.image?b/t>1.17\sqrt{EK_{c}/F_{y}}'>----------------------------------------"] ;
  G(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.0'>-----------------------"]) ;
  H(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.415-0.65\left(\frac{b}{t}\right)\sqrt{\frac{F_{y}}{EK_{c}}}'>---------------------------------------------------------------"]) ;
  I(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=\frac{0.90EK_{c}}{F_{y}\left(\frac{b}{t}\right)^{2}'>-----------------------------------"]) ;

	Variable_def-->C-->D & E & F
D-->G
E-->H
F-->I
    """

    @rule_method
    def Reduction_factor_of_slender_free_projection_plate(fOQs,fIb,fIt,fIFy,fIE,fIkc,fIh,fItw)-> RuleUnitResult:
        """세장한 자유돌출판의 저감계수

        Args:
            fOQs (float): 세장한 자유돌출판의 저감계수
            fIb (float): 자유돌출판의 폭
            fIt (float): 부재의 두께
            fIFy (float): 강재의 항복강도
            fIE (float): 강재의 탄성계수
            fIkc (float): 웨브의 두께
            fItw (float): 자유돌출 세장판 요소의 계수
            fIh (float): 높이


        Returns:
            fOQs (float): 강구조부재설계기준(하중저항계수설계법)  4.2.7.1 세장한 자유돌출판  (2)의 값
        """

        assert isinstance(fOQs, float)
        assert isinstance(fIb, float)
        assert fIb > 0
        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fIFy, float)
        assert fIFy > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIh, float)
        assert fIh > 0
        assert isinstance(fItw, float)
        assert fItw > 0


        if fIb/fIt <= 0.64*(fIE*fIkc/fIFy)**0.5:
          fOQs = 1.0

        elif fIb/fIt > 0.64*(fIE*fIkc/fIFy)**0.5 and fIb/fIt <= 1.17*(fIE*fIkc/fIFy)**0.5:
          fOQs = 1.415 - 0.65*(fIb/fIt)*(fIFy/(fIE*fIkc))**0.5

        else:
          if fIkc == 0:
            fIkc = 4/(fIh/fItw)**2
            fOQs = 0.90*fIE*fIkc/(fIFy*(fIb/fIt)**2)

          else:
            return RuleUnitResult(
              result_variables = {
                "pass_fail": False,
              }
            )

        return RuleUnitResult(
          result_variables = {
            "fOQs": fOQs,
            }
        )