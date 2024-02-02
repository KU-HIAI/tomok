import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_010901_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 1.9.1 (4)' # 건설기준문서
    ref_date = '2023-09-26'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    1. 일반사항
    1.9 콘크리트의 내구성에 관한 지정
    1.9.1 일반사항
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 1.9.1 일반사항
    (4) 콘크리트의 물-결합재비는 원칙적으로 60 % 이하로 하며, 단위수량은 185 kg/m3을 초과하지 않도록 하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 콘크리트의 내구성"];
    B["KCS 14 31 30 1.9.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 1.9.1 (4)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 콘크리트의 물-결합재비"/];
    VarOut2[/"출력변수: 콘크리트의 단위수량"/];

		VarIn1[/"입력변수: 콘크리트의 물-결합재비"/];
		VarIn2[/"입력변수: 콘크리트의 단위수량"/];

    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"콘크리트의 물-결합재비 <= 60%"}
    Variable_def --> D{"콘크리트의 단위수량 <= 185 kg/㎥"}


		C --> |True|F([PASS])
		C --> |False|E([FAIL])

		D --> |True|F([PASS])
		D --> |False|E([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def durability_of_concrete(fIWatRat, fIWatCon) ->str :
        """콘크리트의 내구성

        Args:
            fIWatRat (float): 콘크리트의 물-결합재비
            fIWatCon (float): 콘크리트의 단위수량

        Returns:
            sOWatRat (string): 콘크리트의 물-결합재비
            sOWatCon (string): 콘크리트의 단위수량

        """

        if fIWatRat <= 60:
            sOWatRat = "PASS"
            if fIWatCon <= 185:
                sOWatCon = "PASS"
                return sOWatRat, sOWatCon
            else:
                sOWatCon = "FAIL"
                return sOWatRat, sOWatCon
        else:
            sOWatRat = "FAIL"
            if fIWatCon <= 185:
                sOWatCon = "PASS"
                return sOWatRat, sOWatCon
            else:
                sOWatCon = "FAIL"
                return sOWatRat, sOWatCon