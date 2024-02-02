import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060201_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.1 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소 철근 단면적'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
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
    A["최소 철근 단면적"];
    B["KDS 24 14 21 4.6.2.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:28일 콘크리트 공시체의 기준 압축강도/];
		VarIn2[/입력변수: 철근의 기준항복강도/];
		VarIn3[/입력변수: 단면의 복부폭/];
		VarIn4[/입력변수:단면의 유효깊이/];
		VarIn5[/입력변수: 단면의 복부폭/];
		VarIn6[/입력변수: 단면의 유효깊이/];
		VarIn7[/입력변수: 필요한 철근량/];
		VarIn8[/입력변수: 인장철근/];
		VarIn9[/입력변수: 인장철근의 최소 단면적/];
		VarIn10[/입력변수: 필요한 수축철근량/];
		VarI11[/입력변수:철근의 최대간격/];
		VarIn12[/입력변수:슬래브 두께/];
		VarIn13[/입력변수:기초판의 두께/];
		VarOut1[/출력변수: 최소 철근 단면적/];



		VarOut1 ~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6
		VarIn5~~~VarIn7 & VarIn8 & VarIn9
		VarIn8~~~VarIn10 & VarIn11 & VarIn12 & VarIn13
		end
		Python_Class ~~~ Variable_def--->C
		Python_Class ~~~ Variable_def--->F
		C{예외 경우}
		C--플랜지가 인장상태인 정정 구조물--->D
		C--두께가 균일한 구조용 슬래브의 기초판에 대하여--->E
		D["<img src='https://latex.codecogs.com/svg.image?A_{s}>=max(\frac{0.25\sqrt{f_{ck}}}{f_y}min(b,2b_w)d or \frac{1.4}{f_y}min(b,2b_w)d'>---------------------------------"]
		E["인장철근의 최소 단면적=필요한 수축 철근량, 철근의 최대간격≤min(슬래브 OR 기초판의 두께 *3,450mm)"]
		F["<img src='https://latex.codecogs.com/svg.image?A_{s}>=max(\frac{0.25\sqrt{f_{ck}}}{f_y}b_wd or \frac{1.4}{f_y}b_wd)'>---------------------------------"]
		D---->I
		E---->K
		F---->J
		I(["Pass or Fail"])
		K(["Pass or Fail"])
		J(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_reinforcing_bar_cross_section(fOAsmin,fIfck,fIfy,fIbw,fId,fIb,fIamrere,fItenref,fImincos,fIamosre,fImaxspr,fIslathi,fIthibp,fIuserdefined) ->float:
        """최소 철근 단면적
        Args:
             fOAsmin (float): 최소 철근 단면적
             fIfck (float): 28일 콘크리트 공시체의 기준 압축강도
             fIfy (float): 철근의 기준항복강도
             fIbw (float): 단면의 복부폭
             fId (float): 단면의 유효깊이
             fIb (float): 단면 폭
             fIamrere (float): 필요한 철근량
             fItenref (float): 인장철근
             fImincos (float): 인장철근의 최소 단면적
             fIamosre (float): 필요한 수축철근량
             fImaxspr (float): 철근의 최대간격
             fIslathi (float): 슬래브 두께
             fIthibp (float): 기초판의 두께
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 해석에 의해 인장철근 보강이 요구되는 보의 모든 단면에 대하여 최소 철근 단면적 (1)의 값
        """

        # fIuserdefined == 1 : 플랜지가 인장상태인 정정 구조물
        # fIuserdefined == 2 : 두께가 균일한 구조용 슬래브의 기초판인 경우

        if fIuserdefined == 1:
          if fOAsmin >= max(((0.25) * ((fIfck)**0.5)) / fIfy * min(fIbw,fIb) * fId, (1.4) / fIfy * min(fIbw,fIb) * fId) :
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined == 2:
          if fImincos == fIamosre and fImaxspr <= min(fIslathi*3, fIthibp*3, 450) :
            return "Pass"
          else:
            return "Fail"
        elif fIamrere*(1/3) > fItenref :
          if fOAsmin >= max(((0.25) * ((fIfck)**0.5)) / fIfy * fIbw * fId, (1.4) / fIfy * fIbw * fId) :
            return "Pass"
          else:
            return "Fail"


# 

