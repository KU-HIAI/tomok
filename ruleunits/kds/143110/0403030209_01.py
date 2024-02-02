import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0403030209_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.9 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경사진 웨브의 웨브 높이'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.9 전단강도
    (1)
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
		A[Title: 전단강도] ;
		B["KDS 14 31 10 4.3.3.2.9 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
			VarOut1[/출력변수: 계수하중에 의한 전단력/] ;
      VarIn1[/입력변수: 웨브 높이/] ;
      VarIn2[/입력변수: 경사진 웨브 1개에 작용하는 계수하중에 의한 전단력/] ;
      VarIn3[/입력변수: 연직축에 대한 웨브의 경사각/] ;
			end

			Python_Class ~~~ Variable_def
			VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

			C["<img src=https://latex.codecogs.com/svg.image?V_{ui}=\frac{V_{u}}{cos\theta}>--------------------"]

			Variable_def --> C -->D(["<img src=https://latex.codecogs.com/svg.image?V_{ui}>-------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def web_height(fOVui,fIVu,fItheta) -> bool:
        """충격계수
        Args:
            fOVui (float): 계수하중에 의한 전단력
            fIVu (float): 경사진 웨브 1개에 작용하는 계수하중에 의한 전단력
            fItheta (float): 연직축에 대한 웨브의 경사각

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.9 전단강도 (1)의 값
        """


        fOVui = fIVu / math.cos(fItheta)
        return  fOVui


# 

