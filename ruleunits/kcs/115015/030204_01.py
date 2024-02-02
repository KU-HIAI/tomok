import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115015_030204_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 11 50 15 3.2.4 (1)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2021-05-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '기성말뚝'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    기성말뚝
    3. 시공
    3.2 시공준비
    3.2.4 말뚝 세우기
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.2.4 말뚝 세우기
    (1) 말뚝은 설계도서 및 시공계획서에 따라 정확하고 안전하게 세워야 한다.
    ③ 말뚝의 연직도나 경사도는 1/50 이내로 하고, 말뚝박기 후 평면상의 위치가 설계도면의 위치로부터 D/4(D는 말뚝의 바깥지름)와 100 ㎜ 중 큰 값 이상으로 벗어나지 않아야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 말뚝세우기 시공 조건"];
    B["KCS 11 50 15 3.2.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 15 3.2.4 (1)"])

    subgraph Variable_def
    VarOut[/"출력변수: 말뚝세우기 시공 조건"/];
		VarIn1[/"입력변수: 말뚝 연직도"/];
		VarIn2[/"입력변수: 말뚝 경사도"/];
		VarIn3[/"입력변수: 평면상의 위치"/];
		VarIn4[/"입력변수: 설계도면의 위치"/];
		VarIn5[/"입력변수: 말뚝의 바깥지름(D)"/];


    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"말뚝세우기 시공 조건"}

		D --> |말뚝의 연직도|E[말뚝의 연직도 < 1/50]
		D --> |말뚝의 경사도|F[말뚝의 경사도 < 1/50]
		D --> |평면상의 위치|G["(평면상의 위치-설계도면의 위치) < \n min((D/4), 100 mm)"]

		E --> |True|K([PASS])
		F --> |True|K([PASS])

		E --> |False|J([FAIL])
		F --> |False|J([FAIL])

		G --> |True|K([PASS])
		G --> |False|J([FAIL])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def pile_erection_construction_conditions(fIVerPil, fIPilInc, fIPosPla, fIPosDra, fID) ->str :
        """말뚝세우기 시공 조건

        Args:
            fIVerPil (float): 말뚝 연직도. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            fIPilInc (float): 말뚝 경사도
            fIPosPla (float): 평면상의 위치
            fIPosDra (float): 설계도면의 위치
            fID (float): 말뚝의 바깥지름(D)


        Returns:
            sOEreCon (string) : 말뚝세우기 시공 조건
        """

        if fIVerPil > 1/50:
            sOEreCon = "FAIL"
            return sOEreCon
        elif fIPilInc > 1/50:
            sOEreCon = "FAIL"
            return sOEreCon
        elif abs(fIPosPla-fIPosDra) > max(fID/4, 100):
            sOEreCon = "FAIL"
            return sOEreCon
        else:
            sOEreCon = "PASS"
            return sOEreCon