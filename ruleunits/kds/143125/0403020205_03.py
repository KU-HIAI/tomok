import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020205_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.2.5 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '총 유효용접길이'  # 건설기준명


    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.5 지강관의 용접
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
        A[Title: 지강관의 용접] ;
        B["KDS 14 31 25 4.3.2.2.5(3)"] ;
        A ~~~ B
        end

        subgraph Variable_def
        VarOut1[/출력변수: 겹치는 지강관에 대한 총 유효용접길이/] ;
        VarOut2[/출력변수: 총유효용접길이/] ;
        VarIn1[/입력변수: 오버랩 접합계수/] ;
        VarIn2[/입력변수: 겹치는 지강관의 높이/] ;
        VarIn3[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
        VarIn4[/입력변수: 겹친 브레이스에 용접된 지강관 면의 유효폭/] ;
        VarIn5[/입력변수: 겹치는 지강관의 폭/] ;
        VarIn6[/입력변수: 주강관의 두께/] ;
        VarIn7[/입력변수: 겹친 지강관의 두께/] ;
        VarIn8[/입력변수: 겹친 지강관의 높이/] ;
        VarIn9[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
        VarIn10[/입력변수: 주강관의 항복강도/] ;
        VarIn11[/입력변수: 겹친 지강관 재료의 항복응력/] ;
        VarIn12[/입력변수: 겹친 지강관의 폭/] ;

        VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
        VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
        VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
        VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
        end

        Python_Class ~~~ Variable_def

        C["25%≤O_v≤50%"] ;
        D(["<img src='https://latex.codecogs.com/svg.image?l_{e,i}=\frac{2O_{v}}{50}[(1-\frac{O_{v}}{100})(\frac{H_{bi}}{sin\theta&space;_{i}})&plus;\frac{O_{v}}{100}(\frac{H_{bi}}{sin(\theta&space;_{i}&plus;\theta&space;_{j})})]&plus;b_{eoi}&plus;b_{eov}'>-------------------------------------------------------------------------------------"]) ;
        E["80%≤O_v≤100%"] ;
        F(["<img src='https://latex.codecogs.com/svg.image?l_{e,i}=\2[(1-\frac{O_{v}}{100})(\frac{H_{bi}}{sin\theta&space;_{i}})&plus;\frac{O_{v}}{100}(\frac{H_{bi}}{sin(\theta&space;_{i}&plus;\theta&space;_{j})})]&plus;b_{eoi}&plus;b_{eov}'>-------------------------------------------------------------------------------------"]) ;
        G["80%≤O_v≤100%"] ;
        H(["<img src='https://latex.codecogs.com/svg.image?l_{e,i}=\2[(1-\frac{O_{v}}{100})(\frac{H_{bi}}{sin\theta&space;_{i}})&plus;\frac{O_{v}}{100}(\frac{H_{bi}}{sin(\theta&space;_{i}&plus;\theta&space;_{j})})]&plus;B_{eoi}&plus;b_{eov}'>-------------------------------------------------------------------------------------"]) ;
        J["<img src='https://latex.codecogs.com/svg.image?B_{bi}/B_{b}>0.85'> 또는 <img src='https://latex.codecogs.com/svg.image?\theta&space;_{i}>50^{\circ}'>------------------------------------"] ;
        K["<img src='https://latex.codecogs.com/svg.image?b_{eoi}/2\leq 2t'>----------------------------------------"] ;
        L["<img src='https://latex.codecogs.com/svg.image?B_{bi}/B_{bi}>0.85B_{bi}/B_{b}>0.85'> 또는 <img src='https://latex.codecogs.com/svg.image?(190-\theta&space;_{i}-\theta&space;_{j})>50^{\circ}'>--------------------------------------------"] ;
        M["<img src='https://latex.codecogs.com/svg.image?b_{eoi}/2\leq 2t_{bj}'>-----------------------------------------"] ;
        N["<img src='https://latex.codecogs.com/svg.image?b_{eoi}=\frac{10}{B/t}(\frac{F_{y}t}{F_{ybi}t_{bi}})B_{bi}\leq&space;B_{bi}'>------------------------------------------------------------------------"] ;
        O(["<img src='https://latex.codecogs.com/svg.image?l_{e,j}=\frac{2H_{bj}}{sin\theta&space;_{j}}&plus;2b_{eoi}'>------------------------------------------------------------------------"]) ;
        P["<img src='https://latex.codecogs.com/svg.image?B_{bi}/B>0.85'> 또는 <img src='https://latex.codecogs.com/svg.image?\theta&space;_{j}>50^{\circ}'>--------------------------------------------"] ;
        Q(["<img src='https://latex.codecogs.com/svg.image?l_{e,i}=\frac{2(H_{bj}-1.2t_{bi})}{sin\theta&space;_{i}}'>------------------------------------------------------------------------"]) ;
        Variable_def --> C-->D
        Variable_def --> E-->F
        Variable_def --> G-->H
        Variable_def --> J-->K
        Variable_def --> L
        L-->M
        K-->N
        M-->N
        N-->O
        Variable_def --> P-->Q
        """

      # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def total_effective_weld_length(fOlei,fIOv,fIHbi,fIbeoi,fIbeov,fIBbi,fIt,fItbj,fOlej,fIHbj,fIB,fIFy,fIFybj,fIBbj,fIbeoj,fIthetai,fIthetaj,fIuserdefine) -> float:
        """총 유효용접길이
        Args:
            fOlei (float): 겹치는 지강관에 대한 총 유효용접길이
            fIOv (float): 오버랩 접합계수
            fIHbi (float): 겹치는 지강관의 높이
            fIbeoi (float): 주강관에 용접된 지강관 면의 유효폭
            fIbeov (float): 겹친 브레이스에 용접된 지강관 면의 유효폭
            fIBbi (float): 겹치는 지강관의 폭
            fIt (float): 주강관의 두께
            fItbj (float): 겹친 지강관의 두께
            fOlej (float): 총유효용접길이
            fIHbj (float): 겹친 지강관의 높이
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIFy (float): 주강관의 항복강도
            fIFybj (float): 겹친 지강관 재료의 항복응력
            fIBbj (float): 겹친 지강관의 폭
            fIbeoj (float): 겹친 지강관 면의 유효폭
            fIthetai (float): 각i
            fIthetaj (float): 각j
            fIuserdefine (float) = 사용자가 정의한 값

        Returns:
            float : 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.5 지강관의 용접 (3) 의 값
        """
        # 겹쳐진 지강관 의 경우 : fluserdefine = 1
        # 겹치는 지강관 의 경우 : fluserdefine = 2
        # false -> Bbi/Bb or thetai > 50 일때, beoi/2 > 2t 인 경우
        # false -> Bbi/Bbj > 0.85Bbi/Bb or (190-thetai-thetaj) > 50 일때, beov/2 > 2tbj 인 경우


        if (fIBbi/fIB > 0.85 or fIthetai > 50) and fIbeoi/2 > 2*fIt:
          return "Fail"

        elif (fIBbi/fIBbj > 0.85*fIBbi/fIB or (190-fIthetai-fIthetaj)) > 50 and fIbeov/2 > 2*fItbj:
          return "Fail"

        else:
          if fIuserdefine ==1:
            if 25 <= fIOv <= 50:
              fOlei = 2*fIOv/50*((1-fIOv/100)*(fIHbi/math.sin(fIthetai*math.pi/180)+fIOv/100*(fIHbi/math.sin((fIthetai+fIthetaj)*math.pi/180))))+fIbeoi+fIbeov
            elif 50 <= fIOv <= 80:
              fOlei = 2*((1-fIOv/100)*(fIHbi/math.sin(fIthetai*math.pi/180)+fIOv/100*(fIHbi/math.sin((fIthetai+fIthetaj)*math.pi/180))))+fIbeoi+fIbeov
            elif 80 <= fIOv <= 100:
              fOlei = 2*((1-fIOv/100)*(fIHbi/math.sin(fIthetai*math.pi/180)+fIOv/100*(fIHbi/math.sin((fIthetai+fIthetaj)*math.pi/180))))+fIBbi+fIbeov
            return(fOlei)

          elif fIuserdefine ==2:
            if fIBbj/fIB > 0.85 or fIthetaj > 50:
              fOlej = 2*(fIHbj-1.2*fItbj)/math.sin(fIthetaj*math.pi/180)
            else:
              fIbeoj = min(10/(fIB/fIt)*(fIFy*fIt/(fIFybj*fItbj))*fIBbj, fIBbj)
              fOlej = 2*fIHbj/math.sin(fIthetaj*math.pi/180)+2*fIbeoj
            return(fOlej)


# 

