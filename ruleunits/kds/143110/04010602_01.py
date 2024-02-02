import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04010602_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.6.2 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반 강구조 아이바 구조제한'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.6 아이바
    4.1.6.2 아이바의 구조제한
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
		A[아이바의 구조제한] ;
		B["KDS 14 31 10 4.1.6.2(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 아이바의 원형 머리부분/]
    VarIn2[/입력변수: 몸체 사이 부분의 반지름/]
    VarIn3[/입력변수: 아이바 머리의 직경/]
    VarIn4[/입력변수: 핀 직경/]
    VarIn5[/입력변수: 아이바 몸체 폭/]
    VarIn6[/입력변수: 핀 구멍의 직경/]
    VarIn7[/입력변수: 핀 직경/]
		end

		Python_Class ~~~ Variable_def
	  C(["아이바의 원형 머리부분, 몸체 사이부분의 반지름 > 아이바 머리의 직경"]) ;
    D(["핀 직경 > 아이바 몸체폭x7/8"]) ;
	  E(["핀 구멍의 직경 ≤ 핀직경 +1mm"]) ;
    F["<img src='https://latex.codecogs.com/svg.image?F_{y}>460MPa'>----------------------------"] ;
	  G(["구멍직경<플레이트 두께x5"]) ;
    H(["핀 플레이트와 필러 플레이트를 조임하기 위해 외부 너트를 사용하는 경우"]) ;
    I(["플레이트 두께 ≤ 13mm"]) ;
    J(["아이바 몸체폭x2/3≤플레이트의 연단까지의 폭≤아이바 몸체폭x3/4"]) ;

	  Variable_def-->C
	  Variable_def-->D
	  Variable_def-->E
	  Variable_def-->F-->G
	  Variable_def-->H-->I
	  Variable_def-->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def structure_limit_of_eyebar(fIracheb,fIrapbib,fIdiebhe,fIdiapin,fIebbowi,fIdipiho,fIfy,fIdiahol,fItnp,fIvmwp,fIuserdefined) -> bool:
        """일반 강구조 아이바 구조제한

        Args:
            fIracheb (float): 아이바의 원형 머리부분 반지름
            fIrapbib (float): 몸체 사이부분의 반지름
            fIdiebhe (float): 아이바 머리의 직경
            fIdiapin (float): 핀 직경
            fIebbowi (float): 아이바 몸체 폭
            fIdipiho (float): 핀 구멍의 직경
            fIfy (float): 항복강도
            fIdiahol (float): 구멍 직경
            fItnp (float): 플레이트 두께
            fIvmwp (float): 핀 구멍의 연단으로부터 힘의 방향에 수직으로 측정한 플레이트 연단까지의 폭
            fIuserdefined (float): 사용자선택


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.1.6.2 아이바의 구조제한 (1)의 통과여부
        """

        #핀 플레이트와 필러 플레이트를 조임하기 위해 외부 너트를 사용하지 않는 경우 : fIuserdefined == 1

        #①
        if fIracheb > fIdiebhe and fIrapbib > fIdiebhe and fIdiapin > fIebbowi*7/8 and fIdipiho < (fIdiapin+1) :
          p = 1
        else:
          p = 0

        #②
        if fIfy > 460 :
          if fIdiahol <= fItnp * 5:
            p = p*1
          else:
            p = p*0

        #③
        if fIuserdefined == 1:
          if fItnp > 13:
            p = p*1
          else:
            p = p*0

        #④
        if 2/3 * fIebbowi < fIvmwp <= 3/4 * fIebbowi:
          p = p*1
        else:
          p = p*0

        if p == 1:
          return 'Pass'
        else:
          return 'Fail'


# 

