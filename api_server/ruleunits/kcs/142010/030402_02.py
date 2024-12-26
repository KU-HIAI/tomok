import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_030402_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 3.4.2 (2)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-05-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    3. 시공
    3.4 양생
    3.4.2 습윤 양생
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.4.2 습윤 양생
    (2) 콘크리트는 타설한 후 습윤 상태로 노출면이 마르지 않도록 하여야 하며, 수분의 증발에 따라 살수를 하여 습윤 상태로 보호하여야 한다. 습윤 상태로 보호하는 기간은 표 3.4-1을 표준으로 한다.

표 3.4-1 습윤 양생 기간의 표준
\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 일평균기온}    & {\color[HTML]{333333} 보통포틀랜드 시멘트} & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}고로 슬래그 시멘트 2종\\ 플라이 애시 시멘트 2종\end{tabular}} & {\color[HTML]{333333} 조강포틀랜드 시멘트} \\ \hline
{\color[HTML]{333333} 15 °C 이상} & {\color[HTML]{333333} 5일}         & {\color[HTML]{333333} 7일}                                                                    & {\color[HTML]{333333} 3일}         \\ \hline
{\color[HTML]{333333} 10 °C 이상} & {\color[HTML]{333333} 7일}         & {\color[HTML]{333333} 9일}                                                                    & {\color[HTML]{333333} 4일}         \\ \hline
{\color[HTML]{333333} 5 °C 이상}  & {\color[HTML]{333333} 9일}         & {\color[HTML]{333333} 12일}                                                                   & {\color[HTML]{333333} 5일}         \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 습윤 양생 기간"];
    B["KCS 14 31 30 3.4.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.4.2 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 습윤 양생 기간"/];
		VarIn1[/"입력변수: 일평균기온"/];
		VarIn2[/"입력변수: 시멘트 종류"/];
    VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"일평균기온"}

		D --> |"15°C <= 일평균기온"|E{시멘트 종류}
		D --> |"10°C <= 일평균기온 < 15°C"|F{시멘트 종류}
		D --> |"5°C <= 일평균기온 < 10°C"|G{시멘트 종류}

		E --> |보통포틀랜드 시멘트|H[5]
		E --> |고로 슬래그 시멘트 2종 or\n플라이 애시 시멘트 2종|I[7]
		E --> |조강포틀랜드 시멘트|J[3]

		F --> |보통포틀랜드 시멘트|K[7]
		F --> |고로 슬래그 시멘트 2종 or\n플라이 애시 시멘트 2종|L[9]
		F --> |조강포틀랜드 시멘트|M[4]

		G --> |보통포틀랜드 시멘트|N[9]
		G --> |고로 슬래그 시멘트 2종 or\n플라이 애시 시멘트 2종|O[12]
		G --> |조강포틀랜드 시멘트|P[5]

		E --> Q([습윤 양생 기간])
		F --> Q([습윤 양생 기간])
		G --> Q([습윤 양생 기간])
		H --> Q([습윤 양생 기간])
		I --> Q([습윤 양생 기간])
		J --> Q([습윤 양생 기간])
		K --> Q([습윤 양생 기간])
		L --> Q([습윤 양생 기간])
		M --> Q([습윤 양생 기간])
		N --> Q([습윤 양생 기간])
		O --> Q([습윤 양생 기간])
		P --> Q([습윤 양생 기간])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def moisture_curing_period(fIAveTem, sITypCem) -> RuleUnitResult:
        """습윤 양생 기간

        Args:
            fIAveTem (float): 일평균기온
            sITypCem (str): 시멘트 종류

        Returns:
            nOMoiCur (int): 습윤 양생 기간
        """
        assert isinstance(fIAveTem, float)
        assert isinstance(sITypCem, str)

        if fIAveTem >= 15:
            if sITypCem == "보통포틀랜드 시멘트":
                nOMoiCur = 5
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            if sITypCem == "고로 슬래그 시멘트 2종" or sITypCem == "플라이 애시 시멘트 2종":
                nOMoiCur = 7
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            if sITypCem == "조강포틀랜드 시멘트":
                nOMoiCur = 3
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            else:
                assert 1 != 1
        if 10 <= fIAveTem < 15:
            if sITypCem == "보통포틀랜드 시멘트":
                nOMoiCur = 7
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            if sITypCem == "고로 슬래그 시멘트 2종" or sITypCem == "플라이 애시 시멘트 2종":
                nOMoiCur = 9
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            if sITypCem == "조강포틀랜드 시멘트":
                nOMoiCur = 4
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            else:
                assert 1 != 1
        if 5 <= fIAveTem < 10:
            if sITypCem == "보통포틀랜드 시멘트":
                nOMoiCur = 9
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            if sITypCem == "고로 슬래그 시멘트 2종" or sITypCem == "플라이 애시 시멘트 2종":
                nOMoiCur = 12
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            if sITypCem == "조강포틀랜드 시멘트":
                nOMoiCur = 5
                return RuleUnitResult(
                    result_variables = {
                        "nOMoiCur": nOMoiCur
                }
            )
            else:
                assert 1 != 1
        else:
            assert 1 != 1