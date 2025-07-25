import schedule
import time

def message(interval):
    print(f"{interval}간격 스케줄 실행중...")

# job 설정
job = schedule.every(1).seconds.do(message, '1초')  # 이벤트 등록

# 스케줄러 실행
count = 0

while True:
    schedule.run_pending()
    time.sleep(1)

    count = count + 1

    if count > 5:  # 5회 실행 후 스케줄러 중지
        schedule.cancel_job(job)
        print('스케줄러가 종료되었습니다 !')
        break