import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040501030201_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.1.3.2.1 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '상대구속 가새 소요모멘트'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.3 보 안정용 가새
    4.5.1.3.2 비틀림좌굴 가새
    4.5.1.3.2.1 상대구속 가새
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
		A[Title: 상대구속 가새] ;
		B["KDS 14 31 10 4.5.1.3.2.1 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 소요모멘트/] ;
      VarIn1[/입력변수: 소요휨강도/] ;
      VarIn2[/입력변수: 부재길이/] ;
      VarIn3[/입력변수: 경간 내에서 가새 지점의 수/] ;
      VarIn4[/입력변수: 모멘트 분포에 따른 보정계수/] ;
      VarIn5[/입력변수: 횡적 비지지길이/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5

		Python_Class ~~~ Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?M_{bu}=\frac{0.024M_{u}L}{nC_{b}L_{b}}>--------------------------------"]



		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?M_{bu}>----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def required_moment(fOMbu,fIMu,fIL,fIn,fICb,fILb) -> bool:
        """상대구속 가새 소요모멘트
        Args:
            fOMbu (float): 소요모멘트
            fIMu (float): 소요휨강도
            fIL (float): 부재길이
            fIn (float): 경간 내에서 가새 지점의 수
            fICb (float): 모멘트 분포에 따른 보정계수
            fILb (float): 횡적 비지지길이

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.1.3.2.1 상대구속 가새 (1)의 값
        """

        fOMbu = (0.024 * fIMu * fIL) / (fIn * fICb * fILb)
        return fOMbu


# 

