import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030203_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.2.3 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '사질토의 무리말뚝 침하'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.2 사용한계상태의 변위와 지지력
    3.3.2.3 침하
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
    A[침하];
    B["KDS 24 14 51 3.3.2.3 (3)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:사질토의 무리말뚝 침하/]
			VarIn1[/입력변수:2Db/3지점에 작용하는 순 기초압력/]
			VarIn2[/입력변수:무리말뚝의 폭이나 최소치수/]
			VarIn3[/입력변수:무리말뚝의 침하/]
			VarIn4[/입력변수:무리말뚝의 유효근입깊이에 대한 영향계수/]
			VarIn5[/입력변수:유효깊이/]
			VarIn6[/입력변수:지지층에 근입된 말뚝의 길이/]
			VarIn7[/입력변수:SPT의 타격횟수로서 상재하중에 대해 보정한 대표적인 평균값/]
			VarIn8[/입력변수:침하층에서 측정된 SPT의 타격횟수/]
			VarIn9[/입력변수:유효연직응력/]
			VarIn10[/입력변수:등가확대기초아래 임의의 깊이 z에 대한 평균 정적 콘 저항값/]


			VarOut1
			VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4 ~~~ VarIn5
			VarIn6 ~~~ VarIn7 ~~~ VarIn8 ~~~ VarIn9 ~~~ VarIn10


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?-0.125\frac{D\prime}{X}\geq&space;0.5'>---------------------------------"]
			D["<img src='https://latex.codecogs.com/svg.image?&space;SPT=\rho=\frac{30qI\sqrt{X}}{N_{corr}}'>---------------------------------"]
			E["<img src='https://latex.codecogs.com/svg.image?N_{corr}=[0.77log_{10}(\frac{1.92}{\sigma_{v}^{'}})]N'>---------------------------------"]
			F([사질토에 설치된 무리말뚝의 침하])

			Variable_def ---> C & E ---> D --->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_sedimentation_of_sandstones(fOspt,fOcpt,fIq,fIx,fIp,fIi,fIdp,fIdb,fIncorr,fIn,fIeffstr,fIqc,fIuserdefined) -> float:
        """사질토의 무리말뚝 침하
        Args:
            fOspt (float): 사질토의 무리말뚝 침하
            fOcpt (float): 사질토의 무리말뚝 침하
            fIq (float): 2Db/3 지점에 작용하는 순 기초압력
            fIx (float): 무리말뚝의 폭이나 최소치수
            fIp (float): 무리말뚝의 침하
            fIi (float): 무리말뚝의 유효근입깊이에 대한 영향계수
            fIdp (float): 유효깊이
            fIdb (float): 지지층에 근입된 말뚝의 길이
            fIncorr (float): SPT의 타격횟수로서 상재하중에 대해 보정한 대표적인 평균값
            fIn (float): 침하층에서 측정된 SPT의 타격횟수
            fIeffstr (float): 유효연직응력
            fIqc (float): 등가 확대기초 아래 임의의 깊이 z에 대한 평균 정적 콘저항값
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.2.3(3) 사질토의 무리말뚝 침하

        """

        fIncorr=0.77*math.log10(1.92/fIeffstr)*fIn
        fIi=1-0.125*fIdp/fIx
        if fIi<0.5:
          return "Fail"
        else:
          if fIuserdefined==1: #SPT
            fOspt=30*fIq*fIi*fIx**0.5/fIncorr
            return fOspt
          elif fIuserdefined==2: #CPT
            fOcpt=fIq*fIx*fIi/24/fIqc
            return fOcpt


# 

