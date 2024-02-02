import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_02_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 2.6' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '소요 곡룔연성도'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		2. 소요연성도
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
    A["소요 곡률연성도"];
    B["KDS 24 17 10 부록 2 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:고려하는 방향으로의 단면 최대두께/];
		VarIn2[/입력변수:기둥 형상비의 기준이 되는 기둥길이/];


		VarOut1[/출력변수:소위 변위연성도의 최댓값/];
		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def
		Variable_def--->D---> C

		C([소위 변위연성도의 최대값])
		D["<img src='https://latex.codecogs.com/svg.image?\mu_{\Delta}=\frac{\mu_{\Delta}(0.7&plus;0.75(\frac{h}{L_{s}}))}{0.13(1.1&plus;\frac{h}{L_{s}})}'>---------------------------------"]



    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def The_maximum_value_of_the_so_called_displacement_ductility(fOmaxdis,fIdisduc,fIh,fIls) -> float:
        """소요 곡룔연성도

        Args:
            fOmaxdis (float): 소위 변위연성도의 최댓값
            fIdisduc (float): 소위 변위연성도
            fIh (float): 고려하는 방향으로의 단면 최대두께
            fIls (float): 기둥 형상비의 기준이 되는 기둥길이


        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 2. 소요연성도 (6)의 값
        """

        fOmaxdis = (fIdisduc - 0.5 * (0.7 + 0.75 * (fIh / fIls))) / (0.13 * (1.1 + fIh / fIls))
        return fOmaxdis



# 

