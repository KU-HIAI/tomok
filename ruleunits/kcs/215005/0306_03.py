import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS215005_0306_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 21 50 05 3.6 (3)' # 건설기준문서
    ref_date = '2023-10-30'  # 디지털 건설문서 작성일
    doc_date = '2023-01-31'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거푸집 및 동바리공사 일반사항'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    거푸집 및 동바리공사 일반사항
    3. 시공
    3.6 가새재
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.6 가새재
    (3) 단일부재 가새재 사용이 불가능할 경우의 이음방법은 다음 사항에 따른다.
    ① 이어지는 가새재의 각도는 같아야 한다.
    ② 겹침이음을 하는 가새재 간의 이격되는 순 간격이 100mm 이내가 되도록 설치하여야 한다.
    ③ 가새재의 이음위치는 각각의 가새재에서 서로 엇갈리게 설치하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 겹침이음을 하는 가새재 간의 이격되는 순 간격"];
    B["KCS 21 50 05 3.6 (3)"];
    B ~~~ A
    end

    KCS(["KCS 21 50 05 3.6 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 가새재 간의 순간격"/];


		VarIn1[/"입력변수: 가새재 간의 순간격"/];


    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"가새재 간의 순간격 < 100mm"}


		D --> |True|G([PASS])
		D --> |False|H([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def  spacing_between_overlapping_joists(fIDisBra) -> str:
        """겹침이음을 하는 가새재 간의 이격되는 순 간격

        Args:
            fIDisBra (float): 가새재 간의 순간격

        Returns:
            sODisBra (string): 가새재 간의 순간격
        """

        if fIDisBra <= 100:
            sODisBra = "PASS"
        else:
            sODisBra = "FAIL"
        return sODisBra


