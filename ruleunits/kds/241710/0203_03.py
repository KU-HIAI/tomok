import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_0203_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 10 2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '등가정적 지진하중'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    2. 설계
    2.3 해석방법
    (3) 단일모드스펙트럼해석법
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
    A[해석방법];
    B["KDS 24 17 10 2.3 (3)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:등가정적 지진하중/]
			VarIn1[/입력변수:탄성지진 응답계수/]
			VarIn2[/입력변수:중력가속도/]
			VarIn3[/입력변수:교량상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중/]
			VarIn4[/입력변수:균일한 등분포하중 po에 의한 정적처짐/]

			VarOut1 ~~~
			VarIn1 & VarIn2 &	VarIn3 & VarIn4


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?p_{e}(x)=\frac{\beta&space;C_{s}}{r}w(x)v_{s}(x)'>---------------------------------"]
			D["<img src='https://latex.codecogs.com/svg.image?T=2\pi\sqrt{\frac{r}{p_{o}q\alpha}}'>---------------------------------"]
			E["<img src='https://latex.codecogs.com/svg.image?\beta=\int&space;w(x)v_{s}(x)dx'>---------------------------------"]
			F["<img src='https://latex.codecogs.com/svg.image?r=\int&space;w(x)v_{s}(x)^{2}dx'>---------------------------------"]
			G([등가정적 지진하중])
			D~~~ |"KDS 24 12 10 2.3(2) 식 2.3-1"| D


			Variable_def ---> E & F
			F ---> D
			E & D ---> C ---> G
			Variable_def & F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Equivalent_static_seismic_load(fOPe,fOT,fICs,fIg,fIw,fIVs,fIalpha,fIbeta,fIgamma,fIuserdefined,fIpo) -> float:
        """등가정적 지진하중

        Args:
             fOPe (float): 등가정적 지진하중
             fOT (float): 교량의 주기
             fICs (float): 탄성지진 응답계수
             fIg (float): 중력가속도
             fIw (float): 교량상부구조와 이의 동적거동에 영향을 주는 하부구조의 단위길이당 고정하중
             fIVs (float): 균일한 등분포하중 po에 의한 정적처짐
             fIalpha (float): 설계변수 ɑ
             fIbeta (float): 교량의 등가정적 지진하중을 계산하는데 사용되는 계수
             fIgamma (float): 교량의 주기를 계산하는데 사용되는 계수
             fIuserdefined (float): 사용자 선택
             fIpo (float): 균일한 등분포하중



        Returns:
            float: 교량 내진설계기준(일반설계법) 2.3 해석방법 (3)의 값
        """

        fOPe = fIbeta * fICs / fIgamma * fIw * fIVs
        fOT = 2*math.pi*(fIgamma/fIpo/fIg/fIalpha)**0.5

        #등가정적 지진하중 출력 시: fIuserdefined = 1
        #교량의 주기 출력 시: fIuserdefined = 2

        if fIuserdefined == 1:
          return fOPe
        elif fIuserdefined == 2:
          return fOT



# 

