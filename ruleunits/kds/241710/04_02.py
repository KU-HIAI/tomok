import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_04_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 4.2' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계전단력'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
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
    A["설계전단력"];
    B["KDS 24 17 10 부록.4.(2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:교각의 최대 소성힌지력/];
		VarIn2[/입력변수: 탄성전단력/];



		VarOut1[/출력변수: 설계전단력/];
		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def
		Variable_def--->E--->F

		E["설계전단력=Min(탄성전단력, 교각의 최대 소성힌지력) "]
		E~~~ |"KDS 24 17 10 2.1(4)"| E

		F(["설계전단력"])



    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_plastic_hinge_force_of_piers(fIshforc,fImaxpla,fIelashr) -> float:
        """설계전단력

        Args:
            fIshforc (float): 설계전단력
            fImaxpla (float): 교각의 최대 소성힌지력
            fIelashr (float): 탄성전단력


        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (2)의 값
        """

        fIshforc = min(fImaxpla,fIelashr)
        return fIshforc



# 

