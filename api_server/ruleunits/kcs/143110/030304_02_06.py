import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_06(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ⑥'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '절단면 검사 및 결함보수'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (2)
    ⑥
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ⑥ 형강표면의 결함 보수는 제작자가 해당 산업표준에 준하여 시행해야 하며 절단면의 품질은 표 3.3-1에 준한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ⑥"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ⑥"])

    subgraph Variable_def
    VarOut6[/출력변수: 불연속 보수/];
    VarIn61[/입력변수: 결함 허용면적/];
    VarIn62[/입력변수: 철판면적/];
    VarIn63[/입력변수: 결함 길이/];
    VarIn64[/입력변수: 결함 깊이/];
    VarIn65[/입력변수: 모재 폭/];
    VarIn66[/입력변수: 모재 길이/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{강표면 결함 보수 절단면 품질}

		C --> |강표면 결함 보수 절단면 품질|G{항목}
		G --> |표면거칠기|Ga{품질관리구분}
		Ga --> |다|Gb{교량의 2차부재}
		Gb --> |False|Gc[200S 이하]
		Gb --> |True|Gd[100S 이하]
		Ga --> |라|Ge[50S 이하]
		G --> |노치깊이|Gf{품질관리구분}
		Gf --> |다|Gg{교량의 2차부재}
		Gg --> |False|Gh[2mm 이하]
		Gg --> |True|Gi[1mm 이하]
		Gf --> |라|Gj[노치가 없어야 한다.]
		G --> |슬래그|Gp["슬래그 덩어리가 점점이 부착되어 있을 경우 \n 흔적이 남지 않게 제거해야 함. \n."]
		G --> |절단된 모서리의 상태|Gq["약간은 둥근 모양을 하고 있지만 \n 매끄러운 상태의 것. \n."]
		Gc & Gd & Ge & Gh & Gi & Gj & Gp & Gq --> End4([강표면 결함 보수 절단면 품질])
    """

    @rule_method
    def Secondory_Member_of_Bridge(bISenMem, sICat, sIQuaCon) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        bISenMem (bool): 교량의 2차부재
        sICat (str): 항목
        sIQuaCon (str): 품질관리 구분

        Returns:
        sOQuaCut (str): 강표면 결함 보수 절단면 품질
        """
        assert isinstance(bISenMem, bool)
        assert isinstance(sICat, str)
        assert sICat in["표면거칠기", "노치깊이", "슬래그", "절단된 모서리의 상태"]
        assert isinstance(sIQuaCon, str)
        assert sIQuaCon in["가", "나", "다", "라"]

        if sICat == "표면거칠기":
          if sIQuaCon == "다":
            if bISenMem == True:
              sOQuaCut = "100S 이하"
            elif bISenMem == False:
              sOQuaCut = "200S 이하"
          if sIQuaCon == "라":
            sOQuaCut = "50S 이하"
          elif sIQuaCon == "가" or sIQuaCon == "나":
            sOQuaCut = "-"


        elif sICat == "노치깊이":
          if sIQuaCon == "다":
            if bISenMem == True:
              sOQuaCut = "1mm 이하"
            elif bISenMem == False:
              sOQuaCut = "2mm 이하"
          if sIQuaCon == "라":
            sOQuaCut = "노치가 없어야 한다."
          elif sIQuaCon == "가" or sIQuaCon == "나":
            sOQuaCut = "-"

        elif sICat == "슬래그":
          sOQuaCut = "슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함"

        elif sICat == "절단된 모서리의 상태":
          sOQuaCut = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"

        return RuleUnitResult(
           result_variables={
               "sOQuaCut": sOQuaCut
           }
        )