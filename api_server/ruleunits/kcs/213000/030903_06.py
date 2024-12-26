import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030903_06(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.9.3 (6)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '버팀대와 수평가새의 설치간격'

    description = """
    가설흙막이 공사
    3. 시공
    3.9. 띠장, 버팀대, 중간말뚝, X-브레이싱
    3.9.3. 버팀대(strut), 경사버팀대 및 경사고임대(레이커, raker)
    (6)
    """

    content = """
    #### 3.9.3. 버팀대(strut), 경사버팀대 및 경사고임대(레이커, raker)
    (6) 버팀대 수평가새의 설치간격은 다음을 기준으로 하며, 정밀해석에 의할 경우는 별도로 적용할 수 있다.
    ① 버팀대 설치간격이 2.5m 이내인 경우 : 버팀대 10개 이내마다
    ② 버팀대 설치간격이 2.5m를 초과하는 경우 : 버팀대 9개 이내마다    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 버팀대와 수평가새의 설치간격];
    B["KCS 21 30 00 3.9.3 (6)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.9.3 (6)"])

    subgraph Variable_def
    VarOut1[/출력변수: 수평가새의 설치간격/];
    VarIn1[/입력변수: 버팀대의 설치간격/];
    end
    VarOut1 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"버팀재의 설치간격 <= 2.5m"}
    C1 --> |YES|D1["버팀대 10개 이내마다"]
    C1 --> |NO|D2["버팀대 9개 이내마다"]

    D1 & D2 --> E1(["수평가새의 설치간격"]);
    """

    @rule_method
    def Spacing_of_Supporting_Piers(fISpaSup) -> str:
        """ 버팀대와 수평가새의 설치간격
        Args:
            fISpaSup (float): 버팀대 설치간격

        Returns:
            sOInsSpa (str): 수평가새의 설치간격
        """
        assert isinstance(fISpaSup, float)

        if fISpaSup <= 2.5:
          sOInsSpa = "버팀대 10개 이내마다 수평가새 설치"
        else:
          sOInsSpa = "버팀대 9개 이내마다 수평가새 설치"

        return RuleUnitResult(
                result_variables = {
                    "sOInsSpa": sOInsSpa
                }
            )