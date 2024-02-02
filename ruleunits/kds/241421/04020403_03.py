import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020403_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.4.3 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 유효탄성계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.3 직접 처짐 계산에 의한 검증
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
    A["콘크리트 유효탄성계수"];
    B["KDS 24 14 21 4.2.4.3 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 탄성계수/];
		VarIn2[/입력변수: 하중과 지속 기간에 맞는 크리프계수/];
		VarOut1[/출력변수: 장기거동을 반영한 콘크리트의 유효탄성계수/];
		VarOut1~~~VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def--->C--->F
		C["<img src='https://latex.codecogs.com/svg.image?E_{ce}=\frac{E_c}{1&plus;\varphi(\infty,t_o)}'>---------------------------------"]


		F(["콘크리트 유효탄성계수"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Concrete_effective_modulus_of_elasticity(fOEce,fIEc,fIvarphit) -> float:
        """콘크리트 유효탄성계수

        Args:
             fOEce (float): 장기거동을 반영한 콘크리트의 유효탄성계수
             fIEc (float): 콘크리트의 탄성계수
             fIvarphit (float): 하중과 지속 기간에 맞는 크리프계수

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (3)의 값
        """

        fOEce = fIEc / (1+fIvarphit)
        return fOEce


# 

