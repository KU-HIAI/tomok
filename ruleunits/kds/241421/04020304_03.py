import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020304_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.4 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최종 균열의 최대 간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
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
    A["최종 균열의 최대 간격"];
    B["KDS 24 14 21 4.2.3.4 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 강재의 중심 간격/];
		VarIn2[/입력변수: 최외단 인장철근이나 긴장재의 표면과 콘크리트표면사이의최소피복두께/];
		VarIn3[/입력변수: 부착강도에 따른 계수/];
		VarIn4[/입력변수: 부재의 하중작용에 따른 계수/];
		VarIn5[/입력변수: 콘크리트의 유효인장면적을 기준으로 한 강재비/];
		VarIn6[/입력변수: 철근콘크리트나 긴장재와 철근이 같이 사용된프리스트레스트콘크리트의경우에는가장큰인장철근의지름을,긴장재만사용된프리스트레스트콘크리트의경우에는프리스트레싱강재의등가지름dp,eq/];
		VarIn7[/입력변수: 단면의 깊이/];
		VarIn8[/입력변수: 중립축 깊이/];
		VarOut1[/출력변수: 최종 균열의 최대 간격/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5 ~~~ VarIn6
		VarIn7~~~VarIn8
		end
		Python_Class ~~~ Variable_def--->C
		C{"강재의 중심간격 ≤<img src='https://latex.codecogs.com/svg.image?\leq&space;5(c_c&plus;d_b/2)'>---------------------------------"}
		D["<img src='https://latex.codecogs.com/svg.image?l_{r,max}=3.4c_c&plus;\frac{0.425k_1k_2d_b}{\rho&space;_e}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?l_{r,max}=1.3(h-c)'>---------------------------------"]
		C--yes-->D
		C--No-->E
		D & E--->G
		G(["최종 균열의 최대 간격"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def maximum_spacing_of_final_cracks(fOmaxspc,fIcensst,fIcc,fIk1,fIk2,fIrhoe,fIdb,fIh,fIc) -> float:
        """최종 균열의 최대 간격

        Args:
             fOmaxspc (float):최종 균열의 최대 간격
             fIcensst (float): 강재의 중심 간격
             fIcc (float): 최외단 인장철근이나 긴장재의 표면과 콘크리트표면사이의최소피복두께
             fIk1 (float): 부착강도에 따른 계수
             fIk2 (float): 부재의 하중작용에 따른 계수
             fIrhoe (float): 콘크리트의 유효인장면적을 기준으로 한 강재비
             fIdb (float): 철근콘크리트나 긴장재와 철근이 같이 사용된 프리스트레스트콘크리트의 경우에는 가장 큰 인장철근의 지름을, 긴장재만 사용된 프리스트레스트콘크리트의 경우에는 프리스트레싱강재의 등가지름 d_{p,eq}
             fIh (float): 단면의 깊이
             fIc (float): 중립축 깊이


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (3)의 값
        """

        if fIcensst <= 5*(fIcc + fIdb/2):
         fOmaxspc = 3.4 * fIcc + 0.425 * fIk1 * fIk2 * fIdb / fIrhoe
        else:
         fOmaxspc = 1.3*(fIh-fIc)

        return fOmaxspc


# 

