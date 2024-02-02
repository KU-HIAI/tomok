import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405030303 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.3.3.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '점성토의 고정점까지의 깊이'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.3.3 압축저항
    4.5.3.3.3 좌굴
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
		A[Title: 좌굴] ;
		B["KDS 14 31 10 4.5.3.3.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 고정점까지의 깊이/] ;
      VarIn1[/입력변수: 말뚝의 변형계수/] ;
      VarIn2[/입력변수: 말뚝의 단면2차 모멘트/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2
		Python_Class ~~~ Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?1.4\left|\frac{E_{p}I_{p}}{E_{s}}\right|^{0.25}>------------------------------------------"]
		F["<img src=https://latex.codecogs.com/svg.image?1.8\left|\frac{E_{p}I_{p}}{E_{h}}\right|^{0.25}>------------------------------------------"]
		C["점성토"]
		T["사질토"]

		Variable_def --> C & T
		C --> E
		T --> F
		E & F --> Q(["고정점까지의 깊이"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def depth_to_anchor_point(fOdeanpo,fIEp,fIIp,fIEs,fInh,fIuserdefined) -> bool:
        """점성토의 고정점까지의 깊이
        Args:
            fOdeanpo (float): 고정점까지의 깊이
            fIEp (float): 말뚝의 변형계수
            fIIp (float): 말뚝의 단면2차모멘트
            fIEs (float): 점성토의 변형계수
            fInh (float): 깊이에 따른 사질토의 변형계수 증가율
            fIuserdefined (float): 사용자 선택



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.3.3.3 좌굴의 값
        """

        # fIuserdefined == 1 : 점성토
        # fIuserdefined == 2 : 사질토


        if fIuserdefined == 1:
          fOdeanpo = 1.4 * abs(fIEp * fIIp / fIEs) ** 0.25
          return fOdeanpo
        elif fIuserdefined == 2:
          fOdeanpo = 1.8 * abs(fIEp * fIIp / fInh) ** 0.25
          return fOdeanpo


# 

