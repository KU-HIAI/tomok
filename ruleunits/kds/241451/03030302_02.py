import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030302_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.3.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝의 감가된 지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.2 말뚝의 축방향 하중
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
    A[말뚝의 축방향 하중];
    B["KDS 24 14 51 3.3.3.2 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:말뚝의 감가된 지지력/]
			VarIn1[/입력변수:외말뚝의 지지력에 대한 저항계수/]
			VarIn2[/입력변수:외말뚝의 지지력/]
			VarIn3[/입력변수:말뚝의 선단지지력/]
			VarIn4[/입력변수:말뚝의 주면마찰력/]
			VarIn5[/입력변수:말뚝의 단위 선단지지력/]
			VarIn6[/입력변수:말뚝의 단위 주면 마찰력/]
			VarIn7[/입력변수:말뚝 주면면적/]
			VarIn8[/입력변수:말뚝 선단면적/]
			VarIn9[/입력변수:말뚝의 선단지지에 대한 저항계수/]
			VarIn10[/입력변수:말뚝의 주면마찰에 대한 저항계수/]


			VarOut1
			VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4 ~~~ VarIn5
			VarIn6 ~~~ VarIn7 ~~~ VarIn8 ~~~ VarIn9 ~~~ VarIn10


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{q}Q_{ult}'>---------------------------------"]
			D["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{qp}Q_{p}&plus;\phi&space;_{qs}Q_{s}'>---------------------------------"]
			E["<img src='https://latex.codecogs.com/svg.image?Q_{p}=q_{p}A_{p}'>---------------------------------"]
			F["<img src='https://latex.codecogs.com/svg.image?Q_{s}=q_{s}A_{s}'>---------------------------------"]
			G([말뚝의 감가된 지지력])

			Variable_def ---> E & F ----> D
			Variable_def ---> C
			D & C ---> G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_reduced_support_of_a_stake(fOQr,fIq,fIQult,fIQp,fIQse,fIqp,fIqs,fIAs,fIAp,fIcoesup,fIcofric,fIuserdefined) -> float:
        """말뚝의 감가된 지지력
        Args:
            fOQr (float): 말뚝의 감가된 지지력
            fIq (float): 외말뚝의 지지력에 대한 저항계수
            fIQult (float): 외말뚝의 지지력
            fIQp (float): 말뚝의 선단지지력
            fIQse (float): 말뚝의 주면마찰력
            fIqp (float): 말뚝의 단위 선단지지력
            fIqs (float): 말뚝의 단위 주면마찰력
            fIAs (float): 말뚝 주면면적
            fIAp (float): 말뚝 선단면적
            fIcoesup (float): 말뚝의 선단지지에 대한 저항계수
            fIcofric (float): 말뚝의 주면마찰에 대한 저항계수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.2(2) 말뚝의 감가된 지지력

        """

        fIQp=fIqp*fIAp
        fIQse=fIqs*fIAs
        if fIuserdefined==1: #총 저항력에서 선단지지력과 주면마찰력을 구분하지 않는 경우
          fOQr=fIq*fIQult
          return fOQr
        elif fIuserdefined==2: #선단과 주면 저항을 구별하는 방법일 경우
          fOQr=fIcoesup*fIQp+fIcofric*fIQse
          return fOQr


# 

