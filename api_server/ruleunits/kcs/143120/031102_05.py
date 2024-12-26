import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031102_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.11.2 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '언더컷의 깊이의 허용값'

    description = """
    용접
    3. 시공
    3.11 용접검사
    3.11.2 육안검사
    """

    content = """
    #### 3.11.2 육안검사
    (5) 언더컷
    언더컷의 깊이는 표 3.11-3의 값을 초과해서는 안 된다.
    표 3.11-3 언더컷의 깊이의 허용값(단위 : mm)
    \begin{table}[]
\begin{tabular}{lllll}
\multirow{2}{*}{언더컷의 위치} & \multicolumn{4}{l}{품질관리 구분} \\
 & 가 & 나 & 다 & 라 \\
주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 지단부 & 해당 없음. & 0.5 & 0.5 & 0.3 \\
주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 지단부 & 해당 없음. & 1.0 & 0.8 & 0.5 \\
2차부재의 비드 지단부 & 해당 없음. & 1.0 & 1.0 & 1.0
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 언더컷의 깊이의 허용값"];
    B["KCS 14 31 20 3.11.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.11.2 (5)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 언더컷의 깊이의 허용값"/];
    VarIn1[/입력변수: 언더컷의 위치/];
    VarIn2[/입력변수: 품질관리 구분/];
		VarOut1 ~~~ VarIn1 & VarIn2
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"언더컷의 위치 \n 품질관리 구분"}
    C --> |표 3.11-3|D[언더컷의 깊이의 허용값]
		D --> End([언더컷의 깊이의 허용값])
    """

    @rule_method
    def Location_of_Undercut(sILocUnd, sIClaQua) -> RuleUnitResult:
        """ 언더컷의 깊이의 허용값
        Args:
        sILocUnd (str): 언더컷의 위치
        sIClaQua (str): 품질관리 구분

        Returns:
        fOUndDep (float): 언더컷의 깊이의 허용값
        """
        assert isinstance(sILocUnd, str)
        assert sILocUnd in["주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 지단부", "주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 지단부", "2차부재의 비드 지단부"]
        assert isinstance(sIClaQua, str)
        assert sIClaQua in["나", "다", "라"]

        if sILocUnd == "주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 지단부":
          if sIClaQua == "나":
            fOUndDep = 0.5
          elif sIClaQua == "다":
            fOUndDep = 0.5
          elif sIClaQua == "라":
            fOUndDep = 0.3

        elif sILocUnd == "주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 지단부":
          if sIClaQua == "나":
            fOUndDep = 1.0
          elif sIClaQua == "다":
            fOUndDep = 0.8
          elif sIClaQua == "라":
            fOUndDep = 0.5

        elif sILocUnd == "2차부재의 비드 지단부":
          fOUndDep = 1.0

        return RuleUnitResult(
                result_variables = {
                    "fOUndDep": fOUndDep
                }
            )