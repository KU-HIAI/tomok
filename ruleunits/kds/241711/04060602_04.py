import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060602_04(RuleUnit): # KDS241711_04060602_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.2 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '소요 변위연성도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
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
    A[Title: 소요연성도];
    B["KDS 24 17 11 4.6.6.2 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 소요 변위연성도/] ;
    VarOut2[/출력변수: 변위연성도-응답 수정계수 상관계수/] ;
    VarIn1[/입력변수: 소요 응답수정계수/] ;
    VarIn2[/입력변수: 1차 모드 주기/];
    VarIn3[/입력변수: 상한통제주기/];
		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ Variable_def --소요 응답수정계수 1.0이상-->E -->D
    D(["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\triangle}'>---------"]);
    E["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\triangle}=\lambda&space;_{DR}R_{req}'>---------------------------------------"]
    F["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{DR}=(1-\frac{1}{R_{req}})\frac{1.25T_{s}}{T}&plus;\frac{1}{R_{req}}'>-----------------------------------------------------------------"]
    H{"1차 모드 주기 < 상한통제주기 x1.25"}
    J(["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{DR}'>-----------"])
Variable_def --> H --Yes-->F-->J
H--No-->K([1.0])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def required_displacement_ductility(fOmudelta,fIlambdaDR,fIRreq,fIT,fITs) -> float:
        """소요 변위연성도

        Args:
            fOmudelta (float): 소요 변위연성도
            fIlambdaDR (float): 변위연성도-응답수정계수 상관계수
            fIRreq (float): 소요 응답수정계수
            fIT (float): 1차 모드 주기
            fITs (float): 상한통제주기

        Returns:
            float: fOmudelta, 소요 변위연성도
        """

        if fIRreq >= 1.0:
          if fIT < 1.25 * fITs:
            fIlambdaDR = (1 - 1 / fIRreq) * 1.25 * fITs / fIT + 1 / fIRreq
            fOmudelta = fIlambdaDR * fIRreq
            return fOmudelta
          else:
            fIlambdaDR = 1.0
            fOmudelta = fIlambdaDR * fIRreq
            return fOmudelta