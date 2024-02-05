# tomoku
 고려대학교 토목 과제 RuleUnit 구현용 라이브러리

## 설치방법

1. anaconda 패키지 관리 도구 설치
    1. [Miniconda — miniconda documentation](https://docs.conda.io/projects/miniconda/en/latest/) 페이지 참조
    
    ```bash
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
    ```
    
2. 필수 라이브러리 설치
    
    ```bash
    conda create --name tomok pip
    ```
    
3. 토목 라이브러리 설치
    
    ```bash
    conda activate tomok
    pip install ifcopenshell
    pip install .
    ```

### 내부 API 서버

/server/README.md 참조


## TODO
.ipynb -> .py 기계적 변환 프로세스 구축
