import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '가동받침의 이동량'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.2 설계일반
    4.2.2.3 이동량
    (2)
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
    A[전단성능 검증];
    B["KDS 24 90 11 4.2.2.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 가동받침의 이동량/];
    VarIn1[/입력변수: 온도변화에 의한 이동량/];
		VarIn2[/입력변수: 활하중으로 거더의 처짐에 의한 이동량/];
		VarIn3[/입력변수:콘크리트의 건조수축에 의한 이동량/];
		VarIn4[/입력변수:콘크리트의 크리프에 의한 이동량/];
		VarIn5[/입력변수:열팽창계수/];
		VarIn6[/입력변수:신축거더 길이/];
		VarIn7[/입력변수:건조수축, 크리프의 저감계수/];
		VarIn8[/입력변수:프리스트레싱 직후의 PS 강재에 작용하는 인장력/];
		VarIn9[/입력변수:콘크리트 단면적/];
		VarIn10[/입력변수:콘크리트 탄성계수/];
		VarIn11[/입력변수:콘크리트의 크리프계수/];
		VarIn12[/출력변수:건조수축에 해당하는 온도변화/];
		VarIn13[/입력변수:거더의 중립축으로부터 받침의 회전중심까지의 거리/];
		VarIn14[/입력변수:받침 상부의 거더의 회전각/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->G & H
		G & H--->D
		G--->E
		G["β= 건조수축, 크리프의 저감계수"]
		G~~~ |"KDS 24 90 11 table 4.2-1"| G
		H["Φ= 콘크리트 크리프계수"]
		H~~~|"KDS 24 90 11 table 4.2-2"| H
		D["<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;l_{c}=\frac{P_{i}}{E_{c}A_{c}}\phi&space;l\beta&space;'>--------------------------------------------------------"];
		E["<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;l_{s}=\bigtriangleup&space;T\alpha&space;l\beta&space;'>--------------------------------------------------------"];
		Variable_def--->F
		F["<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;l_{t}=\bigtriangleup&space;T\alpha&space;l'>--------------------------------------------------------"];
		J["<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;l_{r}=\sum(h_{i}\theta&space;_{i})'>--------------------------------------------------------"];
	  Variable_def--->J
	  D & E & F & J---->K--->L
	  K["<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;l=\bigtriangleup&space;l_{t}&plus;\bigtriangleup&space;l_{r}&plus;\bigtriangleup&space;l_{s}&plus;\bigtriangleup&space;l_{c}'>--------------------------------------------------------"];
	  L(["가동받침의 이동량"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Movable_Bearing_Change(fOmovnch,fIdeltalt,fIdeltalr,fIdeltals,fIdeltalc,fIalpha,fIl,fIbeta,fIPi,fIAc,fIEc,fIphi,fIdeltaT,fIhi,fIthetai) -> float:
        """가동받침의 이동량

        Args:
            fOmovnch (float): 가동받침의 이동량
            fIdeltalt (float): 온도변화에 의한 이동량
            fIdeltalr (float): 활하중으로 거더의 처짐에 의한 이동량
            fIdeltals (float): 콘크리트의 건조수축에 의한 이동량
            fIdeltalc (float): 콘크리트의 크리프에 의한 이동량
            fIalpha (float): 열팽창계수
            fIl (float): 신축거더 길이
            fIbeta (float): 건조수축, 크리프의 저감계수
            fIPi (float): 프리스트레싱 직후의 PS 강재에 작용하는 인장력
            fIAc (float): 콘크리트 단면적
            fIEc (float): 콘크리트 탄성계수
            fIphi (float): 콘크리트의 크리프계수
            fIdeltaT (float): 건조수축에 해당하는 온도변화
            fIhi (float): 거더의 중립축으로부터 받침의 회전중심까지의 거리
            fIthetai (float): 받침 상부의 거더의 회전각

        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.2.2.3 이동량 (2)의 값
        """

        fOmovnch = fIdeltaT*fIalpha*fIl+fIhi*fIthetai+fIdeltaT*fIalpha*fIl*fIbeta+fIPi*fIphi*fIl*fIbeta/(fIAc*fIEc)
        return fOmovnch


# 

