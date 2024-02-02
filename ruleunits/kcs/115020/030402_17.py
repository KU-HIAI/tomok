import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030402_17(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.4.2 (13)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '말뚝의 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.4 강널말뚝
    3.4.2 강널말뚝 항타
    (17)
    """

    # 건설기준문서내용(text)
    content = """
        ####
        (17) 말뚝이 소정의 위치, 방향, 높이, 기울기 및 법선 등에 대하여 설계도면에서 규정하고 있는 대로 시공되었는지를 확인하여야 하며, 허용오차는 다음과 같다.
        ① 벽체 길이: (+) 널말뚝 1매 폭, (−) 없음
        ② 법선에 대한 굴곡: (±)100㎜
        ③ 법선에 대한 기울기(횡방향): 1/75 이하
        ④ 법선 방향의 기울기(종방향): (시공 중) 아래 위의 차가 널말뚝 1매 폭 이하, (완료 후) 1/75 이하
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝의 허용오차];
    B["KCS 11 50 20 3.4.2 (17)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.4.2 (17)"])

    subgraph Variable_def
    VarOut[/출력변수: 말뚝의 허용오차/];
    VarIn1[/입력변수: 벽체 길이/];
    VarIn2[/입력변수: 법선에 대한 굴곡/];
    VarIn3[/"입력변수: 법선에 대한 기울기(횡방향)"/];
    VarIn4[/"입력변수: 법선 방향의 기울기(종방향)"/];
    VarIn5[/입력변수: 시공 중/];
    VarIn6[/입력변수: 완료 후/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn1 ~~~ VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"벽체 길이, \n 법선에 대한 굴곡, \n 법선에 대한 기울기(횡방향), \n 법선 방향의 기울기(종방향)"}
    C --> |"벽체 길이"|D["(+) 널말뚝 1매 폭, (−) 없음"]
    C --> |"법선에 대한 굴곡"|E["(±)100㎜"]
    C --> |"법선에 대한 기울기(횡방향)"|F["1/75 이하"]
    C --> |"법선 방향의 기울기(종방향)"|G{"시공 중 \n 완료 후"}
    G --> |"시공 중"|H["아래 위의 차가 널말뚝 1매 폭 이하"]
    G --> |"완료 후"|I["1/75 이하"]
    D & E & F & H & I --> End([말뚝의 허용오차])
    """

    @rule_method
    def tolerance_pile(bIWalLen,bICurNor,bISloTra,bISloLon,bIDurCon, bIAftCon)->str:
        """
        Args:
            bIWalLen (boolean): 벽체 길이
            bICurNor (boolean): 법선에 대한 굴곡
            bISloTra (boolean): 법선에 대한 횡방향 기울기
            bISloLon (boolean): 법선 방향의 종방향 기울기
            bIDurCon (boolean): 시공 중
            bIAftCon (boolean): 완료 후
        Returns:
            sOTolPil (string): 말뚝의 허용오차
        """
        if bIWalLen:
            sOTolPil = "(+) 널말뚝 1매 폭, (−) 없음"
        elif bICurNor:
            sOTolPil = "(±)100㎜"
        elif bISloTra:
            sOTolPil = "1/75 이하"
        elif bISloLon:
            if bIDurCon:
                sOTolPil = "아래 위의 차가 널말뚝 1매 폭 이하"
            else:
                sOTolPil = "1/75 이하"
        return sOTolPil