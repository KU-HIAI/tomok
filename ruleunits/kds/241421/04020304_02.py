import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020304_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.4 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '변형률 차이'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
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
    A["변형률 차이"];
    B["KDS 24 14 21 4.2.3.4 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 균열면에서 계산한 철근 인장응력/];
		VarIn2[/입력변수: 철근의 평균 탄성계수/];
		VarIn3[/입력변수: 콘크리트 탄성계수/];
		VarIn4[/입력변수: 첫 균열이 발생할 때 유효한 콘크리트 인장강도/];
		VarIn5[/입력변수: 하중작용 기간에 따른 계수/];
		VarIn6[/입력변수: 탄성계수비/];
		VarIn7[/입력변수: 유효 철근비/];
		VarIn8[/입력변수: 콘크리트 유효 인장면적/];
		VarIn9[/입력변수: 콘크리트 유효 인장면적 내에 있는 철근의 단면적/];
		VarIn10[/입력변수: 콘크리트 유효 인장면적 내에 있는 프리스트레싱강재의단면적/];
		VarIn11[/입력변수: 콘크리트 유효 인장깊이/];
		VarIn12[/입력변수: 철근과 긴장재의 부착특성 및 지름의 차이에 따른영향을반영하기위한계수/];
		VarIn13[/입력변수: 단면의 깊이/];
		VarIn14[/입력변수: 단면의 유효깊이/];
		VarIn15[/입력변수: 중립축 깊이/];
		VarOut1[/출력변수: 변형률 차이/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3 & VarIn4
		VarIn2~~~VarIn5  & VarIn6 & VarIn7 & VarIn8
		VarIn6~~~VarIn9 & VarIn10 & VarIn11 & VarIn12
		VarIn10~~~VarIn13 & VarIn14 & VarIn15
		end
		Python_Class ~~~ Variable_def--->D & E --->F--->G
		D["<img src='https://quicklatex.com/cache3/1d/ql_83d716ec9ddf5a1ff56c2f0450c5ef1d_l3.png'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?d_{cte}=min[2.5(h-d),(h-c)/3,h/2]'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{sm}-\varepsilon&space;_{cm}=\frac{f_{so}}{E_s}-0.4\frac{f_{cte}}{E_s\rho&space;_e}(1&plus;n\rho&space;_e)\geq&space;0.6\frac{f_{so}}{E_s}'>---------------------------------"]
		G(["변형률 차이"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def strain_difference(fOstrdif,fIEs,fIEc,fIfso,fIfcte,fIkt,fIn,fIrhoe,fIActe,fIAs,fIAp,fIdcte,fIxi1,fIuserdefined,fIh,fId,fIc) -> float:
        """변형률 차이

        Args:
             fOstrdif (float):변형률 차이
             fIEs (float): 철근의 평균 탄성계수
             fIEc (float): 콘크리트 탄성계수
             fIfso (float): 균열면에서 계산한 철근 인장응력
             fIfcte (float): 첫 균열이 발생할 때 유효한 콘크리트인장강도
             fIkt (float): 하중작용 기간에 따른 계수
             fIn (float): 탄성계수비
             fIrhoe (float): 유효 철근비
             fIActe (float): 콘크리트 유효 인장면적
             fIAs (float): 콘크리트 유효 인장면적 내에 있는 철근의 단면적
             fIAp (float): 콘크리트 유효 인장면적 내에 있는 프리스트레싱강재의 단면적
             fIdcte (float): 콘크리트 유효 인장깊이
             fIxi1 (float): 철근과 긴장재의 부착특성 및 지름의 차이에 따른 영향을 반영하기 위한  계수
             fIuserdefined (float): 사용자 선택
             fIh (float): 단면의 깊이
             fId (float): 단면의 유효깊이
             fIc (float): 중립축 깊이


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (2)의 값
        """

        #단기하중일 경우 > fIuserdefined == 1
        #장기하중일 경우 > fIuserdefined == 2



        fIn = fIEs/fIEc
        fIrhoe = (fIAs + (fIxi1**2)*fIAp)/fIActe
        fIdcte = min(2.5*(fIh-fId),(fIh - fIc)/3,fIh/2)


        if fIuserdefined == 1:
          fIkt = 0.6
        if fIuserdefined == 2:
          fIkt = 0.4

        fOstrdif = max(fIfso/fIEs-0.4*fIfcte/fIEs/fIrhoe*(1+fIn*fIrhoe),0.6*fIfso/fIEs)

        return fOstrdif


# 

