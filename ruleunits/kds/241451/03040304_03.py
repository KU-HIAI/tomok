import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03040304_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.4.3.4 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭 단위 선단지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.3 극한한계상태의 지지력
    3.4.3.4 사질토에 설치한 현장타설말뚝의 지지력 산정
    (3)
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
    A[사질토에 설치한 현장타설말뚝의 지지력 산정];
    B["KDS 24 14 51 3.4.3.4 (3)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarOut1[/출력변수:공칭 선단지지력/]
			VarIn1[/입력변수:설계구역지층의 평균 N값으로서, 해머효율에 대해서 보정한 /]
			VarIn2[/입력변수:대상층 중간에서 연직유효응력/]
			VarIn3[/입력변수:대기압/]

			VarOut1
			VarIn1 ~~~ VarIn2 ~~~ VarIn3

      end
			Python_Class ~~~ Variable_def;
      Variable_def
			C[N60 > 50]
			D["<img src='https://latex.codecogs.com/svg.image?q_{p}=0.59[N_{60}(\frac{p_{a}}{\sigma&space;_{v}^{\prime}})]\sigma&space;_{v}^{\prime}'>---------------------------------"]
			E["<img src='https://latex.codecogs.com/svg.image?0.057N_{60}\leq&space;50'>---------------------------------"]
			F["<img src='https://latex.codecogs.com/svg.image?q_{p}=1.2N_{60}'>---------------------------------"]
			G[재하시험을 실시한 경우 외, 공친선단지지력 < 3.0MPa]
			I[N_60값이 50보다 큰 지층에 대해서 중간지반으로 간주]
			K([공칭선단지지력])

			Variable_def ---> E ---> F ---> G ---> K
			Variable_def ---> I ---> C ---> D ---> K
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def unit_nominal_end_bearing_capacity(fOqp,fIN,fIverstr,fIPa,fIuserdefined) -> float:
        """공칭 단위 선단지지력
        Args:
            fOqp (float): 근입 깊이
            fIN (float): 설계구역 지층의 평균 N값으로서, 해머효율에 대해서 보정한 값
            fIverstr (float): 대상층 중간에서 연직유효응력
            fIPa (float): 대기압
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.4 사질토에 설치한 현장타설말뚝의 지지력 산정 (3)의 값

        """

        #재하시험을 실시한 경우 : fIuserdefined == 1
        #그 외 : fIuserdefined == 2

        if fIN * 0.057 <= 50:
          if fIuserdefined ==1:
            fOqp = min(1.2*fIN, 3)
          elif fIuserdefined ==2:
            fOqp = 1.2*fIN

        if fIN > 50:
          fIN = min(fIN, 100)
          fOqp = 0.59*((fIN*(fIPa/fIverstr))**0.8)*fIverstr

        return fOqp


# 

