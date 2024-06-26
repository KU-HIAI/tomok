import requests
import json
from typing import Union
from tomok import RuleIFC, IFCReader, Product, RuleUnitController
from tomok.core.results import OKNGResult


class RuleIFC_KDS142054_01(RuleIFC):
    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.5 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 부착식 앵커의 공칭부착강도'    # 건설기준명
    description = """
    descriptions about this rule.
    """
    ref_url = "https://www.kcsc.re.kr/"
    log = []
    init_log = []

    def ruleunit_call(self, uri, key='f234cf784e7c9669929122343a808bcf9607e425', base_uri='http://tomokapi.hiai.kr/v1.0/', *args, **kwargs):
        headers = {'X-Auth': key}
        api_uri = base_uri + uri
        print(api_uri)
        print(kwargs)
        response = requests.post(api_uri, headers=headers, data=kwargs)
        return response.json()

    # RuleIFC 초기화    
    def __init__(self,
                 rule_units: RuleUnitController):
        """
        초기화 함수입니다. RuleUnitController 객체를 받아서 필요한 룰 유닛을 정리합니다.
        
        Args:
            rule_units (RuleUnitController): Rule unit들을 컨트롤하는 객체입니다.
        """
        self.runit = {
            '01': 'kds/142054/040305_01(2401ver)/nominal_bond_strength_of_a_single_bonded_anchor',
            '03': 'kds/142054/040305_03(2401ver)/correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force',
            '04': 'kds/142054/040305_04(2401ver)/correction_factor_for_edge_influence_of_single_or_group_of_anchor',
            '05': 'kds/142054/040305_05(2401ver)/modification_factors_for_bonded_anchors_used_in_uncracked_concrete'
        }
        self.init_log.append('KDS 14 20 54 4.3.5 (1): 단일 부착식 앵커의 공장부착강도 검토 시작')
        for idx, runit in enumerate(self.runit):
            self.init_log.append('검토 항목:')
            self.init_log.append("[{0}] {1}".format(idx+1, self.runit[runit]))
        print(self.init_log)


    def retrieve_entities(self,
                          reader: IFCReader,
                          guid: str):
        """
        주어진 guid를 기반으로 부재를 검색하여 반환합니다.
    
        Args:
            guid (str): 검색할 제품의 고유 식별자
    
        Return:
            list: 검색된 부재 목록을 반환합니다. 만약 해당 guid를 가진 부재가 없다면 빈 리스트를 반환합니다.
        """
        import traceback
        self.log = [x for x in self.init_log]
        try:
            print(guid)
            target_entity = [reader.get_product_by_guid(guid)] # guid를 기반으로 부재를 검색합니다.
            self.log.append("검토 부재: " + str(target_entity[0]))
        except Exception as ex:
            print('부재 검색 오류')
            # 예외 메시지 출력
            print(f'Exception message: {str(ex)}')
        
            # 스택 추적 정보 출력
            traceback.print_exc()
            return []
        return target_entity


    def _has_p_value(self,
                     entity: Product,
                     krpset_name: str,
                     en_name: str):
         """
        주어진 Product 객체 안에 지정된 krpset_name과 en_name이 있는지 확인한다.
        
        Args:
            entity (Product): 검사할 Product 객체
            krpset_name (str): 찾을 krpset 이름
            en_name (str): 찾을 entity 이름

        Return:
            bool: 주어진 이름이 존재하면 True, 그렇지 않으면 False를 반환한다.
        """
         return en_name in entity[krpset_name]

    def _get_p_value(self,
                     entity: Product,
                     krpset_name: str,
                     en_name: str):
        """
        주어진 Product 객체에서 지정된 krpset_name과 en_name에 해당하는 값을 가져온다.

        Args:
            entity (Product): 검사할 Product 객체
            krpset_name (str): 추출할 krpset 이름
            en_name (str): 추출할 entity 이름

        Return:
            object: 해당 field의 값을 반환한다. 만약에 값이 없다면 -1를 반환한다.
        """
        try:
            return entity[krpset_name][en_name]
        except:                
            return -1
    
    def _set_p_value(self,
                     entity: Product,
                     krpset_name: str,
                     en_name: str,
                     value: object):
        """
        주어진 Product 객체에서 지정된 krpset_name과 en_name에 해당하는 field에 값을 설정한다.

        Args:
            entity (Product): 수정할 Product 객체
            krpset_name (str): 수정할 krpset 이름
            en_name (str): 수정할 entity 이름
            value (object): 설정할 값

        Raises:
            Exception: 만약 field를 수정하지 못하면 Exception을 발생시킨다.
        """
        try:
            entity[krpset_name][en_name] = value
        except Exception as ex:
            raise(ex)
        
    def pre_process(self,
                entity: Product):
        """RuleIFC가 다른 Rule Unit들의 계산 결과를 필요로 할 때, pre-process 함수는 이러한 필요한 계산을 처리하고 그 결과를 저장합니다.
        이 단계는 모든 필요한 데이터와 계산이 주요 규칙 실행 단계에서 사용할 수 있도록 준비되고 정리되어 있음을 보장해야 합니다.

        Args:
            entity (Product): IFC 부재

        Raises:
            ex: 예외
        """
        try:
            # KDS142054_040305_03 계산 결과가 없을 경우 계산하여 저장
            if not self._has_p_value(entity, 
                                     krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                                     en_name="fPosecNa"):
                # fOpsecNa = self._get_p_value(entity=entity,
                #                             krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                #                             en_name="Correction factor for attached anchor groups in which eccentricity of tensile force acts")
                fIeprimN = self._get_p_value(entity=entity,
                                            krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                                            en_name="The distance between the resultant force of the tensile force acting on the anchor group subjected to tensile load and the centroid of the anchor group")
                fIcNa = self._get_p_value(entity=entity,
                                        krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                                        en_name="The distance from the center of the anchor to the edge of the projected influence area required to develop the maximum bond strength")
                runit03_output = self.ruleunit_call(uri=self.runit['03'], fOpsecNa=0, fIeprimN=fIeprimN, fIcNa=fIcNa)
                print(runit03_output)
                fOpsecNa = runit03_output['fOpsecNa']
                print(self.log)
                self.log.append('룰 유닛 실행: '+ self.runit['03'])
                print(self.log)
                self.log.append(f'correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force({0}, {fIeprimN}, {fIcNa})')
                print(self.log)
                self.log.append(f'계산 결과 : {fOpsecNa}')
                print(self.log)
                self._set_p_value(entity=entity,
                                krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                                en_name="fPosecNa",
                                value=fOpsecNa)
            # KDS142054_040305_04 계산 결과가 없을 경우 계산하여 저장
            if not self._has_p_value(entity, 
                                     krpset_name="KRPset_KDS 14 20 54_4.3.5 (4)",
                                     en_name="fOpsedNa"):
                # fOpsedNa = self._get_p_value(entity=entity,
                #                             krpset_name="KRPset_KDS 14 20 54_4.3.5 (4)",
                #                             en_name="Correction factor for edge influence of single anchor anchor or group of anchor anchors")
                fIcamin = self._get_p_value(entity=entity,
                                        krpset_name="KRPset_KDS 14 20 54_4.3.5 (4)",
                                        en_name="Minimum edge distance from anchor shaft center to concrete end")
                fIcNa = self._get_p_value(entity=entity,
                                        krpset_name="KRPset_KDS 14 20 54_4.3.5 (4)",
                                        en_name="The distance from the center of the anchor to the edge of the projected influence area required to develop the maximum bond strength")
                runit04_output = self.ruleunit_call(uri=self.runit['04'], fOpsedNa=0, fIcamin=fIcamin, fIcNa=fIcNa)
                fOpsedNa = runit04_output['fOpsedNa']
                self.log.append('룰 유닛 실행: '+ self.runit['04'])
                self.log.append(f'correction_factor_for_edge_influence_of_single_or_group_of_anchor({0}, {fIcamin}, {fIcNa})')
                self.log.append(f'계산 결과 : {fOpsedNa}')
                self._set_p_value(entity=entity,
                                krpset_name="KRPset_KDS 14 20 54_4.3.5 (4)",
                                en_name="fOpsedNa",
                                value=fOpsedNa)
            # KDS142054_040305_04 계산 결과가 없을 경우 계산하여 저장
            if not self._has_p_value(entity, 
                                     krpset_name="KRPset_KDS 14 20 54_4.3.5 (5)",
                                     en_name="fOpscpNa"):
                # fOpscpNa = self._get_p_value(entity=entity,
                #                             krpset_name="KRPset_KDS 14 20 54_4.3.5 (5)",
                #                             en_name="Modification factors for bonded anchors used in uncracked concrete")
                fIcamin = self._get_p_value(entity=entity,
                                        krpset_name="KRPset_KDS 14 20 54_4.3.5 (5)",
                                        en_name="Minimum edge distance from anchor shaft center to concrete end")
                fIcac = self._get_p_value(entity=entity,
                                        krpset_name="KRPset_KDS 14 20 54_4.3.5 (5)",
                                        en_name="risk podium distance")
                runit05_output = self.ruleunit_call(uri=self.runit['05'], fOpscpNa=0, fIcamin=fIcamin, fIcac=fIcac)
                fOpscpNa = runit05_output['fOpscpNa']
                self.log.append('룰 유닛 실행: '+ self.runit['05'])
                self.log.append(f'modification_factors_for_bonded_anchors_used_in_uncracked_concrete({0}, {fIcamin}, {fIcac})')
                self.log.append(f'계산 결과 : {fOpscpNa}')
                self._set_p_value(entity=entity,
                                krpset_name="KRPset_KDS 14 20 54_4.3.5 (5)",
                                en_name="fOpscpNa",
                                value=fOpscpNa)
        except Exception as ex:
             raise ex

    def process(self, entity: Product):
        """
        이 함수는 각종 연산을 처리하고 그 결과를 저장합니다. 
        계산된 결과는 다른 규칙 유닛에서 참조되거나, 사용될 수 있습니다.
        
        Args:
            entity (Product): IFC 부재
    
        출력:
            현재 "result"라는 이름으로 연산결과를 저장하고 출력합니다.
            프로세스가 성공적으로 완료되면 "process end."를 출력합니다.
            만약 예외가 발생하면 "Fail"을 출력합니다.
        """
        # Your code here...
    
        try:
            # KDS142054_040305_01
            fINa = self._get_p_value(entity=entity,
                                     krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                     en_name="Nominal bond strength of a single bonded anchor")
            fINag = self._get_p_value(entity=entity,
                                      krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                      en_name="Nominal bond strength of adhesive anchor group")
            fIANa = self._get_p_value(entity=entity,
                                      krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                      en_name="Projected influence area of anchor group")
            fIANao = self._get_p_value(entity=entity,
                                       krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                       en_name="Projected influence area of a single anchor")
            # KDS142054_040305_04 실행 결과
            fIpsedNa = self._get_p_value(entity=entity,
                              krpset_name="KRPset_KDS 14 20 54_4.3.5 (4)",
                              en_name="fOpsedNa")
            # KDS142054_040305_05 실행 결과
            fIpscpNa = self._get_p_value(entity=entity,
                              krpset_name="KRPset_KDS 14 20 54_4.3.5 (5)",
                              en_name="fOpscpNa")
            fINba = self._get_p_value(entity=entity,
                                    krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                    en_name="Basic bond strength of a single bonded anchor in tension")
            # KDS142054_040305_03 실행 결과
            fIpsecNa = self._get_p_value(entity=entity,
                              krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                              en_name="fPosecNa")
            fIn = self._get_p_value(entity=entity,
                                krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                en_name="Number of Attachable Anchors")
            fIcNa = self._get_p_value(entity=entity,
                                    krpset_name="KRPset_KDS 14 20 54_4.3.5 (3)",
                                    en_name="The distance from the center of the anchor to the edge of the projected influence area required to develop the maximum bond strength")
            fIda = self._get_p_value(entity=entity,
                                    krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                    en_name="The outer diameter of an anchor, or the shaft diameter of a head stud, head bolt, or claw bolt")
            fItauncr = self._get_p_value(entity=entity,
                                        krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                                        en_name="Characteristics Adhesion strength of adhesive anchors used in uncracked concrete")
            fIuserdefined = 1
            runit01_output = self.ruleunit_call(uri=self.runit['01'], 
                                                fINa=fINa,fINag=fINag,fIANa=fIANa,fIANao=fIANao,fIpsedNa=fIpsedNa,
                                                fIpscpNa=fIpscpNa,fINba=fINba,fIpsecNa=fIpsecNa,fIn=fIn,fIcNa=fIcNa,
                                                fIda=fIda,fItauncr=fItauncr,fIuserdefined=fIuserdefined)
            result = runit01_output['pass_fail']
            self.log.append('룰 유닛 실행: '+ self.runit['01'])
            self.log.append(f'nominal_bond_strength_of_a_single_bonded_anchor({fINa}, {fINag}, {fIANa}, {fIANao}, {fIpsedNa},{fIpscpNa},{fINba},{fIpsecNa},{fIn},{fIcNa},{fIda},{fItauncr},{fIuserdefined})')
            self.log.append(f'계산 결과 : {result}')
            
            # make_result에서 사용하도록 저장
            self._set_p_value(entity=entity,
                              krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                              en_name="result",
                              value="Pass" if result else "Fail")
            # 처리 결과 
            print(result)
            print("process end.")
        except Exception as ex:
            print("Fail")
            raise ex
    
    def make_result(self, entity: Product) -> str | OKNGResult:
        """
        이 함수는 이전에 process 함수에 의해 계산되어 저장된 결과를 가져와 적합성 여부를 반환합니다.
        
        Args:
            entity (Product): IFC 부재
    
        반환:
            OKNGResult: 연산결과에 따라 OKNGResult.PASS 또는 OKNGResult.FAIL 중 하나를 반환합니다.
    
        주의사항:
            이 함수는 연산결과가 "Pass" 또는 "Fail"만 고려하므로, 그 외의 결과를 반환하는 경우 조심해야 합니다.
        """
        # KDS142054_040305_01 실행 결과 불러오기
        result = self._get_p_value(entity=entity,
                              krpset_name="KRPset_KDS 14 20 54_4.3.5 (1)",
                              en_name="result")
        # OKNGResult 형식으로 변환 후 반환
        if result == "Pass":
            self.log.append("검토 결과: {OKNGResult.PASS}")
            return OKNGResult.PASS, self.log
        elif result == "Fail":
            self.log.append("검토 결과: {OKNGResult.FAIL}")
            return OKNGResult.FAIL, self.log