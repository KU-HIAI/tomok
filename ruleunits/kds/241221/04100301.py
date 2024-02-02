import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04100301 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.10.3.1' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-22'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '거스트계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 풍하중
    4.10.3 거스트계수
    4.10.3.1 강체구조물
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
        A[강체구조물 거스트계수];
        B["KDS 24 12 21 4.10.3.1"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 거스트계수/];
    VarIn1[/입력변수 : B/];
    VarIn2[/입력변수 : D/];
    VarIn3[/입력변수 : L/];
    VarIn4[/입력변수 : z/];
    end
    Python_Class~~~Variable_def
    E{"지표상황"};
    F["<img src='https://latex.codecogs.com/svg.image?\alpha_{2}=0.174,\beta=1.25,c=0.15,\varepsilon=0.125,l=200m,z_{b}=2m,z_{G}=200m'>-------------------------------------------------------------------------------"];
    G["<img src='https://latex.codecogs.com/svg.image?\alpha_{2}=0.210,\beta=154,c=0.20,\varepsilon=0.200,l=150m,z_{b}=5m,z_{G}=300m'>-----------------------------------------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?\alpha_{2}=0.286,\beta=2.22,c=0.30,\varepsilon=0.333,l=100m,z_{b}=10m,z_{G}=400m'>———————————————————————————————————————"];
    I["<img src='https://latex.codecogs.com/svg.image?\alpha_{2}=0.400,\beta=3.33,c=0.45,\varepsilon=0.500,l=50m,z_{b}=20m,z_{G}=500m'>———————————————————————————————————————"];
    J["<img src='https://latex.codecogs.com/svg.image?z_{5}=max(z,5m),z_{D}=max(z,z_{b}),I_{z}=c(\frac{10}{z_{D}})^{1/6},L_{z}=l\left(\frac{z_{D}}{10}\right)^{\varepsilon},K_{p}=2.01\beta^{2}\left(\frac{10z_{5}}{z_{D}z_{G}}\right)^{\alpha&space;_{2}},Q=\sqrt{\frac{1}{1&plus;0.63\left(\frac{L&plus;D}{L_{z}}\right)^{0.63}}}'>———————————————————————————————————————"];
    K["<img src='https://latex.codecogs.com/svg.image?G_{r}=K_{p}\frac{1&plus;5.78I_{z}Q}{1&plus;5.78I_{z}}'>———————————————————"];
    M(["거스트계수"]);
    Variable_def—>E—해상,해안—>F—>J—>K—M
    E—개활지,농지,전원수목과 저층건축물이 산재하여 있는 지역—>G—>J
    E—수목과 저층건축물이 밀집하여 있는 지역 or 중,고층 건물이 산재하여 있는 지역—>H—>J
    E—중,고층건물이 밀집하여 있는 지역 or 기복이 심한 구릉지—>I—>J
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def gust_factor(fOGr,fIL,fIB,fIz,fID,fIuserdefine) -> float:
        """거스트계수

        Args:
            fOGr (float): 거스트계수
            fIL (float): 그림 4.10-2의 제원
            fIB (float): 그림 4.10-2의 제원
            fIz (float): 지상또는 수면으로부터 구조물의 대표높이
            fID (float): 그림 4.10-2의 제원
            fIuserdefine (float): 사용자가 정의한 값

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.10.3.1 강체구조물 의 값
        """
        #해상, 해안의 경우 : fIuserdefine = 1
        #개활지, 농지, 전원 수목과 저층건축물이 산재하여 있는 지역의 경우 : fIuserdefine = 2
        #수목과 저층건축물이 밀집하여 있는 지역, 중, 고층 건물이 산재하여 있는 지역, 완만한 구릉지의 경우 : fIuserdefine = 3
        #중, 고층 건물이 밀집하여 있는 지역, 기복이 심한 구릉지의 경우 : fIuserdefine = 4

        if fIuserdefine == 1:
          a = 0.12
          alpha2 = 0.174
          beta = 1.25
          c = 0.15
          ep = 0.125
          l = 200
          zb = 2
          ZG = 200
        if fIuserdefine == 2:
          a = 0.16
          alpha2 = 0.210
          beta = 1.54
          c = 0.20
          ep = 0.200
          l = 150
          zb = 5
          ZG = 300
        if fIuserdefine == 3:
          a = 0.22
          alpha2 = 0.286
          beta = 2.22
          c = 0.30
          ep = 0.333
          l = 100
          zb = 10
          ZG = 400
        if fIuserdefine == 4:
          a = 0.29
          alpha2 = 0.400
          beta = 3.33
          c = 0.45
          ep = 0.500
          l = 50
          zb = 20
          ZG = 500

        ZD = max(fIz,zb)
        Z5 = max(fIz,5)
        Iz = c*(10/ZD)**(1/6)
        Lz = l*(ZD/10)**ep
        Kp = 2.01*beta**2*(10*Z5/ZD/ZG)**alpha2
        Q = (1/(1+0.63*((fIL+fID)/Lz)**0.63))**0.5
        fOGr = Kp*(1+5.78*Iz*Q)/(1+5.78*Iz)

        return(fOGr)


# 

