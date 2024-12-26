import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_02010404_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.1.4.4 (1)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.1 구성재료
    2.1.4 굵은 골재
    2.1.4.4 유해물 함유량의 한도
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.1.4.4 유해물 함유량의 한도
    (1) 천연 굵은 골재의 유해물 함유량의 한도는 표 2.1-4의 값으로 한다. 천연 굵은 골재 이외의 굵은 골재의 유해물질 함유량의 허용한도는 KS F 2527에 따라야 한다. KS F 2527에서 정하지 않은 유해물에 관해서는 책임기술자의 승인을 받아야 한다.

표 2.1-4 굵은 골재의 유해물 함유량 한도(질량 백분율)
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 종류}}                                                                                                  & {\color[HTML]{333333} 천연 굵은 골재}                                          \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 점토덩어리}}                                                                                               & {\color[HTML]{333333} 0.25 1)}                                           \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 연한 석편}}                                                                                               & {\color[HTML]{333333} 5.0 1)}                                            \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.08 mm 체 통과량}}                                                                                       & {\color[HTML]{333333} 1.0}                                               \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}석탄, 갈탄 등으로 밀도 2.0 g/㎤의 액체에 뜨는 것\\ 콘크리트의 외관이 중요한 경우\\ 기타의 경우\end{tabular}}} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}0.5\\ 1.0\end{tabular}} \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 주 1) 점토 덩어리와 연한 석편의 합이 5\%를 넘으면 안된다.}}                                                                                                                                           \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 천연 굵은 골재의 유해물 함유량 한도"];
    B["KCS 14 31 30 2.1.4.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.1.4.4 (1)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 점토 덩어리"/];
		VarIn2[/"입력변수: 연한 석편"/];
		VarIn3[/"입력변수: 0.08mm 체 통과량"/];
		VarIn4[/"입력변수: 석탄, 갈탄등으로 밀도 2.0g/cm^3의 액체에 뜨는 것"/];
		VarIn5[/"입력변수: 콘크리트의 외관이 중요"/];
		VarIn6[/"입력변수: 기타"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{종류}

		D --> |"'점토\n덩어리'"|F[0.25]
		D --> |"'연한\n석편'"|G[5.0]
		D --> |"'0.08mm 체\n통과량'"|H[1.0]
		D --> |"'석탄, 갈탄등으로 \n밀도 2.0g/cm^3의\n액체에 뜨는 것'\n-콘크리트의 외관이\n 중요한 경우"|I[0.5]
		D --> |"'석탄, 갈탄등으로 \n밀도 2.0g/cm^3의\n액체에 뜨는 것\n-기타의 경우'"|J[1.0]

		F --> K([천연 굵은 골재의 유해물 함유량 한도])
		G --> K([천연 굵은 골재의 유해물 함유량 한도])
		H --> K([천연 굵은 골재의 유해물 함유량 한도])
		I --> K([천연 굵은 골재의 유해물 함유량 한도])
		J --> K([천연 굵은 골재의 유해물 함유량 한도])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def harmful_content_limit_in_natural_coarse_aggregates(bIClaLum, bILigSto, bIPasAmo, bICoaLig, bIAppCon, bIOth) -> RuleUnitResult:
        """천연 굵은 골재의 유해물 함유량 한도

        Args:
            bIClaLum (bool): 점토 덩어리
            bILigSto (bool): 연한 석편
            bIPasAmo (bool): 0.08mm 체 통과량
            bICoaLig (bool): 석탄, 갈탄등으로 밀도 2.0g/cm^3의 액체에 뜨는 것
            bIAppCon (bool): 콘크리트의 외관이 중요
            bIOth (bool): 기타

        Returns:
            fOHarLim (float): 천연 굵은 골재의 유해물 함유량 한도

        """

        if bIClaLum == True:
            fOHarLim = 0.25
            return RuleUnitResult(
                result_variables = {
                    "fOHarLim": fOHarLim
                }
            )
        if bILigSto == True:
            fOHarLim = 5.0
            return RuleUnitResult(
                result_variables = {
                    "fOHarLim": fOHarLim
                }
            )
        if bIPasAmo == True:
            fOHarLim = 1.0
            return RuleUnitResult(
                result_variables = {
                    "fOHarLim": fOHarLim
                }
            )
        if bICoaLig == True and bIAppCon == True:
            fOHarLim = 0.5
            return RuleUnitResult(
                result_variables = {
                    "fOHarLim": fOHarLim
                }
            )
        if bICoaLig == True and bIOth == True:
            fOHarLim = 1.0
            return RuleUnitResult(
                result_variables = {
                    "fOHarLim": fOHarLim
                }
            )
        else:
            assert 1 != 1