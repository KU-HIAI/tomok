import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244010_030302_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 3.3.2 (1)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '신축이음 설치시 유간'

    description = """
    신축이음
    3. 시공
    3.3 조정
    3.3.2 설치 시 유간 계산
    (1)
    """

    content = """
    #### 3.3.2 설치 시 유간 계산
    (1) 설치 시 신축이음의 유간() 계산은 다음 식을 따른다.
    \Delta l_{set} = \alpha \cdot (T_{max}-T_{set})\cdot L + \text{여유량}\quad\quad\quad(3.3-1)\\

\text{여기서, }\Delta l_{set} = \text{설치 시 유간(mm)} \\
\alpha = \text{선팽창계수}\\
T_{max} = \text{최고온도(℃)}\\
T_{set} = \text{설치 시 온도(℃)}\\
L = \text{신축길이(m)}\\
\text{여유량} = \text{※ KDS 24 90 10의 설계신축량의 여유량에 따른다. }

"""

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 신축이음 설치시 유간];
    B["KCS 24 40 10 3.2.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 3.2.2 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 설치 시 신축이음의 유간/];
    VarIn1[/입력변수: 선팽창계수/];
    VarIn2[/입력변수: 최고온도/];
    VarIn3[/입력변수: 설치 시 온도/];
    VarIn4[/입력변수: 신축길이/];
    VarIn5[/입력변수: 여유량/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{설치 시 신축이음의 유간계산}

    C --> D["설치 시 유간 = 선팽창계수*(최고온도-설치 시 온도)*신축길이 + 여유량"]
		D --> F([설치 시 신축이음의 유간])
    """

    @rule_method
    def expansion_joint_gap_construction(fICoeExp, fIMaxTem, fIInsTem, fIExpLen, fIAll) -> str :
        """신축이음 설치시 유간

        Args:
            fICoeExp (float): 선팽창계수
            fIMaxTem (float): 최고온도
            fIInsTem (float): 설치 시 온도
            fIExpLen (float): 신축길이
            fIAll (float): 여유량

        Returns:
            fOJoiGap (float) : 설치시 유간
        """
        assert isinstance(fICoeExp, float)
        assert isinstance(fIMaxTem, float)
        assert isinstance(fIInsTem, float)
        assert isinstance(fIExpLen, float)
        assert isinstance(fIAll, float)

        fOJoiGap = fICoeExp * (fIMaxTem-fIInsTem)*fIExpLen + fIAll

        return RuleUnitResult(
                result_variables = {
                    "fOJoiGap": fOJoiGap,
                }
            )