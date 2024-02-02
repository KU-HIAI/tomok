import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010204_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.4 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트의 건조수축 변형률'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.4 건조수축
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
    A["콘크리트의 건조수축 변형률"];
    B["KDS 24 14 21 3.1.2.4 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 평균상대습도/];
		VarIn2[/입력변수: 부재의 크기/];
    VarIn3[/입력변수: 재령 ts에서 외기에 노출된 콘크리트의재령t에서의전체건조수축변형률/] ;
		VarIn4[/입력변수: 개념 건조수축계수/] ;
		VarIn5[/입력변수: 건조기간에 따른 건조수축 변형률 함수/] ;
	 	VarIn6[/입력변수: 콘크리트가 외기 중에 노출되었을 때의 재령/];
		VarIn7[/입력변수: 개념 건조수축계수/];
		VarIn8[/입력변수: εsfcm/];
		VarIn9[/입력변수: 외기습도에 따른 크리프와 건조수축에 미치는영향계수/];
		VarIn10[/입력변수: 건조기간에 따른 건조수축 변형률 함수/];
		VarIn11[/입력변수: 시멘트 종류에 따른 건조수축에 미치는영향계수/];
    VarOut1[/출력변수: 콘크리트의 건조수축 변형률/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
	  VarIn8 ~~~ VarIn10 & VarIn11
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C{"<img src='https://latex.codecogs.com/svg.image?\beta_{sc}'>--------------------------------------------------------"}


		C--2종 시멘트---> G
		C--1종, 5종 시멘트---> H
		C--3종 시멘트---> I

	  G["<img src='https://latex.codecogs.com/svg.image?\beta_{sc}=4'>---------------------------------"]
	  H["<img src='https://latex.codecogs.com/svg.image?\beta_{sc}=5'>---------------------------------"]
	  I["<img src='https://latex.codecogs.com/svg.image?\beta_{sc}=8'>---------------------------------"]
    G & H & I--->J
    J["<img src='https://latex.codecogs.com/svg.image?\varepsilon(f_{cm})=\left[160&plus;10\beta&space;_{sc}(9-f_{cm}/10)\right]\times&space;10^{-6}'>---------------------------------"]

    L["<img src='https://latex.codecogs.com/svg.image?\beta&space;_{RH}=\left\{\begin{matrix}-1.55[1-(1-RH/100)^{3}](40%\leq&space;RH\leq&space;99%)\\0.25(RH\geq&space;99%)\end{matrix}\right.'>---------------------------------"]
    Variable_def--->L
    M["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{sho}=\varepsilon&space;_s(f_{cm})\beta&space;_{RH}'>---------------------------------"]
    L & J--->M
    N["<img src='https://latex.codecogs.com/svg.image?\beta&space;_s(t-t_s)=\sqrt{\frac{(t-t_s)}{0.035h^{2}&plus;(t-t_s)}}'>---------------------------------"]
    Variable_def--->N
    N & M--->O--->K
    O["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{sh}(t,t_s)=\varepsilon&space;_{sho}\beta&space;_s(t-t_s)'>---------------------------------"]

    K(["콘크리트의 건조수축 변형률"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Drying_shrinkage_strain_of_concrete(fOepsilonshtts,fIepsilonsho,fIbetastminusts,fIt,fIts,fIepsilonsfcm,fIbetaRH,fIbetasc,fIh,fIRH,fIfcm,fIuserdefined) -> float:
        """콘크리트의 건조수축 변형률

        Args:
             fOepsilonshtts (float): 콘크리트의 건조수축 변형률; 재령 ts에서 외기에 노출된 콘크리트의 재령 t에서의 전체 건조수축 변형률
             fIepsilonsho (float): 개념 건조수축계수
             fIbetastminusts (float): 건조기간에 따른 건조수축 변형률 함수
             fIt (float): 콘크리트 총 재령
             fIts (float): 콘크리트가 외기 중에 노출되었을 때의 재령
             fIepsilonsfcm (float): 콘크리트 평균압축강도에 따른 건조수축 변형률 함수
             fIbetaRH (float): 외기습도에 따른 크리프와 건조수축에 미치는 영향계수
             fIbetasc (float): 시멘트 종류에 따른 건조수축에 미치는 영향계수
             fIh (float): 부재의 크기
             fIRH (float): 평균상대습도
             fIfcm (float): 콘크리트 평균압축강도
             fIuserdefined (float): 사용자 선택(시멘트 종류)


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.4 건조수축 (1)의 값
        """

        if fIuserdefined == 1:
          fIbetasc = 5
        elif fIuserdefined == 2:
          fIbetasc = 4
        elif fIuserdefined == 3 :
          fIbetasc = 8

        fIbetastminusts = ((fIt-fIts) / (0.035*fIh**2 + fIt-fIts))**0.5

        if 40 <= fIRH < 99:
          fIbetaRH = -1.55 * (1-(fIRH/100)**3)
        elif fIRH >= 99:
          fIbetaRH = 0.25

        fIepsilonsfcm = (160 + 10*fIbetasc*(9-fIfcm/10)) * 10**(-6)
        fIepsilonsho = fIepsilonsfcm * fIbetaRH
        fOepsilonshtts = fIepsilonsho * fIbetastminusts
        return fOepsilonshtts


# 

