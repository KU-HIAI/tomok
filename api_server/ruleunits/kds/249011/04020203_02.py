import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020203_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '가동받침의 이동량'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.2 설계일반
    4.2.2.3 이동량
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가동받침의 이동량];
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

		Python_Class ~~~ C(["KDS 24 90 11 4.2.2.3 (2)"])
		C --> Variable_def;

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

    @rule_method
    def Movable_Bearing_Change(fIalpha,fIl,fIbeta,fIPi,fIAc,fIEc,fIphi,fIdeltaT,fIi,fIhi,fIthetai) -> float:
        """가동받침의 이동량

        Args:
            fIalpha (float): 열팽창계수
            fIl (float): 신축거더 길이
            fIbeta (float): 건조수축, 크리프의 저감계수
            fIPi (float): 프리스트레싱 직후의 PS 강재에 작용하는 인장력
            fIAc (float): 콘크리트 단면적
            fIEc (float): 콘크리트 탄성계수
            fIphi (float): 콘크리트의 크리프계수
            fIdeltaT (float): 건조수축에 해당하는 온도변화
            fIi (float): 반복계수
            fIhi (float): 거더의 중립축으로부터 받침의 회전중심까지의 거리
            fIthetai (float): 받침 상부의 거더의 회전각


        Returns:
            fOmovnch (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.2.3 이동량 (2)의 값 1
            fOdeltalt (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.2.3 이동량 (2)의 값 2
            fOdeltalr (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.2.3 이동량 (2)의 값 3
            fOdeltals (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.2.3 이동량 (2)의 값 4
            fOdeltalc (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.2.3 이동량 (2)의 값 5
        """

        assert isinstance(fIalpha, float)
        assert isinstance(fIl, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIPi, float)
        assert isinstance(fIAc, float)
        assert isinstance(fIEc, float)
        assert isinstance(fIphi, float)
        assert isinstance(fIdeltaT, float)
        assert isinstance(fIi, float)
        assert isinstance(fIhi, float)
        assert isinstance(fIthetai, float)

        fOdeltalt = fIdeltaT * fIalpha * fIl
        fOdeltalr = sum(fIhi[j] * fIthetai[j] for j in range(fIi))
        fOdeltals = fIdeltaT * fIalpha * fIl * fIbeta
        fOdeltalc = (fIPi / (fIAc * fIEc)) * fIphi * fIl * fIbeta

        fOmovnch = fOdeltalt + fOdeltalr + fOdeltals + fOdeltalc


        return RuleUnitResult(
            result_variables = {
                "fOmovnch": fOmovnch,
            }
        )