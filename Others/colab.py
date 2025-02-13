import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

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
