from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip
import time
import datetime
import yaml
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('openai-382120-1dac37454a48.json', scope)
    client = gspread.authorize(creds)
    return client.open('attendance_data').worksheet('attendance_data')

def get_last_date(worksheet):
    all_values = worksheet.get_all_values()
    last_row = all_values[-1][0]
    return datetime.datetime.strptime(last_row, "%Y-%m-%d").date()

def get_date_list(last_date, end_date):
    date_list = []
    current_date = last_date + datetime.timedelta(days=1)
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += datetime.timedelta(days=1)
    return date_list

def generate_attendance_url(date):
    return f"https://cafe.naver.com/AttendanceView.nhn?search.clubid=31201853&search.menuid=15&search.attendyear={date.year}&search.attendmonth={date.month}&search.attendday={date.day}"

def naver_login(driver, naver_id, naver_pw):
    driver.get("https://nid.naver.com/nidlogin.login")
    time.sleep(1)

    id_input = driver.find_element(By.CSS_SELECTOR, "#id")
    id_input.click()
    pyperclip.copy(naver_id)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pw_input = driver.find_element(By.CSS_SELECTOR, "#pw")
    pw_input.click()
    pyperclip.copy(naver_pw)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    login_btn = driver.find_element(By.CSS_SELECTOR, '#log\.login')
    login_btn.click()
    time.sleep(1)

def scrape_attendance(driver, date):
    attendance_url = generate_attendance_url(date)
    driver.get(attendance_url)
    time.sleep(1)
    driver.switch_to.frame("cafe_main")

    list_pages = driver.find_elements(By.CSS_SELECTOR, '#main-area > div.article-attendance > div.attendance_lst_section > div > a')
    time.sleep(1)

    page_hrefs = [page.get_attribute('href') for page in list_pages]

    data = []
    idx = 0

    for page_href in reversed(page_hrefs):
        driver.get(page_href)
        time.sleep(1)
        driver.switch_to.frame("cafe_main")
        list_items = driver.find_elements(By.CSS_SELECTOR, 'ul.list_attendance > li')
        time.sleep(1)

        for item in reversed(list_items):
            idx += 1
            text = item.text
            parts = text.split('\n')

            if len(parts) == 2:
                name = parts[0]
                rank = None
            else:
                name = parts[0]
                rank = parts[1]

            data.append([str(date), name, rank, idx])

    return data

def main():
    with open('config.yaml', encoding='UTF-8') as f:
        _cfg = yaml.load(f, Loader=yaml.FullLoader)
    naver_id = _cfg['naver_id']
    naver_pw = _cfg['naver_pw']

    worksheet = get_google_sheet()
    last_row_date = get_last_date(worksheet)
    print('마지막 데이터 날짜 : ', last_row_date)
    today_date = datetime.datetime.now().date()
    yesterday_date = today_date - datetime.timedelta(days=1)
    print('업데이트 종착역 : ', yesterday_date)

    if last_row_date >= yesterday_date:
        print('--종료합니다--')
        return

    date_list = get_date_list(last_row_date, yesterday_date)

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 자동으로 ChromeDriver 버전 관리
    service = Service() # ChromeDriverManager().install()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        naver_login(driver, naver_id, naver_pw)

        for date in date_list:
            attendance_data = scrape_attendance(driver, date)
            for data in attendance_data:
                worksheet.append_row(data)
                time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
        print('Update DONE!!')

if __name__ == "__main__":
    main()
    input("Press Enter to exit")
