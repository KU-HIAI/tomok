import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030304_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.3.4 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '플럭스 건조'

    description = """
    용접
    3. 시공
    3.3 용접준비
    3.3.4 현장품질관리
    """

    content = """
    #### 3.3.4 현장품질관리
    (2)플럭스
    ② 서브머지드아크용접용 플럭스의 건조는 표 3.3-3에 따른다.
    표 3.3-3 플럭스 건조
    \begin{table}[]
\begin{tabular}{
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l }
{\color[HTML]{333333} 플럭스 종류} & {\color[HTML]{333333} 건조온도}           & {\color[HTML]{333333} 건조시간}   \\
{\color[HTML]{333333} 용융플럭스}  & {\color[HTML]{333333} 150$\sim$200 ℃} & {\color[HTML]{333333} 1시간 이상} \\
{\color[HTML]{333333} 소결플럭스}  & {\color[HTML]{333333} 200$\sim$250 ℃} & {\color[HTML]{333333} 1시간 이상}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 플럭스 건조];
    B["KCS 14 31 20 3.3.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.3.4 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 플럭스 건조/];
    VarIn1[/입력변수: 건조 온도/];
    VarIn2[/입력변수: 건조 시간/];
    VarIn3[/입력변수: 플럭스 종류/];
		end
		VarOut1 ~~~  VarIn1 & VarIn2 & VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> E{"플럭스 종류"}
		E --> |용융플럭스|C{"건조 온도 \n 건조 시간"}
		E --> |소결플럭스|G{"건조 온도 \n 건조 시간"}
		C --> |건조 온도|H["150~200 ℃"]
		G --> |건조 온도|I["200~250 ℃"]
		C --> |건조 시간|J["1시간 이상"]
		G --> |건조 시간|K["1시간 이상"]
		H & I & J & K --> End([플럭스 건조])
    """

    @rule_method
    def Drying_Temperature(bIDryTem, bIDryPer, sITypFlu) -> str:
        """ 플럭스 건조
        Args:
        bIDryTem (bool): 건조 온도
        bIDryPer (bool): 건조 시간
        sITypFlu (str): 플럭스 종류

        Returns:
        sOFluDry (str): 플럭스 건조
        """
        assert isinstance(bIDryTem, bool)
        assert isinstance(bIDryPer, bool)
        assert bIDryTem != bIDryPer
        assert isinstance(sITypFlu, str)
        assert sITypFlu in["용융플럭스", "소결플럭스"]

        if sITypFlu == "용융플럭스":
          if bIDryTem == True:
            sOFluDry = "150~200 ℃"
          elif bIDryPer == True:
            sOFluDry = "1시간 이상"
        elif sITypFlu == "소결플럭스":
          if bIDryTem == True:
            sOFluDry = "200~250 ℃"
          elif bIDryPer == True:
            sOFluDry = "1시간 이상"

        return RuleUnitResult(
                result_variables = {
                    "sOFluDry": sOFluDry
                }
            )