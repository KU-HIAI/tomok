import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244010_010401_06(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 24 40 10 1.4.1 (6)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2018-08-30'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '	교량점검시설'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량점검시설
    1. 일반사항
    1.4 시스템 설명
    1.4.1 설치기준 및 규격
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### 1.4.1 설치기준 및 규격
    (6) 점검계단 및 점검통로의 규격은 표 1.4-1에서 규정한 이상으로 하여야 한다.
\begin{table}[]
\begin{tabular}{lll}
\cline{1-2}
\multicolumn{1}{|l|}{구분}                                               & \multicolumn{1}{l|}{}               & 규격                                                                \\ \cline{1-2}
\rowcolor[HTML]{FFFFFF}
\multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 점검계단}}                                      & {\color[HTML]{333333} 유효폭: 0.60 m}                                \\
\rowcolor[HTML]{FFFFFF}
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                        & {\color[HTML]{333333} 통로}           & \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                   \\
\rowcolor[HTML]{FFFFFF}
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                        & {\color[HTML]{333333} 난간}           & \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                   \\
\rowcolor[HTML]{FFFFFF}
\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 출입 통로}} & {\color[HTML]{333333} 출입사다리 및 출입계단} & \multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}
\end{tabular}
\end{table}
"""

    # 플로우차트(mermaid)
    flowchart = """
 flowchart TD
    subgraph Python_Class
    A["Title: 점검계단 및 점검통로의 규격"];
    B["KCS 24 40 30 1.4.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 30 1.4.1 (6)"])

    subgraph Variable_def
    VarOut[/"출력변수: 점검계단 및 점검통로의 규격"/];
    VarIn1[/"입력변수: 점검계단"/];
    VarIn2[/입력변수: 통로/];
    VarIn3[/입력변수: 난간/];
    VarIn4[/입력변수: 출입사다리/];
    VarIn5[/입력변수: 출입계단/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"구분"}
		D --> |점검계단|E["유효폭: 0.60 m"]
		D --> |통로|F["유효폭: 0.80 m"]
		D --> |난간|G["유효높이: 1.1 m \n 난간 레일: 3단 \n레일수직간격: 0.3 m"]
		D --> |출입사다리|H["발판폭: 0.50 m, 원형 지지대 내경: 0.60 m \n 경사형 출입계단 발판의 깊이: 130 mm 이상\n경사형 출입계단 발판의 높이: 250 mm 이하\n경사형 출입계단의 각도: 45°내외\n발판과 손잡이에 미끄럼방지 시설 설치\n"]
		D --> |출입계단|H

		E --> I([점검계단 및 점검통로의 규격])
		F --> I
		G --> I
		H --> I

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def specifications_of_inspection_stairs_and_passage(bIInsSta, bIPas, bIHan, bIAccLad, bIAccSta) ->str :
        """점검계단 및 점검통로의 규격

        Args:
            bIInsSta (boolean): 점검계단. ifc 파일에 기술된 어떤 부재가 가지고 있는 값에 해당
            bIPas (boolean): 통로
            bIHan (boolean): 난간
            bIAccLad (boolean): 출입사다리
            bIAccSta (boolean): 출입계단

        Returns:
            sOSpeSta (string) : 점검계단 및 점검통로의 규격
        """

        if bIInsSta == True:
            sOSpeSta = "유효폭: 0.60 m"
            return sOSpeSta
        elif bIPas == True:
            sOSpeSta = "유효폭: 0.80 m"
            return sOSpeSta
        elif bIHan == True:
            sOSpeSta = "유효높이: 1.1 m / 난간 레일: 3단 / 레일수직간격: 0.3 m"
            return sOSpeSta
        elif (bIAccLad == True) or (bIAccSta == True):
            sOSpeSta = "발판폭: 0.50 m / 원형 지지대 내경: 0.60 m / 경사형 출입계단 발판의 깊이: 130 mm 이상 / 경사형 출입계단 발판의 높이: 250 mm 이하 / 경사형 출입계단의 각도: 45°내외 / 발판과 손잡이에 미끄럼방지 시설 설치"
            return sOSpeSta