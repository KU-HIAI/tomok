import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04010304_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.1.3.4 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '중심 간격'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.3 설계
    4.1.3.4 설계상세
    (3)
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
    A[설계하중];
    B["KDS 24 90 11 4.1.3.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
			VarIn1[/입력변수: 중심간격/];
			VarIn2[/입력변수: 공기 배출 구멍 직경/];





	  VarIn1

		end
		Python_Class ~~~ Variable_def--->E--->F






		E["중심간격≤460mm, 20mm≤공기 배출 구멍 직경"]
		F(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Centre_To_Centre_Distance (fIcencdi,fIairodi) -> bool:
        """중심 간격
        Args:
            fIcencdi (float): 중심 간격
            fIairodi (float): 공기 배출 구멍 직경


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.1.3.4 설계상세 (3)의 통과 여부
        """

        if fIcencdi <= 460 :
            if fIairodi>= 20 :
                return "Pass"
            else:
                return "Fail"
        else:
           return "Fail"


# 

