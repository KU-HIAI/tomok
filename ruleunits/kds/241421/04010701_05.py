import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010701_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.7.1 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '스트럿의 최대 유효강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.1 판요소 설계
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
    A["콘크리트 스트럿의 최대 유효강도"];
    B["KDS 24 14 21 4.1.7.1 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 항복강도/];
		VarIn2[/입력변수: 콘크리트 압축강도 유효계수/];
		VarIn3[/입력변수: 콘크리트 기준압축강도/];
		VarIn4[/입력변수: 종방향과 횡방향 철근 응력 중에서 큰 값/];
		VarIn5[/입력변수: 철근의 재료계수/];
		VarIn6[/입력변수: 철근의 기준항복강도/];

		VarOut1[/출력변수: 콘크리트 스트럿의 최대 유효강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~VarIn4 & VarIn5 & VarIn6


		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D--->E
		C["<img src='https://latex.codecogs.com/svg.image?f_{c2,max}=[0.85-\frac{f_s}{\phi&space;_sf_y}(0.85-v)]f_{ck}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?vf_{ck}<f_{c2,max}<0.85f_{ck}'>---------------------------------"]
    E(["콘크리트 스트럿의 최대 유효강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_effective_strength_of_strut(fIyiestr,fOc2max,fInu,fIfck,fIfs,fIphis,fIfy) -> bool:
        """스트럿의 최대 유효강도

        Args:
             fIyiestr (float): 항복강도
             fOc2max (float): 콘크리트 스트럿의 최대 유효강도
             fInu (float): 콘크리트 압축강도 유효계수
             fIfck (float): 콘크리트 기준압축강도
             fIfs (float): 종방향과 횡방향 철근 응력 중에서 큰 값
             fIphis (float): 철근의 재료계수
             fIfy (float): 철근의 기준항복강도

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (5)의 통과 여부
        """

        fOc2max = (0.85-fIfs/(fIphis*fIfy)*(0.85-fInu))*fIfck
        if fInu*fIfck < fOc2max < 0.85*fIfck:
          return fOc2max, "Pass"
        else:
          return fOc2max, "Fail"


# 

