import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040404 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.4.4' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '축력과 주축휨이 조합된 하중상태 하에서 인장을 받는 플랜지의 볼트 구멍 위치에서 플랜지의 인장파단강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.4 구멍이 있는 플랜지의 인장파단
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 구멍이 있는 플랜지의 인장파단] ;
		B["KDS 14 31 10 4.4.4"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 플랜지의 인장파단강도/] ;
      VarIn2[/입력변수: 하중조합으로 구해진 소요인장강도/] ;
      VarIn3[/입력변수: 인장파단의 한계상태에 대한 설계인장강도/] ;
      VarIn4[/입력변수: 하중조합으로 구한 소요휨강도/] ;
      VarIn5[/입력변수: 설계휨강도/] ;
      VarIn6[/입력변수: 인장파단에 대한 강도저항계수/] ;
      VarIn7[/입력변수: 휨에 대한 강도저항계수/] ;

			end
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		Python_Class ~~~ Variable_def


		E["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}&plus;\frac{M_{ux}}{M_{rx}}\leq&space;1.0>--------------------------------"]



		Variable_def --> E --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Tensile_breaking_strength_of_flange(fItebrsf,fIPu,fIPt,fIMu,fIMrx,fIphit,fIphib) -> bool:
        """축력과 주축휨이 조합된 하중상태 하에서 인장을 받는 플랜지의 볼트 구멍 위치에서 플랜지의 인장파단강도
        Args:
            fItebrsf (float): 플랜지의 인장파단강도
            fIPu (float): 하중조합으로 구해진 소요인장강도
            fIPt (float): 인장파단의 한계상태에 대한 설계인장강도
            fIMu (float): 하중조합으로 구한 소요휨강도
            fIMrx (float): 설계휨강도
            fIphit (float): 인장파단에 대한 강도저항계수
            fIphib (float): 휨에 대한 강도저항계수



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.4.4 구멍이 있는 플랜지의 인장파단의 통과여부
        """


        fIphit = 0.75
        fIphib = 0.90
        if fIPu / fIPt + fIMu / fIMrx <= 1.0:
          fItebrsf = fIPu / fIPt + fIMu / fIMrx
          return "Pass"
        else:
          return "Fail"


# 

