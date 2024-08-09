import os
import requests
import json
from typing import Union
from tomok import RuleIFC, IFCReader, Product, RuleUnitController
from tomok.core.results import OKNGResult
import streamlit as st
import pandas as pd


def app():
    st.title("IFC 파일 다운로드")
    files = os.listdir("./ifcfiles")
    fname = st.selectbox("파일을 선택하세요.", files)

    with open(f"./ifcfiles/{fname}", "r") as file:
        btn = st.download_button(
            label="IFC File Download",
            data=file,
            file_name=os.path.basename(fname),
            mime="application/octet-stream",
        )
