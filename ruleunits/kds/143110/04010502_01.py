import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04010502_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.5.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반 강구조물의 핀접합부재 구조제한'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.2 핀접합부재의 구조제한
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
		A[핀접합부재의 구조제한] ;
		B["KDS 14 31 10 4.1.5.2(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 핀구멍의 직경/]
    VarIn2[/입력변수: 핀직경/]
    VarIn3[/입력변수: 핀구멍이 있는 플레이트의 폭/]
    VarIn4[/입력변수: 유효연단거리/]
    VarIn5[/입력변수: 재축에 평행한 핀구멍의 연단거리/]
		end

		Python_Class ~~~ Variable_def
	  C["핀구멍의 직경"] ;
    D(["핀구멍의 직경 ≤ 핀직경+1mm"]) ;
	  E["핀구멍이 있는 플레이트의 폭"] ;
    F(["핀구멍이 있는 플레이트폭<img src='https://latex.codecogs.com/svg.image?\geq&space;2b_{eff}&plus;d'>-------------------------------- "]) ;
	  G["재축에 평행한 핀구멍의 연단거리a"] ;
    H(["<img src='https://latex.codecogs.com/svg.image?a\geq&space;1.33b_{eff}'>---------------------------"])

	  Variable_def-->C-->D
	  Variable_def-->E-->F
	  Variable_def-->G-->H
	  D & F & H --> I([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def structure_limit_of_pin_member(fIdipiho,fId,fIwiplpH,fIbeff,fIa) -> bool:
        """일반 강구조물의 핀접합부재 구조제한

        Args:
            fIdipiho (float): 핀구멍의 직경
            fId (float): 핀직경
            fIwiplpH (float): 핀구멍이 있는 플레이트의 폭
            fIbeff (float): 유효연단거리
            fIa (float): 재축에 평행한 핀구멍의 연단거리

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.1.5.2 핀접합부재의 구조제한 (1)의 통과여부
        """

        if fIdipiho <= (fId+1) and fIwiplpH >= (2*fIbeff + fId) and fIa >= 1.33*fIbeff:
          return 'Pass'
        else:
          return 'Fail'


# 

