import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040402 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.4.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '부재 단면의 특정 위치에서 하중조합으로 구한 소요축방향응력'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.2 휨과 축력을 받는 비대칭 단면 부재 및 기타 부재
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
		A[Title: 휨과 축력을 받는 비대칭 단면 부재 및 기타 부재] ;
		B["KDS 14 31 10 4.4.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 부재 단면의 특정위치에서 하중조합으로 구한 소요축방향응력/] ;
      VarIn2[/입력변수: 설계축방향응력/] ;
      VarIn3[/입력변수: 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력/] ;
      VarIn4[/입력변수: 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력/] ;
      VarIn5[/입력변수: 설계휨응력/] ;
      VarIn6[/입력변수: 설계휨응력/] ;
      VarIn7[/입력변수: 강주축 휨을 나타내는 아래첨자/] ;
      VarIn8[/입력변수: 약주축 휨을 나타내는 아래첨자/] ;
      VarIn9[/입력변수: 압축에 대한 강도저항계수/] ;
      VarIn10[/입력변수: 인장에 대한 강도저항계수/] ;
      VarIn11[/입력변수: 휨에 대한 강도저항계수/] ;
			end
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11

		Python_Class ~~~ Variable_def
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		C["<img src=https://latex.codecogs.com/svg.image?\left|\frac{f_{ua}}{F_{ra}}&plus;\frac{f_{ubw}}{F_{rbw}}&plus;\frac{f_{ubz}}{F_{rbz}}\right|\leq&space;1.0>---------------------------------------------------"]

		Variable_def--> C --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Required_axial_stress_obtained_from_a_load_combination_at_a_specific_location_of_the_member_section(fIfua,fIFra,fIfubw,fIfubz,fIFrbw,fIFrbz) -> bool:
        """부재 단면의 특정 위치에서 하중조합으로 구한 소요축방향응력
        Args:
            fIfua (float): 부재 단면의 특정 위치에서 하중조합으로 구한 소요축방향응력
            fIFra (float): 설계축방향응력
            fIfubw (float): 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력
            fIfubz (float): 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력
            fIFrbw (float): 설계휨응력
            fIFrbz (float): 설계휨응력



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.4.2 휨과 축력을 받는 비대칭 단면 부재 및 기타 부재의 통과여부
        """



        if abs(fIfua / fIFra + fIfubw / fIFrbw + fIfubz / fIFrbz) <= 1.0:
          return "Pass"
        else:
          return "Fail"


# 

