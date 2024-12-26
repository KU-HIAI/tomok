import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_010801_05(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 1.8.1 (5)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    1. 일반사항
    1.8 콘크리트의 염화물 함유량 및 강도에 대한 일반사항
    1.8.1 염화물 함유량
    (5)

    """

    # 건설기준문서내용(text)
    content = """
    #### 1.8.1 염화물 함유량
    (5) 재령 28일이 경과한 굳은 콘크리트의 수용성 염소 이온량은 표 1.9-3의 값을 초과하지 않도록 하여야 한다.

표 1.9-3 내구성 확보를 위한 요구조건

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                                                                                                                                  & \multicolumn{16}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 노출범주 및 등급}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   \\ \cline{3-18}
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                                                                                                                                                  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 일반}}   & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}EC\\ (탄산화)\end{tabular}}}                                                                                                                                                                                    & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}ES\\ (해양환경, 제설염 등 염화물)\end{tabular}}}                                                                                                                                                                        & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}EF\\ (동결융해)\end{tabular}}}                                                                                                                                                                                   & \multicolumn{3}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}EA\\ (황산염)\end{tabular}}}                                                            \\ \cline{3-18}
\multicolumn{2}{|l|}{\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 항목}}}                                                                                                                                                                                              & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} E0}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EC1}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EC2}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EC3}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EC4}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} ES1}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} ES2}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} ES3}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} ES4}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EF1}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EF2}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EF3}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EF4}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EA1}}  & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} EA2}}  & {\color[HTML]{333333} EA3}  \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}내구성 기준압축강도\\ \# (MPa)\end{tabular}}}                                                                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 21}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 21}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 24}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 27}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 30}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 30}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 30}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 35}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 35}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 24}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 27}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 30}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 30}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 27}}   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 30}}   & {\color[HTML]{333333} 30}   \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 최대 물-결합재비1)}}                                                                                                                                                                                                       & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.60}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.55}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.50}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.45}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.45}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.45}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.40}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.40}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.55}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.50}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.45}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.45}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.50}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.45}} & {\color[HTML]{333333} 0.45} \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}최소 단위 결합재량\\ (kg/m³)\end{tabular}}}                                                                                                                                                      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{4}{l|}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} KCS 14 20 44 (2.2)}}                                                                                                                                                                                                 & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & {\color[HTML]{333333} -}    \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 최소 공기량(\%)}}                                                                                                                                                                                                        & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}                                                                                                                                                                                                                                     & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} (표 2.2-6)}}                                                                                                                                                                                                                             & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & {\color[HTML]{333333} -}    \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}무근\\ 콘크리트\end{tabular}}}      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}                                                                                                                                                                                                                                     & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}                                                                                                                                                                                                                                     & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}                                                                                                                                                                                                                                     & \multicolumn{3}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}                                                                                                             \\ \cline{2-18}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}철근\\ 콘크리트\end{tabular}}}      & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 1.00}} & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.30}}                                                                                                                                                                                                                                  & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.15}}                                                                                                                                                                                                                                  & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.30}}                                                                                                                                                                                                                                  & \multicolumn{3}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.30}}                                                                                                          \\ \cline{2-18}
\multicolumn{1}{|l|}{\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}수용성 염소이온량\\ (결합재 중량비 \%)2)\end{tabular}}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}프리스트레스트\\ 콘크리트\end{tabular}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.06}} & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.06}}                                                                                                                                                                                                                                  & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.06}}                                                                                                                                                                                                                                  & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.06}}                                                                                                                                                                                                                                  & \multicolumn{3}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.06}}                                                                                                          \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 추가 요구조건}}                                                                                                                                                                                                           & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} -}}    & \multicolumn{8}{l|}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} KDS 14 20 50 (4.3)의 피복두께 규정을 만족할 것.}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            & \multicolumn{4}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}결합재 종류 및 결합재 중 혼화재 사용비율 제한\\ (표 2.2-7)\end{tabular}}}                                                                                                                                                        & \multicolumn{3}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}결합재 종류 및 염화칼슘 혼화제\\ 사용 제한\\ (표 1.9-4)\end{tabular}}}                                 \\ \hline
\multicolumn{18}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 경량골재 콘크리트에는 적용하지 않음. 실적, 연구성과 등에 의하여 확증이 있을 때는 5％ 더한 값으로 할 수 있음.\\ 2) KS F 2715 적용, 재령 28일∼42일 사이\end{tabular}}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 굳은 콘크리트의 수용성 염소이온량"];
    B["KCS 14 20 10 1.8.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 10 1.8.1 (5)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 재령 28일이 경과한 굳은 콘크리트의 수용성 염소 이온량"/];
		VarIn2[/"입력변수: 결합재 종류"/];
		VarIn3[/"입력변수: 노출 범주 및 등급"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"결합재 종류" }

		D --> |"'무근콘크리트'"|Z([Pass or Fail])
		D --> |"'철근콘크리트'"|E{노출 범주 및 등급}
		D --> |"'프리스트레스트 \n콘크리트'"|G{노출 범주 및 등급}

		E --> |"'일반'"|H{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=1.00}
		E --> |"'EC'"|I{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.30}
		E --> |"'ES'"|J{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.15}
		E --> |"'EF'"|K{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.30}
		E --> |"'EA'"|L{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.30}

		G --> |"'일반'"|M{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=1.00}
		G --> |"'EC'"|N{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.30}
		G --> |"'ES'"|O{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.15}
		G --> |"'EF'"|P{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.30}
		G --> |"'EA'"|Q{재령 28일이\n 경과한 굳은\n 콘크리트의\n 수용성 염소\n 이온량 <=0.30}

		H --> Z
		I --> Z
		J --> Z
		K --> Z
		L --> Z
		M --> Z
		N --> Z
		O --> Z
		P --> Z
		Q --> Z
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def water_soluble_chlorine_ions_in_cured_concrete(sITypBin, sICatUne, fIChlIon) -> RuleUnitResult:
        """재령 28일이 경과한 굳은 콘크리트의 수용성 염소 이온량

        Args:
            sITypBin (str): 결합재 종류
            sICatUne (str): 노출 범주 및 등급
            fIChlIon (float): 재령 28일이 경과한 굳은 콘크리트의 수용성 염소 이온량

        Returns:
            pass_fail (bool): 일반콘크리트 1.8.1 염화물 함유량 (5)의 판단 결과
        """
        assert isinstance(sITypBin, str)
        assert isinstance(sICatUne, str)
        assert isinstance(fIChlIon, float)
        assert sITypBin in ["무근콘크리트", "철근콘크리트", "프리스트레스트콘크리트"]
        assert sICatUne in ["일반", "EC", "ES", "EF", "EA", "E0", "EC1", "EC2", "EC3", "EC4", "ES1", "ES2", "ES3", "ES4", "EF1", "EF2", "EF3", "EF4", "EA1", "EA2", "EA3"]
        assert 0 <= fIChlIon <= 100

        if sITypBin == "무근콘크리트":
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True
                }
            )
        elif sITypBin == "철근콘크리트":
            if (sICatUne == "E0") or (sICatUne == "일반"):
                if fIChlIon <= 1:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            elif (sICatUne == "EC") or (sICatUne == "EC1") or (sICatUne == "EC2") or (sICatUne == "EC3") or (sICatUne == "EC4"):
                if fIChlIon <= 0.3:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            elif (sICatUne == "ES") or (sICatUne == "ES1") or (sICatUne == "ES2") or (sICatUne == "ES3") or (sICatUne == "ES4"):
                if fIChlIon <= 0.15:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            elif (sICatUne == "EF") or (sICatUne == "EF1") or (sICatUne == "EF2") or (sICatUne == "EF3") or (sICatUne == "EF4"):
                if fIChlIon <= 0.3:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
            elif (sICatUne == "EA") or (sICatUne == "EA1") or (sICatUne == "EA2") or (sICatUne == "EA3"):
                if fIChlIon <= 0.3:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": True
                        }
                    )
                else:
                    return RuleUnitResult(
                        result_variables = {
                            "pass_fail": False
                        }
                    )
        elif sITypBin == "프리스트레스트콘크리트":
            if fIChlIon <= 0.06:
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": True
                    }
                )
            else:
                return RuleUnitResult(
                    result_variables = {
                        "pass_fail": False
                    }
                )