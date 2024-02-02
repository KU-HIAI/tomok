import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244010_0303_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 24 40 10 3.3 (1)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2018-08-30'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '	교량점검시설'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량점검시설
    3. 시공
    3.3 출입사다리
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3 출입사다리
    (1) 출입사다리 발판은 부재 또는 벽면에서 150 mm 떨어져 설치한다.

"""

    # 플로우차트(mermaid)
    flowchart = """
  flowchart TD
    subgraph Python_Class
    A["Title: 출입사다리 발판 설치"];
    B["KCS 24 40 30 3.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 30 3.3 (1)"])

    subgraph Variable_def
    VarOut[/"출력변수: 출입사다리 발판"/];
    VarIn1[/"입력변수: 출입사다리 발판"/];

    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"출입사다리 발판"}
		D --> E["부재 또는 벽면에서 150 mm 떨어져 설치한다."]
		E --> F([출입사다리 발판])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def access_ladder_steps(bILadSte) ->str :
        """출입사다리 발판

        Args:
            bILadSte (boolean): 출입사다리 발판. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당

        Returns:
            sOLadSte (string) : 출입사다리 발판
        """

        if bILadSte == True:
            sOLadSte = "부재 또는 벽면에서 150 mm 떨어져 설치한다."
            return sOLadSte