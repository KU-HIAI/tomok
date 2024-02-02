import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04020702_01(RuleUnit): # KDS241711_04020702_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.2.7.2 (1)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-21'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '기초의 설계지진력'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.7 설계지진력
    4.2.7.2 기초의 설계지진력
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
		A[기초의 설계지진력];
		B["KDS 24 17 11 4.2.7.2 (1)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 기초의 설계지진력/];
		VarIn1[/입력변수: 교각의 최대소성힌지력/];
		VarIn2[/입력변수: 응답수정계수를 적용하지 않은 탄성지진력/];
		VarOut ~~~ VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def

		C["기초의 설계지진력 = \n min (교각의 최대소성힌지력, 응답수정계수를 적용하지 않은 탄성지진력)"];

		D([기초의 설계지진력]);

		Variable_def --> C --> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def foundation_design_earthquake_load(fODsfofd,fImaphfp,fIebcwoR) -> float:
        """기초의 설계지진력

        Args:
            fODsfofd (float): 기초의 설계지진력
            fImaphfp (float): 교각의 최대소성 힌지력
            fIebcwoR (float): 응답수정계수를 적용하지 않은 탄성지지력

        Returns:
            float: fODsfofd, 기초의 설계지진력
        """
        fODsfofd = min(fImaphfp, fIebcwoR)
        return fODsfofd