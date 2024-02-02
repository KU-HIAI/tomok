import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS112025_030302_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 20 25 3.3.2 (4)' # 건설기준문서
    ref_date = '2023-09-19'  # 디지털 건설문서 작성일
    doc_date = '2020-12-03'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '되메우기 및 뒤채움'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    되메우기 및 뒤채움
    3. 시공
    3.3 시공기준
    3.3.2 되메우기, 흙쌓기 및 땅고르기
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.2 되메우기, 흙쌓기 및 땅고르기
    (4) 되메우기 재료는 모래, 석분 또는 양질의 토사를 사용하고 발파석인 경우 최대 입경이 100 mm 이하로 한다.

    """

    # 플로우차트(mermaid)
    flowchart = """
 flowchart TD
    subgraph Python_Class
    A[Title: 되메우기 재료];
    B["KCS 11 20 25 3.3.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 25 3.3.2 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 되메우기 재료/];
    VarIn1[/입력변수: 발파석/];
    VarIn2[/입력변수: 최대입경/];

    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{발파석인 경우}
    C --> |True|D["최대입경 <= 100 mm"]

    D --> |False|F([FAIL])
    D --> |True|G([PASS])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def backfill_material(bIBlaRoc, fIMaxPar) ->str :
        """되메우기 재료

        Args:
            bIBlaRoc (boolean): 발파석
            fIMaxPar (float): 최대입경

        Returns:
            sOBacMat (string): 되메우기 재료


        """

        if bIBlaRoc == True:
            if fIMaxPar <= 100:
                sOBacMat = "PASS"
                return sOBacMat
            else:
                sOBacMat = "FAIL"
                return sOBacMat