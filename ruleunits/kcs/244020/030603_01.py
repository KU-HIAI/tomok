import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_030603_01(RuleUnit): #KCS244020_030603_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 최정운'  # 작성자명
    ref_code = 'KCS 24 40 20 3.6.3 (1)' # 건설기준문서
    ref_date = '2016-06-30'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '도막식 방수재 시공 시 접착용 아스팔트의 용해'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.6 도막식 방수재의 시공
    3.6.3 고무아스팔트계의 도포
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 접착용 아스팔트의 용해 온도는 210 ℃ 정도이며, 전용 용제를 사용하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 접착용 아스팔트의 용해];
    B["KCS 24 40 20 3.6.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.6.3 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 접착용 아스팔트의 용해/];
    VarIn1[/입력변수: 용해 온도/];
    VarIn2[/입력변수: 전용 용해 가마/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용해 온도 = 210 ℃"}
    C --> |"True"|D{전용 용해 가마}
    C --> |"False"|Fail([Fail])
    D --> |"False"|Fail([Fail])
    D --> |"True"|Pass([Pass])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def melt_adhesive_asphalt(fIMelTem,bIDedKil)->str:
        """
        Args:
            fIMelTem (float): 용해 온도
            bIDedKil (boolean): 전용 용해 가마
        Returns:
            sOMelAsp (string): 접착용 아스팔트의 용해
        """
        if fIMelTem == 210:
            if bIDedKil == True:
                sOMelAsp = "Pass"
            else:
                sOMelAsp = "Fail"
        else:
            sOMelAsp = "Fail"
        return sOMelAsp