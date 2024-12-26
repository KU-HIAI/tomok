import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020204_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.4 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '겹침 K형 접합에서 지강관의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.4 겹침 K형 접합에서 압축력을 받는 지강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 겹침 K형 접합에서 지강관의 설계강도]
	  B["KDS 14 31 25 4.3.2.2.4 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
  	VarOut1[/출력변수: 지강관의 설계강도/] ;
	  VarOut2[/출력변수: 국부항복의 한계상태/] ;
		VarIn1[/입력변수: 겹치는 지강관 재료의 항복응력/] ;
	  VarIn2[/입력변수: 겹치는 지강관의 두께/] ;
  	VarIn3[/입력변수: 오버랩 접합계수/] ;
    VarIn4[/입력변수: 겹치는 지강관의 높이/]
    VarIn5[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
    VarIn6[/입력변수: 겹침 브레이스에 용접된 지강관 면의 유효폭/] ;

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.4 (1)"])
		C --> Variable_def

	  E{"25%≤Ov＜50%"} ;
    D["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{ybi}t_{bi}[(O_{v/50})(2H_{bi}-4t_{bi})&plus;b_{eoi}&plus;b_{eov}]'>------------------------------------------------------------------------------------------------------------"] ;

		Variable_def --> E--"Yes"-->D--"<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>"-->Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>------------------"])
    """

    @rule_method
    def Design_strength_of_steel_pipe(fIFybi,fItbi,fIOv,fIHbi,fIbeoi,fIbeov) -> RuleUnitResult:
        """겹침 K형 접합에서 지강관의 설계강도

        Args:
            fIFybi (float): 겹치는 지강관 재료의 항복응력
            fItbi (float): 겹치는 지강관의 두께
            fIOv (float): 오버랩 접합계수
            fIHbi (float): 겹치는 지강관의 높이
            fIbeoi (float): 주강관에 용접된 지강관 면의 유효폭
            fIbeov (float): 겹친 브레이스에 용접된 지강관 면의 유효폭

        Returns:
            fOPhiPn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.4 겹침 K형 접합에서 압축력을 받는 지강관 (1)의 값 1
            fOPn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.4 겹침 K형 접합에서 압축력을 받는 지강관 (1)의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.4 겹침 K형 접합에서 압축력을 받는 지강관 (1)의 판단 결과
        """

        assert isinstance(fIFybi, float)
        assert isinstance(fItbi, float)
        assert isinstance(fIOv, float)
        assert isinstance(fIHbi, float)
        assert isinstance(fIbeoi, float)
        assert isinstance(fIbeov, float)

        if 25 <= fIOv < 50:
          fOPn = fIFybi * fItbi * ((fIOv / 50) * (2 * fIHbi - 4 * fItbi) + fIbeoi + fIbeov)
          fOPhiPn = 0.95 * fOPn
          return RuleUnitResult(
              result_variables = {
                  "fOPhiPn": fOPhiPn,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )