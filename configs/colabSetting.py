import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os
import subprocess

# 폰트 경로 설정 (로컬 환경에 맞게 수정 필요)
def get_font_path():
    possible_paths = [
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",  # Linux (Ubuntu 등)
        "/Library/Fonts/NanumGothic.ttf",  # macOS
        "C:/Windows/Fonts/NanumGothic.ttf"  # Windows
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

# 나눔고딕 폰트 설치 (Linux의 경우)
def install_font():
    try:
        subprocess.run(["sudo", "apt-get", "install", "-y", "fonts-nanum"], check=True)
        subprocess.run(["fc-cache", "-fv"], check=True)
    except Exception as e:
        print(f"[오류] 폰트 설치 중 오류 발생: {e}")

font_path = get_font_path()
if not font_path:
    print("[알림] 나눔고딕 폰트를 찾을 수 없습니다. 설치를 시도합니다.")
    install_font()
    font_path = get_font_path()

if font_path:
    font_manager.fontManager.addfont(font_path)
    rc('font', family=font_manager.FontProperties(fname=font_path).get_name())
else:
    print("[경고] 나눔고딕 폰트를 찾을 수 없습니다. 기본 폰트를 사용합니다.")

# 시각화 코드
plt.plot([1, 2, 3, 4])
plt.title('한글 제목')
plt.show()
