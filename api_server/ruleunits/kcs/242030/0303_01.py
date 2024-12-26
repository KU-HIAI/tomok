import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS242030_0303_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 20 30 3.3 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-08-15'
    title = '배수구의 간격'

    description = """
    교량 하부 구조물
    3. 시공
    3.3 교각 코핑
    (1)
    """
    content = """
    #### 3.3 교각 코핑
    (1) 강제 파이프 서포트 또는 시스템 동바리 위에 합판 거푸집 또는 유로폼을 설치하는 경우에는 다음 사항을 준수하여야 한다.
    ① 동바리의 지점인 지반의 지지력을 검토하여 깔판, 깔목의 설치 또는 콘크리트 타설 등의 안전조치를 하여 동바리의 침하를 방지한다.
    ② 동바리의 수직도가 1/100 이내가 되도록 설치한다.
    ③ 거푸집을 설치하고 형틀을 수정보완 후 본 체결을 한다.
    ④ 추락재해를 방지하기 위하여 안전대 부착 설비 확보 및 착용 등 필요한 조치를 하여야한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 교각 코핑 동바리의 수직도];
    B["KCS 24 20 30 3.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 20 30 3.3 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 강재 파이프 서포트 또는 시스템 동바리 위에 합판 거푸집 또는 유로폼을 설치/];
    VarIn2[/입력변수: 동바리의 수직도/];
    VarIn1 ~~~ VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강제 파이프 서포트 또는 시스템 동바리 위에 \n 합판 거푸집 또는 유로품을 설치"}
    C --> |True|D{"동바리의 수직도 < 1/100"}
    D --> End([Pass or Fail])
    """

    @rule_method

    def degree_shore(bIPlyEur, fIVerSho) -> RuleUnitResult:
        """
        Args:
            bIPlyEur (bool): 강재 파이프 서포트 또는 시스템 동바리 위에 합판 거푸집 또는 유로폼을 설치
            fIVerSho (float): 동바리의 수직도

        Returns:
            pass_fail (bool): 교량 하부 구조물 3.3 교각 코핑 (1)의 판단 결과
        """
        assert isinstance(bIPlyEur, bool)
        assert isinstance(fIVerSho, float)
        assert bIPlyEur == True

        if bIPlyEur == True:
            if fIVerSho < 0.01:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })