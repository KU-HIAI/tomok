import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030307_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.3.7 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인발저항력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.7 인발
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
    A[인발];
    B["KDS 24 14 51 3.3.3.7 (3)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:감가된 인발저항력/]
			VarIn1[/입력변수:저항계수/]
			VarIn2[/입력변수:무리말뚝의 공칭 인발저항력/]
			VarIn3[/입력변수:외말뚝의 인발저항력/]
			VarIn4[/입력변수:무리말뚝의 인발저항력/]
			VarIn5[/입력변수:무리말뚝의 폭/]
			VarIn6[/입력변수:무리말뚝의 길이/]
			VarIn7[/입력변수:말뚝캡 아래 블록의 깊이/]
			VarIn8[/입력변수:평균 비배수 전단강도/]
			VarIn9[/입력변수:흙, 말뚝, 그리고 말뚝캡을 포함한 블록의 중량/]


			VarOut1
			VarIn1 ~~~ VarIn2 ~~~ VarIn3
			VarIn4 ~~~ VarIn5 ~~~ VarIn6
			VarIn7 ~~~ VarIn8 ~~~ VarIn9


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[외말뚝의 인발 저항력]
			D[무리말뚝의 인발저항력]
			E([공칭인발저항력])
			F[인발저항력]
			G[사질토에 설치된 무리말뚝의 공칭인발 저항력]




			Variable_def ---> C & D ---> I{둘중 작은 값}
			Variable_def ---> F ---> J["<img src='https://latex.codecogs.com/svg.image?Q_{R}=\phi&space;Q_{n}=\phi&space;_{ug}Q_{ug}'>---------------------------------"]
			Variable_def ---> G ---> H["<img src='https://latex.codecogs.com/svg.image?Q_{n}=Q_{ug}=(2XZ&plus;2YZ)\overline{S_{u}}&plus;W_{g}'>---------------------------------"]
			J & H & I ---> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def reduced_pull_resistance(fOQr,fIresfac,fIQug,fIressinsum,fIresbul,fIX,fIY,fIZ,fIaveshe,fIWg) -> float:
        """인발저항력
        Args:
            fOQr (float): 인발저항력
            fIresfac (float): 저항계수
            fIQug (float): 무리말뚝의 공칭 인발저항력
            fIressinsum (float): 외말뚝의 인발저항력의 합
            fIresbul (float): 무리말뚝의 인발저항력
            fIX (float): 무리말뚝의 폭
            fIY (float): 무리말뚝의 길이
            fIZ (float): 말뚝캡 아래 블록의 깊이
            fIaveshe (float): 평균 비배수 전단강도
            fIWg (float): 흙, 말뚝, 그리고 말뚝캡을 포함한 블록의 중량

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.7(3) 인발저항력

        """

        fIresbul=(2*fIX*fIZ+2*fIY*fIZ)*fIaveshe+fIWg
        fIQug=min(fIressinsum,fIresbul)
        fOQr=fIresfac*fIQug
        return fOQr


# 

