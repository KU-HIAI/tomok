import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0303_06(RuleUnit): #KCS244020_0303_06

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 최정운'  # 작성자명
    ref_code = 'KCS 24 40 20 3.3 (6)' # 건설기준문서
    ref_date = '2016-06-30'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '표준 양생시간'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.3 접착층의 시공
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### (6) 양생시간은 고무아스팔트계 및 합성고무계는 20 ℃에서 1시간 정도, 5 ℃에서 2시간 정도이고, 수지계는 20 ℃에서 15분 이내, 5 ℃에서 30분 이내를 표준으로 하며, 접착제의 종류⋅기온⋅바람⋅지촉건조시간 등을 고려하여 결정한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표준 양생시간];
    B["KCS 24 40 20 3.3 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.3 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 표준 양생시간/];
    VarIn1[/입력변수: 고무아스팔트계/];
    VarIn2[/입력변수: 합성고무계/];
    VarIn3[/입력변수: 수지계/];
    VarIn4[/입력변수: 기온/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{수지계, 고무아스팔트계, 합성고무계}
    C --> |고무아스팔트계, 합성고무계|D{기온}
    D --> |"20℃"|E[60분]
    D --> |"5℃"|F[120분]
    C --> |수지계|G{기온}
    G --> |"20℃"|H[ 15분]
    G --> |"5℃"|I[30분]
    E & F & H & I --> End([표준 양생시간])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def curing_time(bIRubAsp, bISynRub,bIRes,nITem)->float:
        """
        Args:
            bIRubAsp (boolean): 고무아스팔트계
            bISynRub (boolean): 합성고무계
            bIRes (boolean): 수지계
            nITem (integar): 기온
        Returns:
            fOCurTim (float)): 표준양생시간
        """
        if bIRubAsp == True or bISynRub == True:
            if nITem == 20:
                fOCurTim = 60
            elif nITem == 5:
                fOCurTim = 120
        elif bIRes:
            if nITem == 20:
                fOCurTim = 15
            elif nITem == 5:
                fOCurTim = 60
        return fOCurTim