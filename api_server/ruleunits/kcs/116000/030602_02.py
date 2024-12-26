import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_030602_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 3.6.2 (2)'
    ref_date = '2020-12-03'
    doc_date = '2023-10-06'
    title = '확인시험'

    description = """
    앵커
    3. 시공
    3.6 현장품질관리
    3.6.2 시험 일반
    (2)
    """

    content = """
    #### 3.6.2. 시험 일반
    (2) 확인시험
    ③ 시험의 방법은 특별히 정한 경우를 제외하고 다음과 같이 한다.
    가. 계획 최대시험하중은 설계하중의 1.2배로 한다.
    다. 재하 도중 계획 최대시험하중의 0.4배, 0.8배, 1.0배의 각 단계로 가압을 정지하고 변위가 안정될 때까지 하중을 유지한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 확인시험];
    B["KCS 11 60 00 3.6.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 3.6.2 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 계획 최대시험하중/];
    VarOut2[/출력변수: 가압 정지 단계의 하중/];
    VarOut3[/출력변수: 가압 정지시 준수사항/];
    VarIn1[/입력변수: 설계하중/];
    VarIn2[/입력변수: 계획 최대시험하중/];
    VarIn3[/입력변수: 하중단계/];
    end
    VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"계획 최대시험하중 >= 설계하중 * 1.2"}
    Variable_def --> C2{"가압 정지 단계의 하중 =
계획 최대시험하중 * 0.1 or 0.8 or 1.0"}
    C1--> D1["계획 최대시험하중"];
    C2--> D2["가압 정지 단계의 하중"];
    C2--> D3["가압을 정지하고 변위가
안정될 때까지 하중을 유지"];
    D2 & D3--> E2(["가압 정지 단계의 하중"]);
    D1--> E(["Pass/Fail"])
    """

    @rule_method
    def Design_Load(fIDesLoa, fIMaxLoa, sILoaSta) -> str:
        """확인시험
        Args:
            fIDesLoa (float): 설계하중
            fIMaxLoa (float): 계획 최대 시험하중
            sILoaSta (str): 하중 단계

        Returns:
            fOMaxLoa (float): 계획 최대 시험하중
            fOLoaHol (float): 가압 정지단계의 하중
            sOShuGui (str): 가압 정지시 준수사항
        """
        assert isinstance(fIDesLoa, float)
        assert isinstance(fIMaxLoa, float)
        assert isinstance(sILoaSta, str)
        assert sILoaSta in ["0.4단계", "0.8단계", "1.2단계"]

        if sILoaSta == "0.4단계":
          fOMaxLoa = 1.2 * fIDesLoa
          fOLoaHol = 0.4 * fIMaxLoa
          sOShuGui = "가압을 정지하고 변위가 안정될 때까지 하중을 유지"
        elif sILoaSta == "0.8단계":
          fOMaxLoa = 1.2 * fIDesLoa
          fOLoaHol = 0.8 * fIMaxLoa
          sOShuGui = "가압을 정지하고 변위가 안정될 때까지 하중을 유지"
        elif sILoaSta == "1.2단계":
          fOMaxLoa = 1.2 * fIDesLoa
          fOLoaHol = 1.2 * fIMaxLoa
          sOShuGui = "가압을 정지하고 변위가 안정될 때까지 하중을 유지"

        return RuleUnitResult(
            result_variables = {
                "fOMaxLoa": fOMaxLoa,
                "fOLoaHol": fOLoaHol,
                "sOShuGui": sOShuGui,
            }
          )