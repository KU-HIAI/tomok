import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.2.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '보와 슬래브의 유효경간'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.2 구조물의 이상화
    1.5.2.2 기하학적 자료
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보와 슬래브의 유효경간];
    B["KDS 24 14 21 1.5.2.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut[/출력변수: 보와 슬래브의 유효경간/];
    VarIn1[/입력변수: 받침점 면 사이의 순경간/] ;
    VarIn2[/입력변수: 지지조건에 따라 정해지는 값/];

		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.2.2 (2)"])
		C --> Variable_def

		Variable_def-->E
		E["<img src='https://latex.codecogs.com/svg.image?&space;l_{eff}=l_{n}&plus;a_{1}&plus;a_{2}'>--------------------------------------------------------"];
	  E ~~~ |"KDS 24 14 21 Picture 1.5-1"| E
		D(["보와 슬래브의 유효경간"]);

    E--->D
    """

    @rule_method
    def Effective_spans_of_beams_and_slabs(fIln,fIa1,fIa2) -> RuleUnitResult:
        """보와 슬래브의 유효경간

        Args:
            fIln (float) : 받침점 면 사이의 순경간
            fIa1 (float) : 지지조건에 따라 정해지는 값
            fIa2 (float) : 지지조건에 따라 정해지는 값

        Returns:
            fOleff (float): 콘크리트교 설계기준 (한계상태설계법) 1.5.2.2 기하학적 자료 (2)의 값
        """

        assert isinstance(fIln, float)
        assert isinstance(fIa1, float)
        assert isinstance(fIa2, float)

        fOleff = fIln + fIa1 + fIa2

        return RuleUnitResult(
            result_variables = {
                "fOleff": fOleff,
            }
        )