import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_030104_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 3.1.4 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '절단 및 가공'

    description = """
    강교량공사
    3. 시공
    3.1 제작
    3.1.4 시공
    (2)
    """
    content = """
    #### 3.1.4 시공
    (2) 절단 및 가공
    ① 주요 부재(플렌지, 웨브)의 강판 절단은 주된 응력의 방향과 압연방향을 일치시켜 절단하며 절단작업 착수 전 재단도를 작성한다. 다만, 제강업체에서 압연 반대방향으로 기계적 시험을 시행하여 KS를 만족할 경우 예외로 한다.
    ② 주요 부재의 절단은 자동가스절단기로 하여야 한다. 가스절단 및 가스 가공한 강판의 허용오차는 KS B 0428에 준하되 절단면의 품질은 표 3.1-1에 따른다.
    표 3.1-1 가스절단면의 품질
    \begin{table}[]
    \begin{tabular}{lll}
    부재의 종류                                         & 주요 부재                                                             & 2차 부재                                                         \\
    표면거칠기1)                                        & 50S 이하                                                            & 100S 이하                                                       \\
    노치 깊이2)                                        & 노치가 없어야 한다.                                                       & 1 ㎜ 이하                                                        \\
    슬래그                                            & \multicolumn{2}{l}{슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함.}                                                                     \\
    절단된 모서리의 상태                                    & \multicolumn{2}{l}{약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것}                                                                                  \\
    \multicolumn{3}{l}{\begin{tabular}[c]{@{}l@{}}주 1) 표면 거칠기란 KS B ISO 4287에 규정하는 표면의 조도(粗度)를 나타내며 50S란 표면 거칠기 50/1,000 ㎜의 요철을 나타낸다.\\ 2) 노치깊이는 노치 마루에서 골밑까지의 깊이를 나타낸다.\end{tabular}}
    \end{tabular}
    \end{table}
    ③ 채움재, 띠철(타이플레이트), 형강, 판두께 10 mm 이하의 연결판, 보강재 등은 전단 절단할 수 있다.
    ④ 두께 50 mm를 초과하는 극후판의 경우 압연강재의 최외측 10 mm 부분은 자동가스 절단하여 drag line을 없애야 하는 정도로 절삭 처리 후 사용하여야 한다.
    ⑤ 절단면의 검사는 표 3.1-1을 기준으로 시행하며 이 값을 초과하는 거친 면, 노치 및 깊이는 기계연마나 그라인더로 다듬질하여 제거하여야 한다.

    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단 및 가공];
    B["KCS 24 30 00 3.1.4 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.1.4 (2)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 가스절단 및 가스가공/];
    VarIn11[/입력변수: 주요 부재의 절단 도구/];
    VarIn12[/입력변수: 가스절단 및 가스 가공한 강판의 허용오차/];
    VarIn13[/입력변수: 절단면의 품질/];
    VarIn14[/입력변수: 부재의 종류/];
    VarIn15[/입력변수: 표면거칠기/];
    VarIn16[/입력변수: 노치 깊이/];
    VarIn17[/입력변수: 슬래그/];
    VarIn18[/입력변수: 절단된 모서리의 상태/];
    end
    subgraph V2
    VarOut2[/출력변수: 압연강재의 절삭처리/];
    VarIn21[/입력변수: 극후판의 두께/];
    end
    subgraph V3
    VarOut3[/출력변수: 가스절단면의 품질/];
    VarIn21[/입력변수: 부재의 종류/];
    VarIn22[/입력변수: 표면거칠기/];
    VarIn23[/입력변수: 노치 깊이/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"가스절단 및 가스가공 \n 압연강재의 절삭처리 \n 가스절단면의 품질"}
    C --> |"가스절단 및 가스가공"|D{"주요 부재의 절단 도구 \n 가스절단 및 가스 가공한 강판의 허용오차 \n 절단면의 품질"}
    D --> |"주요 부재의 절단 도구"|E[자동가스절단기]
    D --> |"가스절단 및 가스 가공한 강판의 허용오차"|F[KS B 0428에 준한다]
    D --> |"절단면의 품질"|G{부재의 종류 \n 표면거칠기 \n 노치 깊이 \n 슬래그 \n 절단된 모서리의 상태}
    G --> |표 3.1-1|H[가스절단 및 가스가공]
    C --> |"압연강재의 절삭처리"|I{극후판의 두께 > 50}
    I --> |True|J["압연강재의 최외측 10 mm 부분은 \n 자동가스 절단하여 drag line을 \n 없애야 하는 정도로 절삭 처리 후 사용\n."]
    C --> |"가스절단면의 품질"|K{부재의 종류}
    K --> |"주요 부재"|L{"표면거칠기≤ 50 \n and \n 노치 깊이 > 0 \n."}
    K --> |"2차 부재"|M{"표면거칠기≤ 100 \n and \n 노치 깊이 > 1 \n."}
    L & M --> |True|Pass([Pass])
    L & M --> |False|N[기계연마나 그라인더로 다듬질하여 제거]
    E & F & H & J & N --> End([절단 및 가공])
    """

    @rule_method

    def gas_cutting_processing(sIMemTyp,bISurRou,bINotDep,bISla,bIConEdg,fIThiExt,fISurRou,fINotDep) -> RuleUnitResult:
        """
        Args:
            sIMemTyp (str): 부재의 종류
            bISurRou (bool): 표면거칠기
            bINotDep (bool): 노치 깊이
            bISla (bool): 슬래그
            bIConEdg (bool): 절단된 모서리의 상태
            fIThiExt (float): 극후판의 두께
            fISurRou (float):표면거칠기
            fINotDep (float): 노치 깊이

        Returns:
            sOCutTol (str): 주요 부재의 절단 도구
            sOTolPla (str): 가스절단 및 가스 가공한 강판의 허용오차
            sOQuaSur (str): 절단면의 품질
            sOCutRol (str): 압연강재의 절삭처리
            pass_fail_1 (bool): 강교량공사 3.1.4 시공 (2) ④의 판단 결과
            pass_fail_2 (bool): 강교량공사 3.1.4 시공 (2) ⑤의 판단 결과
        """
        assert isinstance(sIMemTyp, str)
        assert sIMemTyp in ["주요 부재","2차 부재"]
        assert isinstance(bISurRou, bool)
        assert isinstance(bINotDep, bool)
        assert isinstance(bISla, bool)
        assert isinstance(bIConEdg, bool)
        assert (bISurRou+bINotDep+bISla+bIConEdg) == 1

        assert isinstance(fIThiExt, float)

        assert isinstance(fISurRou, float)
        assert isinstance(fINotDep, float)

        sOCutTol = "자동가스절단기"

        sOTolPla = "KS B 0428 에 준한다"

        if bISurRou:
            if sIMemTyp == "주요 부재":
                sOQuaSur = "50S 이하"
            elif sIMemTyp == "2차 부재":
                sOQuaSur = "100S 이하"
        elif bINotDep:
            if sIMemTyp == "주요 부재":
                sOQuaSur = "노치가 없어야 한다."
            elif sIMemTyp == "2차 부재":
                sOQuaSur = "1 ㎜ 이하"
        elif bISla:
            sOQuaSur = "슬래그 덩어리가 점점이 부착되어 있을 경우 흔적이 남지 않게 제거해야 함."
        elif bIConEdg:
            sOQuaSur = "약간은 둥근 모양을 하고 있지만 매끄러운 상태의 것"

        if fIThiExt > 50:
            sOCutRol = "압연강재의 최외측 10 mm 부분은 자동가스 절단하여 drag line을 없애야 하는 정도로 절삭 처리 후 사용"
            pass_fail_1 = None
        else:
            sOCutRol = None
            pass_fail_1 = True

        if sIMemTyp =="주요 부재":
            if fISurRou <=50 and fINotDep <=0:
                pass_fail_2 = True
            else:
                pass_fail_2 = False
        elif sIMemTyp == "2차 부재":
            if fISurRou <= 100 and fINotDep <= 1:
                pass_fail_2 = True
            else:
                pass_fail_2 = False

        return RuleUnitResult(
            result_variables = {
                "sOCutTol": sOCutTol,
                "sOTolPla": sOTolPla,
                "sOQuaSur": sOQuaSur,
                "sOCutRol": sOCutRol,
                "pass_fail_1": pass_fail_1,
                "pass_fail_2": pass_fail_2,
                })