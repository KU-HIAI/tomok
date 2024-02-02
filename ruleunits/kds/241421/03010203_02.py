import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '양생온도 20°C의 크리프계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.3 크리프
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
    A["크리프 계수"];
    B["KDS 24 14 21 1.5.7.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 개념 크리프계수/];
		VarIn2[/입력변수: 외기의 상대습도와 부재 두께가 크리프에 미치는 영향계수/];
    VarIn3[/입력변수: 콘크리트의 평균압축강도가 크리프에 미치는 영향함수/] ;
		VarIn4[/입력변수: 지속하중이 가해지는 시간 t'가 크리프에 미치는 영향함수/] ;
		VarIn5[/입력변수: 재하기간에 따라 크리프에 미치는 영향함수/] ;
		VarIn6[/입력변수: 외기의 상대습도와 부재의 두께에 따른 계수/] ;
		VarIn7[/입력변수: 개념부재치수/] ;
		VarIn8[/입력변수: 단면적 Ac의 둘레중에서 수분이 외기로 확산되는 둘레길이/] ;
		VarIn9[/입력변수: 평균압축강도/] ;
		VarIn10[/입력변수: 상대습도/] ;
	 	VarOut1[/출력변수: 크리프계수/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C["<img src='https://latex.codecogs.com/svg.image?\varphi_{RH}=1+\frac{1-0.01RH}{0.1\sqrt[3]{h}}'>--------------------------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\beta(f_{cm})=\frac{16.8}{\sqrt{f_{cm}}}'>---------------------------------"]
		Variable_def--->D
		Variable_def--->E
		E["<img src='https://latex.codecogs.com/svg.image?\beta(t')=\frac{1}{0.1+(t')^_{0.2}'>---------------------------------"]
		C & D & E--->F
		F["<img src='https://latex.codecogs.com/svg.image?\varphi_{RH}=\beta(f_{cm})\beta(t')'>---------------------------------"]
		Variable_def--->G
		Variable_def--->H
		G["<img src='https://latex.codecogs.com/svg.image?\beta_{c}(t-t')=[\frac{(t-t')}{\beta_{H}+(t-t')}]^{0.3}'>---------------------------------"]
    H["<img src='https://latex.codecogs.com/svg.image?\beta_{H}=1.5[1+(0.012RH)^{18}]h+250\leq1500'>---------------------------------"]
    I["<img src='https://latex.codecogs.com/svg.image?\varphi(t,t')=\varphi_{0}\beta_{c}(t-t')'>---------------------------------"]
    F & G & H--->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def creep_coefficient(fOphittprime,fIphio,fIphiRH,fIbetafcm,fIbetatprime,fItprime,fIt,fIbetacttprime,fIbetaH,fIh,fIu,fIfcm,fIRH) -> float:
        """양생온도 20°C의 크리프계수

        Args:
             fOphittprime (float): 크리프계수
             fIphio (float): 콘크리트의 개념 크리프계수
             fIphiRH (float): 외기의 상대습도와 부재 두께가 크리프에 미치는 영향계수
             fIbetafcm (float): 콘크리트의 평균압축강도가 크리프에 미치는 영향함수
             fIbetatprime (float): 지속하중이 가해지는 시간 t'가 크리프에 미치는 영향함수
             fItprime (float): 재하할 때의 재령
             fIt (float): 재하할 때의 재령 + 재하기간
             fIbetacttprime (float): 재하기간에 따라 크리프에 미치는 영향함수
             fIbetaH (float): 외기의 상대습도와 부재의 두께에 따른 계수
             fIh (float): 개념부재치수
             fIu (float): 단면적 A_{c}의 둘레 중에서 수분이 외기로 확산되는 둘레길이
             fIfcm (float): 평균압축강도
             fIRH (float): 상대습도


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.3 크리프 (2)의 값
        """

        fIphiRH = 1 + (1-0.01*fIRH)/(0.10*fIh**(1/3))
        fIbetafcm = 16.8/fIfcm**0.5
        fIbetatprime = 1/(0.1+fItprime**0.2)
        fIphio = fIphiRH * fIbetafcm * fIbetatprime
        if 1.5*(1+(0.012*fIRH)**18)*fIh + 250 <= 1500:
          fIbetaH = 1.5*(1+(0.012*fIRH)**18)*fIh + 250
        else:
          fIbetaH = 1500
        fIbetacttprime = ((fIt-fItprime)/(fIbetaH + fIt-fItprime))**0.3
        fOphittprime = fIphio * fIbetacttprime
        return fOphittprime


# 

