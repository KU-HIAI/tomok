import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04061203_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.12.3 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소 횡철근 단면적'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.12 포스트텐션 정착부
    4.6.12.3 정착부의 검토
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
    A["최소 횡철근 단면적"];
    B["KDS 24 14 21 4.6.12.3 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:강선에 작용하는 최대 인장력/];
		VarIn2[/입력변수:철근의 기준항복강도/];
		VarIn3[/입력변수:γp,unfav/];

		VarOut1[/출력변수:최소 횡철근 단면적/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def
		Variable_def--->E--->D--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\gamma&space;_{p,unfav}\geq&space;1.2'>---------------------------------"]

		D["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;A_s=0.15\frac{P_o}{\phi&space;_sf_y}\gamma&space;_{p,unfav}'>---------------------------------"]

		F(["최소 횡철근 단면적"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_transverse_bar_cross_section(fOAs,fIPO,fIfy,fIgpunfav,fIphis) ->bool:
        """최소 횡철근 단면적
        Args:
             fOAs (float): 축방향 철근의 최소 지름
             fIPO (float): 축방향 철근
             fIfy (float): 철근 사이의 순간격
             fIgpunfav (float): 횡철근 단면적 보정상수
             fIphis (float): 재료계수

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.12.3 정착부의 검토 (4)의 값
        """

        fIgpunfav = max(fIgpunfav, 1.2)
        fOAs = 0.15 * fIPO /(fIphis*fIfy) * fIgpunfav
        return fOAs


# 

