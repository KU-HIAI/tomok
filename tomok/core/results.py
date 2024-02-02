# python
from enum import IntEnum
from dataclasses import dataclass


class OKNGResult(IntEnum):
    PASS = (1,)
    FAIL = 0


class StatusCode(IntEnum):
    PASS = 200
    FAIL = 500


@dataclass
class ResultBase:
    code: StatusCode
    result_text: str
    result_variables: dict
    version: str = "1.0.0"


class PassFailResult(ResultBase):
    def __init__(self, pass_fail: bool, code: StatusCode, result_text: str = "ok"):
        super().__init__(
            code=code,
            result_text=result_text,
            result_variables={"pass_fail": pass_fail},
        )


class SingleValueResult(ResultBase):
    def __init__(
        self, var_name: str, var_value: str, code: StatusCode, result_text="ok"
    ):
        assert isinstance(var_name, str), "변수명 타입이 str 이 아닙니다."
        super().__init__(code, result_text, {var_name: var_value})


class MultiValueResult(ResultBase):
    def __init__(self, result_variables: dict, code: StatusCode, text: str = "ok"):
        assert all(isinstance(k, str) for k in result_variables)
        super().__init__(code, text, result_variables)
