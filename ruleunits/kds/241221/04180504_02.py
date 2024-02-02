import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04180504_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.5.4 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '교량파괴확률'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.4 파괴확률
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
    A["교량파괴확률"];
    B["KDS 24 12 21 4.18.5.4 (1)~(3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수:교량파괴확률/];
		VarIn1[/입력변수: 선박의 충격하중/];
		VarIn2[/입력변수: 교각내하력이 상부구조물의 횡방향 내하력으로 표현되는 수평하중에 대한 교량구조물의 강도/];

		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def
		D{"P/H의 범위"}
		E["<img src='https://latex.codecogs.com/png.image?0.0 \leq H/P < 0.1'>-------------------"];
		F["<img src='https://latex.codecogs.com/png.image?0.1 \leq H/P < 1.0'>-------------------"];
		G["<img src='https://latex.codecogs.com/png.image?1.0 \leq H/P'>-------------------"];
		H["<img src='https://latex.codecogs.com/png.image?PC = 0.1+9\left ( 0.1-\frac{H}{P} \right )'>-------------------"];
		I["<img src='https://latex.codecogs.com/png.image?PC = \frac{1}{9}\left ( 1.0-\frac{H}{P} \right )'>-------------------"];
		J["<img src='https://latex.codecogs.com/png.image?PC = 0.0'>-------------------"];
		Variable_def ---> D ---> E & F & G
		E ---> H
		F ---> I
		G ---> J
		H & I & J ---> K
		K(["교량파괴확률(PC)"])
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def bridge_failure_probability(fOPC,fIP,fIH) -> float:
        """교량파괴확률

        Args:
            fOPC (float): 교량파괴확률
            fIP (float): 선박의 충격하중
            fIH (float): 교각내하력이 상부구조물의 횡방향 내하력으로 표현되는 수평하중에 대한 교량구조물의 강도
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.5.4 파괴확률 (2)의 값
        """

        if 0.1<= fIH/fIP <=1.0:
          fOPC = 1/9*(1.0-fIH/fIP)

        return fOPC


# 

