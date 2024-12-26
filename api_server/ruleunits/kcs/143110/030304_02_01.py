import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ①'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '절단면 검사 및 결함보수'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (2)
    ①
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ① 절단면의 검사는 표 3.3-1을 기준으로 시행하며 이 값을 초과하는 거친 면, 노치 및 깊이는 기계연마나 그라인더로 다듬질하여 제거해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ①"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ①"])

    subgraph Variable_def
    VarOut1[/출력변수: 절단면 검사/];
    VarIn01[/입력변수: 교량의 2차부재/];
    VarIn02[/입력변수: 표면거칠기/];
    VarIn03[/입력변수: 노치깊이/];
    VarIn04[/입력변수: 슬래그/];
    VarIn05[/입력변수: 절단된 모서리의 상태/];
    VarIn06[/입력변수: 품질관리 구분/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> D{항목}
		D --> |표면 거칠기, 노치 깊이|Db{표 3.3-1}
		Db --> |True|Pass1([Pass])
		Db --> |False|Dc[기계연마나 그라인더로 다듬질하여 제거]
		D --> |슬래그|Dd[슬래그 덩어리가 점점이 부착되어 있을 경우 \n 흔적이 남지 않게 제거해야 함.]
		D --> |절단된 모서리의 상태|De[약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것]
		Dc & Dd & De --> End1([절단면 검사])
    """

    @rule_method
    def Secondory_Member_of_Bridge(bISenMem, fISurRou, sICat, fINotDep, sIQuaCon) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        bISenMem (bool): 교량의 2차부재
        fISurRou (float): 표면거칠기
        sICat (str): 항목
        fINotDep (float): 노치깊이
        sIQuaCon (str): 품질관리 구분

        Returns:
        sOCutIns (str): 절단면 검사

        """
        assert isinstance(bISenMem, bool)
        assert isinstance(fISurRou, float)
        assert isinstance(sICat, str)
        assert sICat in["표면거칠기", "노치깊이", "슬래그", "절단된 모서리의 상태"]
        assert isinstance(fINotDep, float)
        assert isinstance(sIQuaCon, str)
        assert sIQuaCon in["다", "라"]

        if sICat == "표면거칠기":
          if sIQuaCon == "다":
            if bISenMem == True:
              sOQuaCut = "100S 이하"
              if fISurRou > 100:
                sOCutIns = "기계연마나 그라인더로 다듬질하여 제거"
              else:
                sOCutIns = "100S 이하"
            elif bISenMem == False:
              sOQuaCut = "200S 이하"
              if fISurRou > 200:
                sOCutIns = "기계연마나 그라인더로 다듬질하여 제거"
              else:
                sOCutIns = "200S 이하"
          elif sIQuaCon == "라":
            sOQuaCut = "50S 이하"
            if fISurRou > 50:
              sOCutIns = "기계연마나 그라인더로 다듬질하여 제거"
            else:
              sOCutIns = "50S 이하"

        elif sICat == "노치깊이":
          if sIQuaCon == "다":
            if bISenMem == True:
              sOQuaCut = "1mm 이하"
              if fINotDep > 1:
                sOCutIns = "기계연마나 그라인더로 다듬질하여 제거"
              else:
                sOCutIns = "1mm 이하"
            elif bISenMem == False:
              sOQuaCut = "2mm 이하"
              if fINotDep > 2:
                sOCutIns = "기계연마나 그라인더로 다듬질하여 제거"
              else:
                sOCutIns = "2mm 이하"
          elif sIQuaCon == "라":
            sOQuaCut = "노치가 없어야 한다."
            if fINotDep > 0:
              sOCutIns = "기계연마나 그라인더로 다듬질하여 제거"
            else:
              sOCutIns = "노치가 없어야 한다."

        elif sICat == "슬래그":
          sOCutIns = "슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함"

        elif sICat == "절단된 모서리의 상태":
          sOCutIns = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"

        return RuleUnitResult(
           result_variables={
               "sOCutIns": sOCutIns
           }
        )