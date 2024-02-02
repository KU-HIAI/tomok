import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03020303_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.2.3.3 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기초의 활동저항'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.3 활동 파괴
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
    A[활동파괴];
    B["KDS 24 14 51 3.2.3.3 (3)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수: 점성토의 점착력/];
			VarIn2[/입력변수: 기초와 흙사이 경계면상 수직응력/];


			VarIn1 ~~~ VarIn2

      end
      Python_Class ~~~ Variable_def;
      Variable_def
			C[점성토에 설치된 기초의 활동저항]
			D["min(점성토의 점착력,150mm이상 다져진 사질토위에 놓이는 경우의 기초와 흙사이의 경계면상 수직응력의 1/2)"]


			Variable_def ---> C ---> D
			D ---> G([점성토에 설치된 기초의 활동저항])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Foundation_Resistance(fIAdhvis,fIVersoi) -> float:
        """기초의 활동저항
        Args:
            fIAdhvis (float): 점성토의 점착력
            fIVersoi (float): 기초와 흙사이 경계면상 수직응력

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.3 (3)의 기초의 활동저항력 값
        """
        return min(fIAdhvis,0.5*fIVersoi)


# 

