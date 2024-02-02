import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041805_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.5 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '연간파괴빈도'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
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
        A[교량구성부재의 연간파괴빈도];
        B["KDS 24 12 21 4.18.5 (1)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 연간파괴빈도/];
    VarIn1[/입력변수 : 형태, 크기 및 하중조건에 의해 분류된 수로를 이용하는 연간선ㅂ가의 수/];
    VarIn2[/입력변수 : 선박의 항로이탈확률/];
    VarIn3[/입력변수 : 항로이탈한 선박이 교각이나 상부구조와 충돌할 기하학적 확률/];
    VarIn4[/입력변수 : 항로이탈한 선박과 충돌할 때 교량이 파괴될 확률/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn4

    end
    Python_Class~~~Variable_def
    D["AF=(N)(PA)(PG)(PC)"];
    E(["연간파괴빈도"]);
    Variable_def--->D--->E
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def annual_destruction_frequency(fOAF,iIN,fIPA,fIPG,fIPC) -> float:
        """연간파괴빈도

        Args:
            fOAF (float): 연간파괴빈도
            iIN (float): 형태, 크기 및 하중조건에 의해 분류된 수로를 이용하는 연간선박의수
            fIPA (float): 선박의 항로이탈 확률
            fIPG (float): 항로이탈한 선박이 교각이나 상부구조와 충돌할기하학적확률
            fIPC (float): 항로이탈한 선박과 충돌할 때 교량이 파괴될 확률

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.5 연간파괴빈도 (1) 의 값
        """

        fOAF = iIN*fIPA*fIPG*fIPC
        return(fOAF)


# 

