# python
from struct import unpack
from typing import List, Union, Generator
from argparse import ArgumentTypeError
from functools import reduce
from pprint import pprint  # for debug
from copy import deepcopy

# 3rd-party
from ifcopenshell.entity_instance import entity_instance
from ifcopenshell.file import file


def _entity_to_list(
    tuple_or_entity: Union[tuple, entity_instance]
) -> List[entity_instance]:
    """tuple 혹은 entity_instance를 입력 받아 리스트로 반환.
    ifcopenshell에서 연관정보가 1개인 경우 entity_instance 복수인 경우 tuple 형태로 반환하기 때문에
    이를 list 형태로 변환하여 사용의 편의성을 늘리고자 함

    Args:
        tuple_or_entity (Union[tuple, entity_instance]): 연관정보 (예: RelatingPropertyDefinition)

    Raises:
        ArgumentTypeError: tuple 혹은 entity_instance가 아닐 경우 에러

    Returns:
        List[entity_instance]: list로 변환된 연관정보
    """
    if type(tuple_or_entity) is tuple:
        return list(tuple_or_entity)
    elif type(tuple_or_entity) is entity_instance:
        return [tuple_or_entity]
    raise ArgumentTypeError()


def iter_inverse(
    ifc: file,
    from_entity: entity_instance,
    filter_is_a: Union[None, str] = None,
    parents: List[entity_instance] = [],
) -> Generator[entity_instance, List[entity_instance], entity_instance]:
    """from_entity를 참조하는 entity_instance들의 generator 반환.

    사용 예)
    ```python
    related_entities = list(self._get_inverse(entity))
    ```

    Args:
        ifc (file): IFC 파일
        from_entity (entity_instance): 탐색을 시작하는 entity
        filter_is_a (Union[None, str], optional): 엔터티 타입 필터 문자열. is_a 로 검사해서 true인 entity만 반환합니다.

    Yields:
        Generator[entity_instance, List[entity_instance], entity_instance]: from_entity를 참조하는 entity_instances, parents, psets
    """
    pset = None
    if filter_is_a is None or from_entity.is_a(filter_is_a):
        yield from_entity, parents
    for child_entity in ifc.get_inverse(from_entity):
        yield from iter_inverse(ifc, child_entity, filter_is_a=filter_is_a, parents=parents+[from_entity])


def get_inverse(
    ifc: file,
    from_entity: entity_instance,
    filter_is_a: Union[None, str] = None
) -> List[entity_instance]:
    """from_entity를 참조하는 entity_instance들의 list 반환.

    Args:
        ifc (file): IFC 파일
        from_entity (entity_instance): 탐색을 시작하는 entity
        filter_is_a (Union[None, str], optional): 엔터티 타입 필터 문자열. is_a 로 검사해서 true인 entity만 반환합니다.

    Returns:
        List[entity_instance]: from_entity를 참조하는 entity_instances
    """
    return list([entity for entity, parents in iter_inverse(ifc=ifc, from_entity=from_entity, filter_is_a=filter_is_a)])


def get_ifc_property_set_from_entity(
    ifc: file,
    entity: entity_instance
) -> List[entity_instance]:
    """특정 entity가 가지고 있는 IfcPropertySet들을 반환
    사용 예)
    ```python
    psets = self._get_ifc_property_set(entity)
    ```

    Args:
        ifc (file): IFC 파일
        entity (entity_instance): 탐색을 시작하는 entity

    Returns:
        List[entity_instance]: IfcPropertySet의 집합
    """
    # psets = [entity for entity in get_inverse(ifc, entity)
    #              if entity.is_a('IfcRelDefinesByProperties')]
    psets = get_inverse(ifc, entity, filter_is_a='IfcRelDefinesByProperties')
    nested_psets = [_entity_to_list(pset.RelatingPropertyDefinition) for pset in psets
                    if pset.RelatingPropertyDefinition is not None]
    psets = reduce(lambda x, y: x+y, nested_psets, [])
    filtered_psets = list(
        filter(lambda pset: pset.is_a('IfcPropertySet'), psets))
    return filtered_psets


def get_structural_curve_action_psets_from_entity(
    ifc: file,
    entity: entity_instance
) -> List[entity_instance]:
    """특정 entity가 가지고 있는 IfcPropertySet 중 IfcStructuralCurve의 속성인 것들만 반환

    Args:
        ifc (file): IFC 파일
        entity (entity_instance): 탐색을 시작하는 entity

    Returns:
        List[entity_instance]: IfcPropertySet의 집합
    """
    psets = get_inverse(ifc, entity, filter_is_a='IfcRelDefinesByProperties')
    # for error check: RelatedObjects의 개수가 하나라고 가정하고 개발함
    for pset in psets:
        assert len(
            pset.RelatedObjects) == 1, "unexpected condition: (# of relation) > 1"

    nested_psets = [_entity_to_list(pset.RelatingPropertyDefinition) for pset in psets
                    if pset.RelatingPropertyDefinition is not None and
                    pset.RelatedObjects[0].is_a("IfcStructuralCurveAction")]

    psets = reduce(lambda x, y: x+y, nested_psets, [])
    filtered_psets = list(
        filter(lambda pset: pset.is_a('IfcPropertySet'), psets))
    return filtered_psets


def get_directly_connected_psets_from_entity(
    ifc: file,
    entity: entity_instance
) -> List[entity_instance]:
    """특정 entity에 직접 연결된(IfcStructuralCurveAction같은 다른 entity를 거치지 않고)
    IfcPropertySet들을 반환

    Args:
        ifc (file): IFC 파일
        entity (entity_instance): 탐색을 시작하는 entity

    Returns:
        List[entity_instance]: IfcPropertySet의 집합
    """
    psets = get_inverse(ifc, entity, filter_is_a='IfcRelDefinesByProperties')

    # for error check: RelatedObjects의 개수가 하나라고 가정하고 개발함
    for pset in psets:
        assert len(
            pset.RelatedObjects) == 1, "unexpected condition: (# of relation) > 1"

    nested_psets = [_entity_to_list(pset.RelatingPropertyDefinition) for pset in psets
                    if pset.RelatingPropertyDefinition is not None and
                    pset.RelatedObjects[0] == entity]
    psets = reduce(lambda x, y: x+y, nested_psets, [])
    filtered_psets = list(
        filter(lambda pset: pset.is_a('IfcPropertySet'), psets))
    return filtered_psets


def _get_ifc_material_profile_from_entity(
    ifc: file,
    entity: entity_instance
) -> Union[entity_instance, None]:
    """
    IfcMaterialProfileSet, IfcMaterialProfile 둘 중 하나라도
    존재하지 않을 경우 None을 반환하고,
    두 개 이상일 경우 ValueError를 발생시킵니다.(개발시 상정하지 않은 상황)
    Args:
        ifc: IFC 파일
        entity: 탐색을 시작하는 entity(slab를 염두에 두고 개발)

    Returns:
        entity_instance: IfcMaterialProfile entity
    """
    # print('dd')
    # print(type(entity))
    # pprint([a for a in get_inverse(ifc, entity)])
    ifc_rel_associates_materials = get_inverse(
        ifc, entity, filter_is_a='IfcRelAssociatesMaterial')
    ifc_material_profile_set = [
        a.RelatingMaterial for a in ifc_rel_associates_materials]
    ifc_material_profile_set = [
        a for a in ifc_material_profile_set if a.is_a("IfcMaterialProfileSet")]
    if len(ifc_material_profile_set) > 1:
        print(len(ifc_material_profile_set))
        raise ValueError(
            "IFC의 IfcMaterialProfileSet entity 개수 오류. 개발자에게 문의하세요.")
    if len(ifc_material_profile_set) == 0:
        return None
    ifc_material_profiles = ifc_material_profile_set[0].MaterialProfiles
    if len(ifc_material_profiles) > 1:
        raise ValueError("IFC의 IfcMaterialProfile entity 개수 오류. 개발자에게 문의하세요.")
    if len(ifc_material_profiles) == 0:
        return None
    return ifc_material_profiles[0]


def get_ifc_material_properties_from_entity(
        ifc: file,
        entity: entity_instance
) -> List[entity_instance]:
    """특정 entity가 가지고 있는 IfcMaterialProperties를 반환.

    PSC_girdier_bridge_updated.ifc, 즉 <새로운 구조>에서 사용합니다.
    구조가 바뀌었을 경우 정상 작동을 보장하지 않습니다.

    사용 예)
    ```python
    prts = self.get_ifc_material_properties_from_entity(ifc, entity)
    ```

    Args:
        ifc (file): IFC 파일
        entity (entity_instance): 탐색을 시작하는 entity

    Returns:
        List[entity_instance]: IfcMaterialProperties entity의 집합
    """
    ifc_material_profile = _get_ifc_material_profile_from_entity(ifc, entity)
    if ifc_material_profile is None:
        return []
    return ifc_material_profile.Material.HasProperties


def get_ifc_profile_properties_from_entity(
        ifc: file,
        entity: entity_instance
) -> List[entity_instance]:
    """특정 entity가 가지고 있는 IfcProfileProperties를 반환.

    PSC_girdier_bridge_updated.ifc, 즉 <새로운 구조>에서 사용합니다.
    구조가 바뀌었을 경우 정상 작동을 보장하지 않습니다.

    사용 예)
    ```python
    prts = self.get_ifc_profile_properties_from_entity(ifc, entity)
    ```

    Args:
        ifc (file): IFC 파일
        entity (entity_instance): 탐색을 시작하는 entity

    Returns:
        List[entity_instance]: IfcProfileProperties의 집합
    """
    ifc_material_profile = _get_ifc_material_profile_from_entity(ifc, entity)
    if ifc_material_profile is None:
        return []
    ifc_arbitrary_closed_profile_def = ifc_material_profile.Profile
    # print(entity, "material_profile: ", ifc_material_profile)
    return ifc_material_profile.Profile.HasProperties


def get_ifc_structural_curve_action_from_entity(
        ifc: file,
        entity: entity_instance
) -> List[entity_instance]:
    pass


def save_result_into_ifc_classification(
        product,  # import error occurs when the typing module applied
        code: str,
        result,
):
    """save result string into IFCCLASSIFICATION description.
    Args:
        product: entity of slab, beam, ...etc
        code: "D241421_41121", ...etc
        result: "PASS", "FAIL", ...etc
    """
    if not (code.startswith("D") or code.startswith("E")):
        raise ValueError("code must starts with 'D' or 'E'")
    refs = [ref for id_str, ref in product.id2rel_class.items()
            if id_str == code]
    if not len(refs) == 1:
        raise ValueError("The number of IFCCLASSIFICATIONREFERENCE referencing {} is {},"
                         " which must be 1".format(product, len(refs)))
    refs[0].ReferencedSource.Description = result.name
