import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_040506_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.5.6 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '보강철근의 단면적'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.6 지름이 큰 철근에 대한 추가 규정
    (6)
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
    A["지름이 큰 철근에 대한 추가 규정"];
    B["KDS 24 14 21 4.5.6 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 정착철근의 단면적/];
		VarIn2[/입력변수: 부재내의 같은 위치에 정착된 철근 층의 수/];
		VarIn3[/입력변수: 각 층에서 정착된 철근의 수/];
		VarOut1[/출력변수: 인장면에 평행한 정착철근의 단면적/];
		VarOut2[/출력변수: 인장면에 수직인 정착철근의 단면적/];

		VarOut1 & VarOut2 ~~~VarIn1 & VarIn2 & VarIn3
		end
		Python_Class ~~~ Variable_def--->C & D

		C["<img src='https://latex.codecogs.com/svg.image?A_{sh}=0.25A_sn_1'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?A_{sv}=0.25A_sn_2'>---------------------------------"]

		E(["인장면에 평행한 정착철근의 단면적"])

		F(["인장면에 수직인 정착철근의 단면적"])
		C--->E
		D--->F
		E & F ---> G(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Cross_sectional_area_of_rebar(fIAsh,fIAsv,fIAs,fIn1,fIn2) -> float:
        """보강철근의 단면적

        Args:
            fIAsh (float): 공칭지름
            fIAsv (float): 콘크리트 설계압축강도
            fIAs (float): 최대 지름
            fIn1 (float): 철근 단면적
            fIn2 (float): 용접의 설계전단강도

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.5.6 지름이 큰 철근에 대한 추가 규정 (6)의 값
        """

        if fIAsh >= 0.25*fIAs*fIn1 and fIAsv >= 0.25*fIAs*fIn2:
          return "Pass"
        else:
          return "Fail"


# 

