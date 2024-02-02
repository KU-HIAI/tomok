import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060702_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jong Hyeok'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.7.2 (2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-14'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '플렌지 유효폭 계산시 세부사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.7 플랜지 유효폭
    4.6.7.2 박스형 세그멘탈 콘크리트 보 및 단 격실 박스형 현장타설 콘크리트 보
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
        A[플렌지 유효폭 계산시 세부사항];
        B["KDS 24 10 11 4.6.7.2 (2)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 내부지점 또는 캔틸레버 구간에서의 플랜지 유효폭/];
    VarIn1[/입력변수 : 플랜지 유효폭/];
    VarIn2[/입력변수 : 물리적인 폭/];
    VarIn3[/입력변수 : 지간의 유효지간장/];
    end
    Python_Class~~~Variable_def
    D{"물리적인 폭 &ge; 플랜지 유효폭"};
    E["bs= 지점부의 인접한 지간의 유효지간장 중 큰값"];
    F(["Pass or Fail"]);
    Variable_def--->D--Yes--->E--->F
    D---No--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  detail_of_effective_length_of_flange(fIWefffl,fIWphy,fObs,fILeffsp) -> bool:
        """플렌지 유효폭 계산시 세부사항
        Args:
            fIWefffl (float): 플랜지 유효폭
            fIWphy (float): 물리적인 폭
            fObs (float): 내부지점 또는 캔틸레버 구간에서의 플랜지 유효폭
            fILeffsp (float): 지간의 유효지간장

        Returns:
            float: 교량 설계 일반사항(한계상태설계법) 4.6.7.2 박스형 세그멘탈 콘크리트 보 및 단 격실 박스형 현장타설 콘크리트 보 (2)의 통과여부
        """
        if fIWefffl <= fIWphy and fObs == (max(fILeffsp)):
          return(fObs, "Pass")
        else:
          return(fObs, "Fail")


