# TOMOK Python API

토목 Python API

### 설치

1. tomok 라이브러리 설치
`pip install ..`

2. 관련 라이브러리 설치
`pip install requirements.txt`

### 서버 설정

`/configs/server/defaults.yaml 수정`

1. **app_host**: `'0.0.0.0'`
    - 이는 애플리케이션 호스트 주소를 설정합니다.
2. **app_port**: `51080`
    - 이는 애플리케이션 포트 번호를 설정합니다.
3. **specification_dir**: `openapi`
    - 이는 API 사양이 저장된 디렉토리의 이름을 설정합니다.
4. **api_files**: `['tomok-demo.yaml']`
    - API 초기 설정 파일의 목록을 설정합니다.
5. **api_secret**: `'kDiWQ_idJ8NCKy_sD3p_0hA5ifoewFJRa0WzfzxRVhc='`
    - 이는 API 비밀 키를 설정합니다.
6. **client_max_size**: `524288000` # 500MB
    - 클라이언트에서 업로드 할 수 있는 최대 파일 크기를 설정합니다.
7. **rule_unit_dir**: `'../ruleunits/'`
    - 이는 rule unit들이 저장된 디렉토리의 경로를 설정합니다.
8. **rule_ifc_dir**: `'../ruleifc/'`
    - 이는 rule ifc들이 저장된 디렉토리의 경로를 설정합니다.
9. **process_title**: `'TOMOK API (DEV)'`
    - 이는 프로세스 제목(title)을 설정합니다.

### 서버 실행

`python app.py`

### 메뉴얼

https://tmkor.notion.site/API-TOMOK-Python-5a913a63d8894c6b88ded9f66900e877?pvs=4