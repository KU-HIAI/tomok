import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060602_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.2 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '소요 변위연성도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소요 변위연성도의 최댓값];
    B["KDS 24 17 11 4.6.6.2 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 소요 변위연성도/] ;
    VarOut2[/출력변수: 변위연성도-응답 수정계수 상관계수/] ;
    VarIn1[/입력변수: 소요 응답수정계수/] ;
    VarIn2[/입력변수: 1차 모드 주기/];
    VarIn3[/입력변수: 상한통제주기/];
		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.6.2 (4)"])
		C --> Variable_def

    Variable_def -->G{"소요 응답수정계수 1.0이상"}-->H
    D["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\triangle}=\lambda&space;_{DR}R_{req}'>---------------------------------------"]
		E(["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\triangle}'>---------"]);
    F["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{DR}=(1-\frac{1}{R_{req}})\frac{1.25T_{s}}{T}&plus;\frac{1}{R_{req}}'>-----------------------------------------------------------------"]
    H{"1차 모드 주기 < 상한통제주기 x1.25"}
    J(["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{DR}'>-----------"])

		H --Yes-->F-->J
    H--No-->K([1.0])-->J
		J-->D-->E
    """

    @rule_method
    def required_displacement_ductility(fIRreq,fIT,fITs) -> RuleUnitResult:
        """소요 변위연성도

        Args:
            fIRreq (float): 소요 응답수정계수
            fIT (float): 1차 모드 주기
            fITs (float): 상한통제주기

        Returns:
            fOmudelt (float): 교량내진설계기준(한계상태설계법) 4.6.6.2 소요연성도 (4)의 값 1
            fOlamDR (float): 교량내진설계기준(한계상태설계법) 4.6.6.2 소요연성도 (4)의 값 2
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.6.6.2 소요연성도 (4)의 판단 결과
        """

        assert isinstance(fIRreq, float)
        assert fIRreq > 0
        assert isinstance(fIT, float)
        assert fIT > 0
        assert isinstance(fITs, float)

        if fIRreq >= 1.0:
          if fIT < 1.25 * fITs:
            fOlamDR = (1 - 1 / fIRreq) * 1.25 * fITs / fIT + 1 / fIRreq
            fOmudelt = fOlamDR * fIRreq
            return RuleUnitResult(
                result_variables = {
                    "fOmudelt": fOmudelt,
                }
            )
          else:
            fOmudelt = 1.0 * fIRreq
            return RuleUnitResult(
                result_variables = {
                    "fOmudelt": fOmudelt,
                }
            )

        return RuleUnitResult(
            result_variables = {
                "pass_fail": False,
            }
        )