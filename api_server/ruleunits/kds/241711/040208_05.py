import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_040208_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.2.8 (5)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-13'
    title = '교량의 여유간격'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.8 설계변위
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 교량의 여유간격];
		B["KDS 24 17 11 4.2.8 (5)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 교량의 여유간격/];
		VarIn2[/입력변수: 가동받침의 이동량/];
		VarIn3[/입력변수: 지반에 대한 상부구조의 총 변위/];
		VarIn4[/입력변수: 콘크리트의 건조수축에 의한 이동량/];
		VarIn5[/입력변수: 콘크리트의 크리프에 의한 이동량/];
		VarIn6[/입력변수: 온도변화로 인한 이동량/];
		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ C(["KDS 24 17 11 4.2.8 (5)"])
		C --> Variable_def

		F{"<img src='https://latex.codecogs.com/png.image?\dpi{2000}\Delta&space;l_{i}\geq&space;d&plus;\Delta&space;l_{s}&plus;\Delta&space;l_{c}&plus;0.4\Delta&space;l_{t}'>----------------------------------------------------"};

		D{"<img src='https://latex.codecogs.com/png.image?\dpi{1000}\Delta&space;l_{i}>'>가동받침의 이동량"};

		E([PASS or Fail]);

		Variable_def --> F -- and --> D --> E
    """

    @rule_method
    def Bridge_Clearance(fIdelli,fImoamos,fId,fIdells,fIdellc,fIdellt) -> RuleUnitResult:
        """교량의 여유간격

        Args:
            fIdelli (float): 교량의 여유간격
            fImoamos (float): 가동받침의 이동량
            fId (float): 지반에 대한 상부구조의 총 변위
            fIdells (float): 콘크리트의 건조수축에 의한 이동량
            fIdellc (float): 콘크리트의 크리프에 의한 이동량
            fIdellt (float): 온도변화로 인한 이동량

        Returns:
            pass_fail (bool): 교량내진설계기준(한계상태설계법) 4.2.8 설계변위 (5) 교량의 여유간격의 판단 결과
        """

        assert isinstance(fIdelli, float)
        assert isinstance(fImoamos, float)
        assert isinstance(fId, float)
        assert isinstance(fIdells, float)
        assert isinstance(fIdellc, float)
        assert isinstance(fIdellt, float)

        if fIdelli >= fId + fIdells + fIdellc + 0.4*fIdellt and fIdelli > fImoamos:
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )