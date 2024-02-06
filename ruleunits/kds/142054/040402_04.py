import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040402_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.2 (4)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '앵커 샤프트 중심부터 콘크리트 단부까지의거리'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
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
    A[앵커 샤프트 중심부터 콘크리트단부까지의 거리 산정];
    B["KDS 14 20 54 4.4.2 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트단부까지의 거리/];
    VarIn2[/입력변수 : 앵커가 정착되는 부재 두께/];
    VarIn3[/입력변수 : 전단력 직각방향으로 가장 큰 앵커사이 간격/];
    VarIn4[/입력변수 : 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트 단부까지 거리/];
    VarIn1~~~VarIn3
    VarIn2~~~VarIn4
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?c_{a2}<1.5c_{a1},h_{a}<1.5c_{a1}'>를 모두 만족하는 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?c_{a1}\leq&space;Max(c_{a2}/1.5,h_{a}/1.5,s/3)'>------------------------------------"];
    F(["Pass or Fail"]);
    Variable_def--->D--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Distance_from_anchor_shaft_center_to_concrete_end(fIha,fIcaone,fIcatwo,fIs)-> float:
        """앵커가 정착되는 부재 두께 (앵커 축과 평행한 방향)

        Args:
            fIha (float): 앵커가 정착되는 부재 두께 (앵커축과평행한방향)
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의거리
            fIcatwo (float): 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트단부까지 거리
            fIs (float): 앵커의 중심 간격

        Returns:
            float: 콘크리트용 앵커 설계기준 4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 통과여부
        """
        if fIcatwo < 1.5 * fIcaone and fIha < 1.5 * fIcaone :
          if fIcaone <= max(fIcatwo/1.5, fIha/1.5, fIs/3) :
            return "Pass"
          else:
            return "Fail"


