import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040402_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.2 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-29'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기본 콘크리트 브레이크아웃 강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
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
    A[전단력을 받는 앵커의 기본 콘크리트 브레이크아웃강도];
    B["KDS 14 20 54 4.4.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 기본 콘크리트 브레이크아웃 강도/];
    VarIn2[/입력변수 : 전단력에 대해 앵커가 지압을 받는 길이/];
    VarIn3[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형 볼트의 샤프트 지름/];
    VarIn4[/입력변수 : 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수/];
    VarIn5[/입력변수 : 콘크리트의 설계기준압축강도/];
    VarIn6[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
    VarIn7[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3~~~VarIn6
    end
    Python_Class~~~Variable_def
    D{"앵커 구분"};
    E["헤드스터드 및 전체 묻힘깊이에 걸쳐 단일 관을 가지는 후설치앵커인 경우"];
    F["간격 슬리브가 확장슬리브와 분리된 비틀림제어 확장앵커인 경우"];
    G["<img src='https://latex.codecogs.com/svg.image?l_{e}=h_{ef}(\leq&space;8d_{a})'>----------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?l_{e}=2d_{a}'>"];
    I["<img src='https://latex.codecogs.com/svg.image?V_{b}\leq&space;Min\left(\left(0.6\left(\frac{l_{e}}{d_{a}}\right)^ {0.2}\sqrt{d_{a}}\right)\lambda_{a}\sqrt{f_{ck}}(c_{a1})^{1.5},3.7\lambda_{a}\sqrt{f_{ck }}(c_{a1})^{1.5}\right)'>---------------------------------------------------------------------------------"];
    J(["Pass or Fail"]);
    Variable_def--->D--->E--->G--->I--->J
    D--->F--->H--->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Basic_Concrete_Breakout_Strength(fIVb,fIle,fIda,fIlamda,fIfck,fIcaone,fIhef,fIuserdefined) -> float:
        """기본 콘크리트 브레이크아웃 강도

        Args:
            fIVb (float): 기본 콘크리트 브레이크아웃 강도
            fIle (float): 전단력에 대해 앵커가 지압을 받는 길이
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름
            fIlamda (float): 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수
            fIfck (float): 콘크리트의 설계기준압축강도
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의거리
            fIhef (float): 앵커의 유효묻힘깊이
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준 4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (2)의 통과여부
        """

        #헤드스터드 및 전체 묻힘깊이에 걸쳐 단일 관을 가지는 후설치앵커인 경우: fIuserdefined = 1
        #간격슬리브가 확장슬리브와 분리된 비틀림제어 확장앵커인 경우: fIuserdefined = 2

        if fIuserdefined == 1:
          fIle = fIhef
          if fIVb <= min((0.6 * ((fIle / fIda)**0.2) * (fIda**0.5)) * fIlamda * (fIfck**0.5) * (fIcaone**1.5), 3.7 * fIlamda * (fIfck**0.5) * (fIcaone**1.5)) and fIle <= 8 * fIda :
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined == 2:
          fIle = 2 * fIda
          if fIVb <= min((0.6 * ((fIle / fIda)**0.2) * (fIda**0.5)) * fIlamda * (fIfck**0.5) * (fIcaone**1.5), 3.7 * fIlamda * (fIfck**0.5) * (fIcaone**1.5)) and fIle <= 8 * fIda :
            return "Pass"
          else:
            return "Fail"


