import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020402_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.4.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '보정값'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.2 직접 처짐 계산을 생략하는 경우
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
    A["보정값"];
    B["KDS 24 14 21 4.2.4.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지지단의 철근 인장응력/];
		VarIn2[/입력변수: 철근 인장응력/];
		VarIn3[/입력변수: 사용하중에서 지간 중앙의 인장 철근응력/];
		VarIn4[/입력변수: 극한한계상태에서 중앙단면에 필요한 철근량/];
		VarIn5[/입력변수: 지간 중앙단면에 배치된 철근량/];
		VarOut1[/출력변수: 보정값/];

		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5
		end
		Python_Class ~~~ Variable_def--->C--->E--->G

		C{"지지단 철근 인장응력=310MPa 가정"}
		E["<img src='https://latex.codecogs.com/svg.image?\frac{310}{f_s}=\frac{500}{f_y(A_{s,req}/A_s)}'>---------------------------------"]

		G(["보정값"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_value(fOcorval,fIfs,fIfy,fIAsreq,fIAs) -> float:
        """보정값

        Args:
             fOcorval (float): 보정값
             fIfs (float): 철근 인장응력
             fIfy (float): 철근의 기준항복강도
             fIAsreq (float): 극한한계상태에서 중앙단면에 필요한 철근량
             fIAs (float): 지간 중앙단면에 배치된 철근량

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.4.2 직접 처짐 계산을 생략하는 경우 (3)의 값
        """

        fOcorval = 500/(fIfy*fIAsreq/fIAs)
        return fOcorval


# 

