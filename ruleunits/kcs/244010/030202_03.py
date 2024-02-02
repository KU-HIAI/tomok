import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244010_030202_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 24 40 10 3.2.2 (8)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2018-08-30'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '신축이음'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    신축이음
    3. 시공
    3.2 조립
    3.2.2 조립 시 주의사항
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.2 조립 시 주의사항
    (3) 길이 18 m 이하로 조립된 신축이음 봉함재는 중간에 현장이음이 없이 반입되어야 한다.
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
    VarOut[/출력변수: 신축이음 조립 시 주의사항/];
    VarIn1[/입력변수: 조립된 신축이음 봉합재의 길이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{조립된 신축이음 봉합재의 길이 <=18}

    C --> |True|D["중간에 현장이음이 없이 반입되어야 한다."]
		D --> F([신축이음 조립 시 주의사항])


    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def on_site_joint_sealant(fILenSea) ->str :
        """신축이음 봉함재의 현장이음

        Args:
            fILenSea (float): 조립된 신축이음 봉함재의 길이. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당


        Returns:
            sOJoiSea (string) : 신축이음 봉함재의 현장이음
        """

        if fILenSea <= 18:
            sOJoiSea = "중간에 현장이음이 없이 반입되어야 한다."
            return sOJoiSea
        else:
            return None