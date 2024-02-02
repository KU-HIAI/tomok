import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_04100302_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.10.3.2 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '바닥판의 허용처짐량'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 바닥판과 바닥틀
    4.10.3 한계상태
    4.10.3.2 사용한계상태
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
	    	A[바닥판의 허용처짐량];
	    	B["KDS 24 14 31 4.10.3.2(2)"];
	    	A ~~~ B
	    	end

	    subgraph Variable_def
	     VarOut1[/출력변수: 바닥판의 허용처짐량/];

       VarIn1[/입력변수: 바닥판 지지부재의 중심간 거리/] ;
	    	end

    Python_Class ~~~ Variable_def

		    D[L/1200] ;
		    E{보도부} ;
        G[L/1000];
        H[L/800];
    Variable_def --> E
		    D & G & H --> I([바닥판의 허용처짐량])

     E--매우중요-->D;
     E--Yes-->G;
     E--No-->H;
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def floor_plate_allowable_deflection(fOfpadef,fIpladef,fIdiscbm,fIuserdefined) -> bool:
        """바닥판의 허용처짐량

        Args:
            fOfpadef (float): 바닥판의 허용처짐량
            fIpladef (float): 바닥판의 처짐량
            fIdiscbm (float): 바닥판 지지부재의 중심간 거리
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.10.3.2 사용한계상태 (2)의 값
        """

        if fIuserdefined == 1:
          fOfpadef = fIdiscbm/800
          if fIpladef <= fOfpadef:
              return fOfpadef, "Pass"
          else:
              return fOfpadef, "Fail"

        if fIuserdefined == 2:
          fOfpadef = fIdiscbm/1000
          if fIpladef <= fOfpadef:
            return fOfpadef, "Pass"
          else:
            return fOfpadef, "Fail"

        if fIuserdefined == 3:
          fOfpadef = fIdiscbm/1200
          if fIpladef <= fOfpadef:
            return fOfpadef, "Pass"
          else:
            return fOfpadef, "Fail"

        if fIuserdefined == None:
          fOfpadef = fIdiscbm/1200
          if fIpladef <= fOfpadef:
            return fOfpadef, "Pass"
          else:
            return fOfpadef, "Fail"


# 

