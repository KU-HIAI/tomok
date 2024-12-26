import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04040402_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.4.4.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '최소피복두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.4 내구성 및 피복두께
    4.4.4 콘크리트 피복두께
    4.4.4.2 최소피복두께
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소피복두께];
    B["KDS 24 14 21 4.4.4.2 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 부착에 대한 요구사항을 만족하는 최소피복두께/];
		VarIn2[/입력변수: 환경조건에 대한 요구사항을 만족하는 최소피복두께/];
		VarIn3[/입력변수: 고부식성 노출환경에서 피복두께 증가값/];
		VarIn4[/입력변수: 스테인레스 철근을 사용할 때 피복두께 감소값/];
		VarIn5[/입력변수: 코팅과 같은 추가 보호 조치를 취한 경우 피복두께 감소값/];

		VarOut1[/출력변수: 최소피복두께/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.4.4.2 (2)"])
		C --> Variable_def

		Variable_def--->D--->F
		D["<img src='https://latex.codecogs.com/svg.image?t_{c,min}=max[{t_{c,min,b},t_{c,min,dur}&plus;\Delta&space;t_{c,dur.\gamma}-\Delta&space;t_{c,dur,st}-\Delta&space;t_{c,dur,add},10mm}]'>---------------------------------"]

		F(["최소피복두께"])
    """

    @rule_method
    def minimum_cover_thickness(fItcminb,fItcmidu,fIdtcdug,fIdtcdus,fIdtcdua) -> RuleUnitResult:
        """최소피복두께

        Args:
            fItcminb (float): 부착에 대한 요구사항을 만족하는 최소피복두께
            fItcmidu (float): 환경조건에 대한 요구사항을 만족하는 최소피복두께
            fIdtcdug (float): 고부식성 노출환경에서 피복두께 증가값
            fIdtcdus (float): 스테인레스 철근을 사용할 때 피복두께 감소값
            fIdtcdua (float): 코팅과 같은 추가 보호 조치를 취한 경우 피복두께 감소값

        Returns:
            fOtcmin (float): 콘크리트교 설계기준 (한계상태설계법) 4.4.4.2 일반 사항 (2)의 값
        """

        assert isinstance(fItcminb, float)
        assert isinstance(fItcmidu, float)
        assert isinstance(fIdtcdug, float)
        assert isinstance(fIdtcdus, float)
        assert isinstance(fIdtcdua, float)

        fOtcmin = max(fItcminb, fItcmidu + fIdtcdug - fIdtcdus - fIdtcdua, 10)

        return RuleUnitResult(
            result_variables = {
                "fOtcmin": fOtcmin,
            }
        )