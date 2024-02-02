import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010205_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.5 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트 응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.5 응력-변형률 관계
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
    A["콘크리트의 응력"];
    B["KDS 24 14 21 3.1.2.5 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 압축변형률/];
		VarIn2[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
    VarIn3[/입력변수: 콘크리트에 대한 재료계수/] ;
		VarIn4[/입력변수: 상승 곡선부의 형상을 나타내는 지수/] ;
		VarIn5[/입력변수: 최대 응력에 처음 도달할 때의 변형률/] ;
	 	VarIn6[/입력변수: 극한변형률/];
    VarOut1[/출력변수: 콘크리트 응력/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C & D

		C{"<img src='https://latex.codecogs.com/svg.image?0\leq\varepsilon&space;_c\leq\varepsilon&space;_{co}'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{co}<\varepsilon&space;_c\leq\varepsilon&space;_{cu}'>---------------------------------"}
		C--->K
		K["<img src='https://latex.codecogs.com/svg.image?f_c=\phi&space;_c(0.85f_{ck})[1-(1-\frac{\varepsilon&space;_c}{\varepsilon&space;_{co}})^{n}]'>---------------------------------"]
		D--->E
		E["<img src='https://latex.codecogs.com/svg.image?f_c=\phi&space;_c(0.85f_{ck})'>---------------------------------"]
		F(["콘크리트 강도"])
		K & E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def stress_in_concrete_of_beam(fOfc,fIepsilonc,fIfck,fIphic,fIn,fIepsilonco,fIepsiloncu) -> float:
        """콘크리트 응력

        Args:
             fOfc (float): 콘크리트 응력
             fIepsilonc (float): 콘크리트의 압축변형률
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도
             fIphic (float): 콘크리트에 대한 재료계수
             fIn (float): 상승 곡선부의 형상을 나타내는 지수
             fIepsilonco (float): 최대 응력에 처음 도달할 때의 변형률
             fIepsiloncu (float): 극한변형률


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.5 응력_변형률 관계 (2)의 값
        """

        if fIfck <= 40:
          fIn = 2.0
          fIepsilonco = 0.002
          fIepsiloncu = 0.0033
        else:
          fIn = 1.2 + 1.5+((100-fIfck)/60)**4
          fIepsilonco = 0.002 + (fIfck-40)/100000
          fIepsiloncu = 0.0033 - (fIfck-40)/100000

        if 0 <= fIepsilonc <= fIepsilonco:
          fOfc = fIphic*0.85*fIfck*(1-(1-fIepsilonc/fIepsilonco)**fIn)
        elif fIepsilonco < fIepsilonc <= fIepsiloncu:
          fOfc = fIphic*0.85*fIfck
        return fOfc


# 

