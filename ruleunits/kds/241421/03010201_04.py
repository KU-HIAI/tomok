import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010201_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.1 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '평균인장강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (4)
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
    A[평균인장강도];
    B["KDS 24 14 21 3.1.2.1 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 쪼갬 인장강도의 평균값/];
		VarIn2[/입력변수: 휨인장강도의 평균값/];
		VarIn3[/입력변수: 콘크리트의 평균압축강도/];
		VarIn4[/입력변수: 강도 보정 계수/];
		VarIn5[/입력변수: α/];
		VarIn6[/재령 28일 평균인장강도/];
		VarIn7[/평균인장강도/];
 	  VarOut1[/출력변수: 평균인장강도/];
		VarOut2[/출력변수: 기준인장강도/];
		VarOut3[/출력변수: 재령에서의 콘크리트 인장강도/];

	  VarOut1 ~~~VarIn1
		VarOut1 ~~~VarIn2
		VarOut1~~~VarIn3
	  VarOut2~~~VarIn7
  	VarOut3~~~VarIn4 & VarIn5 & VarIn6
		end
		Python_Class ~~~ Variable_def;
		Variable_def---->D--->F
		Variable_def---->E--->F
		Variable_def---->G--->F
		D["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.9f_{spm'>--------------------------------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.5f_{rm'>--------------------------------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.3(f_{cm})^{3/2'>--------------------------------------------------------"]
		F(["평균인장강도"]);
		I(["콘크리트의 기준인장강도"]);
		H["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctk}=0.7f_{ctm}'>--------------------------------------------------------"]
		Variable_def---->H--->I
		J["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}(t)=[\beta_{cc}(t)]^{\alpha}f_{ctm}'>--------------------------------------------------------"]
		Variable_def---->J--->K
		K(["재령에서의 콘크리트 인장강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Concrete_tensild_strength(fOfctm,fOfctk,fOfctmt,fIfspm,fIfrm,fIfcm,fIbetacc,fIt,fIalpha,fIfctm,fIuserdefined) -> float:
        """평균인장강도

        Args:
             fOfctm (float): 평균인장강도
             fOfctk (float): 콘크리트의 기준인장강도
             fOfctmt (float): 각 재령에서의 콘크리트 인장강도
             fIfspm (float): 쪼갬 인장강도의 평균값
             fIfrm (float): 휨인장강도의 평균
             fIfcm (float): 콘크리트의 평균압축강도
             fIbetacc (float): 강도 보정 계수
             fIt (float): 콘크리트의 재령
             fIalpha (float): t가 28일 미만이면 1, t가 28일 이상이면 2/3
             fIfctm (float): 재령 28일 평균인장강도
             fIuserdefined (float): 사용자 선택


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.1 강도 (4)의 값
        """

        # 콘크리트 쪼갬 인장강도로부터 콘크리트 평균인장강도를 경정하는 경우: fIuserdefined = 1
        # 콘크리트 휨인장강도로부터 콘크리트 평균인장강도를 결정하는 경우: fIuserdefined = 2
        # 콘크리트 평균압축강도로부터 콘크리트 평균인장강도를 결정하는 경우: fIuserdefined = 3
        # 콘크리트 기준인장강도를 결정하는 경우:  fIuserdefined = 4
        # 각 재령에서의 콘크리트 인장강도를 결정하는 경우: fIuserdefined = 5
        if fIuserdefined == 1:
          fOfctm = 0.9 * fIfspm
          return fOfctm
        elif fIuserdefined == 2:
          fOfctm = 0.5 * fIfrm
          return fOfctm
        elif fIuserdefined == 3:
          fOfctm = 0.3 * fIfcm**(2/3)
          return fOfctm
        elif fIuserdefined == 4:
          fOfctk = 0.7 * fOfctm
          return fOfctk
        elif fIuserdefined == 5:
          if fIt < 28:
            fIalpha = 1
          elif fIt >= 28:
            fIalpha = 2/3
          fOfctmt = (fIbetacc**fIalpha) * fIfctm
          return fOfctmt


# 

