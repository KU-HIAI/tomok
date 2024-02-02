import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04010602_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.6.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '교량 강구조 아이바 구조제한'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.6 아이바
    4.1.6.2 아이바의 구조제한
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
		A[아이바의 구조제한] ;
		B["KDS 14 31 10 4.1.6.2(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 아이바의 두께/]
    VarIn2[/입력변수: 머리부분의 순폭/]
    VarIn3[/입력변수: 물체부의 폭/]
    VarIn4[/입력변수: 두께/]
    VarIn5[/입력변수: 관구멍의 중심/]
    VarIn6[/입력변수: 아이바 몸체의 중심축/]
    VarIn7[/입력변수: 핀구멍의 직경/]
    VarIn8[/입력변수: 핀의 직경/]
    VarIn9[/입력변수: 최소항복강도/]
    VarIn10[/입력변수: 구멍의 직경/]

    VarIn1~~~ VarIn6
    VarIn2~~~ VarIn7
    VarIn3~~~ VarIn8
    VarIn4~~~ VarIn9
    VarIn5~~~ VarIn10

		end


		Python_Class ~~~ Variable_def
	  C([" 13mm ≤ 아이바의 두께 ≤ 50mm"]) ;
    D(["핀구멍의 중심선에서 측정한 머리부분의 순폭 ≥ 몸체부의 폭x1.35"]) ;
	  E(["머리부분의 순폭 ≥ 몸체부 폭x0.75"]) ;
    F(["물체부의 폭 < 두께x8"]) ;
	  G(["핀구멍의 중심 on 아이바 몸체의 중심축"]) ;
    H(["핀구멍의 직경 ≤ 핀의 직경+0.8mm"]) ;
    I["최소항복강도 > 460MPa"] ;
    J(["구멍의 직경 < 아이바 두께x5"]) ;

	  Variable_def-->C
	  Variable_def-->D
	  Variable_def-->E
	  Variable_def-->F
	  Variable_def-->G
	  Variable_def-->H
	  Variable_def-->I-->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def structure_limit_of_eyebar(fIibathi,fInewihe,fIbodwid,fIbodthi,fIdipiho,fIdiapin,fImiyist,fIdiahol,fIuserdefined) -> bool:
        """교량 강구조 아이바 구조제한

        Args:
            fIibathi (float): 아이바의 두께
            fInewihe (float): 머리부분의 순폭
            fIbodwid (float): 몸체부의 폭
            fIbodthi (float): 몸체부 두께
            fIdipiho (float): 핀구멍의 직경
            fIdiapin (float): 핀의 직경
            fImiyist (float): 최소항복강도
            fIdiahol (float): 구멍의 직경
            fIuserdefined (float): 사용자선택


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.1.6.2 아이바의 구조제한 (2)의 통과여부
        """
        #핀구멍의 중심선에서 측정한 머리부분의 순폭 : fIuserdefined == 1
        #핀구멍을 지나 아이바의 길이방향에서 측정한 머리부분의 순폭 : fIuserdefined == 2

        #①
        if 13 <= fIibathi <= 50 :
          p = 1
        else:
          p = 0

        #②
        if fIuserdefined == 1 :
          if fInewihe >= fIbodwid * 1.35:
            p = p*1
          else:
            p = p*0

        #③
        if fIuserdefined == 2 :
          if fInewihe >= fIbodwid * 0.75:
            p = p*1
          else:
            p = p*0

        #④
        if fIbodwid <= fIbodthi * 8:
          p = p*1
        else:
          p = p*0

        #⑥
        if fIdipiho <= (fIdiapin + 0.8):
          p = p*1
        else:
          p = p*0

        #⑦
        if fImiyist > 460:
          if fIdiahol <= fIibathi * 5:
            p = p*1
          else:
            p = p*0


        if p == 1:
          return 'Pass'
        else:
          return 'Fail'


# 

