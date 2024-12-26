import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030402_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.4.2 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '볼트 구멍의 치수 및 허용오차'

    description = """
    제작
    3. 시공
    3.4 구멍뚫기
    3.4.2 볼트 구멍의 치수 및 정밀도
    (2)
    """

    content = """
    #### 3.4.2 볼트 구멍의 치수 및 정밀도
    (2) 볼트구멍의 직각도는 1/20 이하이어야 하며 볼트구멍의 허용오차는 표 3.4-1에 준한다. 그러나 마찰이음일 때에는 한 볼트군의 20%에 대하여 +1.0 mm까지 인정할 수 있다.
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                             & \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 허용 오차 (mm)}} \\
    \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 볼트의 호칭(mm)}} & {\color[HTML]{333333} 마찰이음}           & {\color[HTML]{333333} 지압이음}           \\
    {\color[HTML]{333333} M20} & {\color[HTML]{333333} +0.5} & {\color[HTML]{333333} ±0.3} \\
    {\color[HTML]{333333} M22} & {\color[HTML]{333333} +0.5} & {\color[HTML]{333333} ±0.3} \\
    {\color[HTML]{333333} M24} & {\color[HTML]{333333} +0.5} & {\color[HTML]{333333} ±0.3} \\
    {\color[HTML]{333333} M27} & {\color[HTML]{333333} +1.0} & {\color[HTML]{333333} ±0.3} \\
    {\color[HTML]{333333} M30} & {\color[HTML]{333333} +1.0} & {\color[HTML]{333333} ±0.3}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 볼트 구멍의 치수 및 허용오차];
    B["KCS 14 31 10 3.4.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.4.2 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 볼트구멍의 허용오차/];
    VarIn1[/입력변수: 마찰이음/];
    VarIn2[/입력변수: 지압이음/];
    VarIn3[/입력변수: 볼트구멍의 직각도/];
    VarIn4[/입력변수: 볼트의 호칭/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"볼트구멍의 직각도 \n 볼트구멍의 허용오차"}
		C --> |볼트구멍의 직각도|D{"볼트구멍의 직각도 ≤ 1/20"}
		D --> End1([Pass or Fail])
		C --> |볼트구멍의 허용오차|E{마찰이음, 지압이음}
		E --> |마찰이음|G{표 3.4-1}
		G --> |볼트호칭|J["볼트구멍의 허용오차, 한 볼트군의 20%에 대하여 +1.0 mm까지 인정"]
		E --> |지압이음|H{표 3.4-1}
		H --> |볼트호칭|I[볼트구멍의 허용오차]
		J & I --> End2([볼트구멍의 허용오차])
    """

    @rule_method
    def Perpendicularity_of_Bolt_Hole(fIPerBol, bIFriCon, bIBeaCon, sIBolSiz) -> str:
        """ 볼트 구멍의 치수 및 허용오차
        Args:
        fIPerBol (float): 볼트구멍의 직각도
        bIFriCon (bool): 마찰이음
        bIBeaCon (bool): 지압이음
        sIBolSiz (str): 볼트의 호칭

        Returns:
        pass_fail (bool): 제작 3.4.2 볼트 구멍의 치수 및 정밀도 (2)의 판단 결과
        sOTolBol (str): 볼트구멍의 허용오차
        """
        assert isinstance(fIPerBol, float)
        assert isinstance(bIFriCon, bool)
        assert isinstance(bIBeaCon, bool)
        assert bIFriCon != bIBeaCon
        assert isinstance(sIBolSiz, str)
        assert sIBolSiz in ["M20", "M22", "M24", "M27", "M30"]

        if fIPerBol <= 0.05:
          pass_fail = True
        else:
          pass_fail = False

        if sIBolSiz == "M20":
          if bIFriCon == True and bIBeaCon == False:
            sOTolBol = "허용오차는 +0.5, 한 볼트군의 20%에 대하여 +1.0mm까지 인정"
          elif bIFriCon == False and bIBeaCon == True:
            sOTolBol = "±0.3"

        elif sIBolSiz == "M22":
          if bIFriCon == True and bIBeaCon == False:
            sOTolBol = "허용오차는 +0.5, 한 볼트군의 20%에 대하여 +1.0mm까지 인정"
          elif bIFriCon == False and bIBeaCon == True:
            sOTolBol = "±0.3"

        elif sIBolSiz == "M24":
          if bIFriCon == True and bIBeaCon == False:
            sOTolBol = "허용오차는 +0.5, 한 볼트군의 20%에 대하여 +1.0mm까지 인정"
          elif bIFriCon == False and bIBeaCon == True:
            sOTolBol = "±0.3"

        elif sIBolSiz == "M27":
          if bIFriCon == True and bIBeaCon == False:
            sOTolBol = "허용오차는 +1.0, 한 볼트군의 20%에 대하여 +1.0mm까지 인정"
          elif bIFriCon == False and bIBeaCon == True:
            sOTolBol = "±0.3"

        elif sIBolSiz == "M30":
          if bIFriCon == True and bIBeaCon == False:
            sOTolBol = "허용오차는 +1.0, 한 볼트군의 20%에 대하여 +1.0mm까지 인정"
          elif bIFriCon == False and bIBeaCon == True:
            sOTolBol = "±0.3"

        return RuleUnitResult(
           result_variables={
               "pass_fail": pass_fail,
               "sOTolBol": sOTolBol,
           }
        )