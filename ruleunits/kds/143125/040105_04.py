import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_040105_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.5' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트접합에서 끼움재의 두께'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.5 끼움재
    (4)
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
	  A([끼움재])
	  B["KDS 14 31 25 4.1.5(4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 두께/]
	  VarIn2[/입력변수: 끼움재/]
	  end

	  Python_Class ~~~ Variable_def --> C --> D --pass-->E
	  C["6mm < 끼움재 두께 ≤ 19mm"]
	  D["Pass or Fail"]
	  E(["끼움재두께 x<img src='https://latex.codecogs.com/svg.image?\left\lceil&space;1-0.0154(t-6)\right\rceil'>--------------------------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Thickness_of_filler_material_in_bolted_connections(fOthifil,fIresfac,fIt) -> bool:
        """볼트접합에서 끼움재의 두께

        Args:
            fOthifil (float): 끼움재의 두께
            fIresfac (float): 감소계수
            fIt (float): 끼움재의 전체두께
D
        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.5 볼트접합에서 끼움재의 두께 (4)의 값
        """
        fIresfac = [1-0.0154*(fIt-6)]

        if 6 < fOthifil <= 19 :
          fOthifil = fIresfac * fOthifil
          return fOthifil
        else:
          return fOthifil


# 

