import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030104_09(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.1.4 (9)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '강바닥판'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.1 제작
    3.1.4 시공
    (9)
    """

    # 건설기준문서내용(text)
    content = """
    ####(9) 강바닥판(steel deck plate)
    ① 일반사항
    가. 강바닥판은 상세설계도 또는 제작자의 제작상세도 및 용접시공 절차서 등에 따라 제작한다.
    나. 강바닥판의 규격은 교량의 형태에 따른 주부재나 부부재의 보강에 맞추어 제작하되 장폭비 1:1.5를 권장한다.
    다. 강바닥판의 판 이음부는 종방향 및 횡방향 리브의 위치에서 이음부 최소 판 두께의 15배 이상 떨어진 곳에 두는 것이 바람직하다.
    라. 종방향 보강재와 횡방향 보강재가 만나는 지점은 스켈럽 및 용접형상, 용접순서에 따라 허용피로강도에 큰 영향을 미치므로 검토하여 감독자의 승인을 얻어 시공한다.
    마. 강바닥판은 판의 뒤틀림이나 구부러짐이 없도록 지지재나 클램프 등을 사용하여 정밀하게 제작한다.
    바. 강바닥판의 판절단 및 가공은 이 절의 해당요건에 준하며 용접시공은 3.2에 따른다.

    ② 평탄도 및 직선도
    가. 평탄도는 강바닥판 블록 전체를 기준으로 하는 경우와 보강재 사이의 패널크기를 기준으로 하는 경우가 있다. 패널의 평탄도는 최대편차가 다음 값을 초과해서는 안 된다.
        $$\frac{15}{32} 또는 \frac{D}{50}\sqrt{T}$$ (식 3.1-1)
    여기서,
        $$D$$: 패널 경계의 최소길이(㎜)
        $$T$$: 패널 강판의 최소두께(㎜)

    나. 압축력을 받는 보강재와 강바닥판 리브의 직선도압축력을 받는 종방향 보강재, 또는 강바닥판 종 리브의 직선도는 보강재 또는 리브의 횡 방향 최대 오차가 다음 값을 초과해서는 안 된다.
        $$\frac{L}{480}$$  (식 3.3-2)
    여기서, $$L$$: 보강재 또는 리브의 길이, 가로보 또는 횡 리브의 간격(㎜)

    다. 웨브 횡방향 보강재와 압축력을 받지 않는 기타 보강재웨브의 횡방향 보강재, 또는 압축력을 받지 않는 기타 보강재의 직선도는 보강재의 횡 방향 최대 오차가 다음 값을 초과해서는 안 된다.
        $$\frac{L}{240}$$  (식 3.3-3)
    여기서, $$L$$: 보강재의 길이, 보강재의 횡방향 지지점 사이의 길이(㎜)

    """

    # 플로우차트(mermaid)
    flowchart = """
    fflowchart TD
    subgraph Python_Class
    A[Title: 강바닥판의 시공];
    B["KCS 24 30 00 3.1.4 (9)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.1.4 (9)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 판 이음부와 종방향 및 \n 횡방향 리브의 최소거리/];
    VarIn11[/입력변수: 이음부 최소 판 두께/];
    end
    subgraph V2
    VarOut2[/출력변수: 패널의 최대 평탄도/];
    VarIn21[/입력변수: 패널 경계의 최소 길이/];
    VarIn22[/입력변수: 패널 강판의 최소두께/];
    end
    subgraph V3
    VarOut31[/출력변수: 압축력을 받는 종방향 보강재, \n 또는 강바닥판 종 리브의 횡 방향 최대 오차/];
    VarIn31[/입력변수: 보강재 또는 리브의 길이, \n 가로보 또는 횡 리브의 간격/];
    end
    subgraph V4
    VarOut32[/출력변수: 웨브 횡방향 보강재와 \n 압축력을 받지 않는 기타 보강재의 \n 횡 방향 최대 오차/];
    VarIn37[/입력변수: 보강재의 길이, \n 보강재의 횡방향 지지점 사이의 길이/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"판 이음부와 종방향 및 \n 패널의 최대 평탄도 \n 압축력을 받는 종방향 보강재, \n 또는 강바닥판 종 리브의 횡 방향 최대 오차 \n 웨브 횡방향 보강재와 \n 압축력을 받지 않는 기타 보강재의 \n 횡 방향 최대 오차 \n."}
    C --> |"판 이음부와 종방향 및 \n 횡방향 리브의 최소거리"|D["이음부 최소 판 두께 * 15"]
    C --> |"패널의 최대 평탄도"|E["<img src='https://latex.codecogs.com/png.image?\dpi{500} min(\frac{15}{32}, \frac{D}{50}\sqrt{T})'>---------------------------------"];
    C --> |"압축력을 받는 종방향 보강재, \n 또는 강바닥판 종 리브의 횡 방향 최대 오차"|F["<img src='https://latex.codecogs.com/png.image?\dpi{500} \frac{L}{480}'>-------"];
    C --> |"웨브 횡방향 보강재와 \n 압축력을 받지 않는 기타 보강재의 \n 횡 방향 최대 오차"|G["<img src='https://latex.codecogs.com/png.image?\dpi{500} \frac{L}{240}'>-------"];
    D & E & F & G --> End([강바닥판의 시공])
    """

    @rule_method
    def distance_joint_rib(fIThiJoi)-> float:
        """
        Args:
            fIThiJoi (float): 이음부 최소 판 두께
        Returns:
            fOJoiRib (float): 판 이음부와 종방향 및 횡방향 리브의 최소거리
        """
        fOJoiRib = fIThiJoi*15
        return fOJoiRib

    def flatness_panel(self,fID,fIT)-> float:
        """
        Args:
            fID (float): 패널 경계의 최소 길이
            fIT (float): 패널 강판의 최소두께
        Returns:
            fOFlaPan (float): 패널의 최대 평탄도
        """
        fOFlaPan = min(15/32, fID/50*((fIT)**1/2))
        return fOFlaPan

    def deviation_compressive(self,fIL_1)->float:
        """
        Args:
            fIL_1 (float): 보강재 또는 리브의 길이, 가로보 또는 횡 리브의 간격
        Returns:
            fOTraRib (float): 압축력을 받는 종방향 보강재, 또는 강바닥판 종 리브의 횡 방향 최대 오차
        """
        fOTraRib = fIL_1/480
        return fOTraRib

    def deviation_not_compressive(self,fIL_2)->float:
        """
        Args:
            fIL_2 (float): 보강재의 길이, 보강재의 횡방향 지지점 사이의 길이
        Returns:
            fOTraSti (float): 웨브 횡방향 보강재와 압축력을 받지 않는 기타 보강재의 횡 방향 최대 오차
        """
        fOTraSti = fIL_2/240
        return fOTraSti