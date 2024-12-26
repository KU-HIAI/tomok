import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030302_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.2 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '가스절단 및 가스가공한 강판의 허용오차'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.2 강재절단
    (1)
    """

    content = """
    #### 3.3.2 강재절단
    (1) 가스절단을 하는 경우, 원칙적으로 자동가스절단기를 이용한다. 가스절단 및 가스가공한 강판의 허용오차는 KS B 0428 또는 해당 공사시방서에 따른다.
    다만 해당 공사시방서에 정한 바가 없는 경우에는 표 3.3-1에 따르는 것을 원칙으로 한다.
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}품질관리구분\\ 항 목\end{tabular}} &
      {\color[HTML]{333333} 가} &
      {\color[HTML]{333333} 나} &
      {\color[HTML]{333333} 다} &
      {\color[HTML]{333333} 라} \\
    {\color[HTML]{333333} 표면거칠기1)} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}200S 이하\\ (100S 이하)3)\end{tabular}} &
      {\color[HTML]{333333} 50S 이하} \\
    {\color[HTML]{333333} 노치깊이2)} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}2mm 이하\\ (1mm 이하)3)\end{tabular}} &
      {\color[HTML]{333333} 노치가 없어야 한다.} \\
    {\color[HTML]{333333} 슬래그} &
      \multicolumn{4}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함.}} \\
    {\color[HTML]{333333} 절단된 모서리의 상태} &
      \multicolumn{4}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것}} \\
    \multicolumn{5}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 표면 거칠기란 KS B 0161에 규정하는 표면 거칠기로서, 가공 시 가공물의 표면에서 최저점과 최고점의\\      높이차를 나타낸다. 100S=100μm=0.1mm\\ 2) 노치깊이는 노치 마루에서 골밑까지의 깊이를 나타낸다.\\ 3) 교량의 2차부재의 경우에 적용한다.\end{tabular}}}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가스절단 및 가스가공한 강판의 허용오차];
    B["KCS 14 31 10 3.3.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.2 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 가스절단 및 가스가공한 강판의 허용오차/];
    VarIn1[/입력변수: 공사시방서에 정한 바/];
    VarIn2[/입력변수: 교량의 2차부재/];
    VarIn3[/입력변수: 항목/];
    VarIn4[/입력변수: 품질관리 구분 /];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{공사시방서에 정한 바}
		C --> |True|D["KS B 0428 또는 해당 공사시방서에 따른다"]
		C --> |False|E{항목}
		E --> |표면거칠기|F{품질관리구분}
		F --> |다|G{교량의 2차부재}
		G --> |False|H[200S 이하]
		G --> |True|I[100S 이하]
		F --> |라|J[50S 이하]
		E --> |노치깊이|K{품질관리구분}
		K --> |다|L{교량의 2차부재}
		L --> |False|M[2mm 이하]
		L --> |True|N[1mm 이하]
		K --> |라|O[노치가 없어야 한다.]
		E --> |슬래그|P["슬래그 덩어리가 점점이 부착되어 있을 경우 \n 흔적이 남지 않게 제거해야 함. \n."]
		E --> |절단된 모서리의 상태|Q["약간은 둥근 모양을 하고 있지만 \n 매끄러운 상태의 것. \n."]
		D & H & I & J & M & N & O & P & Q --> End([가스절단 및 가스가공한 강판의 허용오차])
    """

    @rule_method
    def Set_by_Project_Specification(bIProSpe, bISenMem, sICat, sIQuaCon) -> str:
        """ 가스절단 및 가스가공한 강판의 허용오차
        Args:
        bIProSpe (bool): 공사시방서에 정한 바
        bISenMem (bool): 교량의 2차 부재
        sICat (str): 항목
        sIQuaCon (str): 품질관리 구분

        Returns:
        sOTolGas (str): 가스절단 및 가스가공한 강판의 허용오차
        """
        assert isinstance(bIProSpe, bool)
        assert isinstance(bISenMem, bool)
        assert isinstance(sICat, str)
        assert sICat in ["표면거칠기", "노치깊이", "슬래그"]
        assert isinstance(sIQuaCon, str)
        assert sIQuaCon in ["가", "나", "다", "라"]

        if bIProSpe == True:
          sOTolGas = "KS B 0428 또는 해당 공사시방서에 따른다"

        elif bIProSpe == False:
          if sICat == "표면거칠기":
            if sIQuaCon == "다":
              if bISenMem == True:
                sOTolGas = "100S 이하"
              elif bISenMem == False:
                sOTolGas = "200S 이하"
            if sIQuaCon == "라":
              sOTolGas = "50S 이하"
            elif sIQuaCon == "가" or sIQuaCon == "나":
              sOTolGas = "-"

          elif sICat == "노치깊이":
            if sIQuaCon == "다":
              if bISenMem == True:
                sOTolGas = "1mm 이하"
              elif bISenMem == False:
                sOTolGas = "2mm 이하"
            if sIQuaCon == "라":
              sOTolGas = "노치가 없어야 한다."
            elif sIQuaCon == "가" or sIQuaCon == "나":
              sOTolGas = "-"

          elif sICat == "슬래그":
            sOTolGas = "슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함"

          elif sICat == "절단된 모서리의 상태":
            sOTolGas = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"

        return RuleUnitResult(
           result_variables={
               "sOTolGas": sOTolGas
           }
        )