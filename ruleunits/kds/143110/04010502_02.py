import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04010502_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.5.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '교량강구조의 핀접합부재 구조제한'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.2 핀접합부재의 구조제한
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
		A[핀접합부재의 구조제한] ;
		B["KDS 14 31 10 4.1.5.2(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 모재판/]
    VarIn2[/입력변수: 핀 보강판의 순단면적/]
    VarIn3[/입력변수: 핀구멍이 없는 단면에서 필요한 모재판의 순단면적/]
    VarIn4[/입력변수: 종방향으로의 모재판/]
    VarIn5[/입력변수: 핀구멍의 직경/]
    VarIn6[/입력변수: 핀직경/]
    VarIn7[/입력변수: 최소항복강도/]
    VarIn8[/입력변수: 구멍의 직경/]
    VarIn9[/입력변수: 핀 보강판의 두께/]
    VarIn10[/입력변수: 구멍 끝에서 핀 연단거리/]
    VarIn11[/입력변수: 모재판의 두께/]
		end
    VarIn1~~~VarIn7
    VarIn2~~~VarIn8
    VarIn3~~~VarIn9
    VarIn4~~~VarIn10
    VarIn5~~~VarIn11
    VarIn6~~~VarIn11

		Python_Class ~~~ Variable_def
	  C(["모재판과 핀 보강판의 순단면적의 합 > 핀구멍이 없는 단면에서 필요한 모재판의 순 단면적X1.4"]) ;
    D(["종방향으로의 모재판과 핀 보강판의 순단면적의 합 > 핀구멍이 없는 단면에서 필요한 모재판의 순단면적"]) ;
	  E(["핀구멍의 직경 ≤ 핀의 직경 +0.8mm"]) ;
    F(["구멍의 직경 ≤ (모재판+핀 보강판의 두께)x5"]) ;
	  G["최소항복강도 > 460Mpa"] ;
    H(["모재판과 핀 보강판의 두께의 합 ≥ 구멍 끝에서 핀 연단거리x0.12"])
    I(["모재판의 두께 > 핀구멍이 없는 단면의 폭x0.12"])

	  Variable_def-->C
	  Variable_def--->D
	  Variable_def--->E
	  Variable_def-->G-->F
    Variable_def-->H
    Variable_def-->I

	  C & D & E & F & H & I ---> J([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def structure_limit_of_pin_member_2(fIpartri,fIncsprp,fIncspr,fIpatrld,fIdipiho,fId,fImiyist,fIholdia,fIthfirp,fIpiedhe,fIthpapl,fIwswp) -> bool:
        """교량강구조의 핀접합부재 구조제한

        Args:
            fIpartri (float): 모재판
            fIncsprp (float): 핀 보강판의 순단면적
            fIncspr (float): 핀구멍이 없는 단면에서 필요한 모재판의 순단면적
            fIpatrld (float): 종방향으로의 모재판 순단면적
            fIdipiho (float): 핀구멍의 직경
            fId (float): 핀직경
            fImiyist (float): 최소항복강도
            fIholdia (float): 구멍의 직경
            fIthfirp (float): 핀 보강판의 두께
            fIpiedhe (float): 구멍 끝에서 핀 연단거리
            fIthpapl (float): 모재판의 두께
            fIwswp (float): 핀구멍이 없는 단면의 폭


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.1.5.2 핀접합부재의 구조제한 (2)의 통과여부
        """

        #①
        if fIpartri+fIncsprp > 1.4*fIncspr:
          p = 1
        else:
          p = 0

        #②
        if fIpatrld+fIncsprp > fIncspr:
          p = p*1
        else:
          p = p*0

        #③
        if fIdipiho <= fId + 0.8:
          p = p*1
        else:
          p = p*0

        #④
        if fImiyist > 460:
          if fIholdia <= 5*(fIthpapl+fIthfirp):
            p = p*1
          else:
            p = p*0

        #⑤
        if fIthpapl+fIthfirp >= fIpiedhe * 0.12 and fIthpapl > fIwswp * 0.12:
          p = p*1
        else:
          p = p*0

        if p == 1:
          return 'Pass'
        else:
          return 'Fail'


# 

