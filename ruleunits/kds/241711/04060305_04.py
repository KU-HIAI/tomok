import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060305_04(RuleUnit): # KDS241711_04060305_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.5 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '연장 길이'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.5 심부구속 횡방향철근상세
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
    A[심부구속 횡방향철근상세];
    B["KDS 24 17 11 4.6.3.5 (3)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 연장길이/] ;
    VarIn2[/입력변수: 갈고리/];
    VarIn3[/입력변수: 띠철근 지름/];
    end

    Python_Class ~~~ Variable_def -->D --> E & F
    D{"갈고리"};
    E["한쪽 단 갈고리>135°"];
    F["다른쪽 단 갈고리>90°"];
    G["135°갈고리의 연장길이 ≥\n max(띠철근 지름X6, 80mm)"]
    H["90°갈고리의 연장길이 ≥띠철근 지름X6"]
   	I([Pass or Fail])

E-->G-->I
F-->H-->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def reinforcement_hoop(fIoneextlen,fIonehook,fIanoextlen,fIanohook,fIhoodia) -> bool:
        """연장 길

        Args:
            fIoneextlen (float): 한쪽 단 연장길이
            fIonehook (float): 한쪽 단 갈고리
            fIanoextlen (float): 다른 쪽 단 연장길이
            fIanohook (float): 다른 쪽 단 갈고리
            fIhoodia (float): 띠철근 지름

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.3.5 심부구속 횡방향철근상세 (4)의 통과 여부
        """

        if fIonehook >= fIanohook:
          hook135 = fIonehook
          hook90 = fIanohook
          extlen135 = fIoneextlen
          extlen90 = fIanoextlen
          if hook135 >= 135 and hook90 >= 90 and extlen135 >= max(6 * fIhoodia, 80) and extlen90 >= 6 * fIhoodia:
            return "Pass"
          else:
            return "Fail"
        else:
          hook135 = fIanohook
          hook90 = fIonehook
          extlen135 = fIanoextlen
          extlen90 = fIoneextlen
          if hook135 >= 135 and hook90 >= 90 and extlen135 >= max(6 * fIhoodia, 80) and extlen90 >= 6 * fIhoodia:
            return "Pass"
          else:
            return "Fail"