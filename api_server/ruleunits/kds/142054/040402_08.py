import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040402_08(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.4.2 (8)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-13'
    title = '수정계수'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 수정계수];
    B["KDS 14 20 54 4.4.2 (8)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 수정계수/];
    VarIn1[/입력변수 : 앵커가 정착되는 부재 두께:앵커축과평행한 방향/];
    VarIn2[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.4.2 (8)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?h_{a}<1.5c_{a1}'>인 부재에 사용되는 앵커인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{h,V}=\sqrt{\frac{1.5c_{a1}}{h_{a}}}(\geq&space;1)'>------------------------------"];
    F(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{h,V}'>"]);
    Variable_def--->D--->E--->F
    """

    @rule_method
    def Correction_factor(fIha,fIcaone) -> RuleUnitResult:
        """수정계수

        Args:
            fIha (float): 앵커가 정착되는 부재 두께(앵커축과평행한방향)
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리

        Returns:
            fOpsihV (float): 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (8)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (8)의 판단 결과
        """

        assert isinstance(fIha, float)
        assert fIha > 0
        assert isinstance(fIcaone, float)
        assert fIcaone > 0

        if fIha < 1.5*fIcaone:
          fOpsihV = max((1.5 * fIcaone / fIha)**0.5, 1.0)
          return RuleUnitResult(
              result_variables = {
                  "fOpsihV": fOpsihV,
              }
          )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )