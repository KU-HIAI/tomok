import tomok

class SampleRule(tomok.RuleUnit):
    # [TODO] meta 정보

    @tomok.rule_method
    def example_method(var1: int, var2: int):
        """_summary_

        Args:
            var1 (int): _description_
            var2 (int): _description_

        Returns:
            _type_: _description_
        """
        return var1 * var2


print(SampleRule().example_method(3,4))