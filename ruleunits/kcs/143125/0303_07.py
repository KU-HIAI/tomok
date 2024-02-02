import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_0303_07(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 3.3 (7)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
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
    VarOut[/출력변수: /];
    VarIn1[/입력변수: 인장부재 순폭/];
    VarIn2[/입력변수: 핀구멍이 있는 인장부재의 웨브 판두께/];
    VarOut ~~~ VarIn11  & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{핀구멍이 있는 인장부재의 웨브 판두께 => 인장부재 순폭*1/8}
    C --> |True|D(["PASS"])
    C --> |False|E(["FAIL"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def web_plate_thickness_of_tension_member_with_pin_holes(fIWebThi, fIWidTen) ->str :
        """핀구멍이 있는 부분의 인장부재의 웨브 판두께

        Args:
            fIWebThi (float): 핀구멍이 있는 부분의 인장부재의 웨브 판두께
            fIWidTen (float): 인장부재 순폭

        Returns:
            sOWebThi (string): 핀구멍이 있는 부분의 인장부재의 웨브 판두께


        """

        if fIWebThi >= (fIWidTen)*1/8:
            sOWebThi = "PASS"
        else:
            sOWebThi = "FAIL"
        return sOWebThi