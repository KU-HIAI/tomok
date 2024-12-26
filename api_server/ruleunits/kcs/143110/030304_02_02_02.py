import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_02_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ② 나'
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
    나
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ② 절단면의 보수는 보수된 강재가 적기에 사용될 수 있도록 부재 조립작업 전에 보수를 완료해야 하며 다음에 준하여 보수해야 한다.
    나. 가스절단면 노치 깊이가 1 mm를 초과하는 것은 그 부분을 덧살용접 후 그라인더로 마무리해야 한다. 다만 두께가 50 mm를 넘는 강판에 대해서는 원칙적으로 노치를 허용하지 않는다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ② 나"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ② 나"])

    subgraph Variable_def
    VarOut2[/출력변수: 절단면 보수/];
    VarIn21[/입력변수: 가스절단면 노치 깊이/];
    VarIn22[/입력변수: 강판 두께/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> CC{강판 두께 > 50 mm}
		CC --> |True|Cb[원칙적으로 노치를 허용하지 않는다.]
		CC --> |Fasle|Cc{가스절단면 노치 깊이 > 1mm}
		Cc --> |True|Cd[그 부분을 덧살용접 후 그라인더로 마무리해야 한다.]
		Cb &  Cd --> End2([절단면 보수])
    """

    @rule_method
    def Secondory_Member_of_Bridge(fINotDep_2, fIThiSte) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        fINotDep_2 (float): 가스절단면 노치 깊이
        fIThiSte (float): 강판 두께

        Returns:
        sOCutRep (str): 절단면 보수
        """
        assert isinstance(fINotDep_2, float)
        assert isinstance(fIThiSte, float)

        if fINotDep_2 > 1:
          if fIThiSte <= 50:
            sOCutRep = "가스절단면 노치 깊이가 1mm가 초과하는 부분을 덧살용접 후 그라인더로 마무리해야 한다."
          else:
            sOCutRep = "원칙적으로 노치를 허용하지 않는다."
        else:
          sOCutRep = None


        return RuleUnitResult(
           result_variables={
               "sOCutRep": sOCutRep
           }
        )