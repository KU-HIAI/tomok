import os
import streamlit as st

IFCFILE_PATH = "./ifcfiles"

# 초기 세션 상태 설정
if "file_loaded" not in st.session_state:
    st.session_state.file_loaded = False
if "subtype" not in st.session_state:
    st.session_state.subtype = ""
if "reader" not in st.session_state:
    st.session_state.reader = None


def app():
    st.title("IFC 파일 업로드")

    uploaded_file = st.file_uploader(
        "Choose a IFC file", type=None, accept_multiple_files=False
    )

    if uploaded_file is not None:
        file_details = {
            "FileName": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size,
        }
        st.write(file_details)

        file_path = os.path.join(IFCFILE_PATH, uploaded_file.name)
        with open(file_path, "w") as fp:
            fp.write(uploaded_file.getvalue().decode("utf-8"))
        st.success("IFC 파일 입력 완료 !")
