import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020702_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.7.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '고장력볼트'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.7 연결 이음부 설계
    4.2.7.2 볼트 이음부 설계
    (4)
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
    A[고장력 볼트 설계];
    B["KDS 24 90 11 4.2.7.2 4)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수:볼트 1개에 작용하는 힘 /];
		VarIn2[/입력변수: 볼트 1개의 허용력/];
		VarIn3[/입력변수: 축방향력/];
		VarIn4[/입력변수: 볼트의 개수/];
		VarIn5[/입력변수: 볼트 1개에 작용하는 힘/];
		VarIn6[/입력변수: 볼트 1개의 허용력/];
		VarIn7[/입력변수: 휨모멘트/];
		VarIn8[/입력변수: 볼트로부터 중심축까지의 거리/];
		VarIn9[/입력변수: 접합선의 한쪽 편에 있는 볼트군의 집합/];
		VarIn10[/입력변수: 가장자리의 볼트의 중심축으로부터의 거리/];
		VarIn11[/입력변수: 축방향력에 의한 볼트 1개의 작용력/];
	  VarIn12[/입력변수: 휨모멘트에 의한 볼트 1개의 작용력/];
	  VarIn13[/입력변수: 전단력에 의한 볼트 1개의 작용력/];
	  VarIn14[/입력변수: 볼트 1개의 허용력/];



    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11~~~VarIn13 & VarIn14

    end

    Python_Class ~~~ Variable_def;
		Variable_def--->C
		C{"고장력 볼트 설계"}

    D["<img src='https://latex.codecogs.com/svg.image?\rho=\frac{P}{n}\leq\rho&space;_{a}'>--------------------------------------------------------"];
		E["<img src='https://latex.codecogs.com/svg.image?\rho=\frac{M}{\sum&space;y_{i}^{2}}y_{i}\leq\frac{y_{i}}{y_{n}}\rho&space;_{a}'>--------------------------------------------------------"];
		F["<img src='https://latex.codecogs.com/svg.image?\sqrt{(\rho&space;_{a}&plus;\rho&space;_{m})^{2}&plus;\rho&space;_{s}^{2}}\leq\rho&space;_{a}'>--------------------------------------------------------"];
		C--축방향력 또는 전단력을 받는 판--->D
		C--휨모멘트가 작용하는 판--->E
		C--축방향력, 휨모멘트 및 전단력이 함께 작용하는 판--->F
		M(["Pass or Fail"])
		D & E & F--->M
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Force_On_A_Single_Bolt(fIrho,fIrhoa,fIP,fIn,fIM,fIyi,fIsbfosj,fIyn,fIrhop,fIrhom,fIrhos,fluserdefined) -> bool:
        """고장력볼트

        Args:
             fIrho (float): 볼트 1개에 작용하는 힘
             fIrhoa (float): 볼트 1개의 허용력
             fIP (float): 축방향력
             fIn (float): 볼트의 개수
             fIM (float): 휨모멘트
             fIyi (float): 볼트로부터 중심축까지의 거리
             fIsbfosj (float): 접합선의 한쪽 편에 있는 볼트군의 집합
             fIyn (float): 가장자리의 볼트의 중심축으로부터의 거리
             fIrhop (float): 축방향력에 의한 볼트 1개의 작용력
             fIrhom (float): 휨모멘트에 의한 볼트 1개의 작용력
             fIrhos (float): 전단력에 의한 볼트 1개의 작용력
             fluserdefined (float): 사용자 선택


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.7.2 볼트 이음부 설계 (4)의 통과 여부
        """



        # fluserdefined == 1 : 축방향력 또는 전단력을 받는 판을 연결하는 경우의 볼트
        # fluserdefined == 2 : 휨모멘트가 작용하는 판을 연결하는 경우의 볼트
        # fluserdefined == 3 : 축방향력, 휨모멘트 및 전단력이 함께 작용하는 판을 연결할 경우의 볼트


        if fluserdefined == 1:
          if fIP / fIn <= fIrhoa:
            fIrho = fIP / fIn
            return "Pass"
          else:
            return "Fail"
        elif fluserdefined == 2:
          if fIM * fIyi / (fIyi ** 2) <= fIyi * fIrhoa / fIyn:
            fIrho = fIM * fIyi / (fIyi ** 2)
            return "Pass"
          else:
            return "Fail"
        elif fluserdefined == 3:
          if ((fIrhop + fIrhom) ** 2 + fIrhos ** 2) ** 0.5 <= fIrhoa:
            return "Pass"
          else:
            return "Fail"


# 

