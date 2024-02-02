import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_0401_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.1 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '앵커의 강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.1 설계 일반
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
    A[앵커의 강도];
    B["KDS 14 20 54 4.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 앵커의 강도/];
    VarIn2[/입력변수 : 최대 소요강도/];
    end
    Python_Class~~~Variable_def
    D["앵커의 강도 &ge; KDS 14 20 10(3.2)의 적용 가능한 하중조합에 의해 결정되는 최대소요강도"];
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def anchor_strength(fIstranc,fIstrmax) -> bool:
        """앵커의 강도

        Args:
            fIstranc (float): 앵커의 강도
            fIstrmax (float): 최대 소요강도

        Returns:
            float: 콘크리트용 앵커 설계기준  4.1 설계 일반 (2)의 통과 여부

        """

        if fIstranc >= fIstrmax :
            return "Pass"
        else:
            return "Fail"


# 

