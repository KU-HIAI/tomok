import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020302_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '부착된 프리스트레스 긴장재 중심으로부터 150mm 이내의 사각형 단면 내에 필요한 최소 철근량'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.2 최소철근량
    (3)
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
    A["최소철근량"];
    B["KDS 24 14 21 4.2.3.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 프리스트레스 긴장재의 단면적/];
		VarIn2[/입력변수: 철근과 긴장재의 부착특성 및 지름의 차이에 따른 영향을 반영하기 위한 계수/];
		VarIn3[/입력변수: 철근과 프리스트레싱 강재의 부착강도 비/];
		VarIn4[/입력변수: 철근 지름/];
		VarIn5[/입력변수: 프리스트레싱 강재의 등가지름/];
		VarIn6[/입력변수: 프리스트레싱 강재의 면적/];
		VarIn7[/입력변수: 연선의 지름/];
		VarOut1[/출력변수:최소 철근량/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5  & VarIn6 & VarIn7
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->D
		Variable_def--철근은 사용되지 않고 프리스트레싱 강재만 사용된 경우--->C
		C["<img src='https://quicklatex.com/cache3/3d/ql_f541c74dbd6864a2ccfb0dc283bc653d_l3.png'>---------------------------------"]
		D--다발 프리스트레싱 강재--->F
		D{"<img src='https://latex.codecogs.com/svg.image?d_{p,eq}'>---------------------------------"}
		D--7연선 1가닥--->G
		D--3연선 1가닥--->H
		F["<img src='https://latex.codecogs.com/svg.image?d_{p,eq}=1.6\sqrt{A_p}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?d_{p,eq}=1.75d_{wire}'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?d_{p,eq}=1.2d_{wire}'>---------------------------------"]
		I["<img src='https://quicklatex.com/cache3/f3/ql_0a2a6ee5d956bcd187cb8bfdf13a07f3_l3.png'>---------------------------------"]
		F & G & H--->I
		I~~~|table 24 14 21 4.2-3|I
		C--->J
		I--->J--->K
		J["<img src='https://quicklatex.com/cache3/25/ql_40f741d3c69c715f84195efa89b00625_l3.png'>---------------------------------"]
		K(["최소 철근량"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_amount_of_rebar(fOAsmin,fIAp,fIxi1,fIxi,fIdb,fIdpeq,fIdwire,fIAsmin,fIuserdefined1,fIuserdefined2) -> float:
        """부착된 프리스트레스 긴장재 중심으로부터 150mm 이내의 사각형 단면 내에 필요한 최소 철근량

        Args:
             fOAsmin (float): 최소 철근량
             fIAp (float): 프리스트레스 긴장재의 단면적
             fIxi1 (float): 철근과 긴장재의 부착특성 및 지름의 차이에 따른 영향을 반영하기 위한 계수
             fIxi (float): 철근과 프리스트레싱 강재의 부착강도 비
             fIdb (float): 철근 지름
             fIdpeq (float): 프리스트레싱 강재의 등가지름
             fIdwire (float): 연선의 지름
             fIAsmin (float): 감소시키기 이전의 최소철근량
             fIuserdefined1 (float): 사용자 선택: 철근의 사용 여부
             fIuserdefined2 (float): 사용자 선택: 프리스트레싱 강재의 종류



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (3)의 값
        """

        #철근은 사용되지 않고 프리스트레싱 강재만 사용된 경우: fIuserdefined1 = 1
        #철근이 사용된 경우: fIsuerdefined1 = 2
        if fIuserdefined1 == 1:
          fIxi1 = fIxi**0.5
        #다발 프시스트레싱 강재: fIuserdefined2 = 1
        #7연선 1가닥: fIuserdefined2 = 2
        #3연선 1가닥: fIuserdefined2 = 3
        elif fIuserdefined1 == 2:
          if fIuserdefined2 == 1:
            fIdpeq = 1.6 * (fIAp**0.5)
          elif fIuserdefined2 == 2:
            fIdpeq = 1.75 * fIdwire
          elif fIuserdefined2 == 3:
            fIdpeq = 1.20 * fIdwire
          fIxi1 = (fIxi * fIdb / fIdpeq)**0.5
        fOAsmin = fIAsmin - fIxi1 * fIAp

        return fOAsmin


# 

