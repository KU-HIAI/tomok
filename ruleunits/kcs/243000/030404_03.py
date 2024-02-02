import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030404_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.4.4 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '콘크리트공'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.4 조립 및 설치
    3.4.4 시공
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####(3) 콘크리트공
    ① 콘크리트 품질은 설계기준 강도를 기준으로 하되 비합성인 경우 사용콘크리트 최소강도는 24 MPa 이상, 합성형인 경우 27 MPa 이상으로 하고, 목표 슬럼프치는 80 mm를 기준으로 하되 100 mm를 초과할 수 없다.
    ② 콘크리트 표면은 기복이 없이 면이 일정해야 하며 표면마무리 계획에 준하여 시공하여야 한다. 콘크리트 슬래브 두께의 허용오차는 최소 -10 mm, +20 mm 이내가 되어야 한다
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트공];
    B["KCS 24 30 00 3.5.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.5.4 (3)"])

    subgraph Variable_def
    subgraph V1
    VarOut[/출력변수: 콘크리트 품질/];
    VarIn1[/입력변수: 콘크리트 강도/];
    VarIn2[/입력변수: 합성형/];
    VarIn3[/입력변수: 비합성형/];
    VarIn4[/입력변수: 목표 슬럼프치/];
    end
    subgraph V2
    VarOut2[/출력변수: 콘크리트 구조물 품질/];
    VarIn5[/입력변수: 콘크리트 표면/];
    VarIn6[/입력변수: 콘크리트 슬래브 두께의 허용오차/];
    end
    end


    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"콘크리트 품질 \n 콘크리트 구조물 품질"}
    C --> |"콘크리트 품질"|D{"콘크리트 강도 \n 목표 슬럼프치"}
    C --> |"콘크리트 구조물 품질"|E{"콘크리트 표면 \n 콘크리트 슬래브 두께의 허용오차"}
    D --> |"콘크리트 강도"|F{합성형 \n 비합성형}
    F --> |"합성형"|G["설계기준 강도를 기준, 24 MPa 이상"]
    F --> |"비합성형"|H["설계기준 강도를 기준, 27 MPa 이상"]
    D --> |"목표 슬럼프치"|I[80 mm를 기준으로 하되 \n 100 mm를 초과할 수 없다]
    E --> |"콘크리트 표면"|J[기복이 없이 면이 일정해야 하며 \n 표면마무리 계획에 준하여 시공]
    E --> |"콘크리트 슬래브 두께의 허용오차"|K[최소 -10 mm, +20 mm 이내]
    G & H & I & J & K --> End([콘크리트공])
    """

    @rule_method
    def concrete_quality(bIStrCon,bIComTyp,bINonTyp,bITarSlu)-> str:
        """
        Args:
            bIStrCon (boolean): 사용콘크리트 최소강도
            bIComTyp (boolean): 합성형
            bINonTyp (boolean): 비합성형
            bITarSlu (boolean): 목표 슬럼프치
        Returns:
            sOConQua (string): 콘크리트 품질
        """
        if bIStrCon:
            if bIComTyp:
                sOConQua = "27MPa 이상"
            elif bINonTyp:
                sOConQua = "24MPa 이상"
            else:
                return "합성형, 비합성형 중에 선택하세요"
        elif bITarSlu:
            sOConQua = "80 mm를 기준으로 하되 100 mm를 초과할 수 없다"
        else:
            return "사용콘크리트 최소강도, 목표 슬럼프치 중에 선택해주세요"
        return sOConQua

    def concrete_structure_quality(self,bIConSur,bITolThi)-> str:
        """
        Args:
            bIConSur (boolean): 콘크리트 표면
            bITolThi (boolean): 콘크리트 슬래브 두께의 허용오차
        Returns:
            sOStrQua (string): 콘크리트 구조물품질
        """
        if bIConSur:
            sOStrQua = "기복이 없이 면이 일정해야 하며 표면마무리 계획에 준하여 시공"
        elif bITolThi:
            sOStrQua = "최소 -10 mm, +20 mm 이내"
        else:
            return "콘크리트 표면, 콘크리트 슬래브 두께의 허용오차 중에 선택하세요"
        return sOStrQua