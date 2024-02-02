import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115010_030904_01(RuleUnit): # 허윤아 박사님에게 확인받기 KDS241431_040303_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 50 10 3.9.4 (1)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2021-05-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '현장타설 콘크리트 말뚝'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    현장타설 콘크리트 말뚝
    3. 시공
    3.9 건전도 시험
    3.9.4 검사 수량 및 시기
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.9.3 검사용 튜브 설치
    (1) 현장타설 콘크리트 말뚝에 대한 초음파검사 수량은 다음 표 3.9-2의 기준을 따른다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 현장타설 콘크리트 말뚝에 대한 초음파검사 수량"];
    B["KCS 11 50 10 3.9.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 10 3.9.4 (1)"])

    subgraph Variable_def
    VarOut[/"출력변수: 시험수량"/];
		VarIn1[/"입력변수: 평균말뚝길이"/];


    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"평균말뚝길이"}

		D --> |20 이하|E[10%]
		D --> |"20~30"|F[20%]
		D --> |30 이상|G[30%]

		E --> H([시험수량])
		F --> H([시험수량])
		G --> H([시험수량])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def inspection_quantity_for_concrete_piles(fIAveLen) ->str :
        """검사용 튜브 설치 수량

        Args:
            fIAveLen (float): 평군말뚝길이. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당

        Returns:
            fOTesQua (float) : 시험수량
        """

        if fIAveLen <= 20:
            fOTesQua = 10
            return fOTesQua
        elif 20 < fIAveLen < 30:
            fOTesQua = 20
            return fOTesQua
        else:
            fOTesQua = 30
            return fOTesQua