# python
from argparse import ArgumentTypeError
from typing import List, Generator, Union
from functools import lru_cache
import re

# 3rd-party
import ifcopenshell
from ifcopenshell.entity_instance import entity_instance

# framework
from .property_set import PropertySet
from .entity import Product
from .util import get_ifc_property_set_from_entity


class IFCReader():
    guid_product_cache = {}

    def __init__(self,
                 ifc_filepath: str):
        # ifcopenshell C language escape character error fix
        self.fix_escape_char_error(ifc_filepath)
        self.ifc = ifcopenshell.open(ifc_filepath)
        self.get_products()

    def fix_escape_char_error(self,
                              ifc_filepath: str):
        """IFC 파일의 escape char 에러를 완화시키는 함수.

        IFC 파일에 esacpe 글자가 들어갈 경우 ifcopenshell이 fault나고, ifc_verifier 프로그램이 종료되게 됩니다.
        escape 글자가 빈번히 사용되므로 (예: FILE_NAME에 파일 경로) 해결해야 될 필요성이 있습니다.
        본 함수는 FILE_NAME의 값을 제거해서 escape 글자 에러를 회피합니다.
        (주의) 이전 IFC파일은 값을 제거한 IFC 파일로 덮어쓰여지게 됩니다.

        Args:
            ifc_filepath (str): 검사를 수행할 IFC 파일 경로
        """
        modified = False
        with open(ifc_filepath, 'r') as fp:
            lines = fp.readlines()
        regex = r"(FILE_NAME\()\'[^\']*\'"
        for idx in range(len(lines)):
            line = lines[idx]
            if line.startswith('FILE_NAME'):
                lines[idx] = re.sub(regex, r"\g<1>''", line)
                modified = lines[idx] != line
                break  # FILE_NAME만 고치면 되므로 이후 line은 볼 필요가 없음
        if(modified):
            with open(ifc_filepath, 'w') as fp:
                fp.writelines(lines)

    @lru_cache
    def _get_ifc_property_set(
        self,
        from_entity: entity_instance
    ) -> List[entity_instance]:
        """특정 entity가 가지고 있는 IfcPropertySet들을 반환

        사용 예)
        ```python
        psets = self._get_ifc_property_set(entity)
        ```

        Args:
            from_entity (entity_instance): 탐색을 시작하는 entity

        Returns:
            List[entity_instance]: IfcPropertySet의 집합
        """
        return get_ifc_property_set_from_entity(self.ifc, from_entity)

    def get_ifc_products(
        self,
        ifc_product_type: str = None
    ) -> List[entity_instance]:
        """IFC 파일에 존재하는 product들을 반환

        사용 예)
        ```python
        ifc.get_products()
        # [#142=IfcBuilding('3jFItWokXEReTKxuco5LtJ',#42,'',$,$,#33,$,'',.ELEMENT.,$,$,#138),
        #  #155=IfcBuildingStorey('3jFItWokXEReTKxubDwgCL',#42,'1F',$,'레벨:삼각형 헤드',#153,$,'1F',.ELEMENT.,0.),
        #  #171=IfcSite('3jFItWokXEReTKxuco5LtG',#42,'Default',$,$,#170,$,$,.ELEMENT.,(37,33,59,529418),(126,58,40,678710),0.,$,$),
        #  #335=IfcBeam('3tke7nC1HEAgqfTM8BlJS6',#42,'2C:2C 고원희 선배님:376319',$,'2C:2C 고원희 선배님',#333,#324,'376319',.BEAM.),
        #  #413=IfcBeam('3tke7nC1HEAgqfTM8BlJLl',#42,'2C:2C 고원희 선배님:376726',$,'2C:2C 고원희 선배님',#412,#405,'376726',.BEAM.),
        #  #463=IfcBeam('3tke7nC1HEAgqfTM8BlJLI',#42,'2C:2C 고원희 선배님:376747',$,'2C:2C 고원희 선배님',#462,#455,'376747',.BEAM.),
        #  #513=IfcBeam('3tke7nC1HEAgqfTM8BlJKo',#42,'2C:2C 고원희 선배님:376779',$,'2C:2C 고원희 선배님',#512,#505,'376779',.BEAM.),
        #  #563=IfcBeam('3tke7nC1HEAgqfTM8BlJKG',#42,'2C:2C 고원희 선배님:376809',$,'2C:2C 고원희 선배님',#562,#555,'376809',.BEAM.),
        #  #647=IfcBeam('3tke7nC1HEAgqfTM8BlKci',#42,'콘크리트-직사각형 보:900 x 2500:377685',$,'콘크리트-직사각형 보:900 x 2500',#646,#639,'377685',.BEAM.),
        #  #720=IfcSlab('1uU3Yi_az468Nth$d2cTyv',#42,'바닥:일반 240mm:383354',$,'바닥:일반 240mm',#689,#716,'383354',.FLOOR.),
        #  #794=IfcSlab('2Ork2ppF5CRx6Mi3QlKWSD',#42,'바닥:일반 240mm:383479',$,'바닥:일반 240mm',#764,#790,'383479',.FLOOR.),
        #  #862=IfcSlab('2Ork2ppF5CRx6Mi3QlKWJe',#42,'바닥:일반 240mm:383506',$,'바닥:일반 240mm',#832,#858,'383506',.FLOOR.),
        #  #930=IfcSlab('2Ork2ppF5CRx6Mi3QlKWJN',#42,'바닥:일반 240mm:383533',$,'바닥:일반 240mm',#900,#926,'383533',.FLOOR.),
        #  #998=IfcSlab('2Ork2ppF5CRx6Mi3QlKWIo',#42,'바닥:일반 240mm:383560',$,'바닥:일반 240mm',#968,#994,'383560',.FLOOR.)]
        ```

        Returns:
            List[entity_instance]: IfcProduct의 집합
        """
        products = self.ifc.by_type('IfcProduct')
        if(ifc_product_type is not None):
            products = [p for p in products if p.is_a(ifc_product_type)]
        return products

    def get_ifc_property_set(
        self,
        property_set_name: str = None,
        from_entity: entity_instance = None
    ) -> List[entity_instance]:
        """IFC 파일 혹은 특정 entity가 가지고 있는 IfcPropertySet을 반환한다.

        사용 예)
        ```python
        ifc.get_property_set('Pset_MaterialConcrete')
        # [#142=IfcBuilding('3jFItWokXEReTKxuco5LtJ',#42,'',$,$,#33,$,'',.ELEMENT.,$,$,#138),
        # #155=IfcBuildingStorey('3jFItWokXEReTKxubDwgCL',#42,'1F',$,'레벨:삼각형 헤드',#153,$,'1F',.ELEMENT.,0.),
        # #171=IfcSite('3jFItWokXEReTKxuco5LtG',#42,'Default',$,$,#170,$,$,.ELEMENT.,(37,33,59,529418),(126,58,40,678710),0.,$,$),
        # #335=IfcBeam('3tke7nC1HEAgqfTM8BlJS6',#42,'2C:2C 고원희 선배님:376319',$,'2C:2C 고원희 선배님',#333,#324,'376319',.BEAM.),
        # #413=IfcBeam('3tke7nC1HEAgqfTM8BlJLl',#42,'2C:2C 고원희 선배님:376726',$,'2C:2C 고원희 선배님',#412,#405,'376726',.BEAM.),
        # #463=IfcBeam('3tke7nC1HEAgqfTM8BlJLI',#42,'2C:2C 고원희 선배님:376747',$,'2C:2C 고원희 선배님',#462,#455,'376747',.BEAM.),
        # #513=IfcBeam('3tke7nC1HEAgqfTM8BlJKo',#42,'2C:2C 고원희 선배님:376779',$,'2C:2C 고원희 선배님',#512,#505,'376779',.BEAM.),
        # #563=IfcBeam('3tke7nC1HEAgqfTM8BlJKG',#42,'2C:2C 고원희 선배님:376809',$,'2C:2C 고원희 선배님',#562,#555,'376809',.BEAM.),
        # #647=IfcBeam('3tke7nC1HEAgqfTM8BlKci',#42,'콘크리트-직사각형 보:900 x 2500:377685',$,'콘크리트-직사각형 보:900 x 2500',#646,#639,'377685',.BEAM.),
        # #720=IfcSlab('1uU3Yi_az468Nth$d2cTyv',#42,'바닥:일반 240mm:383354',$,'바닥:일반 240mm',#689,#716,'383354',.FLOOR.),
        # #794=IfcSlab('2Ork2ppF5CRx6Mi3QlKWSD',#42,'바닥:일반 240mm:383479',$,'바닥:일반 240mm',#764,#790,'383479',.FLOOR.),
        # #862=IfcSlab('2Ork2ppF5CRx6Mi3QlKWJe',#42,'바닥:일반 240mm:383506',$,'바닥:일반 240mm',#832,#858,'383506',.FLOOR.),
        # #930=IfcSlab('2Ork2ppF5CRx6Mi3QlKWJN',#42,'바닥:일반 240mm:383533',$,'바닥:일반 240mm',#900,#926,'383533',.FLOOR.),
        # #998=IfcSlab('2Ork2ppF5CRx6Mi3QlKWIo',#42,'바닥:일반 240mm:383560',$,'바닥:일반 240mm',#968,#994,'383560',.FLOOR.)]

        ifc.get_property_set('Pset_MaterialConcrete', ifc.get_products()[3])
        # [#25011=IfcPropertySet('3P5S1mzfH4txefjZg29E04',#42,'Pset_MaterialConcrete',$,(#25012,#25013,#25014,#25015))]
        ```

        Args:
            property_set_name (str): 
                property_set_name이 지정되어 있을 경우, 해당 set_name을 가지고 있는 property set만 반환한다.
                Defaults to None.
            from_entity (entity_instance, optional): 
                탐색 시작 entity.
                entity를 지정할 경우, 해당 entity아래에 속한 property set만 탐색한다.
                None인 경우, IFC 파일에 있는 모든 property set을 탐색한다.
                Defaults to None.

        Returns:
            List[entity_instance]: IfcPropertySet의 집합
        """
        if(property_set_name is not None):
            def name_filter(name): return name == property_set_name
        else:
            def name_filter(name): return True
        if from_entity:
            return [p_set for p_set in self._get_ifc_property_set(from_entity) if name_filter(p_set.Name)]
        return [p_set for p_set in self.ifc.by_type('IfcPropertySet') if name_filter(p_set.Name)]

    # @lru_cache

    def get_products(
        self,
        ifc_product_type: str = None,
        description: str = None,
        identification: str = None
    ) -> List[Product]:
        def filter(product):
            if description is None:
                return True
            else:
                return description in product.descriptions

        def id_filter(product):
            if identification is None:
                return True
            else:
                return identification in product.identifications
        products = self.get_ifc_products(ifc_product_type=ifc_product_type)
        easy_products = [Product(self.ifc, product) for product in products]
        easy_products = [
            p for p in easy_products if filter(p) and id_filter(p)]

        # find guid of all easy_products
        for e_prod in easy_products:
            # {guid: product}
            self.guid_product_cache[e_prod.get_guid()] = e_prod
        return easy_products

    # @lru_cache
    def get_property_set(
        self,
        property_set_name: str = None,
        from_entity: entity_instance = None
    ) -> List[PropertySet]:
        psets = self.get_ifc_property_set(
            property_set_name=property_set_name,
            from_entity=from_entity
        )
        easy_psets = [PropertySet(self.ifc, pset) for pset in psets]
        return easy_psets

    def get_product_by_guid(
        self,
        guid: str
    ) -> Product:
        return self.guid_product_cache[guid]
