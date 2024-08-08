## 대규모 데이터 처리
### MODIN
https://modin.readthedocs.io/en/stable/getting_started/installation.html  
```
pip intsll "modin[all] @ git+https://github.com/modin-project/modin"
```
### Colab 설치
```
pip install "modin[all]"
```

Colab Runtime 다시 시작

Modin은 pandas의 대체물로 계산을 사용자의 머신이나 클러스터의 모든 코어에 분산 시킨다.  
pandas 스크립트를 그대로 사용할 수 있으며, 행동과 결과는 동일하게 유지한다는 것을 의미  
변경해야할 것은 import 문

```
import modin.pandas as pd
```

Modin 작동 방식
