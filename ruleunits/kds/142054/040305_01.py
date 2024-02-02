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


# 작성하는 룰에 맞게 클래스 이름 수정 (KDS142054_040305_01)
class KDS142054_040305_01(RuleUnit):
    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1  # 건설기준 우선순위
    author = "Seonghan Yoon"  # 작성자명
    ref_code = "KDS 14 20 54 4.3.5 (1)"  # 건설기준문서
    ref_date = "2021-02-18"  # 디지털 건설문서 작성일
    doc_date = "2023-10-05"  # 건설기준문서->디지털 건설기준 변환 기준일
    title = "단일 부착식 앵커의 공칭부착강도"  # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    ####   4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (1) 인장력을 받는 단일 부착식 앵커의 공칭부착강도 $$N_{a}$$ 또는 부착식 앵커 그룹의 공칭부착강도 $$N_{ag}$$는 다음 값을 초과할 수 없다.
    ① 단일 부착식 앵커

		      $$N_{a}=\frac{A_{Na}}{A_{Nao}}\psi _{ed,Na}\psi _{cp,Na}N_{ba}$$      (4.3-18)

    ② 부착식 앵커 그룹

		      $$N_{ag}=\frac{A_{Na}}{A_{Nao}}\psi _{ec,Na}\psi _{ed,Na}\psi _{cp,Na}N_{ba}$$      (4.3-19)

    계수 $$\psi _{ec,Na}$$,$$\psi _{ed,Na}$$  및 $$\psi _{cp,Na}$$는 (3), (4) 및 (5)에 각각 정의되어 있다. 부착식 앵커의 중심(부착식 앵커 그룹에서는 최외곽 앵커 열의 중심선)으로부터 $$c_{Na}$$ 밖으로 투영하여 만들어진 사각면적을 기초로 하여 계산된 단일 부착식 앵커 또는 부착식 앵커 그룹의 투영영향면적을 $$A_{Na}$$라고 하며, $$A_{Na}$$는 $$nA_{Nao}$$ 이하이어야 한다. 여기서 $$n$$은 앵커 그룹에서 인장력을 받는 부착식 앵커의 수이며, $$A_{Nao}$$는 연단거리가 $$c_{Na}$$ 이상인 단일 부착식 앵커에 대한 투영영향면적이다.

		      $$A_{Nao}=\left ( 2c_{Na} \right )^{2}$$      (4.3-20)
		      $$c_{Na}=10d_{a} \sqrt{\frac{\tau _{uncr}}{7.6}}$$      (4.3-21)

    여기서, 상수 7.6은 MPa 단위에 대해 적용한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[공칭부착강도];
    B["KDS 14 20 54 4.3.5 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/출력변수 : 단일 부착식 앵커의 공칭부착강도/];
    VarIn2[/출력변수 : 부착식 앵커 그룹의 공칭부착강도/];
    VarIn3[/입력변수 : 앵커그룹의 투영영향면적/];
    VarIn4[/입력변수 : 단일 앵커의 투영영향면적/];
    VarIn5[/입력변수 : 부착식 앵커에서 연단거리 영향에 따른 인장강도에대한수정계수/];
    VarIn6[/입력변수 :비균열 콘크리트에 사용되는 부착식앵커의수정계수/];
    VarIn7[/입력변수 :인장을 받는 단일부착식 앵커의 기본부착강도/];
    VarIn8[/입력변수 : 부착식 앵커가 편심하중을 받는 경우의 인장강도에대한수정계수/];
    VarIn9[/입력변수 : 부착식 앵커의 수/];
    VarIn10[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리/];
    VarIn1~~~ VarIn5~~~VarIn8
    VarIn2 ~~~ VarIn6~~~VarIn9
    VarIn3 ~~~ VarIn7~~~VarIn10
    VarIn4~~~VarIn5

    end
    Python_Class~~~Variable_def

    D{"단일 부착식 앵커"};
    E{"부착식 앵커 그룹"};
    F{"<img src='https://latex.codecogs.com/svg.image?A_{Na}\leq&space;nA_{Nao}'>----------------------------"};
    G["<img src='https://latex.codecogs.com/svg.image?A_{Nao}=(2\times&space;10d_{a}(\frac{\tau&space;_{uncr}}{7.6})^{0.5})^{2}'>-------------------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?N_{a}=\frac{A_{Na}}{A_{Nao}}\psi_{ed,Na}\psi_{cp,Na}N_{ba}'>---------------------------------------------------"];
    I["<img src='https://latex.codecogs.com/svg.image?N_{ag}=\frac{A_{Na}}{A_{Nao}}\psi_{ec,Na}\psi&space;_{ed,Na}\psi_{cp,Na}N_{ba}'>--------------------------------------------------------------"];
    J(["Pass or Fail"]);

    Variable_def--->D--->H--->J
    Variable_def--->E--->G--->F--->I--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def nominal_bond_strength_of_a_single_bonded_anchor(
        fINa,
        fINag,
        fIANa,
        fIANao,
        fIpsedNa,
        fIpscpNa,
        fINba,
        fIpsecNa,
        fIn,
        fIcNa,
        fIda,
        fItauncr,
        fIuserdefined,
    ) -> bool:
        """단일 부착식 앵커의 공칭부착강도

        Args:
            fINa (float): 단일 부착식 앵커의 공칭부착강도
            fINag (float): 부착식 앵커 그룹의 공칭부착강도
            fIANa (float): 앵커그룹의 투영영향면적
            fIANao (float): 단일 앵커의 투영영향면적
            fIpsedNa (float): 부착식 앵커에서 연단거리 영향에 따른 인장강도에 대한 수정계수
            fIpscpNa (float): 비균열 콘크리트에 사용되는 부착식앵커의 수정계수
            fINba (float): 인장을 받는 단일부착식 앵커의 기본부착강도
            fIpsecNa (float): 부착식 앵커가 편심하중을 받는 경우의 인장강도에 대한 수정계수
            fIn (float): 부착식 앵커의 수
            fIcNa (float): 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형 볼트의 샤프트 지름
            fItauncr (float): 비균열 콘크리트에 사용된 부착식 앵커의 특성 부착강도
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (1)의 통과여부
        """

        # 단일 부착식 앵커 → fIuserdefined = 1
        # 부착식 앵커 그룹 → fIuserdefined = 2

        fIcNa = 10 * fIda * ((fItauncr / 7.6) ** 0.5)
        fIANao = (2 * fIcNa) ** 2
        if fIANa <= fIn * fIANao:
            if fIuserdefined == 1:
                if fINa > (fIANa / fIANao) * fIpsedNa * fIpscpNa * fINba:
                    return "Fail"
                else:
                    return "Pass"

            if fIuserdefined == 2:
                if fINag > (fIANa / fIANao) * fIpsecNa * fIpsedNa * fIpscpNa * fINba:
                    return "Fail"
                else:
                    return "Pass"
        else:
            return "Fail"


# """작성한 룰 유닛은 아래의 코드 블럭과 같이 생성하여, 작성자가 임의로 검증을 수행할 수 있습니다."""

# my_RuleUnit = KDS142054_040305_01()

# fINa = 50
# fINag = None
# fIANa = 500000
# fIANao = None
# fIpsedNa = 1.0
# fIpscpNa = 1.0
# fINba = 15
# fIpsecNa = 0.64
# fIn = 6
# fIcNa = None
# fIda = 13
# fItauncr = 10
# fIuserdefined = 1

# Rule_Review_Result = my_RuleUnit.nominal_bond_strength_of_a_single_bonded_anchor(fINa,fINag,fIANa,fIANao,fIpsedNa,fIpscpNa,fINba,fIpsecNa,fIn,fIcNa,fIda,fItauncr,fIuserdefined)
# # 해당건설기준 항목 의 결과는?

# print("RuleUnit Review Result: {}".format(Rule_Review_Result))

# """<br><br>
# 아래의 코드를 통해, 룰 유닛의 content(건설기준 항목의 실제 내용)의 markdown 렌더링 결과를 확인할 수 있습니다.
# """

# my_RuleUnit.render_markdown()
