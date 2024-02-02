import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04060402_03(RuleUnit): # KDS241712_04060402_03

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.6.4.2 (3)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '전단성능'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.4 주탑 및 교각의 내진성능검증
    4.6.4.2 전단성능 검증
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
    A[전단성능 검증];
    B["KDS 24 17 12 4.6.4.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수:전단강도 /];
		VarOut2[/출력변수: 콘크리트 전단강도/];
    VarIn1[/입력변수: 콘크리트 기준압축강도/];
		VarIn2[/입력변수:검토단면에서 최대응답시의 모멘트와 전단력의 비/];
		VarIn3[/입력변수:고려하는 방향으로의 단면의 치수/];
		VarIn4[/입력변수:β=0.6+22*ρsolid/];
		VarIn5[/입력변수:단면의 외형치수에 대한 축방향 철근비/];
		VarIn6[/입력변수:소요변위연성도로서 항복변위에 대한 최대응답변위의 비/];
		VarIn7[/입력변수:축하중/];
		VarIn8[/입력변수:콘크리트 전단면적/];
		VarIn9[/입력변수:α=1.0-0.22*a/h/];
		VarIn10[/입력변수:모멘트/];
		VarIn11[/입력변수:전단력/];
		VarOut3[/출력변수: 철근 전단강도/];
		VarIn12[/입력변수:전단철근의 단면적/];
		VarIn13[/입력변수:전단철근의 항복강도/];
		VarIn14[/입력변수:단면의 유효깊이/];
		VarIn15[/입력변수:전단철근의 배근간격/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
		VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14 & VarIn15
		end
		Python_Class ~~~ Variable_def;


		D(["<img src='https://latex.codecogs.com/svg.image?V_{n}=V_{c}+V_{s}'>--------------------------------------------------------"]);
		E["<img src='https://latex.codecogs.com/svg.image?&space;V_{c}=0.5\sqrt{f_{ck}}\alpha\beta\gamma\sqrt{1&plus;\frac{P}{f_{ck}A_{g}}}A_{e}'>--------------------------------------------------------"];
		Variable_def --> E & F--->D
		F["<img src='https://latex.codecogs.com/svg.image?V_{s}=\frac{A_{v}f_{y}d}{s}'>--------------------------------------------------------"];
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Verification_of_shear_performance(fOVn,fOVc,fIfck,fIa,fIh,fIbeta,fIrhosolid,fImu,fIP,fIAa,fIAe,fIalpha,fim,fIV,fOVs,fIAy,fIfy,fId,fIs) -> float:
        """전단성능
        Args:
            fOVn (float): 전단강도
            fOVc (float): 콘크리트 전단강도
            fIfck (float): 콘크리트 기준압축강도
            fIa (float): 검토단면에서 최대응답시의 모멘트와 전단력의 비
            fIh (float): 고려하는 방향으로의 단면의 치수
            fIbeta (float): 0.6+22*ρsolid
            fIrhosolid (float): 단면의 외형치수에 대한 축방향 철근비
            fImu (float): 소요변위연성도로서 항복변위에 대한 최대응답변위의 비
            fIP (float): 축하중
            fIAa (float): 콘크리트 전단면적
            fIAe (float): 콘크리트 유효단면적
            fIalpha (float): 1.0-0.22*a/h
            fim (float): 모멘트
            fIV (float): 전단력
            fOVs (float): 철근 전단강도
            fIAy (float): 전단철근의 단면적
            fIfy (float): 전단철근의 항복강도
            fId (float): 단면의 유효깊이
            fIs (float): 전단철근의 배근간격



        Returns:
            float: 교량내진 설계기준(케이블교량) 4.6.4.2 (3) 의 값
        """
        r = (6-fImu)/4
        fOVc = 0.5*(fIfck)**0.5*fIalpha*fIbeta*r*(1+1000*fIP/fIfck/fIAa)**0.5*fIAe/1000
        fOVs = fIAy*fIfy*fId/fIs/1000
        fOVn = fOVc+fOVs
        return(fOVn)


