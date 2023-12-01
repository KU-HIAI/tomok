import sys
import os

# 현재 파일의 디렉토리 경로를 얻습니다.
current_dir = os.path.dirname(__file__)
# 상위 디렉토리 경로를 얻습니다.
parent_dir = os.path.dirname(current_dir)
# 상위 디렉토리 경로를 sys.path에 추가합니다.
sys.path.append(parent_dir)

# 이제 module1.file1을 import 할 수 있습니다.
from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

# 작성하는 룰에 맞게 클래스 이름 수정 (KDS142054_040305_03)
class KDS142054_040305_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.5 (3)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장력의 편심이 작용하는 부착식앵커 그룹에 대한 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (3)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####   4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (3) 인장력의 편심이 작용하는 부착식 앵커 그룹에 대한 수정계수 $$\psi _{ec,Na}$$는 다음과 같이 구하여야 한다.

		      $$\psi _{ec,Na}=\frac{1}{\left ( 1+\frac{e^{'}N}{c_{Na}} \right )}$$      (4.3-23)

    단, $$\psi _{ec,Na}$$는 1.0보다 클 수 없다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[인장력의 편심이 작용하는 부착식 앵커그룹에대한수정계수];
    B["KDS 14 20 54 4.3.5 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 인장력의 편심이 작용하는 부착식 앵커그룹에대한수정계수/];
    VarIn1[/입력변수 : 인장하중을 받는 앵커그룹에 작용하는 인장력의 합력과 앵커그룹도심사이의 거리/];
    VarIn2[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적가장자리까지의 거리 /];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,Na}=\frac{1}{(1&plus;\frac{e^{,}_{N}}{c_{Na}})}(\leq&space;1)'>-------------------------------------------"];
    E(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ec,Na}'>"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force(fOpsecNa,fIeprimN,fIcNa) -> float:
        """인장력의 편심이 작용하는 부착식앵커 그룹에 대한 수정계수

        Args:
            fOpsecNa (float): 인장력의 편심이 작용하는 부착식앵커그룹에 대한 수정계수
            fIeprimN (float): 인장하중을 받는 앵커 그룹에 작용하는 인장력의합력과 앵커그룹 도심사이의 거리
            fIcNa (float): 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (3)의 값
        """

        fOpsecNa = 1 / (1+(fIeprimN/fIcNa))

        if fOpsecNa > 1:
          fOpsecNa = 1.0

        return fOpsecNa

# """작성한 룰 유닛은 아래의 코드 블럭과 같이 생성하여, 작성자가 임의로 검증을 수행할 수 있습니다."""

# my_RuleUnit = KDS142054_040305_03()

# fOpsecNa = None
# fIeprimN = 50
# fIcNa = 90

# Rule_Review_Result = my_RuleUnit.correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force(fOpsecNa,fIeprimN,fIcNa)
# # 해당건설기준 항목 의 결과는?

# print("RuleUnit Review Result: {}".format(Rule_Review_Result))

# """<br><br>
# 아래의 코드를 통해, 룰 유닛의 content(건설기준 항목의 실제 내용)의 markdown 렌더링 결과를 확인할 수 있습니다.
# """

# my_RuleUnit.render_markdown()