import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '개선 절단면 검사'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (1)
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (1) 개선각도(그루브 각도)와 루트는 정밀하게 가공되어야 한다. 개선가공면의 품질은 표 3.3-1에 따른다.
    그루브용접을 위한 그루브 가공 허용오차는 규정값에 –2.5°, +5°(부재조립 정밀도의 1/2) 범위 이내, 루트면의 허용오차는 규정값에 ±1.6 mm 이내로 해야 한다.
    그루브 가공은 자동가스절단기 또는 기계절단기로 하는 것을 원칙으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 개선 절단면 검사];
    B["KCS 14 31 10 3.3.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 개선 절단면 검사/];
    VarIn1[/입력변수: 개선가공면 품질/];
    VarIn2[/입력변수: 그루브 가공 허용오차/];
    VarIn3[/입력변수: 루트면 허용오차/];
    VarIn4[/입력변수: 교량의 2차부재/];
    VarIn6[/입력변수: 항목/];
    VarIn7[/입력변수: 품질관리 구분/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn6 & VarIn7
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{개선가공면의 품질 \n 그루브 가공 허용오차 \n 루트면의 허용오차}
		C --> |그루브 가공 허용오차|D["규정값에 –2.5°, +5° \n (부재조립 정밀도의 1/2) 범위 이내"]
		C --> |루트면의 허용오차|DD["규정값에 ±1.6 mm 이내"]
		C --> |개선가공면의 품질|E{항목}
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
		D & DD & H & I & J & M & N & O & P & Q --> End([가스절단 및 가스가공한 강판의 허용오차])
    """

    @rule_method
    def Quality_of_Cutting_Groove_Surface(bICutGro, bITolGro, bITolRoo, bISenMem, sICat, sIQuaCon) -> str:
        """ 개선 절단면 검사
        Args:
        bICutGro (bool): 개선가공면 품질
        bITolGro (bool): 그루브 가공 허용오차
        bITolRoo (bool): 루트면 허용오차
        bISenMem (bool): 교량의 2차 부재
        sICat (str): 항목
        sIQuaCon (str): 품질관리 구분

        Returns:
        sOInsCut (str): 개선 절단면 검사
        """
        assert isinstance(bICutGro, bool)
        assert isinstance(bITolGro, bool)
        assert isinstance(bITolRoo, bool)
        assert (bICutGro + bITolGro + bITolRoo) == 1
        assert isinstance(bISenMem, bool)
        assert isinstance(sICat, str)
        assert sICat in ["표면거칠기", "노치깊이", "슬래그", "절단된 모서리의 상태"]
        assert isinstance(sIQuaCon, str)
        assert sIQuaCon in ["가", "나", "다", "라"]

        if bICutGro == True and bITolGro == False and bITolRoo == False:
          if sICat == "표면거칠기":
            if sIQuaCon == "다":
              if bISenMem == True:
                sOInsCut = "100S 이하"
              elif bISenMem == False:
                sOInsCut = "200S 이하"
            if sIQuaCon == "라":
              sOInsCut = "50S 이하"
            elif sIQuaCon == "가" or sIQuaCon == "나":
              sOInsCut = "-"

          elif sICat == "노치깊이":
            if sIQuaCon == "다":
              if bISenMem == True:
                sOInsCut = "1mm 이하"
              elif bISenMem == False:
                sOInsCut = "2mm 이하"
            if sIQuaCon == "라":
              sOInsCut = "노치가 없어야 한다."
            elif sIQuaCon == "가" or sIQuaCon == "나":
              sOInsCut = "-"

          elif sICat == "슬래그":
            sOInsCut = "슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함"

          elif sICat == "절단된 모서리의 상태":
            sOInsCut = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"

        elif bICutGro == False and bITolGro == True and bITolRoo == False:
          sOInsCut = "규정값에 –2.5°, +5°(부재조립 정밀도의 1/2) 범위 이내"

        elif bICutGro == False and bITolGro == False and bITolRoo == True:
          sOInsCut = "규정값에 ±1.6 mm 이내"

        return RuleUnitResult(
           result_variables={
               "sOInsCut": sOInsCut
           }
        )