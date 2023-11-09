from tomok.core.rule_ifc import RuleIFC
from tomok.ifc.reader import IFCReader
from tomok.ifc.entity import Product
from kds142054_040305_01 import KDS142054_040305_01
from kds142054_040305_03 import KDS142054_040305_03
from kds142054_040305_04 import KDS142054_040305_04
from kds142054_040305_05 import KDS142054_040305_05
from tomok.core.util import *

class RuleIFC_KDS124054_040305_01(RuleIFC):
    # RuleIFC의 실행함수에 필요한 룰유닛을 가져옵니다.
    ruleunit_1 = KDS142054_040305_01()
    ruleunit_3 = KDS142054_040305_03()
    ruleunit_4 = KDS142054_040305_04()
    ruleunit_5 = KDS142054_040305_05()

    def __init__(self,
                 reader: IFCReader):
        self.reader = reader
    def retrieve_entities(
        self,
        guid: str):
        logging_normal(content=f"Target GUID: {guid}", tag="SEARCH")
        self.reader.get_products() # IFCReader에서 부재의 목록을 가져옵니다.
        try:
            target_entitiy = [self.reader.get_product_by_guid(guid)] # 입력한 guid와 매칭되는 부재를 찾습니다.
            logging_info(content="retrieved entity = {}".format(target_entitiy), tag="FIND")
        except: # 입력한 guid와 매칭되는 부재가 없는 경우
            logging_info(content="Target Entity NOT FOUND!!!", tag="ALART")
            return []
        return target_entitiy
    
    @classmethod
    def process(cls,
                entity: Product,
                ):
        logging_normal("RuleIFC: process START...")
        try:
            # 임시 값입니다. 원래는 IFCPropertySet에서 entity 내에 포함된 값을 가져와야합니다.
            fOpsecNa = None
            fOpsedNa = None
            fOpscpNa = None
            fIeprimN = 50
            fIcNa = 90
            fIcamin = 100
            fIcac = 90
            # ruleunit 1의 실행에 필요한 3, 4, 5번 항목의 결과 값을 계산합니다.
            kds142054_040305_03_result = cls.ruleunit_3.correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force(fOpsecNa,fIeprimN,fIcNa)
            kds142054_040305_04_result = cls.ruleunit_4.correction_factor_for_edge_influence_of_single_or_group_of_anchor(fOpsedNa,fIcamin,fIcNa)
            kds142054_040305_05_result = cls.ruleunit_5.modification_factors_for_bonded_anchors_used_in_uncracked_concrete(fOpscpNa,fIcamin,fIcac)
            
            fINa = 80
            fINag = 80
            fIANa = 500000
            fIANao = 88947.4
            fIpsedNa = kds142054_040305_03_result
            fIpscpNa = kds142054_040305_05_result
            fINba = 15
            fIpsecNa = kds142054_040305_04_result
            iIn = 6

            # ruleunit_1(항목 1)의 실행 결과를 저장합니다.
            Rule_Review_Result = cls.ruleunit_1.nominal_bond_strength_of_a_single_bonded_anchor(
                fINa, fINag, fIANa, fIANao, fIpsedNa, fIpscpNa, fINba, fIpsecNa, iIn, fIcNa)
            
            # 실헹 결과를 출력합니다. 결과와 직접적으로 연관된 룰 유닛의 반환 형태에 따라 해당 부분의 구현이 달라질 수 있습니다.
            # 본 예시에서는 key-value로 이루어진 파이썬 딕셔너리를 반환하는 룰 유닛이 결과가 되므로 그에 맞는 출력 방법을 사용했습니다.
            for k, v in Rule_Review_Result.items():
                print("{}: {}".format(k, v))
            
        except:
            # 정합성 평가에 실패하면 (어떤 이유에서든), 실패했다고 로그를 남기며, False를 반환합니다.
            # 해당 부분의 구현도, 추후 RuleIFC 사용 방향에 따라 달라질 수 있습니다. 
            logging_warn(content="RuleIFC FAILED", tag="RESULT")
            return False