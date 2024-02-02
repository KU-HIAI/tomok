import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040104_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.4 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-23'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '조립 인장부재의 재축방향 긴결간격'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.4 조립 인장부재
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
		A[조립 인장부재] ;
		B["KDS 14 31 10 4.1.4(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 조립 인장부재의 재축방향 긴결간격/]
    VarIn2[/입력변수: 얇은 판 두께/]

		end

		Python_Class ~~~ Variable_def
  	C["도장된 부재 또는 부식의 우려가 없어 도장되지 않는 부재의 경우"]
  	D["대기 중 부식에 노출된 도장되지 않는 내후성강의 경우"]
    E(["조립 인장부재의 재축방향 긴결간격 ≤ 얇은 판 두께의 24배 or 300mm"])
    F(["조립 인장부재의 재축방향 긴결간격 ≤ 얇은 판 두께의 14배 or 180mm"])
	  Variable_def --> C & D
    C-->E-->G([PASS or Fail]);
    D-->F-->H([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Tightening_interval_in_the_reaxial_direction_of_the_assembly_tension_member(fItirdtm,fIthplth,fIuserdefined) -> bool:
        """조립 인장부재의 재축방향 긴결간격

        Args:
            fItirdtm (float): 조립 인장부재의 재축방향 긴결간격
            fIthplth (float): 얇은 판 두께
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.1.4 조립 인장부재 (1)의 통과여부
        """
        #도장된 부재 또는 부식의 우려가 없어 도장되지 않은 부재의 경우 > fIuserdefined == 1
        #대기 중 부식에 노출된 도장되지 않은 내후성강의 경우 > fIuserdefined == 2

        if fIuserdefined == 1:
          if fItirdtm <= min(fIthplth*24,300):
            return 'Pass'
          else:
            return 'Fail'

        if fIuserdefined == 2:
          if fItirdtm <= min(fIthplth*14,180):
            return 'Pass'
          else:
            return 'Fail'


# 

