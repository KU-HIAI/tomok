import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020205_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.5 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '총 유효용접길이'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.5 지강관의 용접
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 총 유효용접길이]
	  B["KDS 14 31 25 4.3.2.2.5 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 총 유효용접길이/] ;
    VarIn1[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
    VarIn2[/입력변수: 지강관의 두께/] ;
    VarIn3[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
    VarIn4[/입력변수: 각도/] ;

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.5 (1)"])
		C --> Variable_def

	  I{"θ≤50º"} ;
    D(["<img src='https://latex.codecogs.com/svg.image?L_{e}=\frac{2(H_{b}-1.2t_{b})}{sin\theta}&plus;2(B_{b}-1.2t_{b})'>------------------------------------------------------------------------"]) ;
    E{"50º≤θ≤60º"} ;
    F(["직선보간법"]) ;
    G{"60º≤θ"} ;
    H(["<img src='https://latex.codecogs.com/svg.image?L_{e}=\frac{2(H_{b}-1.2t_{b})}{sin\theta}&plus;(B_{b}-1.2t_{b})'>------------------------------------------------------------------------"]) ;
    Variable_def --> I-->D
    Variable_def --> E-->F
    Variable_def --> G-->H
    """

    @rule_method
    def total_effective_weld_length(fIHb,fItb,fIBb,fItheta) -> RuleUnitResult:
        """총 유효용접길이

        Args:
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fItb (float): 지강관의 두께
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭
            fItheta (float): 각도

        Returns:
            fOLe (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.5 지강관의 용접 (1)의 값
        """

        assert isinstance(fIHb, float)
        assert isinstance(fItb, float)
        assert isinstance(fIBb, float)
        assert isinstance(fItheta, float)
        assert 0 < fItheta < 180

        import math

        if fItheta <= 50:
          fOLe = 2*(fIHb-1.2*fItb)/math.sin(fItheta*math.pi/180)+(fIBb-1.2*fItb)
        elif fItheta >= 60:
          fOLe = 2*(fIHb-1.2*fItb)/math.sin(fItheta*math.pi/180)
        elif 50 < fItheta < 60:
          theta50 = 2*(fIHb-1.2*fItb)/math.sin(50*math.pi/180)+(fIBb-1.2*fItb)
          theta60 = 2*(fIHb-1.2*fItb)/math.sin(60*math.pi/180)
          fOLe = theta50 + (theta60-theta50)/10*(60-fItheta)

        return RuleUnitResult(
            result_variables = {
                "fOLe": fOLe,
            }
        )