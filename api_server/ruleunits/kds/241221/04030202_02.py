import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030202_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.2.2 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '차로 당 통행비율'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.2 피로하중
    4.3.2.2 빈도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 차로 당 통행비율];
    B["KDS 24 12 21 4.3.2.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 한 방향 한차로의 일일트럭교통량의 설계수명기간동안 평균값/];
    VarIn1[/입력변수 : 한 방향 일일트럭교통량의 설계수명기간동안 평균값/];
    VarIn2[/입력변수 : p/];
    VarIn3[/입력변수 : 트럭이 통행가능한 차로 수/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.3.2.2 (2)"])
		C --> Variable_def

    J{"단일차로의 일평균 트럭교통량에 대한 확실한 정보가 없을 때"};
    D{"트럭이 통행 가능한 차로 수"};
    E["p=1.00"];
    F["p=0.85"];
    G["p=0.80"];
    H["<img src='https://latex.codecogs.com/svg.image? ADTT_{SL} = P X ADTT'>---------------"]

    I(["한 방향 한 차로의 일일트럭교통량의 설계수명기간동안 평균값"]);
    Variable_def--->J--->D--1차로--->E--->H--->I
    D--2차로--->F--->H
    D--3차로 이상--->G--->H
    """

    @rule_method
    def Percentage_of_traffic_per_lane(fIADTT,fIp) -> RuleUnitResult:
        """차로 당 통행비율

        Args:
            fIADTT (float): 한 방향 일일트럭교통량의 설계수명기간동안 평균값
            fIp (float): 표 4.3-3의 값

        Returns:
            fOADTTSL (float): 강교 설계기준(한계상태설계법)  4.3.2.2 빈도 (2)의 값
        """

        assert isinstance(fIADTT, float)
        assert isinstance(fIp, float)

        fOADTTSL = fIp * fIADTT

        return RuleUnitResult(
            result_variables = {
                "fOADTTSL": fOADTTSL,
            }
        )