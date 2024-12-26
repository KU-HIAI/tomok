import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020310(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.10'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '각회전으로 인한 설계변형률'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.10 각회전으로 인한 설계변형률
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 각회전으로 인한 설계변형률];
    B["KDS 24 90 11 4.2.3.10"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 탄성받침의 너비 a를 가로지르는 회전각/];
		VarIn2[/입력변수: 탄성받침의 길이 b를 가로지르는 회전각/];
		VarIn3[/입력변수: 탄성중합체 각 층의 두께/];
		VarIn4[/입력변수: 탄성중합체 각 층의 가장 작은 두께/];
		VarOut1[/출력변수: 각회전으로 인한 설계변형률/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.10"]) --> Variable_def;
		Variable_def-->F--->I


    F["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{\alpha,d}=\frac{(a^{\prime2}\alpha&space;_{a,d}&plus;b^{\prime2}\alpha&space;_{b,d})t_{i}^{\prime}}{2\sum(t_{i}^{3})}'>--------------------------------------------------------"];

     I(["각회전으로 인한 설계변형률"])
    """

    @rule_method
    def Design_Strain_Due_To_Angular_Rotation(fIalphaad, fIalphabd, fIti, fItiprime) -> RuleUnitResult:
        """각회전으로 인한 설계변형률

        Args:
            fIalphaad (float): 탄성받침의 너비 a를 가로지르는 회전각
            fIalphabd (float): 탄성받침의 길이 b를 가로지르는 회전각
            fIti (float): 탄성중합체 각 층의 두께
            fItiprime (float): 탄성중합체 각 층의 가장 작은 두께

        Returns:
            fOepsilonalphad (float): 각회전으로 인한 설계변형률 4.2.3.9 각회전으로 인한 설계변형률의 값
        """
        assert isinstance(fOepsilonalphad, float)
        assert isinstance(fIalphaad, float)
        assert isinstance(fIalphabd, float)
        assert isinstance(fIti, float)
        assert fIti > 0
        assert isinstance(fItiprime, float)

        i = len(fIti)
        temp = sum(fIti[j]**3 for j in range(i))
        fOepsilonalphad = ((fIalphaad+fIalphabd)*fItiprime)/(2*temp)

        return RuleUnitResult(
            result_variables = {
                "fOepsilonalphad": fOepsilonalphad,

            }
        )