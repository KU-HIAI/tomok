import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010701_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.7.1 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근콘크리트 판요소에서 계수하중에 의해 유발된 철근과 콘크리트의 응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.1 판요소 설계
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
    A["콘크리트의 응력"];
    B["KDS 24 14 21 4.1.7.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 종방향/];
		VarIn2[/입력변수: 횡방향/];
		VarIn3[/입력변수: 철근의 콘크리트 단면적에 대한 비/];
		VarIn4[/입력변수: 종방향 축에 일치하게 직교 2방향으로 배치한철근의콘크리트단면적에대한비/];
		VarIn5[/입력변수: 횡방향 축에 일치하게 직교 2방향으로 배치한 철근의콘크리트단면적에대한비/];
		VarIn6[/입력변수: 요소의 종방향으로 작용하는 법선응력/];
		VarIn7[/입력변수: 요소의 횡방향으로 작용하는 법선응력/];
		VarIn8[/입력변수: 요소에 작용하는 전단응력/];
		VarIn9[/입력변수: 콘크리트 스트럿에 유발된 압축응력/];
		VarIn10[/입력변수: 스트럿의 최대 유효 압축강도/];
		VarIn11[/입력변수: 균열면에서 종방향으로 유발된 철근 응력/];
		VarIn12[/입력변수: 균열면에서 횡방향으로 유발된 철근 응력/];
		VarIn13[/입력변수: 종방향 철근의 항복응력/];
		VarIn14[/입력변수: 횡방향 철근의 항복응력/];
		VarIn15[/입력변수: 종방향 축에 대한 스트럿의 경사각/];
		VarIn16[/입력변수: 콘크리트의 응력/];

		VarIn1 & VarIn2 & VarIn3
   ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11~~~ VarIn13 & VarIn14 & VarIn15 & VarIn16
		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C & D & E--->F

		C["<img src='https://latex.codecogs.com/svg.image?\rho&space;_lf_{sl}=f_{nl}&plus;\upsilon&space;cot\theta\leq\phi&space;_s\rho&space;_lf_{yl}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\rho&space;_lf_{st}=f_{nt}&plus;\upsilon&space;cot\theta\leq\phi&space;_s\rho&space;_tf_{yt}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?f_{c2}=\upsilon(tan\theta&plus;cot\theta)\leq\phi&space;_cf_{c2,max}'>---------------------------------"]
		F(["콘크리트의 응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def stress_of_concrete_and_rebar(fIrhol,fIfsl,fIfnl,fIv,fItheta,fIphis,fIfyl,fIrhot,fIfst,fIfnt,fIfyt,fIfc2,fIphic,fIfc2max) -> bool:
        """철근콘크리트 판요소에서 계수하중에 의해 유발된 철근과 콘크리트의 응력

        Args:
             fIfsl (float): 종방향 콘크리트의 응력
             fIfst (float): 횡방향 콘크리트의 응력
             fIfc2 (float): 콘크리트 스트럿이 유발된 압축응력
             fIrhol (float): 종방향 축에 일치하게 배치한 철근의 콘크리트 단면적에 대한 비
             fIfnl (float): 종방향으로 작용하는 법선응력(인장: +)
             fIv (float): 요소에 작용하는 전단응력
             fItheta (float): 종방향 축(철근)에 대한 스트럿의 경사각
             fIphis (float): 철근의 재료계수
             fIfyl (float): 종방향 철근의 항복응력
             fIrhot (float): 횡방향 축에 일치하게 배치한 철근의 콘크리트 단면적에 대한 비
             fIfnt (float): 횡방향으로 작용하는 법선응력(인장: +)
             fIfyt (float): 횡방향 철근의 항복응력
             fIphic (float): 콘크리트 재료계수
             fIfc2max (float): 스트럿의 최대 유효 압축강도

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (2)의 통과 여부
        """

        fIfsl = (fIfnl + fIv/math.tan(math.radians(fItheta)))/fIrhol
        fIfst = (fIfnt + fIv*math.tan(math.radians(fItheta)))/fIrhot
        fIfc2 = fIv*(math.tan(math.radians(fItheta)) + 1/math.tan(math.radians(fItheta)))
        if fIfsl <= fIphis*fIfyl and fIfst <= fIphis*fIfyt and fIfc2 <= fIphic*fIfc2max:
          return "Pass"
        else:
          return "Fail"


# 

