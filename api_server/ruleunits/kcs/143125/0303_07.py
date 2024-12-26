import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143125_0303_07(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 31 25 3.3 (7)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.3 핀 및 롤러
    (7)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3 핀 및 롤러
    (7) 핀구멍이 있는 부분의 인장부재의 웨브 판두께는 인장부재 순폭의 1/8 이상이어야 한다.


    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 핀구멍이 있는 인장부재의 웨브 판두께];
    B["KCS 14 31 25 3.3 (7)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.3"])

    subgraph Variable_def
    VarIn1[/입력변수: 인장부재 순폭/];
    VarIn2[/입력변수: 핀구멍이 있는 인장부재의 웨브 판두께/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{핀구멍이 있는 인장부재의 웨브 판두께 >= 인장부재 순폭*1/8}
    C --> D(["Pass or Fail"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def web_plate_thickness_of_tension_member_with_pin_holes(fIWebThi, fIWidTen) -> RuleUnitResult:
        """핀구멍이 있는 부분의 인장부재의 웨브 판두께

        Args:
            fIWebThi (float): 핀구멍이 있는 부분의 인장부재의 웨브 판두께
            fIWidTen (float): 인장부재 순폭

        Returns:
            pass_fail (bool): 볼트 접합 및 핀 연결 3.3 핀 및 롤로 (7)의 판단 결과


        """
        assert isinstance(fIWebThi, float)
        assert isinstance(fIWidTen, float)

        if fIWebThi >= (fIWidTen)*1/8:
            pass_fail = True
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )
        else:
            pass_fail = False
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )