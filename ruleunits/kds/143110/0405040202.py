import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040202 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.2.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소토피고'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.2 최소토피고
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
		A[Title: 최소토피고] ;
		B["KDS 14 31 10 4.5.4.2.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 최소토피고/] ;
      VarOut2[/출력변수: 대골형 파형간판의 최소토피고/] ;
      VarIn1[/입력변수: 구조물 스프링라인 사이 거리/] ;
      VarIn2[/입력변수: 구조물 단면 점검부에서 스프링라인까지 연직거리의 2배/] ;
			end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?H_{min}=Max(0.6,\frac{D_{h}}{6}\left(\frac{D_{h}}{D_{v}}\right)^{0.5},0.4\left(\frac{D_{h}}{D_{v}}\right)^{2})>---------------------------------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?H_{min}=Min(Max(0.6,\frac{D_{h}}{6}\left(\frac{D_{h}}{D_{v}}\right)^{0.5},0.4\left(\frac{D_{h}}{D_{v}}\right)^{2})or&space;1.5)>------------------------------------------------------------------"]
		Variable_def --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?H_{min}>-----------"])
		Variable_def --> R --> F(["<img src=https://latex.codecogs.com/svg.image?H_{min}>-----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def minimum_cover(fOHmin,fIDh,fIDv,fIuserdefined) -> bool:
        """최소토피고
        Args:
            fOHmin (float): 최소토피고
            fIDh (float): 구조물 스프링라인 사이 거리
            fIDv (float): 구조물 단면 정점부에서 스프링라인까지 연직거리의 2배
            fIuserdefined (float): 사용자 선택


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.2 최소토피고의 값
        """


        # fIuserdefined == 1 : 아치형 파형강판 지중구조물의 단면 정점부에서 뒤채움 흙의 최소높이
        # fIuserdefined == 2 : 대골형 파형강판의 최소토피고

        if fIuserdefined == 1:
          fOHmin = max(0.6, (fIDh / 6) * (fIDh / fIDv) ** 0.5, 0.4 * (fIDh / fIDv) ** 2)
          return fOHmin
        elif fIuserdefined == 2:
          fOHmin = min(max(0.6, (fIDh / 6) * (fIDh / fIDv) ** 0.5, 0.4 * (fIDh / fIDv) ** 2),1.5)
          return fOHmin


# 

