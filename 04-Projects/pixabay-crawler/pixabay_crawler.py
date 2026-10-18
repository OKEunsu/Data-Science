import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import requests
import os

def find_pages(driver):
    import re
    url = '/html/body/div[1]/div[1]/div/div[2]/div[4]/div[2]'
    last_page = driver.find_element(By.XPATH, url).text
    last_page_num = re.search(r"/\s*(\d+)\s*페이지", last_page)
    if last_page_num:
        value = last_page_num.group(1)
    print(f'마지막 페이지는 {value}입니다.')
    return value


def search_img(keyword, page_num=10):
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    url = f'https://pixabay.com/ko/images/search/{keyword}'
    driver.get(url=url)
    
    time.sleep(5)
    
    try:
        last_page_num = int(find_pages(driver))
        print(last_page_num)
    except Exception as e:
        print(f"페이지 번호를 찾을 수 없습니다: {e}")
        driver.quit()
        return

    time.sleep(5)
    
    print('크롤링 중...')
    for i in range(1, min(page_num, last_page_num) + 1):
        try:
            # 페이지의 모든 이미지를 로드하기 위해 스크롤을 내립니다.
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            image_cells = driver.find_elements(
            By.XPATH,
            '/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div/div//div[contains(@class, "cell--UMz-x")]')
            
            img_list = []
            for cell in image_cells:
                img = cell.find_element(By.TAG_NAME, 'img')
                src = img.get_attribute('src')
                if src and 'blank.gif' not in src:
                    img_list.append(src)
                
            if not os.path.exists(f'img/{keyword}'):
                os.makedirs(f'img/{keyword}', exist_ok=True)

            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            for idx, img_url in enumerate(img_list):
                try:
                    response = requests.get(img_url, headers=headers, stream=True, timeout=10)
                    response.raise_for_status()
                
                    time.sleep(1)

                    with open(f'img/{keyword}/{keyword}_{i}_{idx+1}.jpg', 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                except requests.exceptions.RequestException as e:
                    print(f"다운로드 실패 {img_url}: {e}")
            
            print(f"{i} 페이지 크롤링 완료")
            
            # 다음 페이지로 이동
            if i < last_page_num:
                next_page_url = f"{url}&pagi={i+1}"
                driver.get(next_page_url)
                time.sleep(5)

        except Exception as e:
            print(f"{i} 페이지 처리 중 오류 발생: {e}")
            continue

    print(f"{keyword} 이미지 저장이 완료되었습니다.")
    driver.quit()
    
if __name__ == '__main__':
    search_img('바나나')