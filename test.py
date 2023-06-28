import tomok

class SampleRuleUnit(tomok.RuleUnit):
    # [TODO] meta 정보
    content = """$z  _{cp} $= 콘크리트 단면의 도심과 프리스트레싱 강재 도심 사이의 거리"""

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

rule_unit = SampleRuleUnit()
print(rule_unit.example_method(3,4))
print(rule_unit.render_markdown())