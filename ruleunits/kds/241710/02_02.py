import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_02_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 2.2' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '소요 응답수정계수'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		2. 소요연성도
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
    A["소요 응답수정계수"];
    B["KDS 24 17 10 부록 2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:지진하중을 포함한 하중조합에 따른 기둥의 탄성모멘트/];
		VarIn2[/입력변수:기둥의 설계휨강도/];


		VarOut1[/출력변수:소요 응답수정계수/];
		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def
		Variable_def ---> D ---> C


		C([소요 응답수정계수])
		D["<img src='https://latex.codecogs.com/svg.image?R_{req}=\frac{M_{el}}{\phi&space;M_{n}}'>---------------------------------"]
		D~~~ |"2.6(2)②"| D
		D~~~ |"2.2(4)"| D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def required_response_modification_factor(fOrrea,fImel,fImn) -> float:
        """소요 응답수정계수

        Args:
            fOrrea (float): 소요 응답수정계수
            fImel (float): 지진하중을 포함한 하중조합에 따른 기둥의 탄성모멘트
            fImn (float): 기둥의 설계휨강도


        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 2. 소요연성도 (2)의 값
        """
        fOrrea = fImel / fImn
        return fOrrea


# 

