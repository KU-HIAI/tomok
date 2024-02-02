import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010201_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.1 (7)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경량콘크리트의 인장강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
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
    A[경량콘크리트의 인장강도];
    B["KDS 24 14 21 3.1.2.1 (7)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 평균인장강도/];
    VarIn2[/입력변수: 절대건도 밀도/];
 	  VarOut1[/출력변수: 경량콘크리트의 인장강도/];


	  VarOut1~~~VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def;
		Variable_def---->D-->G



		D["경량콘크리트 인장강도<img src='https://latex.codecogs.com/svg.image?&space;=f_{ctm}(0.4+0.6\gamma_{g}/2200) '>--------------------------------------------------------"]

		D~~~ |"KDS 24 14 21 Table 3.1-1"| D
		G(["경량콘크리트의 인장강도"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Tensile_strength_of_lightweight_concrete(fOtencon,fIfctm,fIgammag) -> float:
        """경량콘크리트의 인장강도

        Args:
             fOunrcon (float): 무근콘크리트 밀도
             fOdencon (float): 철근콘크리트 밀도
             fIgammag (float): 절대건조 밀도
             fIuserdefined (float): 사용자 선택


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.1 강도 (7)의 값
        """

        fOtencon = fIfctm * (0.4 + 0.6 * fIgammag / 2200)
        return fOtencon


# 

