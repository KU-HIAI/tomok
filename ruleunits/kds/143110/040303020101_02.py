import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303020101_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.1.1 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '플랜지의 계수비틀림 전단강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.1 일반사항
    4.3.3.2.1.1 응력계산
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
		A[Title: 응력계산] ;
		B["KDS 14 31 10 4.3.3.2.1.1 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 플랜지의 계수비틀림 전단강도/] ;
      VarIn1[/입력변수: 박스플랜지의 순수비틀림 전단응력/] ;
      VarIn2[/입력변수: 전단에 대한 강도저항/] ;
      VarIn3[/입력변수: 플랜지의 최소항복강도/] ;
			end

			VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
			Python_Class ~~~ Variable_def

			C["<img src=https://latex.codecogs.com/svg.image?&space;F_{vr}=0.75\phi&space;_{v}\frac{F_{yf}}{\sqrt{3}}>------------------------"]
			D(["<img src=https://latex.codecogs.com/svg.image?&space;F_{vr}>---------"])
			Variable_def --> C --> D

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Modulus_torsional_shear_strength_of_flange(fIFvr,fIptssbf,fIphiv,fIFyf) -> bool:
        """플랜지의 계수비틀림 전단강도
        Args:
            fIFvr (float): 플랜지의 계수비틀림 전단강도
            fIptssbf (float): 박스플랜지의 순수비틀림 전단응력
            fIphiv (float): 전단에 대한 강도저항
            fIFyf (float): 플랜지의 최소항복강도



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.1.1 응력계산 (2)의 값
        """

        fIFvr = 0.75 * fIphiv * fIFyf / (3 ** 0.5)
        if fIptssbf <= fIFvr:
          return "Pass"
        else:
          return "Fail"


# 

