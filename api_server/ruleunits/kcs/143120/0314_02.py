import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_0314_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.14 (2)'
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
    ② 315℃ 이상에서의 가열비(℃/hr)는 가장 두꺼운 부재를 기준으로 25 mm당 1시간에 220 ℃를 초과해서는 안 된다.
    또한 어떠한 경우도 단위 시간당의 가열온도가 220℃를 초과해서는 안 된다. 가열 중에 가열시키는 부재의 전 부위의 온도편차는 5 m 길이 이내에서 140 ℃ 이하가 되도록 해야 한다.
    ③ 열처리 고장력강이 최대온도 600 ℃에 도달된 후 또는 다른 강재가 평균온도범위 590℃와 650 ℃ 사이에 도달된 후에는, 용접두께에 따라 표 3.14-1의 규정시간 이상 동안 조립품의 온도를 유지시켜야 한다.
    응력제거가 치수안정을 목적으로 하는 경우, 유지시간은 두꺼운 쪽의 부재를 기준으로 하여 표 3.14-1에 기록된 시간 이상으로 유지시켜야 한다. 또한 유지시간 동안 가열된 부재의 전 부분에 걸쳐서 최고온도와 최저온도 차이가 80℃ 이상이 되어서는 안 된다.
    표 3.14-1 최소 유지시간
    \begin{table}[]
\begin{tabular}{
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l }
{\color[HTML]{333333} 두께  6.0 mm 이하} &
  {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}두께 6.0 mm 초과\\ ∼50 mm 이하\end{tabular}} &
  {\color[HTML]{333333} 두께  50 mm 초과} \\
{\color[HTML]{333333} 15분} &
  {\color[HTML]{333333} 1시간/25 mm} &
  {\color[HTML]{333333} 2시간+50 mm를 초과하는 두께에 대해서 25 mm당 15분 추가}
\end{tabular}
\end{table}
    ④ 315 ℃ 이상에서의 냉각비(℃/hr)는 밀폐된 노(爐) 또는 용기 내에서 가장 두꺼운 부재를 기준으로 25 mm당 1시간에 315 ℃ 이하가 되어야 하며,
    어떠한 경우에도 단위시간당 냉각온도가 260 ℃를 초과해서는 안 된다. 또, 315 ℃ 미만에서는 조립품을 공냉 시킬 수 있다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 응력제거 열처리"];
    B["KCS 14 31 20 3.14 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.14 (2)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/"출력변수: 가열비"/];
    VarIn1[/입력변수: 온도/];
    VarIn2[/입력변수: 가열비/];
    VarIn3[/입력변수: 단위 시간당 가열온도/];
    VarIn4[/입력변수: 가열 부재 전부위의 온도편차/];
		end
		subgraph V2
    VarOut2[/"출력변수: 최소 유지시간"/];
    VarIn51[/입력변수: 열처리 고장력강 최대온도/];
    VarIn5[/입력변수: 다른 강재의 평균온도 범위/];
    VarIn6[/입력변수: 용접 두께/];
    VarIn7[/입력변수: 응력제거가 치수안정을 목적/];
    VarIn8[/입력변수: 두꺼운 쪽의 부재/];
    VarIn9[/입력변수: 부재의 최저온도와 최고온도의 차이/];
		end
		subgraph V3
    VarOut3[/"출력변수: 냉각비"/];
    VarIn10[/입력변수: 온도/];
    VarIn11[/입력변수: 냉각비/];
    VarIn12[/입력변수: 단위시간당 냉각온도/];
		end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"가열비 \n 최소 유지시간 \n 냉각비\n."}
		C --> |"가열비"|D{"온도 ≥ 315℃"}
		D --> |True|F{가열비 \n 단위 시간당의 가열온도 \n 가열 부재 전부위의 온도편차}
		F --> |가열비|G["가장 두꺼운 부재를 기준으로 \n25 mm당 1시간에 220 ℃를 초과해서는 안 된다."]
		F --> |단위 시간당의 가열온도|H["220℃를 초과해서는 안 된다"]
		F --> |가열 부재 전부위의 온도편차|I["5 m 길이 이내에서 140 ℃ 이하"]
		C --> |"최소 유지시간"|J{"열처리 고장력강 최대온도 \n or \n 다른 강재의 평균온도 범위 \n."}
		J --> K{응력제거가 치수안정을 목적}
		K --> |True|L{두꺼운 쪽의 부재}
		K --> |False|M{용접두께}
		L --> |True|M{용접두께}
		M --> |"표 3.14-1"|N[최소 유지시간]
		C --> |냉각비|O{"온도 ≥ 315℃"}
		O --> |True|P{냉각비, 단위시간당 냉각온도}
		P --> |냉각비|Q["밀폐된 노(爐) 또는 용기 내에서 \n 가장 두꺼운 부재를 기준으로 \n25 mm당 1시간에 315 ℃ 이하"]
		P --> |단위시간당 냉각온도|R["260 ℃를 초과해서는 안 된다"]
		O --> |False|S[조립품을 공냉 시킬 수 있다.]
		G & H & I & N & Q & R & S --> End([응력제거 열처리])
    """

    @rule_method
    def Heating_Ratio(fITem, bIHeaRat, bIHeaTem, bITemDev, fIMaxQue, fIAveRan, fIThiWel, bIDemSta, bIThiMem, fIDifMem, bICooRat, bICooTem) -> str:
        """ 응력제거 열처리
        Args:
        fITem (float): 온도
        bIHeaRat (bool): 가열비
        bIHeaTem (bool): 단위 시간당 가열온도
        bITemDev (bool): 가열 부재 전부위의 온도편차
        fIMaxQue (float): 열처리 고장력장 최대온도
        fIAveRan (float): 다른 강재의 평균온도 범위
        fIThiWel (float): 용접 두께
        bIDemSta (bool): 응력제거가 치수안정을 목적
        bIThiMem (bool): 두꺼운 쪽의 부재
        fIDifMem (float): 부재의 최저온도와 최고온도의 차이
        bICooRat (bool): 냉각비
        bICooTem (bool): 단위시간당 냉각온도

        Returns:
        sOHeaRat (str): 가열비
        sOMinTim (str): 최소 유지시간
        sOCooRat (str): 냉각비
        """
        assert isinstance(fITem, float)
        assert isinstance(bIHeaRat, bool)
        assert isinstance(bIHeaTem, bool)
        assert isinstance(bITemDev, bool)
        assert (bIHeaRat + bIHeaTem + bITemDev) == 1
        assert isinstance(fIMaxQue, float)
        assert isinstance(fIAveRan, float)
        assert isinstance(fIThiWel, float)
        assert isinstance(bIDemSta, bool)
        assert isinstance(bIThiMem, bool)
        assert isinstance(fIDifMem, float)
        assert isinstance(bICooRat, bool)
        assert isinstance(bICooTem, bool)
        assert bICooRat != bICooTem

        if fITem >= 350:
          if bIHeaRat == True:
            sOHeaRat = "가장 두꺼운 부재를 기준으로 25 mm당 1시간에 220 ℃를 초과해서는 안 된다."
          elif bIHeaTem == True:
            sOHeaRat = "단위 시간당의 가열온도가 220℃를 초과해서는 안 된다."
          elif bITemDev == True:
            sOHeaRat = "가열시키는 부재의 전 부위의 온도편차는 5 m 길이 이내에서 140 ℃ 이하가 되도록 해야 한다."

        if fIMaxQue >= 600 or 590 <= fIAveRan <= 650:
          if bIDemSta == True and bIThiMem == True:
            if fIDifMem < 80:
              if fIThiWel <= 6.0:
                sOMinTim = "15분 이상으로 유지"
              elif 6 < fIThiWel <= 50:
                sOMinTim = "1시간/25 mm 이상으로 유지"
              elif fIThiWel > 50:
                sOMinTim = "2시간+50 mm를 초과하는 두께에 대해서 25 mm당 15분 추가 이상으로 유지"
            elif fIDifMem >= 80:
              sOMminTim = "Fail"
          else:
            if fIThiWel <= 6.0:
              sOMinTim = "15분"
            elif 6 < fIThiWel <= 50:
              sOMinTim = "1시간/25 mm"
            elif fIThiWel > 50:
              sOMinTim = "2시간+50 mm를 초과하는 두께에 대해서 25 mm당 15분 추가"

        if fITem >= 315:
          if bICooRat == True:
            sOCooRat = "밀폐된 노(爐) 또는 용기 내에서 가장 두꺼운 부재를 기준으로 25 mm당 1시간에 315 ℃ 이하"
          elif bICooTem == True:
            sOCooRat = "단위시간당 냉각온도가 260 ℃를 초과해서는 안 된다."
        else:
          sOCooRat = "조립품을 공냉 시킬 수 있다."

        return RuleUnitResult(
                result_variables = {
                    "sOHeaRat": sOHeaRat,
                    "sOMinTim": sOMinTim,
                    "sOCooRat": sOCooRat,
                }
            )