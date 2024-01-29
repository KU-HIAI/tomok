# python
from enum import IntEnum
# 3rd-party
from ifcopenshell.file import file


def ifc_single_value_to_python(
    value_type: str,
    wrapped_value: object,
    prop: object
) -> object:
    try:
        if wrapped_value is None:
            return None
        if value_type == 'IfcInteger':
            return int(wrapped_value)
        if value_type == 'IfcCountMeasure':
            return int(wrapped_value)
        if value_type == 'IfcReal':
            return float(wrapped_value)
        if value_type == 'IfcBoolean':
            return bool(wrapped_value)
        if value_type == 'IfcLogical':
            return bool(wrapped_value)
        if value_type == 'IfcPlaneAngleMeasure':
            return float(wrapped_value)
        if value_type == 'IfcPositiveLengthMeasure':
            return float(wrapped_value)
        if value_type == 'IfcLengthMeasure':
            return float(wrapped_value)
        if value_type == 'IfcText':
            return str(wrapped_value)
        if type(wrapped_value) is str:
            return wrapped_value
        if type(wrapped_value) is float:
            return float(wrapped_value)
        else:
            raise TypeError('currently {0} ({1}, {2}) type is not handled in IFCReader.'.format(
                value_type, wrapped_value, type(wrapped_value)))
    except Exception as ex:
        raise ValueError('parsing value ({0}) with {1} type is not possible. prop:{2}'.format(
            wrapped_value, value_type, prop))


def python_to_ifc_single_value(
    ifc: file,
    name: str,
    value: object,
    value_type: str = None,
    description: str = None
):
    new_entity = ifc.createIfcPropertySingleValue()
    new_entity.Name = name
    if description is not None:
        new_entity.Description = description
    if value_type is None:
        value_type = _recognize_value_type(value)
    new_entity.NominalValue = ifc.create_entity(value_type, value)
    return new_entity


def _recognize_value_type(
    value: object
):
    if type(value) is float:
        return "IfcReal"
    if type(value) is str:
        return "IfcText"
    if issubclass(type(value), IntEnum):
        return "IfcInteger"
    if type(value) is int:
        return "IfcInteger"
    else:
        raise TypeError('currently {0} ({1}) type is not writable in IFCReader'.format(
            type(value), value))
