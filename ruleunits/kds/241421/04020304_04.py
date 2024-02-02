import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020304_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.4 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최대균열간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
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
    A["최대균열간격"];
    B["KDS 24 14 21 4.2.3.4 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 주응력 축과 철근 방향 사이의 각/];
		VarIn2[/입력변수: 최대균열간격/];
		VarIn3[/입력변수: 종방향 철근과 압축 주응력 방향 사잇각/];
		VarIn4[/입력변수: 종방향에서 계산한 균열 간격/];
		VarIn5[/입력변수: 횡방향에서 계산한 균열 간격/];

		VarOut1[/출력변수: 최대균열간격/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5
		end
		Python_Class ~~~ Variable_def--->C--->D
		C{"주응력 축과 철근 방향 사이의 각이 15°보다 클 때"}
		D["<img src='https://latex.codecogs.com/svg.image?l_{r,max}=\frac{1}{(cos\theta/l_{rl,max})&plus;(sin\theta/l_{rt,max})}'>---------------------------------"]


		D--->G
		G(["최대균열간격"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def maximum_crack_spacing(fIangsxb,fOlrmax,fItheta,fIlrlmax,fIlrtmax) -> float:
        """최대균열간격

        Args:
             fIangsxb (float): 주응력 축과 철근 방향 사이의 각
             fOlrmax (float): 최대균열간격
             fItheta (float): 종방향 철근과 압축 주응력 방향 사잇각
             fIlrlmax (float): 종방향에서 계산한 균열 간격
             fIlrtmax (float): 횡방향에서 계산한 균열 간격

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (4)의 값
        """

        if fIangsxb > 15:
          fOlrmax = 1/((math.cos(fItheta*math.pi/180)/fIlrlmax)+(math.sin(fItheta*math.pi/180)/fIlrtmax))

        return fOlrmax


# 

