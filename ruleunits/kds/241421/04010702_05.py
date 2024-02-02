import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010702_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.7.2 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '쉘요소 설계'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.2 쉘요소 설계
    (5)
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
    A["쉘요소 설계"];
    B["KDS 24 14 21 4.1.7.2 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 판-1의 셀요소의 단위폭당 면내 전단력/];
		VarIn2[/입력변수: 쉘요소의 두께/];
		VarIn3[/입력변수: 판-1의 두께/];
		VarIn4[/입력변수: 판-2의 두께/];
		VarIn5[/입력변수: 판-2의 셀요소의 단위폭당 면내 전단력/];
		VarIn6[/입력변수: 셀요소의 단위폭당 면내 전단력/];
		VarIn7[/입력변수: 판-1의 면내 종방향 축력/];
		VarIn8[/입력변수: 횡방향 휨모멘트/];
		VarIn9[/입력변수: 핵판의 두께/];
		VarIn10[/입력변수: 횡방향 휨모멘트/];
		VarOut1[/출력변수: 판-1의 전단응력/];
		VarOut2[/출력변수: 판-2의 전단응력/];
		VarOut3[/출력변수: 판-1의 종방향 압축응력/];
		VarOut4[/출력변수: 판-2의 종방향 압축응력/];
		VarOut5[/출력변수: 판-1의 횡방향 압축응력/];
		VarOut6[/출력변수: 판-2의 횡방향 압축응력/];

		VarOut1 & VarOut2 & VarOut3 & VarOut4 & VarOut5 & VarOut6
		~~~VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    VarIn3~~~VarIn6 & VarIn7 & VarIn8 & VarIn9 & VarIn10
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D & E & F & G & H & I
		C{"콘크리트 기준강도 50MPa이하인경우"}
		D["<img src='https://latex.codecogs.com/svg.image?v&space;_1=\frac{q_1}{t_1}=\frac{q(t-t_2)}{(2t-t_1-t_2)t_1}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?v&space;_2=\frac{q_2}{t_2}=\frac{q(t-t_1)}{(2t-t_1-t_2)t_2}'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?f_{nl1}=\frac{n_{l1}}{t_1}=\frac{n_l(t-t_2)}{(2t-t_1-t_2)t_1}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?f_{nl1}=\frac{n_{l1}}{t_2}=\frac{n_l(t-t_1)}{(2t-t_1-t_2)t_2}'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?f_{nt1}=\frac{m_u}{z_ct_1}=\frac{m_u}{[t-(t_1&plus;t_2)/2]t_1}'>---------------------------------"]
		I["<img src='https://latex.codecogs.com/svg.image?f_{nt2}=\frac{m_u}{z_ct_2}=\frac{m_u}{[t-(t_1&plus;t_2)/2]t_2}'>---------------------------------"]
		J(["판-1의 전단응력"])
		K(["판-2의 전단응력"])
		L(["판-1의 종방향 압축응력"])
		M(["판-2의 종방향 압축응력"])
		N(["판-1의 횡방향 압축응력"])
		O(["판-2의 횡방향 압축응력"])
		D--->J
		E--->K
		F--->L
		G--->M
		H--->N
		I--->O
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shear_stress(fOv1,fIq1,fIt,fIt1,fIt2,fOv2,fIq2,fIq,fOfnl1,fInl1,fOfnl2,fOfnt1,fImu,fIzc,fOfnt2) -> bool:
        """쉘요소 설계

        Args:
             fOv1 (float): 판-1의 전단응력
             fIq1 (float): 판-1의 셀요소의 단위폭당 면내 전단력
             fIt (float): 쉘요소의 두께
             fIt1 (float): 판-1의 두께
             fIt2 (float): 판-2의 두께
             fOv2 (float): 판-2의 전단응력
             fIq2 (float): 판-2의 셀요소의 단위폭당 면내 전단력
             fIq (float): 셀요소의 단위폭당 면내 전단력
             fOfnl1 (float): 판-1의 종방향 압축응력
             fInl1 (float): 판-1의 면내 종방향 축력
             fOfnl2 (float): 판-2의 종방향 압축응력
             fOfnt1 (float): 판-1의 횡방향 압축응력
             fImu (float): 횡방향 휨모멘트
             fIzc (float): 핵판의 두께
             fOfnt2 (float): 판-2의 횡방향 압축응력

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.7.2 쉘요소 설계 (5)의 값
        """

        fOv1 = fIq*(fIt-fIt2)/((2*fIt-fIt1-fIt2)*fIt1)
        fOv2 = fIq*(fIt-fIt2)/((2*fIt-fIt1-fIt2)*fIt2)
        fOfnl1 = fInl1*(fIt-fIt1)/((2*fIt-fIt1-fIt2)*fIt1)
        fOfnl2 = fInl1*(fIt-fIt1)/((2*fIt-fIt1-fIt2)*fIt2)
        fOfnt1 = fImu/((fIt-(fIt1+fIt2)/2)*fIt1)
        fOfnt2 = fImu/((fIt-(fIt1+fIt2)/2)*fIt2)

        return fOv1,fOv2, fOfnl1, fOfnl2, fOfnt1, fOfnt2


# 

