import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010203_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (7)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '추가 인장력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (7)
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
    A["추가 인장력"];
    B["KDS 24 14 21 4.1.2.3 (7)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 추가 인장력/];
		VarIn1[/입력변수: 작용하는계수하중에의한단면전단력/];
		VarIn2[/입력변수: 부재 복부에 형성된 스트럿의 경사각/];
		VarIn3[/입력변수: 경사전단철근과 주인장철근 사이의 경사각/];


		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3



		end
		Python_Class ~~~ Variable_def;
		Variable_def--->L--->K

		L["<img src='https://latex.codecogs.com/svg.image?\Delta&space;T=0.5V_u(cot\theta-cot\alpha)'>---------------------------------"]

		K(["추가 인장력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def additional_tensile_force(fOdeltaT,fIVu,fItheta,fIalpha) -> float:
        """추가 인장력

        Args:
             fOdeltaT (float): 추가 인장력
             fIVu (float): 작용하는 계수하중에 의한 단면전단력
             fItheta (float): 부재 복부에 형성된 스트럿의 경사각
             fIalpha (float): 경사전단철근과 주인장철근 사이의 경사각



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (7)의 값
        """

        fOdeltaT = 0.5 * fIVu * ( 1/math.tan(math.radians(fItheta)) - 1/math.tan(math.radians(fIalpha)))
        return fOdeltaT


# 

