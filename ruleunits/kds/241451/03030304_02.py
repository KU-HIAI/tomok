import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030304_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.3.4 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝의 공칭 단위선단지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가
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
    A[현장 원위치시험을 통한 말뚝지지력의 평가];
    B["KDS 24 14 51 3.3.3.4 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:말뚝의 공칭 단위선단지지력/]
			VarOut2[/출력변수:타입말뚝에 대한 단위 주면 마찰/]
			VarIn1[/입력변수:사질토에서 깊이/]
			VarIn2[/입력변수:말뚝 선단근처의 대표적인 SPT 타격횟수/]
			VarIn3[/입력변수:SPT 타격횟수/]
			VarIn4[/입력변수:말뚝의 폭 또는 직경/]
			VarIn5[/입력변수:지지층에 관입된 말뚝길이/]
			VarIn6[/입력변수:한계 선단지지력/]
			VarIn7[/입력변수:말뚝 주면을 따라 얻은 보정하지 않은 평균 SPT 타격횟수/]

			VarOut1 ~~~ VarOut2
			VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4
			VarIn5 ~~~ VarIn6 ~~~ VarIn7


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[표준 관입시험을 이용한 방법]
			D[말뚝 선단지지력]
			E[주면마찰력]
			F["<img src='https://latex.codecogs.com/svg.image?&space;q_{p}=\frac{0.038N_{corr}D_{b}}{D}\leq&space;q_{l}'>---------------------------------"]
			G["<img src='https://latex.codecogs.com/svg.image?N_{corr}=[0.77log_{10}(\frac{1.92}{\sigma&space;_{v}^{'}})]N'>---------------------------------"]
			H["<img src='https://latex.codecogs.com/svg.image?q_{s}=0.0019\overline{N}'>---------------------------------"]
			I["<img src='https://latex.codecogs.com/svg.image?q_{s}=0.00096\overline{N}'>---------------------------------"]
			J([말뚝지지력 평가])

			Variable_def ---> C ---> D & E
			D ---> G ---> F
			E ---> H & I

			H & F & I ---> J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_unit_end_support(fOqp,fINcorr,fIN,fID,fIDblaye,fIql,fIsigpriv,fOqs,fIavespt,fIuserdefined) -> float:
        """말뚝의 공칭 단위선단지지력
        Args:
            fOqp (float): 말뚝의 공칭 단위선단지지력
            fINcorr (float): 말뚝 선단근처의 대표적인 SPT 타격횟수
            fIN (float): SPT 타격횟수
            fID (float): 말뚝의 폭 또는 직경
            fIDblaye (float): 지지층에 관입된 말뚝길이
            fIql (float): 한계 선단지지력
            fIsigpriv (float): 상재응력
            fOqs (float): 타입말뚝에 대한 단위 주면마찰력
            fIavespt (float): 말뚝 주면을 따라 얻은 보정하지 않은 평균 SPT 타격횟수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.4(2) 말뚝의 공칭 단위선단지지력과 타입말뚝에 대한 단위 주면마찰력

        """

        #배토 말뚝 : fIuserdefined == 1
        #비배토 말뚝 : fIuserdefined == 2

        fINcorr=0.77*math.log10(1.92/fIsigpriv)*fIN
        fOqp=0.038*fINcorr*fIDblaye/fID
        if fOqp>fIql:
          return "Fail"
        else:
          if fIuserdefined==1:
            fOqs=0.0019*fIavespt
          elif fIuserdefined==2:
            fOqs=0.00096*fIavespt
          return (fOqp,fOqs)


# 

