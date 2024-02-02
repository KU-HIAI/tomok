import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030305_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.3.5 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝의 공칭 단위선단지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.5 암반 지지 말뚝
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
    A[암반 지지 말뚝];
    B["KDS 24 14 51 3.3.3.5 (1)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:말뚝의 공칭 단위선단지지력/]
			VarIn1[/입력변수:불연속면 간격/]
			VarIn2[/입력변수:암석시편의 평균 일축압축강도/]
			VarIn3[/입력변수:무차원 깊이계수/]
			VarIn4[/입력변수:무차원 지지력계수/]
			VarIn5[/입력변수:불연속면 간격/]
			VarIn6[/입력변수:불연속면 폭/]
			VarIn7[/입력변수:말뚝 폭/]
			VarIn8[/입력변수:암반에 근입된 말뚝의 근입깊이/]
			VarIn9[/입력변수:암반 근입부 말뚝 폭/]



			VarOut1
			VarIn1 ~~~ VarIn2 ~~~ VarIn3
			VarIn4 ~~~ VarIn5 ~~~ VarIn6
			VarIn7 ~~~ VarIn8 ~~~ VarIn9


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[말뚝 폭 또는 직경, 암반의 불연속면 간격 > 300mm ]
			D[속이 차있지 않은 불연속면의 폭이 < 6.4mm]
			E[흙 또는 암편으로 차있는 불연속면의 폭 < 25mm]

			F["<img src='https://latex.codecogs.com/svg.image?K_{sp}=\frac{3&plus;\frac{s_{d}}{D}}{10\sqrt{1&plus;300\frac{t_{d}}{s_{d}}}}'>---------------------------------"]
			G["<img src='https://latex.codecogs.com/svg.image?&space;q_{p}=3q_{u}K_{sp}d'>---------------------------------"]
			H["<img src='https://latex.codecogs.com/svg.image?d=1&plus;0.4H_{s}/D_{s}\leq&space;3.4'>---------------------------------"]
			K([공친 단위 선단지지력])

			Variable_def ---> C & D & E
			C & D & E ---> I{만족} ---> F & H ---> G ---> K
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_unit_end_support(fOqp,fIqu,fId,fIksp,fIsd,fItd,fID,fIHs,fIDs) -> float:
        """말뚝의 공칭 단위선단지지력
        Args:
            fOqp (float): 말뚝의 공칭 단위선단지지력
            fIqu (float): 암석시편의 평균 일축압축강도
            fId (float): 무차원 깊이계수
            fIksp (float): 무차원 지지력계수
            fIsd (float): 불연속면 간격
            fItd (float): 불연속면 폭
            fID (float): 말뚝 폭
            fIHs (float): 암반에 근입된 말뚝의 근입깊이
            fIDs (float): 암반 근입부 말뚝 폭

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.5(1) 공칭 단위선단지지력

        """

        fIksp=(3+fIsd/fID)/(1+300*fItd/fIsd)**0.5/10
        fId=1+0.4*fIHs/fIDs
        if fId>3.4:
          return "Fail"
        else:
          fOqp=3*fIqu*fIksp*fId
        return fOqp


# 

