import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030401_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.4.1 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '모재의 예열 온도'

    description = """
    용접
    3. 시공
    3.4 예열
    3.4.1 예열에 관한 일반사항
    """

    content = """
    #### 3.4.1 예열에 관한 일반사항
    (2) 모재의 최소예열과 용접층간 온도는 강재의 성분과 강재의 두께 및 용접구속 조건을 기초로 하여 설정한다. 최소예열 및 층간온도는 용접절차서에 규정한다. 최대 예열온도는 공사감독자의 별도의 승인이 없는 경우 230 ℃ 이하로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 모재의 예열 온도];
    B["KCS 14 31 20 3.4.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.4.1 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 모재의 예열 온도/];
    VarIn1[/입력변수: 최소예열 및 층간온도/];
    VarIn2[/입력변수: 최대 예열 온도/];
    VarIn3[/입력변수: 공사감독자의 별도의 승인/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"최소예열 및 층간온도\n최대 예열 온도"}
    C --> |"최소예열 및 층간온도"|D["강재의 성분과 강재의 두께 및 용접구속 조건을 기초로 하여 설정 \n 용접절차서에 규정 "]
    C --> |"최대 예열 온도"|E{"공사감독자의 별도의 승인"}
		E --> |False|F["230 ℃ 이하"]
		D & F --> End([모재의 예열 온도])

    """

    @rule_method
    def Minimum_Preheating_and_Interlayer_Temperature(bIMinInt, bIMaxPre, bIAppSup) -> RuleUnitResult:
        """ 모재의 예열 온도
        Args:
        bIMinInt (bool): 최소예열 및 층간온도
        bIMaxPre (bool): 최대 예열 온도
        bIAppSup (bool): 공사감독자의 별도의 승인

        Returns:
        sOPreBas (str): 모재의 예열 온도
        """
        assert isinstance(bIMinInt, bool)
        assert isinstance(bIMaxPre, bool)
        assert bIMinInt != bIMaxPre
        assert isinstance(bIAppSup, bool)

        if bIMinInt == True:
          sOPreBas = "강재의 성분과 강재의 두께 및 용접구속 조건을 기초로 하여 용접절차서에 규정"
        elif bIMaxPre == True:
          if bIAppSup == False:
            sOPreBas = "230 ℃ 이하"
          else:
            sOPreBas = "공사감독자의 별도 승인에 따른다"

        return RuleUnitResult(
                result_variables = {
                    "sOPreBas": sOPreBas
                }
            )