# TOMOK Python API

토목 Python API

### 설치

1. (옵션) tomok 라이브러리 설치

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
4. **api_files**: `['tomok-api.yaml']`
    - API 초기 설정 파일의 목록을 설정합니다.
9. **process_title**: `'TOMOK API (DEV)'`
    - 이는 프로세스 제목(title)을 설정합니다.

### 룰 유닛 적재

1. 전처리가 끝난 룰 유닛을 /ruleunits/ 디렉토리에 복사합니다.
2. `openapi_generator.py` 를 실행하여 /ruleunits/ 내의 룰 유닛을 사용 가능하도록 tomok-api.yaml 을 생성합니다.


### 서버 실행

`python app.py`