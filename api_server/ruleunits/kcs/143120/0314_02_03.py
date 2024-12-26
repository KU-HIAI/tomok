import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_0314_02_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.14 (2) ③'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '응력제거 열처리'

    description = """
    용접
    3. 시공
    3.14 응력제거 열처리
    """

    content = """
    #### 3.14 응력제거 열처리
    (2) 응력제거 열처리는 다음 조건에 준하여 실시해야 한다.
    ③ 열처리 고장력강이 최대온도 600 ℃에 도달된 후 또는 다른 강재가 평균온도범위 590℃와 650 ℃ 사이에 도달된 후에는, 용접두께에 따라 표 3.14-1의 규정시간 이상 동안 조립품의 온도를 유지시켜야 한다.
    응력제거가 치수안정을 목적으로 하는 경우, 유지시간은 두꺼운 쪽의 부재를 기준으로 하여 표 3.14-1에 기록된 시간 이상으로 유지시켜야 한다. 또한 유지시간 동안 가열된 부재의 전 부분에 걸쳐서 최고온도와 최저온도 차이가 80℃ 이상이 되어서는 안 된다.
    표 3.14-1 최소 유지시간
    \begin{table}[]
\begin{tabular}{lll}
두께  6.0 mm 이하 & \begin{tabular}[c]{@{}l@{}}두께 6.0 mm 초과\\ ∼50 mm 이하\end{tabular} & 두께  50 mm 초과 \\
15분 & 1시간/25 mm & 2시간+50 mm를 초과하는 두께에 대해서 25 mm당 15분 추가
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 응력제거 열처리"];
    B["KCS 14 31 20 3.14 (2) ③"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.14 (2) ③"])

    subgraph Variable_def
    VarOut[/"출력변수: 최소 유지시간"/];
    VarIn1[/입력변수: 열처리 고장력강 최대온도/];
    VarIn2[/입력변수: 다른 강재의 평균온도 범위/];
    VarIn3[/입력변수: 용접 두께/];
    VarIn4[/입력변수: 응력제거가 치수안정을 목적/];
    VarIn5[/입력변수: 두꺼운 쪽의 부재/];
    VarIn6[/입력변수: 부재의 최저온도와 최고온도의 차이/];
		end
		VarOut & VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{열처리 고장력강 최대온도 >= 600 \n or 590 <= 다른 강재의 평균온도 범위 <= 650}
    C --> D{응력제거가 치수안정을 목적}
    D --|True|--> E{부재의 최저온도와 최고온도의 차이 >= 80}
    D --|False|--> F{용접두께}
    E --|True|--> G{두꺼운 쪽 부재의 두께}
    E --|Fales|--> End2
    F & G --|<= 6|--> H[15]
    F & G --|>6 and <= 50|--> I[두께/25 * 60]
    F & G --|> 50|--> J["120 + (두께-50)/25 * 15"]
    H & I & J --> End([최소 유지시간])
    H & I & J --> End2([pass or Fail])
    """

    @rule_method
    def Stress_Relief_Heat_Treatment(fIMaxQue, fIAveRan, fIThiWel, bIDemSta, fIThiMem, fIDifMem) -> RuleUnitResult:
        """ 응력제거 열처리
        Args:
        fIMaxQue (float): 열처리 고장력장 최대온도
        fIAveRan (float): 다른 강재의 평균온도 범위
        fIThiWel (float): 용접 두께
        bIDemSta (bool): 응력제거가 치수안정을 목적
        fIThiMem (float): 두꺼운 쪽의 부재 두께
        fIDifMem (float): 부재의 최저온도와 최고온도의 차이

        Returns:
        fOMinTim (float): 최소 유지시간
        pass_fail (bool): 용접 3.14 응력제거 열처리 (2) ③의 판단 결과
        """
        assert isinstance(fIMaxQue, float)
        assert isinstance(fIAveRan, float)
        assert isinstance(fIThiWel, float)
        assert isinstance(bIDemSta, bool)
        assert isinstance(fIThiMem, float)
        assert isinstance(fIDifMem, float)

        if fIMaxQue >= 600 or 590 <= fIAveRan <= 650:
          if bIDemSta == True:
            if fIDifMem < 80:
              if fIThiMem <= 6.0:
                fOMinTim = 15
                pass_fail = True
              elif 6 < fIThiMem <= 50:
                fOMinTim = (fIThiMem / 25) * 60
                pass_fail = True
              elif fIThiMem > 50:
                fOMinTim = 120 + ((fIThiMem - 50) / 25) * 15
                pass_fail = True
            else:
              fOMinTim = None
              pass_fail = False
          else:
            if fIThiWel <= 6.0:
              fOMinTim = 15
              pass_fail = True
            elif 6 < fIThiWel <= 50:
              fOMinTim = (fIThiWel / 25) * 60
              pass_fail = True
            elif fIThiWel > 50:
              fOMinTim = 120 + ((fIThiWel - 50) / 25) * 15
              pass_fail = True
        else:
          fOMinTim = None
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "fOMinTim": fOMinTim,
                    "pass_fail": pass_fail
                }
            )