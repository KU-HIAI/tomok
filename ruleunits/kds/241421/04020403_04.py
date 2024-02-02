import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020403_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.4.3 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '건조수축에 의한 곡률'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.3 직접 처짐 계산에 의한 검증
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
    A["건조수축에 의해 유발된 곡률"];
    B["KDS 24 14 21 4.2.4.3 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 건조수축에 의해 유발된 곡률/];
		VarIn2[/입력변수: 콘크리트 유효탄성계수를 적용한 탄성계수비/];
		VarIn3[/입력변수: 건조수축 변형률/];
		VarIn4[/입력변수: 단면 도심에 대한 철근 면적의 1차모멘트/];
		VarIn5[/입력변수: 단면 2차모멘트/];
		VarIn6[/입력변수: 콘크리트 유효탄성계수를 적용한 탄성계수비/];
		VarIn7[/입력변수: 건조수축 변형률/];
    VarIn8[/입력변수: 단면 도심에 대한 철근 면적의 1차모멘트/];
		VarIn9[/입력변수: 단면 2차모멘트/];
		VarOut1[/출력변수: 건조수축에 의해 유발된 곡률/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5  & VarIn6
		VarIn5~~~VarIn7 & VarIn8  & VarIn9
		end
		Python_Class ~~~ Variable_def--->C--->F
		C["<img src='https://latex.codecogs.com/svg.image?\frac{1}{r_{sh}}=n\varepsilon&space;_{sh}\frac{S}{I}'>---------------------------------"]


		F(["건조수축에 의해 유발된 곡률"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def flange_width(fO1rsh,fIn,fIepsilonsh,fIS,fII) -> float:
        """건조수축에 의한 곡률

        Args:
             fO1rsh (float): 건조수축에 의해 유발된 곡률
             fIn (float): 콘크리트 유효탄성계수를 적용한 탄성계수비
             fIepsilonsh (float): 건조수축 변형률
             fIS (float): 단면 도심에 대한 철근 면적의 1차모멘트
             fII (float): 단면 2차모멘트

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (4)의 값
        """

        fO1rsh = fIn * fIepsilonsh * fIS / fII
        return fO1rsh


# 

