import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010401_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.4.1 (1)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '나무말뚝의 허용압축응력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.4.1 나무말뚝
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
    A[나무말뚝의 허용응력];
    B["KDS 11 50 15 4.1.4.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 나무말뚝의 허용압축응력/];
    VarIn1[/입력변수: 상시 습윤상태에서의 허용압축응력/] ;



		VarOut~~~VarIn1


		end
		Python_Class ~~~ Variable_def;
		Variable_def---->D
		D{"소나무, 낙엽송, 미송의 경우"}
		C["5 MPa"]
		E["min(상시습윤상태에서의 허용압축응력, 5Mpa)"]
		F(["나무말뚝의 허용압축응력"])

		D--YES---->C
		D--NO---->E
		C & E----->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def allowable_compressive_stress_of_timber_pile(fOacsotp,fItimois,fIuserdefined) -> float:
        """나무말뚝의 허용압축응력

        Args:
            fOacsotp (float): 나무말뚝의 허용압축응력
            fItimois (float): 상시 습윤상태에서의 허용압축응력
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.4.1 나무말뚝 (1)의 값
        """
        #소나무, 낙엽송, 미송이 아닐 경우 = fIuserdefined == 1
        #소나무, 낙엽송, 미송일 경우 = fIuserdefined == 2

        if fIuserdefined == 1:
          fOacsotp = min(fItimois,5)
          return fOacsotp

        if fIuserdefined == 2:
          fOacsotp = 5
          return fOacsotp


# 

