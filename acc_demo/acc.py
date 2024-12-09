import os
import requests
import json
from typing import Union
from tomok import RuleIFC, IFCReader, Product, RuleUnitController
from tomok.core.results import OKNGResult
import streamlit as st
import pandas as pd

from acc_utils import ACCEngine, RuleUnitCallingDescriptor


# 초기 세션 상태 설정
# if "file_loaded" not in st.session_state:
#     st.session_state.file_loaded = False
# if "subtype" not in st.session_state:
#     st.session_state.subtype = ""
# if "reader" not in st.session_state:
#     st.session_state.reader = None
# if "entities" not in st.session_state:
#     st.session_state.entities = []


def app():
    if "file_loaded" not in st.session_state:
        st.session_state.file_loaded = False
    if "subtype" not in st.session_state:
        st.session_state.subtype = ""
    if "reader" not in st.session_state:
        st.session_state.reader = None
    if "entities" not in st.session_state:
        st.session_state.entities = []
    if "flag" not in st.session_state:
        st.session_state.flag = False

    st.title("디지털 건설기준 자동 검토(ACC)")
    log = []
    log_entity = []
    log_scc = []
    rule_idx = 0
    files = os.listdir("./ifcfiles")
    fname = st.selectbox("파일을 선택하세요.", files)

    # IFC 파일 읽기
    if st.button("IFC 파일 읽기"):
        st.session_state.reader = IFCReader(f"./ifcfiles/{fname}")
        st.session_state.file_loaded = True

    # 파일이 읽혔을 때만 Subtype 입력 표시
    if st.session_state.file_loaded:
        st.session_state.subtype = st.text_input(
            "Subtype을 입력하세요.",
            value=(
                st.session_state.subtype
                if st.session_state.subtype
                else "RC_STIFFENINGGIRDER"
            ),
        )  # RC_STIFFENINGGIRDER

    if st.session_state.subtype:
        if st.button("부재 검색"):
            st.session_state.entities = st.session_state.reader.get_products_by_subtype(
                st.session_state.subtype
            )
            st.session_state.flag = False

    if st.session_state.entities:
        if st.button("자동검토 실행"):
            st.session_state.flag = True  # 검토 버튼 눌렀다는 뜻
            log = []
            for entity in st.session_state.entities:
                log_entity = []
                engine = ACCEngine(
                    rule_file="tree_temp2.csv",
                    module_file="module_temp.csv",
                    # target_rule='KDS241421_04010201_01'
                )
                rule_idx = 0
                for order in engine.execution_orders:
                    log_scc = []
                    if isinstance(order, list):
                        while True:
                            for code in order:
                                rule_idx += 1  # scc 내 룰 실행 횟수 체크
                                log_scc.append(
                                    "[{}] 룰유닛 {} 실행".format(rule_idx, code)
                                )
                                try:
                                    input_value = engine.get_input_values(entity, code)
                                    log_scc.append("입력 변수: " + str(input_value))
                                    path = engine.get_api_path(code)
                                    result = engine.ruleunit_call(path, **input_value)
                                    for k, v in result.items():
                                        engine.var_cache[k] = v
                                    log_scc.append("api 반환 결과: " + str(result))
                                    print(result)
                                except Exception as e:
                                    print(f"Error executing code {code}: {e}")
                            if engine.var_cache.get("pass_fail") == -9999:
                                log_scc.append("\n--- CCC 재실행 ---\n")
                            else:
                                break
                    else:
                        rule_idx += 1  # scc 내 룰 실행 횟수 체크
                        code = order
                        log_scc.append("[{}] 룰유닛 {} 실행".format(rule_idx, code))
                        try:
                            input_value = engine.get_input_values(entity, code)
                            log_scc.append("입력 변수: " + str(input_value))
                            path = engine.get_api_path(code)
                            result = engine.ruleunit_call(path, **input_value)
                            for k, v in result.items():
                                engine.var_cache[k] = v
                            log_scc.append("api 반환 결과: " + str(result))
                        except Exception as e:
                            print(f"Error executing code {code}: {e}")
                    log_entity.append(log_scc)
                log.append(log_entity)

        if st.session_state.flag:
            temp = [str(x) for x in st.session_state.entities]
            selected_entity = st.selectbox("Choose an entity", temp)
            selected_index = temp.index(selected_entity)
            log_entity_ = log[selected_index]
            # print(log_entity_)
            for idx, log_scc_ in enumerate(log_entity_):
                with st.expander("{}번째 CCC 로그".format(idx + 1)):
                    st.write(log_scc_)
