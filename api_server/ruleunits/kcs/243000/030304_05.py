import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_030304_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 3.3.4 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '아이바'

    description = """
    강교량공사
    3. 시공
    3.3 볼트접합
    3.3.4 시공
    (5)
    """
    content = """
    #### 3.3.4 시공
    (5) 아이바
    ① 아이바의 단면적은 계산상 필요단면적의 135% 이상으로 한다.
    ② 아이바의 머리모양은 핀구멍과 동심원으로 한다.
    ③ 아이바의 두께는 최소 25 mm 이상으로 하고 핀의 지름은 아이바 폭의 8/10 보다 크게 하는 것이 좋다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 아이바];
    B["KCS 24 30 00 3.3.4 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.3.4 (5)"])

    subgraph Variable_def
    VarIn1[/입력변수: 아이바의 단면적/];
    VarIn2[/입력변수: 아이바의 필요단면적/];
    VarIn3[/입력변수: 아이바의 두께/];
    VarIn4[/입력변수: 핀의 지름/];
    VarIn5[/입력변수: 아이바 폭/];
    VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"아이바의 단면적 >= 아이바의 필요단면적*1.35 \n 아이바의 두께 >=25 \n 핀의 지름>아이바 폭*0.8 \n."}
    C --> End([Pass or Fail])
    """

    @rule_method

    def eyebar_dimension(fISecAre,fIReqAre,fIThiEye,fIDiaPin,fIEyeWid) -> RuleUnitResult:
        """
        Args:
            fISecAre (float): 아이바의 단면적
            fIReqAre (float): 아이바의 필요단면적
            fIThiEye (float): 아이바의 두께
            fIDiaPin (float): 핀의 지름
            fIEyeWid (float): 아이바 폭

        Returns:
            pass_fail (bool): 강교량공사 3.3.4 시공 (5)의 판단 결과
        """
        assert isinstance(fISecAre,float)
        assert isinstance(fIReqAre,float)
        assert isinstance(fIThiEye,float)
        assert isinstance(fIDiaPin,float)
        assert isinstance(fIEyeWid,float)


        if fISecAre>=fIReqAre*1.35 and fIThiEye>=25 and fIDiaPin >fIEyeWid*0.8:
            pass_fail = True
        else:
            pass_fail = False
        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })