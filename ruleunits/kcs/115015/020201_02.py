import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115015_020201_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 50 15 2.2.1 (2)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2021-05-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '기성말뚝'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    기성말뚝
    2. 자재
    2.2 강관말뚝
    2.2.1 강관
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.9.3 검사용 튜브 설치
    (2) 강관말뚝은 이음이 없어야 하나 부득이한 경우 다음과 같이 이을 수 있으며, 이음하는 부분의 상세에 대하여는 시공 전 공사감독자의 승인을 받아야 한다.
    ① 신규말뚝으로 이음하는 경우 이음부분의 길이가 3.0 m 이상이어야 하며 이은 말뚝은 길이가 긴 부분이 말뚝의 끝단(머리)이 되게 타입하여야 하고, 시공 중 또는 시공 후 말뚝머리에서 이음이 필요한 경우에는 1.0 m 이상의 말뚝으로 이음할 수 있다.
    ② 타입후 지상에 돌출된 잉여말뚝을 산소로 절단한 재생말뚝(또는 재생 재사용 강관말뚝)으로 이음하는 경우, 이음길이가 5.0 m 이상이어야 한다.
    ③ 타입하지 않은 잉여말뚝을 절단하여 긴 말뚝에 용접하는 짧은 말뚝의 이음부분 길이(신규말뚝 또는 잉여 재사용 강관말뚝)는 3.0 m 이상이어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 강관 말뚝의 이음"];
    B["KCS 11 50 15 2.2.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 15 2.2.1 (2)"])

    subgraph Variable_def
    VarOut[/"출력변수: 강관 말뚝의 이음 길이"/];
		VarIn1[/"입력변수: 강관말뚝의 이음 길이"/];
		VarIn2[/"입력변수: 신규말뚝"/];
		VarIn7[/"입력변수: 재생말뚝"/];
		VarIn8[/"입력변수: 재생 재사용 강관말뚝"/];
		VarIn9[/"입력변수: 짧은말뚝"/];


    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~ VarIn5 & VarIn6 & VarIn7 & VarIn8 & VarIn9
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"강관말뚝 종류"}

		D --> |신규말뚝|E[이음길이 >= 3.0 m]
		D --> |재생말뚝 or \n재생 재사용 강관말뚝|F[이음길이 >= 5.0 m]
		D --> |짧은말뚝|G[이음길이 >= 3.0 m]

		E --> |True|H([PASS])
		F --> |True|H([PASS])
		G --> |True|H([PASS])

		E --> |False|J([FAI])
		F --> |False|J([FAIL])
		G --> |False|J([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def joint_length_of_steel_pipe_pile(bINewPil, bIRegPil, bIReuPil, bIShoPil) ->str :
        """강관말뚝의 이음

        Args:
            bINewPil (boolean): 신규말뚝. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            bIRegPil (boolean): 재생말뚝
            bIReuPil (boolean): 재생 재사용 강관말뚝
            bIShoPil (boolean): 짧은말뚝
            fOJoiLen (float): 강관말뚝의 이음 길이

        Returns:
            sOJoiLen (string) : 강관말뚝의 이음 길이
        """

        if bINewPil == True:
            if fOJoiLen >= 3.0:
                sOJoiLen = "PASS"
                return sOJoiLen
            else:
                sOJoiLen = "FAIL"
                return sOJoiLen
        elif (bIRegPil == True) or (bIReuPil == True):
            if fOJoiLen >= 5.0:
                sOJoiLen = "PASS"
                return sOJoiLen
            else:
                sOJoiLen = "FAIL"
                return sOJoiLen
        elif bIShoPil == True:
            if fOJoiLen >= 3.0:
                sOJoiLen = "PASS"
                return sOJoiLen
            else:
                sOJoiLen = "FAIL"
                return sOJoiLen