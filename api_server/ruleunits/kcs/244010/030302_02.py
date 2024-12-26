import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244010_030302_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 3.3.2 (2)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '제품의 유간 조정량'

    description = """
    신축이음
    3. 시공
    3.3 조정
    3.3.2 설치 시 유간 계산
    (2)
    """

    content = """
    #### 3.3.2 설치 시 유간 계산
    (2) 현장으로 반입된 신축이음장치는 (1)의 설치 시 유간을 확보하기 위해 다음 식만큼 유간을 조정하여 설치하여야 한다.
\Delta l_{cal} = \Delta l_{set} - \Delta l_{m}\quad\quad\quad(3.3-2)\\
\text{여기서, }\Delta l_{cal} = \text{제품의 유간 조정량(mm)}\\
\text{여기서, }\Delta l_{set} = \text{설치 시 유간(mm)}\\
\text{여기서, }\Delta l_{m} = \text{반입 시 제품의 유간(mm)}\\

"""

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 제품의 유간 조정량];
    B["KCS 24 40 10 3.3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 3.3.2 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 유간 조정량/];
    VarIn1[/입력변수: 선팽창계수/];
    VarIn2[/입력변수: 최고온도/];
    VarIn3[/입력변수: 설치 시 온도/];
    VarIn4[/입력변수: 신축길이/];
    VarIn5[/입력변수: 여유량/];
    VarIn6[/입력변수: 반입 시 제품의 유간/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5 & VarIn6
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C


    C["설치 시 유간 = 선팽창계수*(최고온도-설치 시 온도)*신축길이 + 여유량"]
    C --> D["<img src='https://latex.codecogs.com/png.image?\dpi{500} \Delta l_{cal} = \Delta l_{set} = \Delta l_{m}'>--------------------------------------------------------"];
		D --> F([유간 조정량 ])
    """

    @rule_method
    def joint_gap_during_installation(fICoeExp, fIMaxTem, fIInsTem, fIExpLen, fIAll, fIjoiEnt) -> str :
        """제품의 유간 조정량

        Args:
            fICoeExp (float): 선팽창계수. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            fIMaxTem (float): 최고온도
            fIInsTem (float): 설치 시 온도
            fIExpLen (float): 신축길이
            fIAll (float): 여유량
            fIjoiEnt (float): 반입 시 제품의 유간

        Returns:
            fOJoiAdj (float) : 유간 조정량
        """
        assert isinstance(fICoeExp, float)
        assert isinstance(fIMaxTem, float)
        assert isinstance(fIInsTem, float)
        assert isinstance(fIExpLen, float)
        assert isinstance(fIAll, float)
        assert isinstance(fIjoiEnt, float)

        fIJoiGap = fICoeExp * (fIMaxTem-fIInsTem)*fIExpLen + fIAll
        fOJoiAdj = fIJoiGap - fIjoiEnt

        return RuleUnitResult(
                result_variables = {
                    "fOJoiAdj": fOJoiAdj,
                }
            )