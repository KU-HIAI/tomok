import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03020301_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 51 3.2.3.1 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '편심하중을 받는 기초의 감소된 유효면적'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.1 지지력
    (5)
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
    A["편심하중의 영향"];
    B["KDS 24 14 51 3.2.3.1 (5)"];
    A ~~~ B
    end



		subgraph Variable_def;
		    VarIn1[/입력변수:유효면적/];
		    VarIn2[/입력변수:수정된 B방향 길이/];
		    VarIn3[/입력변수:수정된 L방향 길이/];
		    VarIn4[/입력변수:B방향의 편심거리/];
		    VarIn5[/입력변수:L방향의 편심거리/];
		    VarIn6[/입력변수:감가된 지지력/];
		    VarIn7[/입력변수:설계하중/];
		    VarIn8[/입력변수:기초의 편심/];
		    VarIn9[/입력변수:기초의 크기/];


		    VarIn1
		    VarIn2 ~~~ VarIn3 ~~~ VarIn4
		    VarIn5 ~~~ VarIn6 ~~~ VarIn7
		    VarIn8 ~~~ VarIn9
        end

		    Python_Class ~~~ Variable_def
        Variable_def--->C
		    C["감가된 지지력 ≥ 설계하중"]
		    C--->D & F
		    D["지진하중을 고려하는 극단상황한계상태"]
		    D--->E
		    E["B or L < 4/10"]
		    F["B or L < 1/4"]
		    E & F ---> G
		    G["<img src='https://latex.codecogs.com/svg.image?B^\prime=B-2e_B'>---------------------------------"]
		    G-->H
		    H["<img src='https://latex.codecogs.com/svg.image?L^\prime=L-2e_L'>---------------------------------"]
		    H-->I
		    I["<img src='https://latex.codecogs.com/svg.image?B^\prime\times&space;L^\prime'>---------------------------------"]
		    I--->J
		    J["편심하중을 받는 기초의 감소된 유효면적"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_area (fOEffare, fIBp, fILp, fIEb, fIEl, fIdimsup, fIDgnlod, fIEccfou, fIB, fIuserdefined) -> float:
        """편심하중을 받는 기초의 감소된 유효면적
        Args:
            fOEffare (float): 유효면적
            fIBp (float): 수정된 B방향 길이
            fILp (float): 수정된 L방향 길이
            fIEb (float): B방향의 편심거리
            fIEl (float): L방향의 편심거리
            fIdimsup (float): 감가된 지지력
            fIDgnlod (float): 설계하중
            fIEccfou (float): 기초의 편심
            fIB (float): 기초의 B 크기
            fILp (float): 기초의 L 크기
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (5)의 편심하중을 받는 기초의 감소된 유효면적값
        """

        #극단상황한계상태 : fIuserdefined == 1
        if fIdimsup >= fIDgnlod:
          if fIuserdefined == 1:
            if fIEb < fIB/4 and fIEl < fIL/4:
              fIBp = fIB - 2*fIEb
              fILp = fIL - 2*fIEl
              fOEffare = fIBp * fILp
              return "Pass", fOEffare
            else:
              return "Fail"
          else:
            if fIEb < fIB*0.4 and fIEl < fIL*0.4:
              fIBp = fIB - 2*fIEb
              fILp = fIL - 2*fIEl
              fOEffare = fIBp * fILp
              return "Pass", fOEffare
            else:
              return "Fail"
        else:
          return "Fail"




# 

