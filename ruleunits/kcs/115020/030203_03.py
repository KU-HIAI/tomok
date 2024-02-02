import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115020_030203_03(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 20 3.2.3 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-08-18'
    title = '안내보의 설치 높이'

    # 건설기준문서항목 (분류체계정보)
    description = """
    널말뚝
    3. 시공
    3.2 시공준비
    3.2.3 안내보
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    ####3.2.3 안내보
    (3) 안내보의 설치 높이는 강널말뚝의 타입을 완료했을 때 햄머가 안내보에 닿지 않도록 강널말뚝의 타입 목표 높이보다 300mm~500mm 정도 낮은 위치에 설치하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 안내보의 설치 높이];
    B["KCS 11 50 20 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.2.3 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 안내보의 설치 높이/];
    VarIn1[/입력변수: 안내보의 설치 높이/];
    VarIn2[/입력변수: 강널말뚝의 타입 목표 높이/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강널말뚝의 타입 목표 높이 - 500mm \n < 안내보의 설치 높이 \n < 강널말뚝의 타입 목표 높이 - 300mm\n."}
    C --> |"True"|Pass([Pass])
    C --> |"False"|Fail([Fail])
    """

    @rule_method
    def install_height(fIHeiGui, fIHeiPil):
        """
        Args:
            fIHeiGui (float): 안내보의 설치 높이
            fIHeiPil (float): 강널말뚝의 타입 목표 높이
        Returns:
            sOHeiGui (string): 안내보의 설치 높이
        """
        if fIHeiGui > fIHeiPil-500 and fIHeiGui < fIHeiPil-300:
            sOHeiGui = "Pass"
        else:
            sOHeiGui = "Fail"
        return sOHeiGui