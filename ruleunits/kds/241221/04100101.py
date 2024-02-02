import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04100101 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.10.1.1' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기본풍속'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 풍하중
    4.10.1 풍속
    4.10.1.1 기본풍속
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
        A[구조물의 충격계수];
        B["KDS 24 12 21 4.10.1.1"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 기본풍속/];
    end
    Python_Class~~~Variable_def
    D{"풍속자료 가용"};
    E["대상지역 인근 기상관측소의 장기종속기록과
    지역적 위치를 동시에 고려하여 극치분포로부터 추정"];
    F["내륙(서울,대구,대전,춘천,청주,수원,추풍령, 전주, 익산,진주,광주)"];
    G["서해안(서산,인천)"];
    H["서남해안, 남해안,동남해안(군산,여수,통영,부산,포항,울산)"];
    I["동해안,제주지역,특수지역(속초,강릉,제주,서귀포,목포)"];
    J["울릉도"]
    K["V10=30m/s"];
    N["V10=35m/s"];
    M["V10=40m/s"];
    O["V10=45m/s"];
    P["V10=50m/s"];
    Q(["기본풍속"]);
    R["지역"];
    Variable_def--->D--Yes--->E--->Q
    D--No--->R--->F--->K--->Q
    R--->G--->N--->Q
    R--->H--->M--->Q
    R--->I--->O--->Q
    R--->J--->P--->Q
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def basic_wind_speed(fOVwbas,fIuserdefine) -> float:
        """기본풍속

        Args:
            fOVwbas (float): 기본풍속
            fluserdefine (float): 사용자 정의 값


        Returns:
            float: 강교 설계기준(한계상태설계법) 4.10.1.1 기본풍속 의 값
        """
        #대상지역의 풍속자료가 가용치 못한 경우에만 사용가능한 값이다.
        #내륙(서울, 대구, 대전, 춘천, 청주, 수원, 추풍령, 전주, 익산, 진주, 광주)의 경우 : fIuserdefine = 1
        #서해안(서산, 인천)의 경우 : fIuserdefine = 2
        #서남해안(군산), 남해안(여수, 통영, 부산), 동남해안(포항, 울산)의 경우 : fIuserdefine = 3
        #동해안(속초, 강릉), 제주지역(제주, 서귀포), 특수지역(목포)의 경우 : fIuserdefine = 4
        #울릉도 : fIuserdefine = 5


        if fIuserdefine == 1:
          fOVwbas = 30
        elif fIuserdefine == 2:
          fOVwbas = 35
        elif fIuserdefine == 3:
          fOVwbas = 40
        elif fIuserdefine == 4:
          fOVwbas = 45
        elif fIuserdefine == 5:
          fOVwbas = 50

        return(fOVwbas)


# 

