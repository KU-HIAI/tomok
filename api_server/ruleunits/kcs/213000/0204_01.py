import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_0204_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 2.4 (1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-13'
    title = '지하연속벽 타설 콘크리트 재료'

    description = """
    가설흙막이 공사
    2. 자재
    2.4 지하연속벽
    (1)
    """

    content = """
    #### 2.4. 지하연속벽
    (1) 타설되는 콘크리트는 공사시방서에 따르며, 달리 명시된 것이 없는 경우에는 다음을 따른다.
    ② 골재 치수는 13~25mm를 표준으로 한다.
    ③ 공기 함유율은 (4.5±l.5)％를 표준으로 한다.
    ④ 단위시멘트량은 350kg/m3 이상, 물․시멘트 비는 50％ 이하로 한다.
    ⑤ 슬럼프값은 18~21cm를 표준으로 한다.
    ⑥ 배합강도는 설계강도의 125％ 이상으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지하연속벽 타설 콘크리트 재료];
    B["KCS 21 30 00 2.4 (1) ② ~ ⑥"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 2.4 (1) ② ~ ⑥"])

    subgraph Variable_def
    VarOut[/출력변수: 배합강도/];
    VarIn1[/입력변수: 골재치수/];
		VarIn2[/입력변수: 공기 함유율/];
    VarIn3[/입력변수: 단위시멘트량/];
		VarIn4[/입력션수: 물시멘트 비/];
		VarIn5[/입력변수: 슬럼프값/];
		VarIn6[/입력변수: 설계강도/];
    end
		VarOut & VarIn1 & VarIn2 ~~~ VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"검토항목"}
    C --> |"골재치수"|C1{"13mm <= <= 25mm"}
    C --> |"공기함유율"|C2{"3% <= <= 6%"}
    C --> |"단위시멘트량"|C3{">= 350kg/m^3"}
    C --> |"물시멘트 비"|C4{" <= 50%"}
    C --> |"슬럼프값"|C5{"18cm <= <= 21cm"}
    C --> |"배합강도"|C6{"= 설계강도*1.25"}

    C1 & C2 & C3 & C4 & C5 --> D1([Pass or Fail])
    C6 --> D2["배합강도"]
    D2 --> E(["배합강도"])
    """

    @rule_method
    def Dimension_of_Aggregate(fIDimAgg, fIAirRat,fICemCon, fIWatRat, fISluVal, fIDesStr) -> bool:
        """ 지하연속벽 타설 콘크리트 재료
        Args:
            fIDimAgg (float): 골재 치수
            fIAirRat (float): 공기 함유율
            fICemCon (float): 단위 시멘트량
            fIWatRat (float): 물, 시멘트 비
            fISluVal (float): 슬럼프 값
            fIDesStr (float): 설계강도

        Returns:
            pass_fail (bool): 가설흙막이 공사 2.4 지하연속벽 (1)의 판단 결과
            fOTarStr (float): 배합강도
        """
        assert isinstance(fIDimAgg, float)
        assert isinstance(fIAirRat, float)
        assert isinstance(fICemCon, float)
        assert isinstance(fIWatRat, float)
        assert isinstance(fISluVal, float)
        assert isinstance(fIDesStr, float)

        fOTarStr = fIDesStr*1.25

        if 13 <= fIDimAgg <= 25 and 3 <= fIAirRat <= 6 and fICemCon >= 350 and fIWatRat <=50 and 18 <= fISluVal <= 21:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "fOTarStr": fOTarStr,
                }
            )