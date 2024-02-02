import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030203_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.2.3 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '보조말뚝의 설치'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.2 시공준비
    3.2.3 안내보
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####3.2.3 안내보
    (2) 시공법선에 따라 보조말뚝을 2열로 박고 (10m 간격) 보조말뚝 내측에 보조버팀대를 내측 간격이 강널말뚝을 꽉 물린 상태보다 20mm~50mm의 여유를 주도록 설치한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보조말뚝의 설치];
    B["KCS 11 50 20 3.2.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.2.3 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 보조말뚝의 설치/];
    VarIn1[/입력변수: 보조말뚝의 열/];
    VarIn2[/입력변수: 보조말뚝의 간격/];
    VarIn3[/입력변수: 보조버팀대 내측 간격/];
    VarIn4[/입력변수: 강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"보조말뚝의 열 = 2"}
    C --> |"True"|D{"보조말뚝의 간격 = 10 m"}
    C --> |"False"|Fail([Fail])
    D --> |"True"|E{"강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격 + 20 mm \n < 보조버팀대 내측 간격 \n < 강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격 + 50 mm \n."}
    D --> |"False"|Fail([Fail])
    E --> |"True"|Pass([Pass])
    E --> |"False"|Fail([Fail])
"""

    @rule_method
    def supplementary_pile(nIRowPil, fIDisPil, fISpaStr_1, fISpaStr_2):
        """
        Args:
            nIRowPil (integer): 보조말뚝의 열
            fIDisPil (float): 보조말뚝의 간격
            fISpaStr_1 (float): 보조버팀대 내측 간격
            fISpaStr_2 (float): 강널말뚝을 꽉 물린 상태의 보조버팀대 내측 간격
        Returns:
            sOSupPil (string): 보조말뚝의 설치
        """
        if nIRowPil == 2:
            if fIDisPil == 10:
                if fISpaStr_1 > fISpaStr_2 + 20 and fISpaStr_1 < fISpaStr_2 + 50:
                    sOSupPil = "Pass"
                else:
                    sOSupPil = "Fail"
            else:
                sOSupPil = "Fail"
        else:
            sOSupPil= "Fail"
        return sOSupPil