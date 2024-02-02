import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060701_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.7.1 (4)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-17'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '외측거더의 플랜지 유효폭'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.7 플랜지 유효폭
    4.6.7.1 일반사항
    (4)
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
     A[외측거더의 플렌지 유효폭];
     B["KDS 24 10 11 4.6.7.1 (4)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 외측거더의 플랜지 유효폭/];
    VarIn1[/입력변수 : 내측거더 유효폭/];
    VarIn2[/입력변수 : 등가지간장/];
    VarIn3[/입력변수 : 슬래브 평균두께/];
    VarIn4[/입력변수 : 복부 두께/];
    VarIn5[/입력변수 : 주거더 상부플랜지폭/];
    VarIn6[/입력변수 : 내민부분의 폭/];
    VarIn3~~~VarIn6
    VarOut~~~VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    end
    Python_Class~~~Variable_def
    D["외측거더의 플랜지 유효폭=내측거더 유효폭X0.5
    +Min(등가지간장/8,내민부분의 폭, (스래브 평균두께X6+Max(복부 두께X0.5, 주거더 상부플랜지폭/4)))"];
    E(["외측거더의 플랜지 유효폭"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  Flange_effective_width_of_outer_girder(fOWoutfl,fIWingd,fILeqsp,fItavsl,fItabdor,fIWuppfl,fIWoverh) -> float:
        """외측거더의 플랜지 유효폭

        Args:
            fOWoutfl (float): 외측거더의 플랜지 유효폭
            fIWingd (float): 내측거더 유효폭
            fILeqsp (float): 등가지간장
            fItavsl (float): 슬래브 평균두께
            fItabdor (float): 복부 두께
            fIWuppfl (float): 주거더 상부플랜지폭
            fIWoverh (float): 내민부분(overhang)의 폭

        Returns:
            float: 교량 설계 일반사항(한계상태설계법) 4.6.7.1(4) 외측거더의 플랜지 유효폭
        """
        fOWoutfl=fIWingd/2+min(fILeqsp/8,6*fItavsl+max(fItabdor/2,fIWuppfl/4),fIWoverh)
        return fOWoutfl


