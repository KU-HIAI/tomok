import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031202_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.12.2 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '그루브 용접의 더돋기'

    description = """
    용접
    3. 시공
    3.12 결함부의 보수
    3.12.1 결함 종류 및 보수방법
    """

    content = """
    #### 3.12.1 결함 종류 및 보수방법
    (1) 그루브용접
    설계에서 마무리를 지정하지 않은 그루브용접을 하는 경우에는 표 3.12-2에 표시한 범위 내의 더돋기는 용접한 대로 두어도 좋다.
    다만 더돋기가 표 3.12-2의 값을 초과 할 때에는 비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다.
    표 3.12-2 그루브용접의 더돋기 허용값 (mm)
    \begin{table}[]
\begin{tabular}{lllll}
\multicolumn{1}{r}{\begin{tabular}[c]{@{}r@{}}품질관리 구분\\ 비드폭(B)\end{tabular}} & 가 & 나 & 다 & 라 \\
\textit{B<15} & 해당 없음. & 5 & 5 & 3 \\
15≤B<25 & 해당 없음. & 6 & 6 & 4 \\
\textit{B≥25} & 해당 없음. & 0.24B & 0.24B & 0.16B
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 그루브 용접의 더돋기"];
    B["KCS 14 31 20 3.12.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.12.2 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 그루브 용접의 더돋기"/];
    VarIn1[/입력변수: 그루브 용접의 더돋기/];
    VarIn2[/입력변수: 설계에서 마무리 지정/];
    VarIn3[/입력변수: 비드폭/];
    VarIn4[/입력변수: 품질관리 구분/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"설계에서 마무리 지정"}
		C --> |False|D{비드폭\n품질관리 구분}
    D --> |표 3.12-2|E[그루브용접의 더돋기 허용값]
		E --> F{ 그루브 용접의 더돋기 \n < 그루브용접의 더돋기 허용값}
		F --> |True|G[용접한 대로 두어도 좋다]
		F --> |False|H["비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다."]
		G & H --> End([그루브 용접의 더돋기])
    """

    @rule_method
    def Weld_Reinforcement_of_Groove_Weld(bIDesFin, fIWidBea, fIReiGro, sIClaQua) -> RuleUnitResult:
        """ 그루브 용접의 더돋기
        Args:
        bIDesFin (bool): 설계에서 마무리 지정
        fIWidBea (float): 비드폭
        fIReiGro (float): 그루브 용접의 더돋기
        sIClaQua (str): 품질관리 구분

        Returns:
        sOReiGro (str): 그루브 용접의 더돋기
        """
        assert isinstance(bIDesFin, bool)
        assert isinstance(fIWidBea, float)
        assert isinstance(fIReiGro, float)
        assert isinstance(sIClaQua, str)
        assert sIClaQua in["나", "다", "라"]

        if bIDesFin == False:
          if fIWidBea < 15:
            if sIClaQua == "나":
              if fIReiGro <= 5:
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
            elif sIClaQua == "다":
              if fIReiGro <= 5:
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
            elif sIClaQua == "라":
              if fIReiGro <= 3:
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"

          elif 15 <= fIWidBea < 25:
            if sIClaQua == "나":
              if fIReiGro <= 6:
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
            elif sIClaQua == "다":
              if fIReiGro <= 6:
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
            elif sIClaQua == "라":
              if fIReiGro <= 4:
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"

          elif fIWidBea >= 25:
            if sIClaQua == "나":
              if fIReiGro <= (0.24 * fIWidBea):
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
            elif sIClaQua == "다":
              if fIReiGro <= (0.24 * fIWidBea):
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
            elif sIClaQua == "라":
              if fIReiGro <= (0.16 * fIWidBea):
                sOReiGro = "용접한 대로 두어도 좋다"
              else:
                sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리해야 한다"
        else:
          sOReiGro = None

        return RuleUnitResult(
                result_variables = {
                    "sOReiGro": sOReiGro
                }
            )