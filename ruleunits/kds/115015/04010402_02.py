import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010402_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.4.2 (2)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-31'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트의 허용하중'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.4.2 기성콘크리트말뚝
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
    A[콘크리트 말뚝 허용하중];
    B["KDS 11 50 15 4.1.4.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 콘크리트 허용하중/];
    VarIn1[/입력변수: 말뚝 최소단면/] ;
    VarIn2[/입력변수: 설계기준강도/];


		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["콘크리트 허용하중= 말뚝 최소단면X설계기준강도"];
    D(["콘크리트 허용하중"]);

    C--->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def allowable_load_of_concrete(fOalconc,fIfck,fIminsep) -> float:
        """콘크리트의 허용하중

        Args:
            fOalconc (float): 콘크리트의 허용하중
            fIfck (float): 콘크리트 설계기준강도
            fIminsep (float): 말뚝의 최소단면

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.4.2 기성콘크리트말뚝 (2)의 값
        """
        if fIfck >= 35:
          fOalconc = fIminsep * fIfck
          return fOalconc
        else:
          return "Fail"


# 

