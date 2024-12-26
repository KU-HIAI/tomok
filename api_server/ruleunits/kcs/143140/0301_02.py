import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_0301_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.1 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-10-31'
    title = '블라스트의 일반적인 사항'

    description = """
    도장
    3. 시공
    3.1 표면처리 관리
    (2)
    """

    content = """
    #### 3.1 표면처리 관리
    (2) 블라스트의 장치에서 노즐의 구경과 형상은 작업에 적절한 것을 선택하여 사용해야 한다. 블라스트의 일반적인 사항은 다음과 같다.
    ① 노즐의 구경은 일반적으로 8~13 mm를 사용한다.
    ③ 분사거리는 연강판의 경우에는 150~200 mm, 강판의 경우에는 300 mm 정도로 유지한다
    ④ 연마재의 분사각도는 피도물에 대하여 50~60°정도로 유지한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 블라스트의 일반적인 사항];
    B["KCS 14 31 40 3.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 40 3.1 (2)"])

    subgraph Variable_def
		subgraph V1
    VarIn1[/입력변수: 노즐 구경/];
		end
		subgraph V2
    VarOut[/출력변수: 분사거리/];
    VarIn2[/입력변수: 연강판/];
    VarIn3[/입력변수: 강판/];
		end
		subgraph V3
    VarIn4[/입력변수: 분사각도/];
		end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{노즐 구경\n분사거리\n분사각도}
		C --> |노즐 구경|D{"8<노즐 구경<13"}
		D --> End1([Pass or Fail])
		C --> |분사거리|E{"연강판\n강판"}
		E --> |연강판|F["150~200 mm"]
		E --> |강판|G[300 mm]
		C --> |분사각도|H{"50<분사각도<60"}
		F & G --> End2([블라스트의 일반적인 사항])
		H --> End3([Pass or Fail])
    """

    @rule_method
    def Norminal_Diameter_of_Nozzle(fIDiaNoz, bIMilSte, bIStePla, fIBlaAng) -> str:
        """ 블라스트의 일반적인 사항
        Args:
        fIDiaNoz (float): 노즐 구경
        bIMilSte (bool): 연강판
        bIStePla (bool): 강판
        fIBlaAng (float): 분사각도

        Returns:
        pass_fail_1 (bool): 도장 3.1 표면처리 관리 (2) ①의 판단 결과
        sOBlaDis (str): 분사거리
        pass_fail_2 (bool): 도장 3.1 표면처리 관리 (2) ④의 판단 결과
        """
        assert isinstance(fIDiaNoz, float)
        assert isinstance(bIMilSte, bool)
        assert isinstance(bIStePla, bool)
        assert bIMilSte != bIStePla
        assert isinstance(fIBlaAng, float)

        if 8 <= fIDiaNoz <= 13:
          pass_fail_1 = True
        else:
          pass_fail_1 = False

        if bIMilSte == True and bIStePla == False:
          sOBlaDis = "150~200mm"
        elif bIMilSte == False and bIStePla == True:
          sOBlaDis ="300mm 정도"

        if 50 <= fIBlaAng <= 60:
          pass_fail_2 = True
        else:
          pass_fail_2 = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail_1": pass_fail_1,
                    "sOBlaDis": sOBlaDis,
                    "pass_fail_2": pass_fail_2,
                }
            )