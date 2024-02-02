import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143120_04010205 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 20 4.1.2.5' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-08-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '피로강도 검토'    # 건설기준명

    #
    description = """
    강구조 피로 및 파단 설계기준(하중저항계수설계법)
    4. 설계(피로 및 파단)
    4.1 피로
    4.1.2 하중유발피로
    4.1.2.5 피로강도
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
    A["KDS 14 31 20 4.1.2.5"];
    B[Title: 공칭피로강도];
		A ~~~ B
		end

		C(["KDS 14 31 20 4.1.2.5"]);

		Python_Class ~~~ C ;

		subgraph Variable_def;
    VarOut1[/출력변수: 공칭피로강도/];

		VarIn1[/입력변수: N/] ;
    VarIn2[/입력변수: 일정진폭 피로한계값/];
    VarIn3[/입력변수: 무한수명 공칭피로강도/];
    VarIn4[/입력변수: 일정진폭 피로한계값에 해당하는 응력범위 반복횟수/];
    VarIn5[/입력변수: 무한수명 응력범위에 해당하는 응력 범위 반복횟수/];
    VarIn6[/입력변수: 상세범주 C에 대한 공칭피로강도/];
		VarIn7[/입력변수: 하중 전달판의 두께방향으로의 용접루트 사이 간격/];
    VarIn8[/입력변수: 하중을 받는 판의 두께/];
    VarIn9[/입력변수: 하중 전달판 두께 방향의 필릿용접의 각장/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

		end

		D["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\frac{N_{TH}}{N})^{\frac{1}{3}}(\Delta&space;)_{TH}'>------------------------------------------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\frac{N_{TH}}{N})^{\frac{1}{5}}(\Delta&space;F)_{TH}'>--------------------------------------------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\Delta&space;F)_{n}^{c}(\frac{1.12-(\frac{2a}{t_{p}})&plus;1.24(\frac{\omega}{t_{p}})}{t_{p}^{0.167}})\leq(\Delta&space;F)_{n}^{c}'>-----------------------------------------------------------------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?N\leq&space;N_{TH}'>-------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?N_{TH}\leq&space;N\leq&space;N_{CL}'>-------------------------------------"]
		U["<img src='https://latex.codecogs.com/svg.image?N\leq&space;N_{TH}'>-------------------------"]

		C --> Variable_def ;
		Variable_def --> I;
    Variable_def --> J;
		Variable_def --> K;

		I{일정진폭응력}
		J{다양한 진폭응력}
		K{불연속된 판에 의해 하중을 받고 응력방향과 수직한 방향으로 \n 필릿 용접 또는 부분용입 그루브용접 연결된 상세부 모재}

		I-->G-->D;
		J-->H & U
		H-->E --> R
		U-->D --> Q
		K-->F --> S

		Q(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
		R(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
		S(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])

		flowchart TD
    subgraph Python_Class
    A["KDS 14 31 20 4.1.2.5"];
    B[Title: 공칭피로강도];
		A ~~~ B
		end

		C(["KDS 14 31 20 4.1.2.5"]);

		Python_Class ~~~ C ;

		subgraph Variable_def;
    VarOut1[/출력변수: 공칭피로강도/];

		VarIn1[/입력변수: N/] ;
    VarIn2[/입력변수: 일정진폭 피로한계값/];
    VarIn3[/입력변수: 무한수명 공칭피로강도/];
    VarIn4[/입력변수: 일정진폭 피로한계값에 해당하는 응력범위 반복횟수/];
    VarIn5[/입력변수: 무한수명 응력범위에 해당하는 응력 범위 반복횟수/];
    VarIn6[/입력변수: 상세범주 C에 대한 공칭피로강도/];
		VarIn7[/입력변수: 하중 전달판의 두께방향으로의 용접루트 사이 간격/];
    VarIn8[/입력변수: 하중을 받는 판의 두께/];
    VarIn9[/입력변수: 하중 전달판 두께 방향의 필릿용접의 각장/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

		end

		D["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\frac{N_{TH}}{N})^{\frac{1}{3}}(\Delta&space;)_{TH}'>------------------------------------------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\frac{N_{TH}}{N})^{\frac{1}{5}}(\Delta&space;F)_{TH}'>--------------------------------------------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\Delta&space;F)_{n}^{c}(\frac{1.12-(\frac{2a}{t_{p}})&plus;1.24(\frac{\omega}{t_{p}})}{t_{p}^{0.167}})\leq(\Delta&space;F)_{n}^{c}'>-----------------------------------------------------------------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?N\leq&space;N_{TH}'>-------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?N_{TH}\leq&space;N\leq&space;N_{CL}'>-------------------------------------"]
		U["<img src='https://latex.codecogs.com/svg.image?N\leq&space;N_{TH}'>-------------------------"]

		C --> Variable_def ;
		Variable_def --> I;
    Variable_def --> J;
		Variable_def --> K;

		I{일정진폭응력}
		J{다양한 진폭응력}
		K{불연속된 판에 의해 하중을 받고 응력방향과 수직한 방향으로 \n 필릿 용접 또는 부분용입 그루브용접 연결된 상세부 모재}

		I-->G-->D;
		J-->H & U
		H-->E --> R
		U-->D --> Q
		K-->F --> S

		Q(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
		R(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
		S(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Examine_fatigue_strength(fOdeltaFn, fIdeltaFth, fIdeltaFcl, IINth, IINcl, fIdeltaFnc, fItwoa, fItp, flw, fIuserdefined) -> bool:
        """피로강도 검토

        Args:
            fOdeltaFn (float): 공칭피로강도
            fIN (float): 대상 구조상세가 설계수명 동안 받을 것으로 예상되는 활하중에 의한 응력범위 반복횟수
            fIdeltaFth (float): 일정진폭 피로한계값
            fIdeltaFcl (float): 무한수명 공칭피로강도
            IINth (float): 일정진폭 피로한계값에 해당하는 응력범위 반복횟수
            IINcl (float): 무한수명 응력범위(cut-off limit)에 해당하는 응력범위 반복횟수
            fIdeltaFnc (float): 상세범주 C에 대한 공칭피로강도
            fItwoa (float): 하중 전달판의 두께방향으로의 용접루트 사이 간격
            fItp (float): 하중을 받는 판의 두께
            flw (float): 하중 전달판 두께방향의 필릿용접의 각장
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강구조 피로 및 파단 설계기준(하중저항계수설계법)  4.1.2.5 피로강도의 값
        """
        #일정진폭응력에 대한 각 상세별 공칭피로강도: fIuserdefined = 1
        #다양한 진폭응력에 대한 각 상세별 공칭피로강도: fIuserdefined = 2
        #불연속된 판에 의해 하중을 받고 응력방향과 수직한 방향으로 필릿용접 또는 부분용입 그루브용접 연결된 상세부 모재에 대한 공칭피로강도: fIuserdefined = 3

        if fIuserdefined == 1:
          fOdeltaFn = (IINth/fIN)**(1/3)*fIdeltaFth

        if fIuserdefined == 2:
          if fIN <= IINth:
            fOdeltaFn = (IINth/fIN)**(1/3)*fIdeltaFth
          elif IINth <= fIN <= IINcl:
            fOdeltaFn = (IINth/fIN)**(1/5)*fIdeltaFth

        if fIuserdefined == 3:
          fOdeltaFn = min(fIdeltaFnc*(1.12-(fItwoa/fItp)+1.24*(fIw/fItp))/(fItp^1.167), fIdeltaFnc)

        return fOdeltaFn


# 

