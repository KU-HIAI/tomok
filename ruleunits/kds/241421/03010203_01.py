import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010203_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전체 변형률'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.3 크리프
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
    A["시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘"];
    B["KDS 24 14 21 3.1.2.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 시간 t'에서 작용응력/];
		VarIn2[/입력변수: 설계기준압축강도/];
    VarIn3[/입력변수: 콘크리트의 압축강도/] ;
		VarIn4[/입력변수: 부재의 크기/] ;
		VarIn5[/입력변수: 평균 상대습도/] ;
		VarIn6[/입력변수: 재하할 때의 재령/] ;
		VarIn7[/입력변수: 재하기간/] ;
		VarIn8[/입력변수: 시멘트의 종류/] ;
		VarIn9[/입력변수: 양생온도/] ;
		VarIn10[/입력변수: 온도변화/] ;
		VarIn11[/입력변수: 작용응력의 크기/] ;
		VarIn12[/입력변수: 재령t'일에서의 초기접선 탄성계수/] ;
		VarIn13[/입력변수: 재령 28일에서의 초기접선 탄성계수/] ;
		VarIn14[/입력변수: 강도보정계수/] ;
	 	VarOut1[/출력변수: 전체 변형률/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C["<img src='https://latex.codecogs.com/svg.image?E_{ci}=1.18E_{c}'>--------------------------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?E_{ci}(t')=\sqrt{\beta&space;_{cc}(t)}E_{ci}'>---------------------------------"]
		C--->D
		D--->E
		E["<img src='https://latex.codecogs.com/svg.image?\varepsilon_{c\sigma}(t,t')=f_{c}(t')[\frac{1}{E_{ci}(t')}+\frac{\varphi(t,t')}{E_{ci}}]'>---------------------------------"]
		E--->F
		F([전체변형률])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def total_strain(fOepsiloncottprime,fIfctprime,fIEcitprime,fIEci,fIbetacct,fIEc) -> float:
        """전체 변형률

        Args:
             fOepsiloncottprime (float): 시간 t'에서 작용응력
             fIfctprime (float): 전체 변형률
             fIEcitprime (float): 재령 t'일에서의 초기접선 탄성계수
             fIEci (float): 재령 28일에서의 초기접선 탄성계수
             fIbetacct (float): 강도 보정 계수
             fIEc (float): 보통 콘크리트의 탄성계수


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.3 크리프 (1)의 값
        """

        fIEci = 1.18*fIEc
        fIEcitprime = (fIbetacct)**0.5 * fIEci
        fOepsiloncottprime = fIfctprime * (1/fIEcitprime+fIfctprime/fIEci)
        return fOepsiloncottprime


# 

