import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030401_02(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.4.1 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '말뚝 세우기'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.4 강널말뚝
    3.4.1 세우기
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####3.4.1 세우기
    (2) 말뚝 세우기에 앞서 말뚝 매기를 완전히 행하고 상향 속도를 10m/min 정도로 권양하여야 하며, 세우기가 완료된 때의 말뚝의 연직에 대한 기울기 허용오차는 말뚝길이의 1/100 이내가 되어야 한다
    """

    # 플로우차트(mermaid)
    flowchart = """
        flowchart TD
        subgraph Python_Class
        A[Title: 말뚝 세우기];
        B["KCS 11 50 20 3.4.1 (2)"];
        B ~~~ A
        end

        KCS(["KCS 11 50 20 3.4.1 (2)"])

        subgraph Variable_def
        VarOut[/출력변수: 말뚝 세우기/];
        VarIn1[/입력변수: 완전한 말뚝 매기/];
        VarIn2[/"입력변수: 10m/min 정도의 상향 속도"/];
        VarIn3[/"입력변수: 기울기 허용오차"/];
        VarIn4[/"입력변수: 말뚝 길이"/];
        VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
        end

        Python_Class ~~~ KCS
        KCS --> Variable_def
        Variable_def --> C{"완전한 말뚝 매기 \n 10m/min 정도의 상향 속도 \n 기울기 허용오차 < 말뚝길이/100 \n."}
        C --> |"True"|Pass([Pass])
        C --> |"False"|Fail([Fail])
    """

    @rule_method
    def pile_setup(bIPilDri, bIUpwVel,fIGraTol,fIPilLen):
        """
        Args:
            bIPilDri (boolean): 완전한 말뚝 매기
            bIUpwVel (boolean): 10m/min 정도의 상향 속도
            fIGraTol (float): 기울기 허용오차
            fIPilLen (float): 말뚝 길이
        Returns:
            sOPilSet (string): 말뚝 세우기
        """
        if bIPilDri == True and bIUpwVel == True and fIGraTol < fIPilLen/100:
            sOPilSet = "Pass"
        else:
            sOPilSet = "Fail"
        return sOPilSet