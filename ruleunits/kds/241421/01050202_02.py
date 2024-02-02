import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.2.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '보와 슬래브의 유효경간'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.2 구조물의 이상화
    1.5.2.2 기하학적 자료
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
    A[보와 슬래브의 유효경간];
    B["KDS 24 14 21 1.5.2.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 보와 슬래브의 유효경간/];
    VarIn1[/입력변수: 받침점 면 사이의 순경간/] ;
    VarIn2[/입력변수: 지지조건에 따라 정해지는 값/];


		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["<img src='https://latex.codecogs.com/svg.image?&space;l_{eff}=l_{n}&plus;a_{1}&plus;a_{2}'>--------------------------------------------------------"];
	 C ~~~ |"KDS 24 14 21 Picture 1.5-1"| C
		D(["보와 슬래브의 유효경간"]);

    C--->D

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_Spans_Of_Beams_And_Slabs(fOleff,fIln,fIa1,fIa2) -> float:
        """철근의 기준항복강도

        Args:
            fOleff (float) : 보와 슬래브의 유효 경간
            fIln (float) : 받침점 면 사이의 순경간
            fIa1 (float) : 지지조건에 따라 정해지는 값
            fIa2 (float) : 지지조건에 따라 정해지는 값



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 1.5.2.2 기하학적 자료 (2)의 값
        """

        fOleff = fIln+fIa1+fIa2
        return fOleff


# 

