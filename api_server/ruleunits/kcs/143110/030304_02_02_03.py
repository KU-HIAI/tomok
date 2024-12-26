import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_02_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ② 다'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '절단면 검사 및 결함보수'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (2)
    ②
    다
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ② 절단면의 보수는 보수된 강재가 적기에 사용될 수 있도록 부재 조립작업 전에 보수를 완료해야 하며 다음에 준하여 보수해야 한다.
    다. 가스 절단면의 직각도가 강판두께 20 mm 이하인 경우 1 mm 이하, 20 mm를 초과하는 경우에는 t/20(mm) 이하로서 이 규정치를 초과하는 부분은 그라인더로 다듬어 규정치 이내로 해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ② 다"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ② 다"])

    subgraph Variable_def
    VarOut3[/출력변수: 절단면 보수/];
    VarIn31[/입력변수: 가스절단면 직각도/];
    VarIn32[/입력변수: 강판 두께/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{가스 절단면의 직각도}
		C --> |"강판 두께 ≤ 20 mm"|Cf{가스 절단면의 직각도 ≤ 1 mm}
		C --> |"강판 두께 > 20 mm"|Cg{가스 절단면의 직각도 ≤ 강판두께/20}


		Cf & Cg --> Pass2([절단면 검사 및 결함보수])
    """

    @rule_method
    def Secondory_Member_of_Bridge(fIThiSte, fIPerCut) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        fIThiSte (float): 강판 두께
        fIPerCut (float): 가스절단면 직각도

        Returns:
        sOCutRep_2 (str): 절단면 보수
        """
        assert isinstance(fIThiSte, float)
        assert isinstance(fIPerCut, float)

        if fIThiSte <= 20:
          if fIPerCut <= 1:
            sOCutRep_2 = "Pass"
          else:
            sOCutRep_2 = "규정치를 초과하는 부분은 그라인더로 다듬어 규정치 이내로 해야한다."
        else:
          if fIPerCut <= (fIThiSte / 20):
            sOCutRep_2 = "Pass"
          else:
            sOCutRep_2 = "규정치를 초과하는 부분은 그라인더로 다듬어 규정치 이내로 해야한다."

        return RuleUnitResult(
           result_variables={
               "sOCutRep_2": sOCutRep_2,
           }
        )