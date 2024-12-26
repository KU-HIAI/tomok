import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_030602_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 3.6.2 (5)'
    ref_date = '2020-12-03'
    doc_date = '2023-08-16'
    title = '리프트오프 시험'

    description = """
    앵커
    3. 시공
    3.6 현장품질관리
    3.6.2 시험 일반
    (5)
    """

    content = """
    #### 3.6.2.
    (5) 리프트오프(lift-off)시험
    ③ 인장재의 자유장은 압축형앵커에서는 인장재 전체 길이로 하며, 인장형앵커에서는 자유장 + 정착장/2으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 리프트오프 시험];
    B["KCS 11 60 00 3.6.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 3.6.2 (5)"])

    subgraph Variable_def
    VarOut1[/출력변수: 인장재의 자유장/];
    VarIn1[/입력변수: 앵커의 종류/];
    VarIn2[/입력변수: 인장재 전체 길이/];
    VarIn3[/입력변수: 자유장/];
    VarIn4[/입력변수: 정착장/];
    end
    VarOut1 & VarIn1 ~~~ VarIn2

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"앵커의 종류"}
    C1--> |"압축형앵커"|C2{"인장재의 자유장 = 인장재 전체 길이"};
    C1--> |"인장형앵커"|C3{"인장재의 자유장 = 자유장 + 정착장/2"};
    C2--> D1["인장재의 자유장"];
    C3--> D2["인장재의 자유장"];
    D1 & D2--> E1(["인장재의 자유장"])
    """

    @rule_method
    def Free_Length_of_Tensioning_Material(sITypAnc, fITotTen, fIFreLen, fISolLen) -> float:
        """ 리프트오프(lift-off) 시험
        Args:
        sITypAnc (str): 앵커의 종류
        fITotTen (float): 인장재 전체 길이
        fIFreLen (float): 자유장
        fISolLen (float): 정착장

        Returns:
        fOFreTen (float): 인장재의 자유장
        """
        assert isinstance(sITypAnc, str)
        assert sITypAnc in ["인장형앵커", "압축형앵커"]
        assert isinstance(fITotTen, float)
        assert isinstance(fIFreLen, float)
        assert isinstance(fISolLen, float)

        if sITypAnc == "인장형앵커":
            fOFreTen = fITotTen

        elif sITypAnc == "압축형앵커":
            fOFreTen = fIFreLen + 0.5 * fISolLen

        return RuleUnitResult(
            result_variables={
                "fOFreTen": fOFreTen
            }
        )