import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030703_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.7.3 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '말뚝의 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.7 콘크리트 널말뚝
    3.7.3 검사 및 허용오차
    (2)
    """

    # 건설기준문서내용(text)
    content = """
        ####3.7.3 검사 및 허용오차
        (2) 허용오차에 대하여는 3.4.2(17)의 요건에 따르며 널말뚝 마루높이에 대한 허용오차는 (±)50mm로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
        flowchart TD
        subgraph Python_Class
        A[Title: 말뚝의 허용오차];
        B["KCS 11 50 20 3.7.3 (2)"];
        B ~~~ A
        end

        KCS(["KCS 11 50 20 3.7.3 (2)"])

        subgraph Variable_def
        VarOut[/출력변수: 말뚝의 허용오차/];
        VarIn0[/입력변수: 널말뚝 마루높이/];
        VarIn1[/입력변수: 널말뚝 마루높이의 설계값/];
        VarIn2[/입력변수: 널말뚝 마루높이의 시공값/]
        VarOut ~~~ VarIn1 & VarIn2
        end

        Python_Class ~~~ KCS
        KCS --> Variable_def
        Variable_def --> C{말뚝의 허용오차}
        C-->|True|D{"|널말뚝 마루높이의 설계값-널말뚝 마루높이의 시공값| ≤ 50"}
        D --> |True|Pass([Pass])
        D --> |False|Fail([Fail])
        C --> |False|E["3.4.2(17)의 요건에 따른다"]
    """

    @rule_method
    def tolerance_pile(bIFloHei,fIDesHei, fIConHei):
        """
        Args:
            bIFloHei (boolean): 널말뚝 마루높이
            fIDesHei (float): 널말뚝 마루높이의 설계값
            fIConHei (float): 널말뚝 마루높이의 시공값
        Returns:
            sOTolPil (string): 말뚝의 허용오차
        """
        if bIFloHei:
            if abs(fIDesHei - fIConHei) <= 50:
                sOTolPil = "Pass"
            else:
                sOTolPil = "Fail"
        else:
            sOTolPil = "3.4.2(17)의 요건에 따른다"
        return sOTolPil