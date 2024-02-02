import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010206_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.6 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트의 휨인장강도를 포함한 설계인장강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.6 설계압축강도 및 설계인장강도
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
    A["설계인장강도"];
    B["KDS 24 14 21 3.1.2.6 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 기준인장강도/];
		VarIn2[/입력변수: 콘크리트의 재료계수/];
    VarIn3[/입력변수: 인장강도 유효계수/] ;
    VarOut1[/출력변수: 설계인장강도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->F

		C["<img src='https://latex.codecogs.com/svg.image?f_{ctd}=\phi&space;_c\alpha&space;_{ct}f_{ctk}'>---------------------------------"]
		F(["설계인장강도"])
		C~~~ |"Table 24 14 21 1.4-1"| C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_tensile_strength(fOfctd,fIphic,fIalphact,fIfctk) -> float:
        """콘크리트의 휨인장강도를 포함한 설계인장강도

        Args:
             fOfctd (float): 설계인장강도
             fIphic (float): 콘크리트의 재료계수
             fIalphact (float): 인장강도 유효계수
             fIfctk (float): 기준인장강도


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.6 설계압축강도 및 설계인장강도 (2)의 값
        """

        fOfctd = fIphic * fIalphact * fIfctk
        return fOfctd


# 

