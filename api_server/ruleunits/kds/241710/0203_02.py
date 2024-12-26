import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_0203_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '탄성지진응답계수'

    description = """
    교량 내진설계기준(일반설계법)
    2. 설계
    2.3 해석방법
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 탄성지진응답계수]
	  B["KDS 24 17 10 2.3 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarOut1[/출력변수:탄성지진응답계수/]
		VarIn1[/입력변수:가속도계수/]
		VarIn2[/입력변수:상세예측법을 통해 획득한 안전율/]
		VarIn3[/입력변수:지반 특성에 대한 무차원의 계수/]
		VarIn4[/입력변수:교량의 주기/]
		VarIn5[/입력변수:교량의 주기/]

		VarOut1 ~~~
		VarIn1 & VarIn2 ~~~
		VarIn3 & VarIn4 & VarIn5

    end

	  Python_Class ~~~ C(["KDS 24 17 10 2.3 (2)"])
		C --> Variable_def


	  J["<img src='https://latex.codecogs.com/svg.image?C_{s}=\frac{1.2AS}{T^{\frac{2}{3}}}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?C_{sm}=\frac{1.2AS}{T_{m}^{\frac{2}{3}}}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?C_{sm}=\frac{3AS}{T_{m}^{\frac{4}{3}}}'>---------------------------------"]
		F([탄성지진응답계수])
		G([탄성지진응답계수])
		H{교량의 주기 ≥ 4.0}
		I{탄성지지응답계수 ≤ 2.5}

		Variable_def ---> J ---> F
		Variable_def ---> H -- Yes ---> E ---> G
		H -- No ---> I ---> D ---> G
    """

    @rule_method
    def Elastic_seismic_response_coefficient(fIA,fIS,fIT,fITm) -> RuleUnitResult:
        """탄성지진응답계수

        Args:
            fIA (float): 가속도계수
            fIS (float): 지반 특성에 대한 무차원의 계수
            fIT (float): 교량의 주기
            fITm (float): m번째 진동모드에 대한 교량의 주기

        Returns:
            fOCs (float): 교량 내진설계기준(일반설계법)  2.3 해석방법 (2)의 값 1
            fOCsm (float): 교량 내진설계기준(일반설계법)  2.3 해석방법 (2)의 값 2
        """

        assert isinstance(fIA, float)
        assert isinstance(fIS, float)
        assert isinstance(fIT, float)
        assert fIT > 0
        assert isinstance(fITm, float)
        assert fITm > 0

        fOCs = min(1.2 * fIA * fIS / (fIT**(2/3)), 2.5 * fIA)

        if fITm > 4 :
          fOCsm = 3 * fIA * fIS / (fITm**(4/3))
        else:
          fOCsm = min(1.2 * fIA * fIS / (fITm**(2/3)), 2.5 * fIA)

        return RuleUnitResult(
            result_variables = {
                "fOCs": fOCs,
                "fOCsm": fOCsm,
            }
        )