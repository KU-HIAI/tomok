import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142024_040301_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 14 20 24 4.3.1 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '타이의 공칭강도'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.3 타이의 인장강도
    4.3.1 강도 산정
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[타이의 공칭강도];
    B["KDS 14 20 24 4.3.1 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 타이의 공칭강도/];
    VarIn1[/입력변수 : 계수축력에 의한 긴장재의 응력 증가분/];
    VarIn2[/입력변수 : 긴장재의 유효 프리스트레스 응력/];
    VarIn3[/입력변수 : 긴장재 타이의 단면적/];
    VarIn4[/입력변수 : 철근의 설계기준항복강도/];
    VarIn5[/입력변수 : 철근타이의 단면력/];
    VarIn6[/입력변수 : 긴장재의 설계기준항복강도/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    end
    Python_Class~~~Variable_def
    D{"긴장재가 부착된 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\Delta&space;f_{p}=420MPa'>----------------------"];
    F{"해석에 의해 증명된 경우"};
    G["<img src='https://latex.codecogs.com/svg.image?\Delta&space;f_{p}=70MPa'>----------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?\Delta&space;f_{p}'>해석으로 증명된 값 사용"];
    I["<img src='https://latex.codecogs.com/svg.image?f_{pe}&plus;\Delta&space;f_{p}<f_{py}'>----------------------"];
    J["<img src='https://latex.codecogs.com/svg.image?F_{nt}=A_{st}f_{y}&plus;A_{ps}(f_{pe}&plus;\Delta&space;f_{p})'>---------------------------------"];
    K(["타이의 공칭강도"]);
    Variable_def--->D--Yes--->E--->I--->J--->K
    D--No --->F--Yes--->H--->I
    F--No --->G--->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_strength_of_tie(fOFnt,fIfpe,fIdelfp,fIfy,fIAst,fIAps,fIuserdefined) -> float:
        """타이의 공칭강도

        Args:
            fOFnt (float): 타이의 공칭강도
            fIfpe (float): 긴장재의 유효프리스트레스 응력
            fIdelfp (float): 계수축력에 의한 긴장재의 응력 증가분
            fIfy (float): 철근의 설계기준항복강도
            fIAst (float): 철근타이의 단면적
            fIAps (float): 긴장재타이의 단면력
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트 스트럿-타이모델 기준  4.3.1 강도 산정 (1)의 타이의 공칭강도 값
        """

        #부착된 긴장재의 경우: fIuserdefined = 1
        #부착되지 않는 긴장재의 경우: fIuserdefined = 2

        if fIuserdefined == 1:
          fOFnt = (fIAst*fIfy+fIAps*(fIfpe+420))
        elif fIuserdefined == 2:
          fOFnt = (fIAst*fIfy+fIAps*(fIfpe+70))
        else:
          fOFnt = (fIAst*fIfy+fIAps*(fIfpe+fIdelfp))

        return fOFnt


# 

