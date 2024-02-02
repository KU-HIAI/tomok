import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010504_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.5.4 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '타이가 정착되지 않은 압축절점에서 압축응력의 최대설계유효강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.5 스트럿-타이 모델
    4.1.5.4 절점영역
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
    A["콘크리트 스트럿의 유효설계강도"];
    B["KDS 24 14 21 4.1.5.4 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:콘크리트 스트럿의 유효설계강도/];
		VarIn2[/입력변수: 콘크리트 기준압축강도/];
		VarIn3[/입력변수: 콘크리트 재료계수/];
		VarIn4[/입력변수: 콘크리트 스트럿의 유효설계강도/];
		VarIn5[/입력변수: 압축 절점 1에서의 콘크리트 압축응력/];
		VarIn6[/입력변수: 압축 절점 1에서의 콘크리트 압축력/];
		VarIn7[/입력변수: 압축 절점 1에서의 콘크리트 바닥판의 유효폭길이/];
		VarIn8[/입력변수: 두께/];
		VarIn9[/입력변수: 압축 절점 2에서의 콘크리트 압축응력/];
		VarIn10[/입력변수: 압축 절점 2에서의 콘크리트 압축력/];
		VarIn11[/입력변수: 압축 절점 2에서의 콘크리트 바닥판의 유효폭길이/];
		VarIn12[/입력변수: 압축 절점 3에서의 콘크리트 압축응력/];
		VarIn13[/입력변수: 압축 절점 3에서의 콘크리트 압축력/];
		VarIn14[/입력변수: 압축 절점 3에서의 콘크리트 바닥판의 유효폭길이/];
		VarOut1[/출력변수: 콘크리트 스트럿의 유효설계강도/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
		VarIn5~~~VarIn8 & VarIn9 & VarIn10
		VarIn9~~~VarIn11 & VarIn12 & VarIn13 & VarIn14
		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C--타이가 정착되지 않은 압축 절점--->D--->E
		C{"타이 정착 방향에 따라"}
		D["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=(1-f_{ck}/250)\phi&space;_cf_{ck}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=max(f_{c1}=C_1/w_1t,f_c2=C_2/w_2t,f_{c3}=C_3/w_3t)'>---------------------------------"]
		C--한 쪽 타이가 있는 압축인장 절점--->F--->G
		F["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=0.85(1-f_{ck}/250)\phi&space;_cf_{ck}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=max(f_{c1}=C_1/w_1t,f_c2=C_2/w_2t)'>---------------------------------"]
		C--두 방향으로 타이가 있는 압축 인장 절점--->H
		H["<img src='https://latex.codecogs.com/svg.image?f_{cd,max}=0.75(1-f_{ck}/250)\phi&space;_cf_{ck}'>---------------------------------"]
		I(["콘크리트 스트럿의 유효설계강도"])
		E & G & H--->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_design_strength_of_concrete_struts(fOfcdmax,fIfck,fIphic,fIfc1,fIC1,fIw1,fIt,fIfc2,fIC2,fIw2,fIfc3,fIC3,fIw3,fIuserdefined) -> bool:
        """타이가 정착되지 않은 압축절점에서 압축응력의 최대설계유효강도

        Args:
             fOfcdmax (float): 콘크리트 스트럿의 유효설계강도
             fIfck (float): 콘크리트 기준압축강도
             fIphic (float): 콘크리트 재료계수
             fIfc1 (float): 압축 절점 1에서의 콘크리트 압축응력
             fIC1 (float): 압축 절점 1에서의 콘크리트 압축력
             fIw1 (float): 압축 절점 1에서의 콘크리트 바닥판의 유효폭길이
             fIt (float): 두께
             fIfc2 (float): 압축 절점 2에서의 콘크리트 압축응력
             fIC2 (float): 압축 절점 2에서의 콘크리트 압축력
             fIw2 (float): 압축 절점 2에서의 콘크리트 바닥판의 유효폭길이
             fIfc3 (float): 압축 절점 3에서의 콘크리트 압축응력
             fIC3 (float): 압축 절점 3에서의 콘크리트 압축력
             fIw3 (float): 압축 절점 3에서의 콘크리트 바닥판의 유효폭길이
             fIuserdefined (float): 사용자 선택



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.5.4 절점영역 (5)의 통과 여부
        """

        # 타이가 정착되지 않은 압축 절점: fIuserdefined = 1
        # 한쪽에 정착 타이가 있는 압축-인장 절점: fIuserdefined = 2
        # 두 방향으로 정착 타이가 있는 압축-인장 절점: fIuserdefined = 3

        if fIuserdefined == 1:
          fOfcdmax = (1-fIfck/250)*fIphic*fIfck
          fIfc1 = fIC1/(fIw1*fIt)
          fIfc2 = fIC2/(fIw2*fIt)
          fIfc3 = fIC3/(fIw3*fIt)
          fOfcdmax = max(fIfc1,fIfc2,fIfc3)

        elif fIuserdefined == 2:
          fOfcdmax = 0.85*(1-fIfck/250)*fIphic*fIfck
          fIfc1 = fIC1/(fIw1*fIt)
          fIfc2 = fIC2/(fIw2*fIt)
          fOfcdmax = max(fIfc1,fIfc2)

        elif fIuserdefined == 3:
          fOfcdmax = 0.75*(1-fIfck/250)*fIphic*fIfck
          fIfc1 = fIC1/(fIw1*fIt)

        return fOfcdmax


# 

