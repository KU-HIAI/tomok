import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_0203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 10 2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '탄성지진응답계수'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    2. 설계
    2.3 해석방법
    (2) 탄성지진응답계수
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
    B["KDS 24 17 10 2.3 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:탄성지진응답계수/]
			VarIn1[/입력변수:가속도계/]
			VarIn2[/입력변수:상세예측법을 통해 획득한 안전율/]
			VarIn3[/입력변수:지반 특성에 대한 무차원의 계수/]
			VarIn4[/입력변수:교량의 주기/]
			VarIn5[/입력변수:교량의 주기/]

			VarOut1 ~~~
			VarIn1 & VarIn2 ~~~
			VarIn3 & VarIn4 & VarIn5


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?C_{s}=\frac{1.2AS}{T^{\frac{2}{3}}}'>---------------------------------"]
			D["<img src='https://latex.codecogs.com/svg.image?C_{sm}=\frac{1.2AS}{T_{m}^{\frac{2}{3}}}'>---------------------------------"]
			E["<img src='https://latex.codecogs.com/svg.image?C_{sm}=\frac{3AS}{T_{m}^{\frac{4}{3}}}'>---------------------------------"]
			F([탄성지진응답계수])
			G([탄성지진응답계수])
			H[교량의 주기 ≥ 4.0]
			I[탄성지지응답계수 ≤ 2.5]

			Variable_def ---> C ---> F
			Variable_def ---> H -- Yes ---> E ---> G
			H -- No ---> I ---> D ---> G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Elastic_seismic_response_coefficient(fOCs,fIA,fIS,fIT,fOCsm,fITm,fIuserdefined) -> float:
        """탄성지진응답계수

        Args:
             fOCs (float): 탄성지진응답계수
             fIA (float): 가속도계수
             fIS (float): 지반 특성에 대한 무차원의 계수
             fIT (float): 교량의 주기
             fOCsm (float): m번째 진동모드에 대한 탄성지진응답계수
             fITm (float): m번째 진동모드에 대한 교량의 주기
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 교량 내진설계기준(일반설계법) 2.3 해석방법 (2)의 값
        """

        #단일모드스펙트럼해석 시: fIuserdefined = 1
        #다중모드스펙트럼해석 시: fIuserdefined = 2
        if fIuserdefined == 1:
          fOCs = 1.2 * fIA * fIS / fIT**(2/3)
          return fOCs
        elif fIuserdefined == 2:
          if fITm <= 4:
            fOCsm = min(1.2 * fIA * fIS / fITm**(2/3) , 2.5 * fIA)
          else:
            fOCsm = 3 * fIA * fIS / fITm**(2/3)
          return fOCsm


# 

