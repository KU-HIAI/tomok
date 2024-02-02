import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020605_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.6.5 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '알루미늄 합금'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.5 재료
    (5)
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
    A[알루미늄 합금];
    B["KDS 24 90 11 4.2.6.5 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 코팅의 최소 평균두께/];
		VarIn2[/입력변수: 최소 국부두께/];
		VarIn3[/입력변수: 거칠기/];

	  VarIn1 & VarIn2 & VarIn3


		end

		Python_Class ~~~ Variable_def;
		Variable_def--->L
		Variable_def--->K
			Variable_def--->M

		L(["코팅의 최소 평균두께=15μm"])
		M(["최소 국부두께=14μm"])
		K(["거칠기<3μm"])
		K~~~ |"KS B ISO 4287"| K
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_Average_Thickness_Of_The_Coating(fIminavg,fIminlth,fIRy5i) -> bool:
        """알루미늄 합금

        Args:
            fIminavg (float): 코팅의 최소 평균두께
            fIminlth (float): 최소 국부두께
            fIRy5i (float): 거칠기

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.6.5 재료 (5) 의 통과 여부
        """

        if fIminavg >= 15 and fIminlth >= 14 and fIRy5i <= 3 :
          return  "Pass"
        else :
          return "Fail"


# 

