import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010403 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.4.3' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-29'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단 파괴선을 따라 발생하는 전단파단과 직각으로 발생하는 인장파단의 블록전단파단 한계상태에 대한 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.3 블록전단강도
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
	  A([블록전단강도])
	  B["KDS 14 31 25 4.1.4.3"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 설계강도/]
	  VarIn2[/입력변수: 공칭강도/]
	  VarIn3[/입력변수: 저항계수/]
	  VarIn4[/입력변수: 피접합체의 공칭인장강도/]
	  VarIn5[/입력변수: 유효전단단면적/]
	  VarIn6[/"입력변수: <img src='https://latex.codecogs.com/svg.image?U_{bs}'>--------"/]
	  VarIn7[/입력변수: 인장저항순단면적/]
	  VarIn8[/입력변수: 핀의항복강도/]
	  VarIn9[/입력변수: 전단력을 받는 총단면적/]
	  VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	  VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

	  end


	  Python_Class ~~~ Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?R_n=\left\lceil0.6F_uA_{nv}&plus;U_{bs}F_uA_{nt}\right\rceil\leq\left\lceil&space;0.6F_yA_{gv}&plus;U_{bs}F_uA_{nt}\right\rceil'>------------------------------------------------------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>-----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength(fOphiRn,fIRn,fIphi,fIFu,fIAnv,fIUbs,fIAnt,fIFy,fIAgv) -> bool:
        """전단 파괴선을 따라 발생하는 전단파단과 직각으로 발생하는 인장파단의 블록전단파단 한계상태에 대한 설계강도

        Args:
            fOphiRn (float): 설계강도
            fIRn (float): 공칭강도
            fIphi (float): 저항계수
            fIFu (float): 피접합재의 공칭인장강도
            fIAnv (float): 유효전단단면적
            fIUbs (float): 인장저항 순단면적
            fIAnt (float): 핀의 항복강도
            fIAgv (float): 전단력을 받는 총단면적

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.3 블록전단강도의 값
        """

        fIRn = min((0.6 * fIFu * fIAnv + fIUbs * fIFu * fIAnt), (0.6 * fIFy * fIAgv + fIUbs * fIFu * fIAnt))
        fOphiRn = 0.75 * fIRn
        return fOphiRn


# 

