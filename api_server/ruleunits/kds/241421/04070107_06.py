import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070107_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.1.7 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '단순 받침부의 공칭길이'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.1 프리캐스트 콘크리트 구조물의 일반사항
    4.7.1.7 프리캐스트 요소의 받침부 지압판
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단순 받침부의 공칭길이];
    B["KDS 24 14 21 4.7.1.7 (6)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:받침점 반력/];
		VarIn2[/입력변수:받침부의 순 폭/];
		VarIn3[/입력변수:설계지압강도/];
		VarIn4[/입력변수:지지하는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리/];
		VarIn5[/입력변수:지지되는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리/];
		VarIn6[/입력변수: 지지하는 부재사이의 간격에 대한 오차의 허용값/];
		VarIn7[/입력변수:부재길이/];

		VarOut1[/출력변수:단순 받침부의 공칭길이/];
		VarOut2[/출력변수:지압응력을 고려한 순 지압판 길이/];
		VarOut3[/출력변수:부재 길이/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~~VarIn4 & VarIn5 & VarIn6
		VarIn5~~~~VarIn7
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.1.7 (6)"])
		C --> Variable_def

		Variable_def--->E & D

		D["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;a_1=F_u/(b_1f_d)'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\Delta&space;a_3=l_n/2500'>---------------------------------"]
		D & E--->F--->G
		F["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;a=a_1&plus;a_2&plus;a_3&plus;\sqrt{\Delta&space;a_2^2&plus;\Delta&space;a_3^2}'>---------------------------------"]
		G(["단순 받침부의 공칭길이"])
    """

    @rule_method
    def Nominal_Length_of_Simple_Support(fIFu,fIb1,fIfd,fIa2,fIa3,fIdela2,fIln) -> RuleUnitResult:
        """단순 받침부의 공칭길이

        Args:
            fIFu (float): 받침점 반력
            fIb1 (float): 받침부의 순 폭
            fIfd (float): 설계지압강도
            fIa2 (float): 지지하는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리
            fIa3 (float): 지지되는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리
            fIdela2 (float): 지지하는 부재사이의 간격에 대한 오차의 허용값
            fIln (float): 부재길이

        Returns:
            fOa (float):  콘크리트교 설계기준 (한계상태설계법)  4.7.1.7 프리캐스트 요소의 받침부 지압판 (6)의 값 1
            fOa1 (float):  콘크리트교 설계기준 (한계상태설계법)  4.7.1.7 프리캐스트 요소의 받침부 지압판 (6)의 값 2
            fOdela3 (float):  콘크리트교 설계기준 (한계상태설계법)  4.7.1.7 프리캐스트 요소의 받침부 지압판 (6)의 값 3
        """

        assert isinstance(fIFu, float)
        assert isinstance(fIb1, float)
        assert fIb1 != 0
        assert isinstance(fIfd, float)
        assert fIfd != 0
        assert isinstance(fIa2, float)
        assert isinstance(fIa3, float)
        assert isinstance(fIdela2, float)
        assert isinstance(fIln, float)

        import math

        fOa1 = fIFu/(fIb1*fIfd)

        fOdela3 = fIln/2500

        fOa = fOa1 + fIa2 + fIa3 + (fIdela2**2 + fOdela3**2)**0.5

        return RuleUnitResult(
            result_variables = {
                "fOa": fOa,
            }
        )