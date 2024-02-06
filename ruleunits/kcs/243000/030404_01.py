import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030404_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.4.4 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '조립 및 설치 가설공'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.4 조립 및 설치
    3.4.4 시공
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 가설공
    ① 교량받침은 KCS 24 30 05의 해당요건에 따른다.
    ② 현장 조립품을 일체로 운반하여 설치할 경우는 조립부재의 길이, 중량 및 형상을 고려하여 장비의 종류와 소요대수를 계획해야 하며 부재의 변형이 발생하지 않도록 안전하게 설치하여야 한다.
    ③ 플레이트거더교의 가설 시 10분 평균 풍속이 산들바람(3.4 m/sec ~ 5.4 m/sec) 이상의 기상조건에서는 I형 주거더의 단독 가설작업을 중지하여야 한다.
    ④ 드리프트핀
        가. 드리프트핀은 여러 부재를 함께 조립하는 경우에만 사용하여야 하되 허용오차를 벗어나 제작된 부재나 부품을 조립하는데 사용하여서는 안 된다.
        나. 부재의 조립에 사용하는 가조임볼트와 드리프트 핀의 합계는 1개소의 연결 고장력 볼트 수의 25% 이상(웨브는 15% 이상)으로, 그 중의 5% 이상을 드리프트 핀으로 하는 것이 좋다. 단, 큰 가설응력이 작용하는 경우는 그 가설 응력에 견딜 수 있는 가조임볼트와 드리프트 핀을 사용하여야 한다.
        다. 드리프트핀은 재료가 비틀리게 하거나 손상될만한 힘을 주어서 사용하여서는 안 되며, 정교하게 제작되지 않은 부재가 있을 시는 감독자의 승인을 받아 처리한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가설공];
    B["KCS 24 30 00 3.4.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.4.4 (1)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 플레이트거더교 가설 시 풍속/];
    VarIn1[/입력변수: 플레이트거더교 가설/];
    VarIn2[/입력변수: 10분 평균 풍속/];
    end
    subgraph V2
    VarOut2[/출력변수: 부재의 조립에 사용하는 가조임볼트와 드리프트 핀/];
    VarIn3[/입력변수: 가조임볼트 수/];
    VarIn4[/입력변수: 드리프트 핀 수/];
    VarIn5[/입력변수: 웨브/];
    VarIn6[/입력변수: 1개소의 연결 고장력 볼트 수/];
    VarIn7[/입력변수: 큰 가설응력 작용/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"플레이트거더교 가설 시 풍속 \n 부재의 조립에 사용하는 \n 가조임볼트와 드리프트 핀"}
    C --> |"플레이트거더교 가설 시 풍속"|D{"플레이트거더교 가설"}
    D --> |True|E{"10분 평균 풍속 > 3.4 m/sec"}
    E --> |True|F["I형 주거더의 단독 가설작업을 중지"]
    E --> |False|Pass1([Pass])
    C --> |"부재의 조립에 사용하는 가조임볼트와 드리프트 핀"|G{"큰 가설응력 작용"}
    G --> |True|L[그 가설 응력에 견딜 수 있는 가조임볼트와 드리프트 핀을 사용]
    G --> |False|H{웨브}
    H --> |True|I{"가조임볼트 수 + 드리프트 핀 수 \n ≥ 1개소의 연결 고장력 볼트 수 * 0.15 \n드리프트 핀 수 \n ≥ 1개소의 연결 고장력 볼트 수 * 0.05\n."}
    H --> |False|J{"가조임볼트 수 + 드리프트 핀 수 \n ≥ 1개소의 연결 고장력 볼트 수 * 0.25 \n 드리프트 핀 수 \n ≥ 1개소의 연결 고장력 볼트 수 * 0.05\n."}
    I & J --> |True|Pass([Pass])
    I & J --> |False|Fail([Fail])

    """

    @rule_method
    def wind_speed(bIPlaGir,fIAveWin)-> str:
        """
        Args:
            bIPlaGir (boolean): 플레이트거더교 가설
            fIAveWin (float): 10분 평균 풍속
        Returns:
            sOWinSpe (string): 플레이트거더교 가설 시 풍속
        """
        if bIPlaGir:
            if fIAveWin >3.4:
                sOWinSpe = "I형 주거더의 단독 가설작업을 중지"
            else:
                sOWinSpe = "Pass"
        else:
            return "이 기준은 플레이트거더교 가설 시에만 적용됩니다."
        return sOWinSpe

    def tightening_bolt_draft_pin(self, nINumTig,nINumDri,bIWeb,nINumHig,bILarStr)-> str:
        """
        Args:
            nINumTig (integar): 가조임볼트 수
            nINumDri (integar): 드리프트 핀 수
            bIWeb (boolean): 웨브
            nINumHig (integar): 1개소의 연결 고장력 볼트 수
            bILarStr (boolean): 큰 가설응력 작용
        Returns:
            sOTigDri (string): 부재의 조립에 사용하는 가조임볼트와 드리프트 핀
        """
        if bILarStr:
            sOTigDri = "가설 응력에 견딜 수 있는 가조임볼트와 드리프트 핀을 사용"
        else:
            if bIWeb == False:
                if nINumTig+nINumDri > nINumHig*0.25 and nINumDri > nINumHig*0.05:
                    sOTigDri = "Pass"
                else:
                    sOTigDri = "Fail"
            else:
                if nINumTig+nINumDri > nINumHig*0.15 and nINumDri > nINumHig*0.05:
                    sOTigDri = "Pass"
                else:
                    sOTigDri = "Fail"
        return sOTigDri