import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020312_01(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.12 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '회전 안정성'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 회전 안정성];
    B["KDS 24 90 11 4.2.3.12 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 총 수직변형/];
		VarIn2[/입력변수: 원형 받침의 유효직경/];
		VarIn3[/입력변수: 탄성받침의 너비 a를 가로지르는 회전각/];
		VarIn4[/입력변수: 탄성받침의 길이 b를 가로지르는 회전각/];
		VarIn5[/입력변수: a 방향 유효길이/];
		VarIn6[/입력변수: b 방향 유효길이/];
    VarIn1 & VarIn2
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4 & VarIn5 & VarIn6

    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.12 (1)"]) -->Variable_def;
		Variable_def--->G
		G{받침의 종류}
		G--직사각형 받침--->K
		G--원형 받침--->L
		K["\n <img src='https://latex.codecogs.com/svg.image? \sum_{i=1}^{n} v_{z,d} - \frac{a^{\prime} \cdot \alpha_{a,d} + b^{\prime} \cdot \alpha_{b,d}}{3} \geq 0'>-----------------------------"];
		L["\n <img src='https://latex.codecogs.com/svg.image? \sum_{i=1}^{n} v_{z,d} - \frac{D^{\prime} \cdot \alpha_{d}}{3} \geq 0'>-----------------------------"];
    K & L--->I
    I(["Pass or Fail"])
    """

    @rule_method
    def Square_Bearings(fIvzd, fIeffdia, fIalphaad, fIalphabd, fIa, fIb) -> RuleUnitResult:
        """직사각형 받침

        Args:
            fIvzd(float): 총 수직변형
            fID (float): 원형 받침의 직경
            fIalphaad (float): 탄성받침의 너비 a를 가로지르는 회전각
            fIalphabd (float): 탄성받침의 길이 b를 가로지르는 회전각
            fIa (float): a 방향 유효길이
            fIb (float): b 방향 유효길이

        Returns:
            pass_fail (bool): 실행함수의 판단 결과 4.2.3.12 (1) 각회전으로 인한 직사각형 받침의 값
        """
        assert isinstance(fIvzd, float)
        assert isinstance(fID, float)
        assert isinstance(fIalphaad, float)
        assert isinstance(fIalphabd, float)
        assert isinstance(fIa, float)
        assert isinstance(fIb, float)


        temp = sum(fIvzd[j] for j in range(i))

        if fIeffdia != 0:
          if temp-fIeffdia*fIalphaad/3 >= 0 :
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False
                }
            )

        else :
          if temp - (fIalphaad*fIa+fIalphabd*fIb)/3 >= 0:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True
                }
            )
          else:
             return RuleUnitResult(
                result_variables = {
                    "pass_fail": False
                }
            )