import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060602_02(RuleUnit): # KDS241711_04060602_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.2 (2)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '소요 응답수정계수'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
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
    A[소요 응답수정계수];
    B["KDS 24 17 11 4.6.6.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 소요 응답수정계수/] ;
    VarIn1[/입력변수: 지진하중을 포함한 하중조합에 따른 기둥의 탄성모멘트/] ;
    VarIn2[/입력변수: 기둥의 설계휨강도/];
		VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ Variable_def --> E
    D(["소요 응답수정계수"]);
    E["<img src='https://latex.codecogs.com/svg.image?R_{req}=\frac{M_{el}}{\phi&space;M_{n}'>---------------------"]


    E--> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def required_response_modification_factor(fIMel,fIphiMn) -> float:
        """소요 응답수정계수

        Args:
            fORreq (float): 소요 응답수정계수
            fIMel (flaot): 지진하중을 포함한 하중조합에 따른 기둥의 탄성모멘트
            fIphiMn (flaot): 기둥의 설계휨강도

        Returns:
            float: fORreq, 소요 응답수정계수
        """

        fORreq = fIMel / fIphiMn
        return fORreq