import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115010_030904_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 10 3.9.4 (1)'
    ref_date = '2023-09-11'
    doc_date = '2021-05-12'
    title = '현장타설 콘크리트 말뚝에 대한 초음파검사 수량'

    description = """
    현장타설 콘크리트 말뚝
    3. 시공
    3.9 건전도 시험
    3.9.4 검사 수량 및 시기
    (1)
    """

    content = """
    #### 3.9.3 검사용 튜브 설치
    (1) 현장타설 콘크리트 말뚝에 대한 초음파검사 수량은 다음 표 3.9-2의 기준을 따른다.
    """

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

    @rule_method
    def inspection_quantity_for_concrete_piles(fIAveLen) -> str :
        """검사용 튜브 설치 수량

        Args:
            fIAveLen (float): 평균말뚝길이

        Returns:
            fOTesQua (float) : 시험수량
        """
        assert isinstance (fIAveLen, float)

        if fIAveLen <= 20:
            fOTesQua = 10
        elif 20 < fIAveLen < 30:
            fOTesQua = 20
        else:
            fOTesQua = 30

        return RuleUnitResult(
                result_variables = {
                    "fOTesQua": fOTesQua,
                }
            )