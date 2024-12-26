import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '절단면 검사 및 결함보수'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (2)
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ① 절단면의 검사는 표 3.3-1을 기준으로 시행하며 이 값을 초과하는 거친 면, 노치 및 깊이는 기계연마나 그라인더로 다듬질하여 제거해야 한다.
    ② 절단면의 보수는 보수된 강재가 적기에 사용될 수 있도록 부재 조립작업 전에 보수를 완료해야 하며 다음에 준하여 보수해야 한다.
    나. 가스절단면 노치 깊이가 1 mm를 초과하는 것은 그 부분을 덧살용접 후 그라인더로 마무리해야 한다. 다만 두께가 50 mm를 넘는 강판에 대해서는 원칙적으로 노치를 허용하지 않는다.
    다. 가스 절단면의 직각도가 강판두께 20 mm 이하인 경우 1 mm 이하, 20 mm를 초과하는 경우에는 t/20(mm) 이하로서 이 규정치를 초과하는 부분은 그라인더로 다듬어 규정치 이내로 해야 한다.
    ④ 절단면의 결함 허용오차 및 보수는 표 3.3-2에 준한다.
    ⑥ 강표면의 결함 보수는 제작자가 해당 산업표준에 준하여 시행해야 하며 절단면의 품질은 표 3.3-1에 준한다.
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    {\color[HTML]{333333} 결함의 길이1)} &
      {\color[HTML]{333333} 보수 방법2)} \\
    {\color[HTML]{333333} 길이 25 mm 이하의 결함} &
      {\color[HTML]{333333} 불필요, 조사 불필요} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 최대깊이 3 mm 이하의 결함\end{tabular}} &
      {\color[HTML]{333333} 불필요, 깊이는 조사} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 깊이 3 mm$\sim$6 mm 결함\end{tabular}} &
      {\color[HTML]{333333} 제거, 용접할 필요는 없음} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 깊이 6 mm$\sim$25 mm인 결함\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}완전하게 제거후 용접\\  용접부의 총길이는 보수하는 부재단부 길이의 20\% 이하\end{tabular}} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 깊이 25 mm 초과하는 결함\end{tabular}} &
     {\color[HTML]{333333} 4.3.4의 ⑧에 의하여 보수} \\
    \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 결함의 길이는 강재 절단면의 긴 변(주된 응력 방향)의 치수이며 결함의 깊이는 절단면에서 강재방향으로 연장된 불연속거리이다.\\ 2) 품질저하가 우려되는 산소절단면의 불연속 10\%에 대해 깊이를 결정하기 위해서 절단면을 그라인딩하여 무작위 추출조사를 실시해야 한다. 이때 조사된 결함 중 하나라도그 깊이가 3 mm를 초과하면 절단면의 나머지 부분도 깊이를 결정하기 위해 절단면을 그라인딩한 후 조사해야 한다. 만약 10\% 무작위 추출조사 때 어떠한 결함도 그 깊이가 3 mm를 초과하지 않을 경우 절단면의 나머지 부분은 조사할 필요가 없다.\end{tabular}}}
    \end{tabular}
    \end{table}
    ⑧ 결함 길이가 25 mm를 초과하고 깊이가 25 mm보다 큰 불연속 보수는 다음에 준하여 보수해야 한다.
    나.  W, X, Z-형의 결함 허용면적은 철판면적의 4%를 초과해서는 안 된다. 또한 결함 길이나 깊이가 모재의 폭과 길이의 각각 20%를 초과해서는 안 된다.
    다. 나.항의 허용면적을 초과하지 않는 Z-형 결함은 용접면에서 25 mm 이상 떨어져 있을 경우에는 보수할 필요가 없으나 25 mm 이내일 경우에는 용접열영향부에서 25 mm까지 치핑, 아크에어가우징, 또는 그라인더에 의하여 가우징하고
    층당 3  mm를 초과하지 않는 최소 4개층을 가스메탈아크용접(GMAW)을 실시하고 나머지는 서브머지드 아크용접(SAW) 또는 승인된 용접방법에 의하여 용접해야 한다.
    마.  용접보수의 전체길이가 모재단부 길이의 20%를 초과하는 경우 다른 재료로 대체해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/출력변수: 절단면 검사/];
    VarIn01[/입력변수: 교량의 2차부재/];
    VarIn02[/입력변수: 표면거칠기/];
    VarIn03[/입력변수: 노치깊이/];
    VarIn04[/입력변수: 슬래그/];
    VarIn05[/입력변수: 절단된 모서리의 상태/];
    VarIn06[/입력변수: 품질관리 구분/];
    end
		subgraph V2
    VarOut2[/출력변수: 절단면 보수/];
    VarIn21[/입력변수: 가스절단면 노치 깊이/];
    VarIn22[/입력변수: 강판 두께/];
    end
		subgraph V3
    VarOut3[/출력변수: 절단면 보수/];
    VarIn31[/입력변수: 가스절단면 직각도/];
    VarIn32[/입력변수: 강판 두께/];
    end
		subgraph V4
    VarOut4[/출력변수: 절단면의 결함 허용오차 및 보수방법/];
    VarIn41[/입력변수: 결함 길이/];
    VarIn42[/입력변수: 결함 깊이/];
    end
		subgraph V5
    VarOut5[/출력변수: 강표면 결함 보수 절단면 품질/];
    VarIn51[/입력변수: 교량의 2차부재/];
    VarIn52[/입력변수: 항목/];
    VarIn53[/입력변수: 품질관리 구분/];
    end
		subgraph V6
    VarOut6[/출력변수: 불연속 보수/];
    VarIn61[/입력변수: 결함 허용면적/];
    VarIn62[/입력변수: 철판면적/];
    VarIn63[/입력변수: 결함 길이/];
    VarIn64[/입력변수: 결함 깊이/];
    VarIn65[/입력변수: 모재 폭/];
    VarIn66[/입력변수: 모재 길이/];
    end
		subgraph V7
    VarOut7[/출력변수: 불연속 보수/];
    VarIn71[/입력변수: 용접면까지 떨어진 길이/];
    end
		subgraph V8
    VarOut8[/출력변수:용접 보수/];
    VarIn81[/입력변수: 용접보수의 전체길이/];
    VarIn82[/입력변수: 모재단부 길이/];
    end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{절단면 검사\n절단면 보수\n 절단면의 결함 허용오차 및 보수방법 \n 강표면 결함 보수 절단면 품질 \n 용접 보수 \n.}
		C --> |절단면 검사|D{항목}
		D --> |표면 거칠기, 노치 깊이|Db{표 3.3-1}
		Db --> |True|Pass1([Pass])
		Db --> |False|Dc[기계연마나 그라인더로 다듬질하여 제거]
		D --> |슬래그|Dd[슬래그 덩어리가 점점이 부착되어 있을 경우 \n 흔적이 남지 않게 제거해야 함.]
		D --> |절단된 모서리의 상태|De[약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것]
		Dc & Dd & De --> End1([절단면 검사])
		C --> |절단면 보수|CC{가스 절단면의 직각도 \n 가스 절단면 노치 깊이}
		CC --> |가스 절단면 노치 깊이|Ca{강판 두께 > 50 mm}
		Ca --> |True|Cb[원칙적으로 노치를 허용하지 않는다.]
		Ca --> |Fasle|Cc{가스절단면 노치 깊이 > 1mm}
		Cc --> |True|Cd[그 부분을 덧살용접 후 그라인더로 마무리해야 한다.]
		Cb &  Cd --> End2([절단면 보수])
		CC --> |가스 절단면의 직각도|Ce{"강판 두께 ≤ 20 mm"}
		Ce --> |True|Cf{"가스 절단면의 직각도 ≤ 1 mm"}
		Ce --> |False|Cg{"가스 절단면의 직각도 ≤ 강판두께/20"}
		Cf & Cg --> |True|Pass2([Pass])
		Cf & Cg --> |False|Fail2([Fail])

		C --> |절단면의 결함 허용오차 및 보수방법|E{결함의 깊이, 결함의 길이}
		E --> |"결함의 길이 ≤ 25 mm"|Ea[불필요, 조사 불필요]
		E --> |"결함의 길이 > 25 mm \n 결함깊이 ≤ 3 mm"|Eb[불필요, 깊이는 조사]
		E --> |"결함의 길이 > 25 mm \n 3 < 결함깊이 ≤ 6 mm"|Ec[제거, 용접할 필요는 없음]
		E --> |"결함의 길이 > 25 mm \n 6 < 결함깊이 ≤ 25 mm"|Ed[완전하게 제거후 용접 \n  용접부의 총길이는 보수하는 부재단부 길이의 20% 이하]
		E --> |"결함의 길이 > 25 mm \n  결함깊이 > 25 mm"|H{불연속 보수}
		Ea & Eb & Ec & Ed  --> End3([절단면의 결함 허용오차 및 보수방법])

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

		H --> Ha{"결함허용면적 ≤ 철판면적*0.04,\n 결함 길이, 결함 깊이 ≤ min(모재의 폭, 모재의 길이) * 0.2"}
		Ha --> |False|Fail4([Fail])
		Ha --> |True|Pass4([Pass])
		H --> Hb{용접면까지 떨어진 길이}
		Hb --> |"≥ 25 mm"|Hc[보수할 필요가 없다]
		Hb --> |"< 25 mm"|Hd["용접열영향부에서 25 mm까지 \n 치핑, 아크에어가우징, 또는 그라인더에 의하여 가우징하고 \n 층당 3  mm를 초과하지 않는 \n 최소 4개층을 가스메탈아크용접(GMAW)을 실시하고 \n 나머지는 서브머지드 아크용접(SAW) \n 또는 승인된 용접방법에 의하여 용접보수할 필요가 없다\n. "]
		H --> |"용접보수의 전체길이 > 모재단부 길이 * 0.2"|He[다른 재료로 대체]
		Hc & Hd & He --> End5([불연속 보수])
    """

    @rule_method
    def Secondory_Member_of_Bridge(bISenMem, fISurRou, sICat, fINotDep, sIQuaCon, fINotDep_2, fIThiSte, fIPerCut, fILenDef, fIDepDef, fITolDef, fIAreSte, fIWidBas, fILenBas, fIDisWel, fILenWel, fILenEnd) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        bISenMem (bool): 교량의 2차부재
        fISurRou (float): 표면거칠기
        sICat (str): 항목
        fINotDep (float): 노치깊이
        sIQuaCon (str): 품질관리 구분
        fINotDep_2 (float): 가스절단면 노치 깊이
        fIThiSte (float): 강판 두께
        fIPerCut (float): 가스절단면 직각도
        fILenDef (float): 결함 길이
        fIDepDef (float): 결함 깊이
        fITolDef (float): 결함 허용면적
        fIAreSte (float): 철판면적
        fIWidBas (float): 모재 폭
        fILenBas (float): 모재 길이
        fIDisWel (float): 용접면까지 떨어진 길이
        fILenWel (float): 용접보수의 전체길이
        fILenEnd (float): 모재단부 길이

        Returns:
        sOCutIns (str): 절단면 검사
        sOCutRep (str): 절단면 보수
        sOCutRep_2 (str): 절단면 보수
        sORepCut (str): 절단면의 결함 허용오차 및 보수방법
        sOQuaCut (str): 강표면 결함 보수 절단면 품질
        sODisRep (str): 불연속 보수
        sOWelRep (str): 용접 보수
        """
        assert isinstance(bISenMem, bool)
        assert isinstance(fISurRou, float)
        assert isinstance(sICat, str)
        assert sICat in["표면거칠기", "노치깊이", "슬래그", "절단된 모서리의 상태"]
        assert isinstance(fINotDep, float)
        assert isinstance(sIQuaCon, str)
        assert sIQuaCon in["다", "라"]
        assert isinstance(fINotDep_2, float)
        assert isinstance(fIThiSte, float)
        assert isinstance(fIPerCut, float)
        assert isinstance(fILenDef, float)
        assert isinstance(fIDepDef, float)
        assert isinstance(fITolDef, float)
        assert isinstance(fIAreSte, float)
        assert isinstance(fIWidBas, float)
        assert isinstance(fILenBas, float)
        assert isinstance(fIDisWel, float)

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
          sOQuaCut = "슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함"

        elif sICat == "절단된 모서리의 상태":
          sOCutIns = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"
          sOQuaCut = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"

        if fINotDep_2 > 1:
          if fIThiSte <= 50:
            sOCutRep = "가스절단면 노치 깊이가 1mm가 초과하는 부분을 덧살용접 후 그라인더로 마무리해야 한다."
          else:
            sOCutRep = "원칙적으로 노치를 허용하지 않는다."

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

        if fILenDef <= 25:
          sORepCut = "불필요, 조사 불필요"
        else:
          if fIDepDef <= 3:
            sORepCut = "불필요, 깊이는 조사"
          elif 3 < fIDepDef <= 6:
            sORepCut = "제거, 용접할 필요는 없음"
          elif 6 < fIDepDef <= 25:
            sORepCut = "완전하게 제거후 용접, 용접부의 총길이는 보수하는 부재단부 길이의 20% 이하"
          elif fIDepDef > 25:
            sORepCut = "4.3.4의 ⑧에 의하여 보수"

        if fILenDef > 25 and fIDepDef > 25:
          if fITolDef <= (fIAreSte * 0.04) and fILenDef <= (fIWidBas * 0.2) and fIDepDef <= (fILenBas * 0.2):
            sODisRep = "Pass"
          else:
            sODisRep = "Fail"
        else:
          sODisRep = "보수할 필요가 없다"

        if fILenDef > 25 and fIDepDef > 25:
          if fITolDef <= (fIAreSte * 0.04):
            if fIDisWel >= 25:
              sODisRep = "보수할 필요가 없다."
            else:
              sODisRep = "용접열영향부에서 25 mm까지 치핑, 아크에어가우징, 또는 그라인더에 의하여 가우징하고 층당 3  mm를 초과하지 않는 최소 4개층을 가스메탈아크용접(GMAW)을 실시하고 나머지는 서브머지드 아크용접(SAW) 또는 승인된 용접방법에 의하여 용접"
        else:
          sODisRep = "보수할 필요가 없다"

        if fILenDef > 25 and fIDepDef > 25:
          if fILenWel > (fILenEnd * 0.2):
            sOWelRep = "다른 재료로 대체"
        else:
          sOWelRep = "보수할 필요가 없다"

        return RuleUnitResult(
           result_variables={
               "sOCutIns": sOCutIns,
               "sOCutRep": sOCutRep,
               "sOCutRep_2": sOCutRep_2,
               "sORepCut": sORepCut,
               "sOQuaCut": sOQuaCut,
               "sODisRep": sODisRep,
               "sOWelRep": sOWelRep,
           }
        )