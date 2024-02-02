import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010205_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.5 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단기 1축 압축력을 받는 콘크리트의 응력-변형률 곡선'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.5 응력-변형률 관계
    (1)
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
    B["KDS 24 14 21 3.1.2.5 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 응력/];
		VarIn2[/입력변수: 콘크리트 탄성계수/];
    VarIn3[/입력변수: 콘크리트 압축강도의 평균값/] ;
		VarIn4[/입력변수: 최대 응력에 도달하였을 때의 정점 변형률/] ;
		VarIn5[/입력변수: 극한한계변형률/] ;
	 	VarIn6[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
    VarOut1[/출력변수: 콘크리트의 응력/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D

		C["<img src='https://latex.codecogs.com/svg.image?k=1.1\frac{E_c\varepsilon&space;_{co,r}}{f_{cm}}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?f_{c}=f_{cm}[\frac{k(\varepsilon&space;_c/\varepsilon_{co,r})-(\varepsilon&space;_c/\varepsilon&space;_{co,r})^{2}}{1&plus;(k-2)(\varepsilon&space;_{c}/\varepsilon&space;_{co,r})}]'>---------------------------------"]
		D--->K
		K(["콘크리트의 응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def stress_in_concrete_with_short_period_uniaxial_load(fOstrcon,fIk,fIEc,fIfcm,fIepsiloncor,fIepsiloncur,fIfck) -> float:
        """단기 1축 압축력을 받는 콘크리트의 응력

        Args:
             fOstrcon (float): 콘크리트의 응력
             fIk (float): 정점에서의 최대응력과 콘크리트 평균 압축응력의 비
             fIEc (float): 콘크리트 탄성계수
             fIfcm (float): 콘크리트 압축강도의 평균값
             fIepsiloncor (float): 최대 응력에 도달하였을 때의 정점 변형률
             fIepsiloncur (float): 극한한계변형률
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.5 응력_변형률 관계 (1)의 값
        """

        if 18 <= fIfck < 21:
          fIepsiloncor = 1.83 + 0.07/3*(fIfck-18)
          fIepsiloncur = 3.3
        elif 21 <= fIfck < 24:
          fIepsiloncor = 1.90 + 0.07/3*(fIfck-21)
          fIepsiloncur = 3.3
        elif 24 <= fIfck < 27:
          fIepsiloncor = 1.97 + 0.06/3*(fIfck-24)
          fIepsiloncur = 3.3
        elif 27 <= fIfck < 30:
          fIepsiloncor = 2.03 + 0.06/3*(fIfck-27)
          fIepsiloncur = 3.3
        elif 30 <= fIfck < 35:
          fIepsiloncor = 2.09 + 0.09/5*(fIfck-30)
          fIepsiloncur = 3.3
        elif 35 <= fIfck < 40:
          fIepsiloncor = 2.18 + 0.08/5*(fIfck-35)
          fIepsiloncur = 3.3
        elif 40 <= fIfck < 50:
          fIepsiloncor = 2.26 + 0.16/10*(fIfck-40)
          fIepsiloncur = 3.3 - 0.1/10*(fIfck-40)
        elif 50 <= fIfck < 60:
          fIepsiloncor = 2.42 + 0.15/10*(fIfck-50)
          fIepsiloncur = 3.2 - 0.1/10*(fIfck-50)
        elif 60 <= fIfck < 70:
          fIepsiloncor = 2.57 + 0.11/10*(fIfck-60)
          fIepsiloncur = 3.1 - 0.1/10*(fIfck-60)
        elif 70 <= fIfck < 80:
          fIepsiloncor = 2.68 + 0.09/10*(fIfck-70)
          fIepsiloncur = 3.0 - 0.1/10*(fIfck-70)
        elif 80 <= fIfck <= 90:
          fIepsiloncor = 2.79 + 0.01/10*(fIfck-80)
          fIepsiloncur = 2.9 - 0.1/10*(fIfck-80)

        fIk = 1.1 * fIEc * fIepsiloncor / fIfcm
        fOstrcon = fIfcm * (fIk*fIepsilonc/fIepsiloncor - (fIepsilonc/fIepsiloncor)**2)/(1 + (fIk-2)*(fIepsilonc/fIepsiloncor))
        print(fIepsiloncor)
        return fOstrcon


# 

