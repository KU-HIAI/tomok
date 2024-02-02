import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경량 콘크리트의 탄성계수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.2 탄성변형
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
    A[경량콘크리트의 탄성계수];
    B["KDS 24 14 21 3.1.2.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 보통 콘크리트의 탄성계수/];
    VarIn2[/입력변수: 경량콘크리트 계수/] ;
		VarIn3[/입력변수: 절대건조 밀도의 상한값/] ;
  	VarOut1[/출력변수: 경량콘크리트 탄성계수/];


	  VarOut1~~~VarIn1 & VarIn2 & VarIn3
		end
		Python_Class ~~~ Variable_def;
		Variable_def---->D-->E--->G



		D["<img src='https://latex.codecogs.com/svg.image?&space;\eta_{E}=(\gamma_{g}/2200)^2'>--------------------------------------------------------"]

		E["경량콘크리트 탄성계수=<img src='https://latex.codecogs.com/svg.image?&space;\eta_{E}E_{c}'>--------------------------------------------------------"]
    G(["경량콘크리트의 탄성계수"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Modulus_of_elasticity_of_light_concrete(fIEc,fIetac,fOmodelc,fIgammag) -> float:
        """경량콘크리트의 탄성계수

        Args:
             fOmodelc (float): 경량콘크리트 탄성계수
             fIEc (float): 보통 콘크리트의 탄성계수
             fIetac (float): 경량콘크리트 계수
             fIgammag (float): 절대건조 밀도의 상한값


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.2 탄성변형 (2)의 값
        """

        fIetaE = (fIgammag/2200)**2
        fOmodelc = fIEc * fIetaE
        return fOmodelc


# 

