import streamlit as st
import page_file_upload
import download_ifc
import acc

# 초기 세션 상태 설정
if "file_loaded" not in st.session_state:
    st.session_state.file_loaded = False
if "subtype" not in st.session_state:
    st.session_state.subtype = ""
if "reader" not in st.session_state:
    st.session_state.reader = None


PAGES = {
    "IFC 파일 업로드": page_file_upload,
    "디지털 건설기준 자동 검토": acc,
    "IFC 파일 다운로드": download_ifc,
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        page.app()


if __name__ == "__main__":
    main()
