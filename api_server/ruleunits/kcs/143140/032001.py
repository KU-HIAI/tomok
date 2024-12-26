import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_032001(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.20.1'
    ref_date = '2019-05-20'
    doc_date = '2023-10-31'
    title = '이론도포율 산출방법'

    description = """
    도장
    3. 시공
    3.20 도료소요량의 산출방법
    3.20.1 이론도포율 산출방법
    """

    content = """
    #### 3.20.1 이론도포율 산출방법
    \text { 이론도포율 }\left(\mathrm{m}^2 / l\right)=\frac{\text { 고형분용적비 }(\%) \times 10}{\text { 요구하는D.F.T }(\mu)}
    """

    flowchart = """
    flowchart TD
        subgraph Python_Class
        A[Title: 이론 도포율 산출방법];
        B["KCS 14 31 40 3.20.1"];
        B ~~~ A
        end

        KCS(["KCS 14 31 40 3.20.1"])

        subgraph Variable_def
        VarOut1[/출력변수: 이론 도포율/];
        VarIn1[/입력변수: 고형분 용적비/];
        VarIn2[/입력변수: 요구하는 D.F.T/];
    		VarOut1 ~~~ VarIn1 & VarIn2
    		end

        Python_Class ~~~ KCS
        KCS --> Variable_def
    		Variable_def --> C["이론도포율 = 고형분 용적비*10/요구하는 D.F.T"]
		    C --> End([이론 도포율])
    """

    @rule_method
    def Solid_Volume_Ratio(fISolVRa, fIDFT) -> float:
        """ 이론도포율 산출방법
        Args:
        fISolVRa (float): 고형분 용적비
        fIDFT (float): 요구하는 D.F.T

        Returns:
        fOTheSpr (float): 이론 도포율
        """
        assert isinstance(fISolVRa, float)
        assert isinstance(fIDFT, float)
        assert fIDFT > 0

        fOTheSpr = (fISolVRa * 10) / fIDFT

        return RuleUnitResult(
                result_variables = {
                    "fOTheSpr": fOTheSpr
                }
            )