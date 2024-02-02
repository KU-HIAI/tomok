import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244010_030302_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 24 40 10 3.3.2 (1)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2018-08-30'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '신축이음'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    신축이음
    3. 시공
    3.3 조정
    3.3.2 설치 시 유간 계산
    (1)
    """

    # 건설기준문서내용(text)
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

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 신축이음 봉함재의 현장이음];
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

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def expansion_joint_gap_construction(fICoeExp, fIMaxTem, fIInsTem, fIExpLen, fIAll) ->str :
        """신축이음 설치시 유간

        Args:
            fICoeExp (float): 선팽창계수. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            fIMaxTem (float): 최고온도
            fIInsTem (float): 설치 시 온도
            fIExpLen (float): 신축길이
            fIAll (float): 여유량

        Returns:
            fIJoiGap (float) : 설치시 유간
        """

        fIJoiGap = fICoeExp * (fIMaxTem-fIInsTem)*fIExpLen + fIAll
        return fIJoiGap