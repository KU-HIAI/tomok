import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010204_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.4 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '외기의 온도가 20°C가 아닐 경우의 영향계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.4 건조수축
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
    A["건조수축"];
    B["KDS 24 14 21 3.1.2.4 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 외기습도에 따른 크리프와 건조수축에 미치는영향계수/];
		VarIn2[/입력변수: 건조기간에 따른 건조수축 변형률 함수/];
    VarIn3[/입력변수: 상대습도/] ;
		VarIn4[/입력변수: 온도/] ;
		VarIn5[/입력변수: 재령일/] ;
	 	VarIn6[/입력변수: 콘크리트가 외기 중에 노출되었을 때의 재령/];
    VarOut1[/출력변수: 건조기간에 따른 건조수축 변형률 함수/];
		VarOut2[/출력변수: 외기습도에 따른 크리프와 건조수축에 미치는 영향계수/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarOut2 ~~~ VarIn4 & VarIn5 & VarIn6
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C & D

		C["<img src='https://latex.codecogs.com/svg.image?\beta&space;_{RH,T}=[1&plus;(\frac{8}{103-RH})(\frac{T-20}{40})]\beta&space;_{RH}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\beta&space;_{(t-t_s)}=\sqrt{\frac{(t-t_s)}{0.035h^{2}exp[-0.06(T-20)]&plus;(t-t_s)}}'>---------------------------------"]
		C--->K
		K(["외기습도에 따른 크리프와 건조수축에 미치는 영향계수"])
		D--->L
		L(["건조기간에 따른 건조수축 변형률 함수"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Coefficient_correction_by_temperature(fIbetaRH,fIRH,fIT,fIt,fIts,fObetastminusts,fIh,fObetaRHT,fIuserdefined) -> float:
        """외기의 온도가 20°C가 아닐 경우의 영향계수

        Args:
             fObetaRHT (float): 외기 온도가 20℃가 아닌 경우 외기습도에 따른 크리프와 건조수축에 미치는 영향계수
             fObetastminusts (float): 건조기간에 따른 건조수축 변형률 함수
             fIbetaRH (float): 외기습도에 따른 크리프와 건조수축에 미치는 영향계수
             fIRH (float): 상대습도
             fIT (float): 외기 온도
             fIt (float): 재령(일)
             fIts (float): 콘크리트가 외기 중에 노출되었을 때의 재령(일)
             fIh (float): 부재 크기
             fIuserdefined (float): 사용자 선택


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.4 건조수축 (2)의 값
        """

        import numpy as np
        #외기습도에 따른 영향계수 보정값: fIuserdefined = 1
        #건조기간에 따른 영향계수 보정값: fIuserdefined = 2
        if fIuserdefined == 1:
          #식 3.1-33
          if 40 <= fIRH < 99:
            fIbetaRH = -1.55*(1-(fIRH/100)**3)
          elif fIRH >= 99:
            fIbetaRH = 0.25
          fObetaRHT = (1 + 8/(103-fIRH)*(fIT-20)/40)*fIbetaRH
          return fObetaRHT
        elif fIuserdefined == 2:
          fObetastminusts = ((fIt-fIts)/((0.035*fIh**2)*np.exp(-0.06*(fIT-20))+fIt-fIts))**0.5
          return fObetastminusts


# 

