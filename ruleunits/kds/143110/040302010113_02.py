import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040302010113_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.2.1.1.13 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = 'H형강 부재의 단면제한'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.1 휨강도
    4.3.2.1.1.13 휨부재의 단면산정
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
	  A[휨부재의 단면산정]
	  B["KDS 14 31 10 4.3.2.1.1.13(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: y축에 대한 압축플랜지의 단면2차모멘트 또는 복곡률의 경우 압축플랜지중 작은플랜지의 단면2차모멘트/]
	  VarIn2[/입력변수: y축에 대한 단면2차모멘트/]
	  VarIn3[/입력변수: 수직보강재의 순간격/]
	  VarIn4[/입력변수: 웨브의 높이/]
	  VarIn5[/입력변수: 웨브의 두께/]
	  VarIn6[/입력변수: 강재의 탄성계수/]
	  VarIn7[/입력변수: 항복강도/]
	  VarIn8[/입력변수: 웨브의 면적/]
	  VarIn9[/입력변수: 압축플랜지면적/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  VarIn6 ~~~ VarIn8 & VarIn9
	  end
	  Python_Class ~~~ Variable_def --> C & I
	  C --> L -->  D & F
	  D --> E
	  F --> G
	  E & G --> H
	  I --> J & K
	  C["H형강 부재의 단면제한"]
	  D["<img src='https://latex.codecogs.com/svg.image?\frac{a}{h}\leq&space;1.5'>-------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}=11.7\sqrt{\frac{E}{F_y}}'>------------------------"]
	  F["<img src='https://latex.codecogs.com/svg.image?\frac{a}{h}>1.5'>-------------"]
	  G["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}=\frac{0.42E}{F_y}'>--------------------"]
	  H(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}'>---------------"])
	  I["보강재가 없는 보"]
	  J(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}<260'>--------------------------"])
	  K(["웨브의 면적 < 압축플랜지면적 x10"])
	  L["<img src='https://latex.codecogs.com/svg.image?0.1\leq\frac{I_{yc}}{I_y}\leq&space;0.9'>----------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Moment_of_inertia_of_the_compression_flange_about_the_y_axis_or_moment_of_inertia_of_the_smaller_of_the_compression_flanges_in_case_of_back(fIIyc,fIIy,fIa,fIh,fItw,fIE,fIFy,fIAw,fIAfc,fIuserdefined) -> bool:
        """H형강 부재의 단면제한
        Args:
            fIIyc (float): y축에 대한 압축플랜지의 단면2차모멘트 또는 복곡률의 경우 압축플랜지 중 작은플랜지의 단면2차모멘트
            fIIy (float): y축에 대한 단면2차모멘트
            fIa (float): 수직보강재의 순간격
            fIh (float): 웨브의 높이
            fItw (float): 웨브의 두께
            fIE (float): 강재의 탄성계수
            fIFy (float): 항복강도
            fIAw (float): 웨브의 면적
            fIAfc (float): 압축플랜지면적
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)4.3.2.1.1.13 휨부재의 단면산정 (2)의 통과여부
        """

        # fIuserdefined == 1 : 보강재가 있는 보
        # fIuserdefined == 2 : 보강재가 없는 보


        if fIuserdefined == 1:
            if 0.1 <= fIIyc / fIIy <= 0.9:
                if fIa / fIh <= 1.5:
                  fIh / fItw == 11.7 * (fIE / fIFy) ** 0.5
                  return "Pass"
                else:
                  fIh / fItw == 0.42 * fIE / fIFy
                  return "Fail"
            else:
                return "Fail"
        elif fIuserdefined == 2:
            if fIh / fItw <= 260 and fIAw <= fIAfc * 10:
                return "Pass"
            else:
                return "Fail"


# 

