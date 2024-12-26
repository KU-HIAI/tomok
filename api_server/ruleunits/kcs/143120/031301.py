import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031301(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.13.1'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법'

    description = """
    용접
    3. 시공
    3.13 변형교정
    3.13.1 강재의 표면온도
    """

    content = """
    #### 3.13.1 강재의 표면온도
    용접에 의해서 생긴 부재의 변형은 프레스나 가스화염 가열법 등에 의하여 교정할 수 있다. 가스화염 가열법에 의해 교정을 실시하는 경우의 강재 표면온도 및 냉각법은 표 3.13-1에 의한다.
    표 3.13-1 가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법
    \begin{table}[]
\begin{tabular}{llll}
\multicolumn{2}{l}{강재} & \begin{tabular}[c]{@{}l@{}}강재\\ 표면온도\end{tabular} & 냉각법 \\
\multicolumn{2}{l}{조질강(Q)} & 750 ℃이하 & 공냉 또는 공냉 후 600 ℃이하에서 수냉 \\
\multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}열가공제어강\\ (TMC, HSB)\end{tabular}} & Ceq>0.38 & 900 ℃이하 & 공냉 또는 공냉 후 500 ℃이하에서 수냉 \\
 & Ceq≤0.38 & 900 ℃이하 & 가열 직후 수냉 또는 공냉 \\
\multicolumn{2}{l}{기타강재} & 900 ℃이하 & 적열상태에서의 수냉은 피한다.
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법"];
    B["KCS 14 31 20 3.13.1"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.13.1"])

    subgraph Variable_def
    VarOut1[/"출력변수: 가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법"/];
    VarIn1[/입력변수: 강재/];
    VarIn2[/입력변수: 탄소당량/];
    VarIn3[/입력변수: 강재 표면온도/];
    VarIn4[/입력변수: 냉각법/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"강재 \n 탄소당량 \n 강재 표면온도 \n 냉각법"}
		C --> |표 3.13-1|D[가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법]
		D --> End([가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법])
    """

    @rule_method
    def Surface_Temperature_of_Steel(sISteel, fICeq, bISurTem, bICooMet) -> RuleUnitResult:
        """ 가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법
        Args:
        sISteel (str): 강재
        fICeq (float): 탄소당량
        bISurTem (bool): 강재 표면온도
        bICooMet (bool): 냉각법

        Returns:
        sOTemCoo (str): 가스화염법에 의한 선상가열시의 강재 표면온도 및 냉각법
        """
        assert isinstance(sISteel, str)
        assert sISteel in["조질강", "열가공제어강", "기타강재"]
        assert isinstance(fICeq, float)
        assert isinstance(bISurTem, bool)
        assert isinstance(bICooMet, bool)
        assert bISurTem != bICooMet

        if sISteel == "조질강":
          if bISurTem == True:
            sOTemCoo = "750 ℃이하"
          elif bICooMet == True:
            sOTemCoo = "공냉 또는 공냉 후 600 ℃이하에서 수냉"

        elif sISteel == "열가공제어강":
          if fICeq > 0.38:
            if bISurTem == True:
              sOTemCoo = "900 ℃이하"
            elif bICooMet == True:
              sOTemCoo = "공냉 또는 공냉 후 500 ℃이하에서 수냉"
          elif fICeq <= 0.38:
            if bISurTem == True:
              sOTemCoo = "900 ℃이하"
            elif bICooMet == True:
              sOTemCoo = "가열 직후 수냉 또는 공냉"

        elif sISteel == "기타강재":
          if bISurTem == True:
            sOTemCoo = "900 ℃이하"
          elif bICooMet == True:
            sOTemCoo = "적열상태에서의 수냉은 피한다."

        return RuleUnitResult(
                result_variables = {
                    "sOTemCoo": sOTemCoo
                }
            )