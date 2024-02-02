import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04040101 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.4.1.1' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '하중조합으로 구한 소요압축강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.1 휨과 축력이 작용하는 1축 및 2축 대칭단면 부재
    4.4.1.1 압축력과 휨을 받는 1축 및 2축 대칭단면 부재
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
		A[Title: 압축력과 휨을 받는 1축 및 2축 대칭단면 부재] ;
		B["KDS 14 31 10 4.4.1.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 하중조합으로 구한 소요압축강도/] ;
      VarIn2[/입력변수: 설계압축강도/] ;
      VarIn3[/입력변수: 압축에 대한 강도 저항계수/] ;
      VarIn4[/입력변수: 하중조합으로 구한 소요휨강도/] ;
      VarIn5[/입력변수: 설계휨강도/] ;
      VarIn6[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn7[/입력변수: 강축 휨을 나타내는 아래첨자/] ;
      VarIn8[/입력변수: 약축 휨을 나타내는 아래첨자/] ;
			end

		Python_Class ~~~ Variable_def
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8

		C["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}\geq&space;0.2>--------------------"]
		D["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}&plus;\frac{8}{9}(\frac{M_{ux}}{M_{rx}}&plus;\frac{M_{uy}}{M_{ry}})\leq&space;1.0>---------------------------------------------"]
		E["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}<0.2>--------------------"]
		F["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{2P_{r}}&plus;(\frac{M_{ux}}{M_{rx}}&plus;\frac{M_{uy}}{M_{ry}})\leq&space;1.0>-------------------------------------------"]

		Variable_def --> C --> D
		Variable_def --> E --> F
		D & F --> G(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Required_compressive_strength_obtained_from_load_combinations(fIPu,fIPr,fIphic,fIMux,fIMuy,fIMrx,fIMry,fIphib) -> bool:
        """하중조합으로 구한 소요압축강도
        Args:
            fIPu (float): 하중조합으로 구한 소요압축강도
            fIPr (float): 설계압축강도
            fIphic (float): 압축에 대한 강도저항계수
            fIMux (float): x축 하중조합으로 구한 소요휨강도
            fIMuy (float): y축 하중조합으로 구한 소요휨강도
            fIMrx (float): x축 설계휨강도
            fIMry (float): y축 설계휨강도
            fIphib (float): 휨에 대한 강도저항계수



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.4.1.1 압축력과 휨을 받는 1축 및 2축 대칭단면 부재의 통과여부
        """




        fIphic = 0.90
        fIphib = 0.90
        if fIPu / fIPr >= 0.2:
           if fIPu / fIPr + (8 / 9) * (fIMux / fIMrx + fIMuy / fIMry) <= 1.0:
              return "Pass"
           else:
              return "Fail"
        else:
          if fIPu / (2 * fIPr) + (fIMux / fIMrx + fIMuy / fIMry) <= 1.0:
              return "Pass"
          else:
              return "Fail"


# 

