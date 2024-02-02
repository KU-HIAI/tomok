import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040504020304 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.2.3.4' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '충격계수'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
    4.5.4.2.3.4 충격계수
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
		A[Title: 충격계수] ;
		B["KDS 14 31 10 4.5.4.2.3.4"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 충격계수/] ;
      VarIn1[/입력변수: 최소 충격계수/] ;
      VarIn2[/입력변수: 설계토피고/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?i=0.4(1-0.5\times&space;H)\geq&space;0.1>--------------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?i_{min}=0.1>------------------"]

		Variable_def --> W --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?i>--"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def impact_factor(fIi,fIimin,fIH) -> bool:
        """충격계수
        Args:
            fIi (float): 충격계수
            fIimin (float): 최소 충격계수
            fIH (float): 설계토피고

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3.4 충격계수의 값
        """


        fIimin = 0.1
        if 0.4 * (1 - 0.5 * fIH) >= 0.1:
          fIi = 0.4 * (1 - 0.5 * fIH)
          return "Pass"
        else:
          return "Fail"


# 

