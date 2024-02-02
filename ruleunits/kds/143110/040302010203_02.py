import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040302010203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.2.1.2.3 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장역항복의 한계상태에 따른 인장역작용을 이용한 공칭전단강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.2 전단강도
    4.3.2.1.2.3 인장역작용을 이용한 설계공칭전단강도
    (2)
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
	  A[인장역장용을 이용한 설계공칭전단강도]
	  B["KDS 14 31 10 4.3.2.1.2.3(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 공칭전단강도/]
	  VarIn1[/입력변수: 웨브의 높이/]
	  VarIn2[/입력변수: 웨브의 두께/]
	  VarIn3[/입력변수: 웨브 판 좌굴계수/]
	  VarIn4[/입력변수: 강재의 탄성계수/]
	  VarIn5[/입력변수: 웨브의 최소항복강도/]
	  VarIn5[/입력변수: 웨브의 단면적/]
	  VarIn6[/입력변수: 단면2차모멘트/]
	  VarIn7[/입력변수: 웨브 전단항복응력에 대한 선형좌굴이론에 따른 웨브 임계응력의 비율을 나타내는 정수/]
	  VarIn8[/입력변수: 보강재의 간격/]

	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
   	VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
  	VarIn5 ~~~ VarIn7 & VarIn8
  	end
	  Python_Class ~~~ Variable_def --> C --> D
  	D --Pass--> E
  	D --Fail--> F
  	C["<img src='https://latex.codecogs.com/svg.image?h/t_w\leq&space;1.10\sqrt{k_vE/F_{yw}}'>-----------------------------------"]
	  D["Pass or Fail"]
	  E(["<img src='https://latex.codecogs.com/svg.image?V_n=0.6F_{yw}A_w'>-----------------------"])
	  F(["<img src='https://latex.codecogs.com/svg.image?V_n=0.6F_{yw}A_w(C_v&plus;\frac{1-C_v}{1.15\sqrt{1&plus;(a/h)^2}})'>----------------------------------------------------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def niominal_shear_strength(fOVn,fIh,fItw,fIKv,fIE,fIFyw,fIAw,fICv,fIa) -> bool:
        """인장역항복의 한계상태에 따른 인장역작용을 이용한 공칭전단강도
        Args:
            fOVn (float): 공칭전단강도
            fIh (float): 웨브의 높이
            fItw (float): 웨브 두께
            fIKv (float): 웨브 판 좌굴계수
            fIE (float): 강재의 탄성계수
            fIFyw (float): 웨브의 최소항복강도
            fIAw (float): 웨브의 단면적
            fICv (float): 웨브 전단항복응력에 대한 선형좌굴 이론에 따른 웨브 임계응력의 비율을 나타내는 정수
            fIa (float): 보강재의 간격


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.2.3 인장역작용을 이용한 설계공칭전단강도 (2)의 값
        """

        if fIh / fItw <= 1.10 * (fIKv * fIE / fIFyw) ** 0.5:
            fOVn = 0.6 * fIFyw * fIAw
            return fOVn
        else:
            fOVn = 0.6 * fIFyw * fIAw * (fICv + (1 - fICv) / (1.15 * (1 + (fIa / fIh) ** 2)))
            return fOVn


# 

