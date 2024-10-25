from typing import Optional
from itertools import product, islice
from pandas import DataFrame
import inspect
from .util import typename, import_check
from .repo import prepare_tf_repo, tf_commit
from .results import ResultBase
from .base_unit import BaseUnit


class TableCellFunction:
    def __init__(self, func, label):
        self.func = func
        self.label = label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return "⚙️" + self.label


class TableUnit(BaseUnit):
    priority: int = 1
    acc_able: bool = True
    version: float = 1.0
    author: str = "unknown"
    ref_code: str = "KDS # # #"
    ref_date: str = "YYYY-MM-DD"
    identification_code: str = "D # # #"
    title: str = ""
    description: str = """
    descriptions about this table.
    """
    ref_url: str = "https://www.kcsc.re.kr/"
    filename: str = ""
    _index: int = 0
    content: str = ""
    table: DataFrame = None

    def __init__(self):
        self.table_functions = self._regist_table_functions()
        self.table = self.setup_table()

    def _regist_table_functions(self):
        method_list = [
            getattr(self, attr)
            for attr in dir(self)
            if typename(getattr(self, attr)) == "tomok.core.decorator.TableFunction"
            or typename(getattr(self, attr))
            == "tomok.tomok.core.decorator.TableFunction"
        ]
        return method_list

    def setup_table(self):
        pass

    def regist(
        self, TF_REPO_TOKEN, target_path, commit_msg=None, source_file="working.py"
    ):
        prepare_tf_repo(overwrite=True, TF_REPO_TOKEN=TF_REPO_TOKEN)
        tf_commit(
            target_path=target_path,
            target_class=self,
            TF_REPO_TOKEN=TF_REPO_TOKEN,
            commit_msg=commit_msg,
            source_file=source_file,
        )

    def verify(self, with_stdin=True):
        error_flag = 0  # 하나라도 오류가 있으면 1를 반환

        # 메타 데이터 검증
        print("\033[1m[메타 데이터 검증]\033[0m")
        print("acc_able: ", self.acc_able)
        if self.acc_able is not None:
            print(
                "\033[92m"
                + "[통과]"
                + "\033[0m"
                + " table 가능여부가 설정되어 있습니다."
            )
        else:
            print(
                "\033[91m"
                + "[오류]"
                + "\033[0m"
                + " 메타데이터에 acc_able (Table 가능여부)가 설정되어야 합니다. Table 가능일 경우 True 아닌 경우 False 값을 설정해야 합니다."
            )
            error_flag = 1
        print("")

        print("\033[1m[테이블 함수 목록]\033[0m")
        print(self.table_functions)
        print("")

        for rule_method in self.table_functions:
            # 기반 데이터 준비
            func = rule_method.fn
            docstring = inspect.getdoc(func)
            body = inspect.getsource(func)
            source = self._get_source_body(func)

            # 룰 인자 검증
            print("\033[1m[테이블 함수 입력 인자 검증]\033[0m")
            params = inspect.signature(func).parameters
            input_list = list(params.keys())
            print("- 함수에 정의된 인자 리스트: ", input_list)
            docstring_params = self._find_docstring_variables(func)
            docstring_params = {var[0]: var[1] for var in docstring_params}
            print("- docstring에 정의된 인자 리스트: ", docstring_params.keys())
            is_variables_matched = set(docstring_params.keys()) == set(input_list)
            if is_variables_matched:
                print("\033[92m" + "[통과]" + "\033[0m" + " 함수와 docstring 인자 일치")
            else:
                print(
                    "\033[91m"
                    + "[오류]"
                    + "\033[0m"
                    + " 함수와 docstring 인자 불일치.\n"
                )
                print(
                    "맞는데도 이 오류가 발생한다면 docstring의 띄어쓰기를 확인하세요."
                )
                error_flag = 1

            # 입력 인자에 userdefined 있는지 여부
            has_userdefined = False
            for input_name in input_list:
                if "userdefined" in input_name.lower():
                    has_userdefined = True
            if not has_userdefined:
                print("\033[92m" + "[통과]" + "\033[0m" + " UserDefined 인자 불검출")
            else:
                print("\033[91m" + "[오류]" + "\033[0m" + " UserDefined 인자 검출")
                error_flag = 1

            # 모든 입력 인자의 사용 여부 검사
            source_vars = self._get_source_vars(source)
            print("- 소스코드에 사용된 인자 리스트: ", source_vars)
            all_variable_used = len(set(input_list).difference(set(source_vars))) == 0
            if all_variable_used:
                print("\033[92m" + "[통과]" + "\033[0m" + " 입력 인자 모두 사용")
            else:
                print("\033[91m" + "[오류]" + "\033[0m" + " 미사용 입력 인자 존재")
                print(
                    "\033[91m" + "[미사용 인자]" + "\033[0m",
                    set(input_list).difference(set(source_vars)),
                )
                error_flag = 1
            print("")

            # 룰 실행여부 검증
            print("\033[1m[테이블 함수 실행 여부 검증]\033[0m")
            if len(set(input_list).difference(set(docstring_params.keys()))) > 0:
                print(
                    "\033[91m"
                    + "[오류]"
                    + "\033[0m"
                    + " 입력 인자 중 일부가 docstring에 기재되어 있지 않습니다. 자료형(예: float, str, int)을 알 수 없으므로 룰 실행 여부 검정이 불가합니다."
                )
                print(set(input_list).difference(set(docstring_params.keys())))
                print(
                    "\033[91m"
                    + "위 인자에 대한 docstring 작성 후 다시 실행 해주시기 바랍니다."
                    + "\033[0m"
                )
                return 1
            if with_stdin:  # input()의 stdin 입력 없이 검토하는 기능 추가
                user_input = {}
                for param in input_list:
                    user_input[param] = input(
                        f"{param} ({docstring_params[param]}) 인자의 값을 넣어주세요 : "
                    )
                    try:
                        user_input[param] = self.wrap_value(
                            docstring_params[param], user_input[param]
                        )
                        print(f"{param}: {user_input[param]}")
                    except Exception as ex:
                        print("\033[91m" + "[오류]" + "\033[0m" + " 인자 형 변환 실패")
                        print(ex)
                        error_flag = 1
                try:
                    result = func(**user_input)
                    print("\033[92m" + "[통과]" + "\033[0m" + " 테이블 실행 확인")
                except Exception as ex:
                    print("\033[91m" + "[오류]" + "\033[0m" + " 테이블 실행 실패")
                    print(ex)
                    error_flag = 1

                # 룰 반환형 검사
                print("\033[1m[테이블 함수 반환 데이터 검증]\033[0m")
                print("결과:", result)
                if isinstance(result, ResultBase):
                    print("\033[92m" + "[통과]" + "\033[0m" + " 반환 자료형 확인")
                else:
                    # print('\033[91m' + '[오류]' + '\033[0m' + ' 반환 자료는 ResultBase, PassFailResult, SingleValueResult, MultiValueResult 등 이어야 합니다.')
                    print(
                        "\033[91m"
                        + "[오류]"
                        + "\033[0m"
                        + " 반환 자료형은 RuleUnitResult 이어야 합니다."
                    )
                    return 1
            else:
                print("건너뜁니다... (입력값 없이 진행)")
            print("")

            docstring_return_params = self._find_return_docstring_variables(func)
            docstring_return_params = {
                var[0]: var[1] for var in docstring_return_params
            }

            def validate_return_docstring(returned_value):
                if (
                    len(
                        set(returned_value.result_variables.keys()).difference(
                            set(docstring_return_params)
                        )
                    )
                    > 0
                ):
                    print(
                        "\033[91m"
                        + "[오류]"
                        + "\033[0m"
                        + " 반환 인자 중 일부가 docstring에 기재되어 있지 않습니다."
                    )
                    print(
                        set(returned_value.result_variables.keys()).difference(
                            set(docstring_return_params)
                        )
                    )
                    print(
                        "\033[91m"
                        + "위 인자의 변수명이 docstring에 기록되어 있는지, 변수명에 오류가 없는지 확인 바랍니다."
                        + "\033[0m"
                    )
                    print("")
                    return 1
                else:
                    return 0

            if with_stdin:
                if validate_return_docstring(result) == 1:
                    error_flag = 1

            # 경곗값 테스트 (Boundary Value Test) - 입력변수에 극단적인 값이 들어와도 안전한지 검증
            print("\033[1m[다양한 입력값 대응 여부 검증]\033[0m")
            value_dict = {  # 임의로 설정한 극단적 값
                "int": [-1, 0, 10, 100, 99999],
                "float": [-1.0, 0.0, 10.0, 100.0, 99999.9],
                "str": ["", "테스트", "Test!Test!Test!Test!Test!Test!\nTest!"],
                "bool": [True, False],
                "list": [[-1.0], [0.0, 999.9], [0.0]],
                "dict": [{"1": 1}],
                "set": [{1.0}, {1.0, 999.9}],
            }
            arg_to_type = {k: docstring_params[k] for k in input_list}
            try:  # 오류메시지를 구체적으로 출력
                candidates = [value_dict[v] for v in arg_to_type.values()]
            except KeyError:
                print(
                    "\033[91m"
                    + "[오류]"
                    + "\033[0m"
                    + " docstring의 변수 type이 정확하게 적혀 있는지 확인해주세요"
                )
                raise
            for extreme_args in islice(
                product(*candidates), 10000
            ):  # 나중에 product의 순서가 랜덤으로 되도록 해야 함
                try:
                    output = func(*extreme_args)

                    # docstring 검사
                    if validate_return_docstring(output) == 1:
                        raise TypeError

                    # return type 검사
                    if not isinstance(output, ResultBase):
                        print(
                            "\033[91m"
                            + "[오류]"
                            + "\033[0m"
                            + " RuleUnitResult를 반환하지 않는 경우 존재"
                        )
                        raise TypeError("TableFunction 반환형 오류")

                except AssertionError:
                    pass  # no problem with AssertionError when given extreme arguments
                except TypeError:
                    # print("\033[91m" + "[오류]" + "\033[0m" + " 룰 안전하지 않음")
                    print(
                        "\033[1m"
                        + f"오류 당시 입력변수"
                        + "\033[0m"
                        + f": {str({k:v for k, v in zip(input_list, extreme_args)})}"
                    )
                    raise
            print("\033[92m" + "[통과]" + "\033[0m" + " 극단적 입력값 테스트 완료")

        return error_flag
