import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jaeguk Jang'  # 작성자명
    ref_code = 'KDS 14 20 24 4.2.2 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-08-23'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 스트럿의 유효압축강도 산정'    # 건설기준명

    #
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.2 스트럿의 축강도
    4.2.2 유효압축강도
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
    A[콘크리트 스트럿 압축강도를 계산할 때 균열의 영향과 구속철근의 영향을 고려하기 위한 계수];
    B["KDS 14 20 24 4.2.2 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut1[/출력변수 : 균열의 영향과 구속철근의 영향을 고려하기 위한 계수/];
    VarIn1[/입력변수 : 경량 콘크리트 계수/];
    VarIn2[/입력변수 : 스트럿 길이 중앙부의 단면적/];
    VarIn3[/입력변수 : 스트럿 양단의 단면적/];
    end
    Python_Class~~~Variable_def
    D{"전 길이에 걸쳐 스트럿의 단면적이 일정한 경우"}
    E{"'스트럿 길이 중앙부의 단면적>스트럿 양단의 단면적'
    조건을 만족하는 스트럿인 경우에서
    4.2.3 철근 배치에 관한 규정 만족하는 경우"};
    F{"인장요소 또는 콘크리트 구조 부재의 인장플랜지 콘크리트의 스트럿인 경우"}
    G{"기타의 모든 경우"}
    H["<img src='https://latex.codecogs.com/svg.image?\beta_{s}=1.0'>----------------------------"];
    I["<img src='https://latex.codecogs.com/svg.image?\beta_{s}=0.60'>-------------------------------"];
    J["<img src='https://latex.codecogs.com/svg.image?\beta_{s}=0.75'>------------------------"];
    K["<img src='https://latex.codecogs.com/svg.image?\beta_{s}=0.40'>------------------------"];
    N["<img src='https://latex.codecogs.com/svg.image?\beta_{s}=0.60\lambda&space;'>-------------------------"];
    M["<img src='https://latex.codecogs.com/svg.image?\lambda= KDS 14 20 10(4.3.4)'>----------------------------------------"];
    O(["<img src='https://latex.codecogs.com/svg.image?\beta_{s}'>"]);
    Variable_def--->D--->H--->O;
    Variable_def--->E--Yes--->J--->O;
    Variable_def--->F--->K--->O;
    Variable_def--->G--->I--->O;
    E--No--->M--->N--->O;
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Calculate_coefficients_to_account_for_the_effects_of_cracks_and_restraints(fObetas, fIlambda,fIuserdefined) -> bool:
        """균열의 영향과 구속철근의 영향을 고려하기 위한 계수 산정.

        Args:
            fObetas (float): 균열의 영향과 구속철근의 영향을 고려하기 위한 계수 산정
            fIlambda (float): 경량 콘크리트 계수
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 콘크리트 스트럿-타이모델 기준  4.2.2 설계원칙 (2)의 통과 여부
        """
        #전 길이에 걸쳐 스트럿의 단면적이 일정할 경우: fIuserdefined = 1
        #스트럿 길이 중앙부의 단면적이 스트럿 양단의 단면적보다 큰 병모양인 스트럿의 경우 4.2.3의 철근 배치에 관한 규정을 만족할 때: fIuserdefined = 2
        #스트럿 길이 중앙부의 단면적이 스트럿 양단의 단면적보다 큰 병모양인 스트럿의 경우 4.2.3의 철근 배치에 관한 규정을 만족하지 못할 때: fIuserdefined = 3
        #인장요소 또는 콘크리트 구조 부재의 인장플랜지 콘크리트의스트럿인 경우: fIuserdefined = 4
        #기타의 모든 경우: fIuserdefined = 5

        if fIuserdefined == 1:
          fObetas = 1.0
        elif fIuserdefined == 2:
          fObetas = 0.75
        elif fIuserdefined == 3:
          fObetas = 0.6 * fIlambda
        elif fIuserdefined == 4:
          fObetas = 0.4
        elif fIuserdefined == 5:
          fObetas = 0.6

        return fObetas


# 

