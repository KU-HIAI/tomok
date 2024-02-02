import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241442_040103_02 (RuleUnit):

   # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
   priority = 1   # 건설기준 우선순위
   author = 'Sunjae Lee'  # 작성자명
   ref_code = 'KDS 24 14 42 4.1.3 (2)' # 건설기준문서
   ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
   doc_date = '2023-11-10'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
   title = '케이블의 공칭피로강도'   # 건설기준명

   # 건설기준문서항목 (분류체계정보)
   description = """
   교량 케이블구조 설계기준
   4. 설계
   4.1 한계 상태
   4.1.3 피로한계상태
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
   A[케이블의 공칭피로강도];
   B["KDS 24 14 42 4.1.3 (2)"];
   A ~~~ B
   end

		subgraph Variable_def;
		VarIn1[/입력변수: 케이블의 공칭피로강도/];
		VarIn2[/입력변수: 하중계수/];
		VarIn3[/입력변수: 피로설계트럭하중 통과 시 발생하는 응력범위에 1.4를 곱한 값/];
		VarIn4[/입력변수: 일정진폭 피로한계값/];
		VarIn5[/입력변수: 케이블 설계수명 동안의 피로설계트럭하중의 통과로 인한 반복횟수/];
		VarIn6[/입력변수: 일정진폭 피로한계값에 해당하는 응력범위 반복횟수/];
		VarIn7[/입력변수: 케이블 설계수명/];
		VarIn8[/입력변수: 한 방향 한 차로의 일일트럭교통량의 설계수명기간 동안 평균값/];
		VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4 & VarIn5
  	VarIn3 ~~~ VarIn6 & VarIn7 & VarIn8

		end

		Python_Class ~~~ Variable_def;
		Variable_def--->D--->E & F
		E--->G
		F--->H
		G & H --->I--->J

		D["<img src='https://latex.codecogs.com/svg.image?&space;N=365(DL)(1.0)ADTT_{SL}'>--------------------------------------------------------"];
		E["<img src='https://latex.codecogs.com/svg.image?&space;N\leq N_{TH}'>--------------------------------------------------------"];
		F["<img src='https://latex.codecogs.com/svg.image?&space;N> N_{TH}'>--------------------------------------------------------"];
		G["<img src='https://latex.codecogs.com/svg.image?&space;\left ( \Delta F \right )_{n}=\left ( \frac{N_{TH}}{N} \right )^{\frac{1}{3}}\left ( \Delta F \right )_{TH}'>--------------------------------------------------------"];
		H["<img src='https://latex.codecogs.com/svg.image?&space;\left ( \Delta F \right )_{n}=\frac{1}{2}\left ( \Delta F \right )_{TH}'>--------------------------------------------------------"];
		I["<img src='https://latex.codecogs.com/svg.image?&space;\gamma \left ( \Delta f \right )\leq \left ( \Delta F \right )_{n}'>--------------------------------------------------------"];
		J(["Pass or Fail"])
   """

   # 작성하는 룰에 맞게 함수 이름과 내용을 수정
   @rule_method
   def nominal_fatigue_strength_of_cable(fIdeltaFn,fIgamma,fIdeltaf,fIdeltaFth,fIN,fINth,fIcadeli,fOADTTSL) -> bool:
       """케이블의 공칭피로강도

       Args:
           fIdeltaFn (float): 케이블의 공칭피로강도
           fIgamma (float): 하중계수
           fIdeltaf (float): 피로설계트럭하중 통과 시 발생하는 응력범위에 1.4를 곱한 값
           fIdeltaFth (float): 일정진폭 피로한계값
           fIN (float):케이블 설계수명 동안의 피로설계트럭하중의 통과로 인한 반복횟수
           fINth (float): 일정진폭 피로한계값에 해당하는 응력범위 반복횟수
           fIcadeli (float): 케이블 설계수명(년)
           fIADTTSL (float): 한 방향 한 차로의 일일트럭교통량의 설계수명기간 동안 평균값

       Returns:
           bool: 교량 케이블구조 설계기준  4.1.3 피로한계상태 (2)의 통과 여부
       """
       fIN = 365 * fIcadeli * 1.0 * fIADTTSL

       if fIN <= fINth :
         fIdeltaFn = ((fINth/fIN)**(1/3)) * fIdeltaFth
         if fIgamma * fIdeltaf <= fIdeltaFn :
           return "Pass"
         else:
           return "Fail"

       if fIN > fINth :
         fIdeltaFn = 1 / 2 * fIdeltaFth
         if fIgamma * fIdeltaf <= fIdeltaFn :
           return "Pass"
         else:
           return "Fail"


