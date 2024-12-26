import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020402_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.4.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '보정값'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.2 직접 처짐 계산을 생략하는 경우
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보정값];
    B["KDS 24 14 21 4.2.4.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 지지단의 철근 인장응력/];
		VarIn2[/입력변수: 철근 인장응력/];
		VarIn3[/입력변수: 사용하중에서 지간 중앙의 인장 철근응력/];
		VarIn4[/입력변수: 극한한계상태에서 중앙단면에 필요한 철근량/];
		VarIn5[/입력변수: 지간 중앙단면에 배치된 철근량/];
		VarOut1[/출력변수: 보정값/];

		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.4.2 (2)"])
		C --> Variable_def

		Variable_def--->D--->E--->G

		D{"지지단 철근 인장응력=310MPa 가정"}
		E["<img src='https://latex.codecogs.com/svg.image?\frac{310}{f_s}=\frac{500}{f_y(A_{s,req}/A_s)}'>---------------------------------"]

		G(["보정값"])
    """

    @rule_method
    def correction_value(fIfy,fIAsreq,fIAs) -> RuleUnitResult:
        """보정값

        Args:
            fIfy (float): 철근의 기준항복강도
            fIAsreq (float): 극한한계상태에서 중앙단면에 필요한 철근량
            fIAs (float): 지간 중앙단면에 배치된 철근량

        Returns:
            fOcorval (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.2 직접 처짐 계산을 생략하는 경우 (2)의 값
        """

        assert isinstance(fIfy, float)
        assert fIfy != 0
        assert isinstance(fIAsreq, float)
        assert fIAsreq != 0
        assert isinstance(fIAs, float)
        assert fIAs != 0

        fOcorval = 500 / (fIfy * fIAsreq / fIAs)

        return RuleUnitResult(
            result_variables = {
                "fOcorval": fOcorval,
            }
        )