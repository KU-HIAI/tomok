# framework
from .util import *
from .property_set import PropertySet


class SupertypeIfcEntityOfPsetAndProp:
    """
    Variables:
        property_set_names: PropertySet 또는 Properties의 이름을 모은 집합
    """
    property_set_names = []

    def __getattr__(self, key):
        raise AttributeError("{0} property_set is not in {1}. {2}".format(
            key, self, self.property_set_names))

    def __getitem__(self, key):
        if key not in self.__dict__:
            raise AttributeError("{0} property_set is not in {1}. {2}".format(
            key, self, self.property_set_names))
        return self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return repr(self.entity.wrapped_data)

    def get_psets(self):
        return [
            self.__getattribute__(name) for name in self.property_set_names
        ]

    def get_props(
        self,
        names_only: bool = True
    ):
        def get_key(pset: PropertySet):
            if(names_only):
                return pset.entity.Name
            else:
                return pset
        return {get_key(pset): pset.get_properties() for pset in self.get_psets()}

    def get_descriptions(
        self
    ):
        return sum([list(pset.descriptions.values()) for pset in self.get_psets() if len(pset.descriptions.values()) > 0], [])

    def set_psets(self, psets: dict):
        for property_set_name in psets:
            self.property_set_names.append(property_set_name)
            self.__setattr__(property_set_name, psets[property_set_name])
            if is_decodable(property_set_name):
                decoded_property_set_name = decode_2byte(property_set_name)
                self.__setattr__(decoded_property_set_name, psets[property_set_name])
