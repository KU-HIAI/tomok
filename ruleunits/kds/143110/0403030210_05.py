import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0403030210_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.10 (5)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '합성플랜지에서 전단연결재 사이의 횡방향 최대간격'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.10 전단연결재
    (5)
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
		A[Title: 전단연결재] ;
		B["KDS 14 31 10 4.3.3.2.10 (5)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 전단연결재 사이의 횡방향 최대간격/] ;
      VarIn2[/입력변수: 박스플랜지의 두께/] ;
      VarIn3[/입력변수: 플랜지의 최소항복강도/] ;
      VarIn4[/입력변수: 균일분포 수직응력에 대한 판의 좌굴계수/]
      VarIn5[/입력변수: 강재의 탄성계수/] ;
      VarIn6[/입력변수: 박스플랜지의 한계세장비/]
			end

			Python_Class ~~~ Variable_def
			VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

			C["<img src=https://latex.codecogs.com/svg.image?\frac{s_{t}}{t_{f}}\sqrt{\frac{F_{yf}}{kE}}\leq&space;R_{1}>--------------------------"]

			Variable_def --> C --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_transverse_spacing_between_shear_connectors(fIst,fItf,fIFyf,fIk,fIE,fIR1) -> bool:
        """합성플랜지에서 전단연결재 사이의 횡방향 최대간격
        Args:
            fIst (float): 전단연결재 사이의 횡방향 최대간격
            fItf (float): 박스플랜지의 두께
            fIFyf (float): 플랜지의 최소항복강도
            fIk (float): 균일분포 수직응력에 대한 판의 좌굴계수
            fIE (float): 강재의 탄성계수
            fIR1 (float): 박스플랜지의 한계세장비

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.10 전단연결재 (5)의 통과여부
        """


        if (fIst / fItf) * (fIFyf / (fIk * fIE)) ** 0.5 <= fIR1:
          return "Pass"
        else:
          return "Fail"


# 

