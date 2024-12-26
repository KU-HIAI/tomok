import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031102_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.11.2 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '용접비드 표면의 요철 품질'

    description = """
    용접
    3. 시공
    3.11 용접검사
    3.11.2 육안검사
    """

    content = """
    #### 3.11.2 육안검사
    (4) 용접비드 표면의 요철
    비드길이 25 mm 범위에서의 고저차로 나타내는 비드 표면의 요철은 다음 표 3.11-2의 값을 초과해서는 안 된다.
    표 3.11-2 용접비드 표면의 요철 허용값(단위 : mm)
    \begin{table}[]
\begin{tabular}{lllll}
품질관리 구분 & 가 & 나 & 다 & 라 \\
요철 허용 값 & 해당 없음. & 4 & 4 & 3
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 용접비드 표면의 요철 품질"];
    B["KCS 14 31 20 3.11.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.11.2 (4)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 요철 허용 값"/];
    VarIn1[/입력변수: 비드길이/];
    VarIn2[/입력변수: 품질관리 구분/];
		VarOut1 ~~~ VarIn1 & VarIn2
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"비드길이 < 25 mm"}
    C --> |"True"|D{품질관리 구분}
		D --> |나, 다|E[4 mm]
		D --> |라|F[3 mm]
		E & F --> End([요철 허용 값])
    """

    @rule_method
    def Length_of_Bead(fILenBea, sIClaQua) -> RuleUnitResult:
        """ 용접비드 표면의 요철 품질
        Args:
        fILenBea (float): 비드길이
        sIClaQua (str): 품질관리 구분

        Returns:
        fOValIrr (float): 요철 허용 값
        """
        assert isinstance(fILenBea, float)
        assert fILenBea < 25
        assert isinstance(sIClaQua, str)
        assert sIClaQua in["나", "다", "라"]

        if fILenBea < 25:
          if sIClaQua == "나":
            fOValIrr = 4
          elif sIClaQua == "다":
            fOValIrr = 4
          elif sIClaQua == "라":
            fOValIrr = 3

        return RuleUnitResult(
                result_variables = {
                    "fOValIrr": fOValIrr
                }
            )