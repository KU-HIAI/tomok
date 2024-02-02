import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03040303_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.4.3.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭 단위 선단지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.3 극한한계상태의 지지력
    3.4.3.3 점성토에 설치한 현장타설말뚝의 지지력 산정
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
    A[점성토에 설치한 현장타설말뚝의 지지력 산정];
    B["KDS 24 14 51 3.4.3.3 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:공칭 단위 선단지지력/]
			VarIn1[/입력변수:말뚝의 지름/]
			VarIn2[/입력변수:말뚝의 관입깊이/]
			VarIn3[/입력변수:비배수전단강도/]
			VarIn4[/입력변수:지름/]
			VarIn5[/입력변수:현장시험결과/]
			VarIn6[/입력변수:실내시험결과/]
			VarIn7[/입력변수: Nc값/]


			VarIn1 ~~~ VarIn2 ~~~ VarIn3
			VarIn4 ~~~ VarIn5 ~~~ VarIn6 ~~~ VarIn7


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?q_{p}=N_{c}S_{u}\leq&space;4.0'>---------------------------------"]
			D["<img src='https://latex.codecogs.com/svg.image?N_{c}=6[1&plus;0.2(\frac{Z}{D})]\leq&space;9'>---------------------------------"]
			E{선단으로부터 지름 2배만큼 떨어진 깊이 이내의 위치에서 시행한 현장시험결과}
			F{이 깊이에서 채취한 불교란 시료를 사용한 실내시험 결과}
			H{비배수전단강도가 0.024MPa 이하라면 Nc 값에 0.67을 곱한다}

			Variable_def ---> E & F & D
			D ---> H
			E & F ---> G[비배수전단강도] ---> C
			C & H ---> I[공칭 단위 선단지지력] ---> K([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def unit_nominal_end_bearing_capacity(fOqp,fID,fIZ,fISu,fINc) -> float:
        """공칭 단위 선단지지력
        Args:
            fOqp (float): 근입 깊이
            fID (float): 말뚝의 탄성계수
            fIZ (float): 말뚝의 관성모멘트
            fISu (float): 사질토의 깊이에 따른 탄성계수 증가비
            fINc (float): 표준관입시험 타격횟수

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.3 점성토에 설치한 현장타설말뚝의 지지력 산정 (2)의 값

        """
        fINc = min(6*(1+0.2*(fIZ/fID)), 9)
        if fISu <= 0.024 :
          fOqp = min(fINc*0.67*fISu, 4)
        else:
          fOqp = min(fINc*fISu, 4)

        return fOqp


# 

