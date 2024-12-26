import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020306_02(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.6 (2)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '압축하중에 의한 설계변형률'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.6 설계원리
    (2)
    """
    content = """
    """
    flowchart = """
   flowchart TD
    subgraph Python_Class
    A[Title: 압축하중에 의한 설계변형률];
    B["KDS 24 90 11 4.2.3.6 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 압축설계하중에 의한 설계변형률/];
		VarIn2[/입력변수: 설계이동변위에 의한 설계전단변형률/];
		VarIn3[/입력변수: 설계각회전에 의한 설계변형률/];
		VarIn4[/입력변수: 하중종류에 따른 계수/];
		VarOut1[/출력변수: 최대설계변형률/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.6 (2)"]) --> Variable_def;
		Variable_def-->E
		E{"차량 활하중에 의해 계산되는 경우"}
		E--Yes--->F
		E--NO--->G
		F & G--->H--->I

    F["<img src='https://latex.codecogs.com/svg.image?K_{L}=1.5'>--------------------------------------------------------"];
		G["<img src='https://latex.codecogs.com/svg.image?K_{L}=1.0'>--------------------------------------------------------"];
		H["<img src='https://latex.codecogs.com/svg.image?\varepsilon_{t,d}=K_{L}(\varepsilon&space;_{c,d}&plus;\varepsilon&space;_{q,d}&plus;\varepsilon&space;_{\alpha,d})'>--------------------------------------------------------"];
		I(["최대설계변형률"])
    """

    @rule_method
    def Maximum_Design_Strain(fIepsiloncd, fIepsilonqd, fIepsilonalphad, fIKL) -> RuleUnitResult:
        """최대설계변형률

        Args:
            fIepsiloncd (float): 압축설계하중에 의한 설계변형률
            fIepsilonqd (float): 설계이동변위에 의한 설계전단변형률
            fIepsilonalphad (float): 설계각회전에 의한 설계변형률
            fIKL (float): 하중종류에 따른 계수

        Returns:
            fOmaxdst (float): 교량 기타시설설계기준(한계상태설계법)  4.2.3.6 설계원리(2)의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.1.4 조립 인장부재(2)의 통과여부
            sOdst (string): 교량 기타시설설계기준(한계상태설계법) 4.2.6.9 설계검증(2)의 판단 결과 2
        """

        assert isinstance(fIepsiloncd, float)
        assert isinstance(fIepsilonqd, float)
        assert isinstance(fIepsilonalphad, float)
        assert isinstance(fIKL, float)


        fOmaxdst = fIKL*(fIepsiloncd + fIepsilonqd + fIepsilonalphad)

        if fOmaxdst < 5:
          return RuleUnitResult(
             result_variables={
                  "fOmaxdst": fOmaxdst,
                  "pass_fail": True,
                   "sOdst": "사용한계상태 만족, 극한한계상태 만족",
             }
          )
        elif 5 < fOmaxdst < 7:
            return RuleUnitResult(
               result_variables={
                   "fOmaxdst": fOmaxdst,
                   "pass_fail": True,
                   "sOdst": "사용한계상태 불만족, 극한한계상태 만족",
               }
            )
        elif fOmaxdst >= 7:
            return RuleUnitResult(
               result_variables={
                   "fOmaxdst": fOmaxdst,
                   "pass_fail": False,
                   "sOdst": "사용한계상태 불만족, 극한한계상태 불만족",
               }
            )
        else:
          return RuleUnitResult(
             result_variables={
                  "fOmaxdst": fOmaxdst,
                  "pass_fail": False,
                  "sOdst": "사용한계상태 불만족, 극한한계상태 불만족",
             }
          )