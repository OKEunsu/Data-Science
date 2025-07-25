# 파이썬 병렬 크롤러 학습

이 프로젝트는 파이썬을 이용한 병렬 웹 크롤러 구현을 학습하기 위해 만들어졌습니다. 다양한 파이썬 라이브러리와 모듈을 사용하여 웹 크롤링, 멀티프로세싱, 스케줄링 등의 기능을 구현하고 테스트합니다.

## 💻 학습 내용

이 프로젝트를 통해 다음 내용들을 학습했습니다.

*   **웹 크롤링**: `requests` 라이브러리로 웹 페이지의 HTML을 가져오고, `BeautifulSoup`으로 원하는 데이터를 파싱하는 방법을 학습했습니다.
*   **멀티프로세싱**: `multiprocessing` 모듈을 사용하여 여러 개의 CPU 코어를 활용하여 크롤링 작업을 병렬로 처리함으로써 성능을 향상시키는 방법을 학습했습니다.
*   **스케줄링**: `schedule` 라이브러리를 사용하여 특정 시간 간격으로 작업을 반복 실행하는 방법을 학습했습니다.
*   **커맨드 라인 인자 처리**: `argparse` 모듈을 사용하여 프로그램 실행 시 커맨드 라인에서 CPU 사용 개수, 실행 주기 등의 옵션을 받는 방법을 학습했습니다.
*   **로깅**: `logging` 모듈을 사용하여 프로그램 실행 정보, 오류 등을 콘솔과 파일에 기록하는 방법을 학습했습니다.
*   **서브프로세스 실행**: `subprocess` 모듈을 사용하여 다른 파이썬 스크립트를 현재 스크립트에서 실행하고 그 결과를 제어하는 방법을 학습했습니다.
*   **시스템 정보 확인**: `platform`, `psutil` 라이브러리를 사용하여 OS, CPU, RAM 등 시스템 정보를 확인하는 방법을 학습했습니다.

## ⚙️ 설치 및 실행

1.  **저장소 복제**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **필요한 라이브러리 설치**
    프로젝트 루트 디렉터리에 있는 `requirements.txt` 파일을 사용하여 필요한 모든 라이브러리를 한 번에 설치합니다.
    ```bash
    pip install -r requirements.txt
    ```

3.  **크롤러 실행**
    `main.py` 파일을 실행하여 병렬 크롤러를 시작합니다.
    ```bash
    python main.py
    ```
    **옵션:**
    *   `--cpu`: 사용할 CPU 코어 수를 지정합니다. (기본값: 3)
    *   `--run_interval`: 크롤러 실행 주기를 초 단위로 지정합니다. (기본값: 5)
    ```bash
    # 예시: CPU 4개를 사용하여 10초 간격으로 실행
    python main.py --cpu 4 --run_interval 10
    ```

## 📂 프로젝트 구조

```
.
├── main.py             # 메인 병렬 크롤러 실행 파일
├── requirements.txt    # 필요한 파이썬 라이브러리 목록
├── output.log          # 크롤러 실행 로그 파일
├── argment_1.py        # sys.argv 인자 처리 예제
├── argment_2.py        # argparse 인자 처리 예제
├── logg.py             # logging 모듈 사용 예제
├── platform1.py        # platform, psutil 모듈 사용 예제
├── schedd.py           # schedule 라이브러리 사용 예제
├── subprocesss.py      # subprocess 모듈 사용 예제
├── test.py             # subprocesss.py 에서 호출하는 테스트 파일
└── README.md           # 프로젝트 설명 파일
```
