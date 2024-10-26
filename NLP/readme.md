- Regular expression
- 특정한 패턴과 일정한
- 정규표현식의 도움없이 패턴을 찾는 작업(Rule 기반)은 불완전 하거나, 작업의 cost가 높음
- e.g) 이메일 형식 판별, 전화번호 형식 판별, 숫자로만 이루어진 문자열 등
- rat string
    - 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 변환

```python
a = 'abcdef\n'
print(a)
# abcdef

b = r'abcdef\n'
print(b)
# abcdef\n
```

### 기본 패턴

- a, X, 9 등등 문자 하나하나의 character들은 정확히 해당 문자와 일치
    - e.g) 패턴 test는 test문자열과 일치
    - 대소문자의 경우 기본적으로 구별하나, 구별하지 않도록 설정 가능
- 몇몇 문자들에 대해서는 예외가 존재하는데, 이들은 특별한 의미로 사용됨
    - .^$*+?{}[]\|()
- .(마침표) - 어떤 한 개의 character와 일치(newline(엔터) 제외)
- \w - 문자 character와 일치 [a-zA-Z0-9_]
- \s - 공백문자와 일치
- \t, \n, \r - tab, newline, return
- \d - 숫자 character와 일치 [0-9]
- ^=시작,$ = 끝 각각 문자열의 시작과 끝을 의미
- \가 붙으면 스페셜한 의미가 없어짐. 예를 들어 \.는 .자체를 의미 \\는 \를 의미
- https://docs.python.org/3/library/re.html

### Search method

- 첫번째로 패턴을 찾으면 match 개겣를 반환
- 패턴을 찾지 못하면 None 반환

```python
import re
m = re.search(r'abc', 'abcdef')
print(m.start()) # **0**
print(m.end()) **# 3**
print(m.group()) # **abc**

m = re.search(r'abc', 'abdef')
print(m) # None

**m = re.search(r'\d\d\d\w', '112abcdef119')
m # <re.Match object; span=(0, 4), match='112a'> 숫자 숫자 숫자 문자

m = re.search(r'..\w\w', '@#$%ABCDabcd')
m # <re.Match object; span=(2, 6), match='$%AB'> 한글자 한글자 문자 문자**

```

### matacharacters(메타 캐릭터)

> []문자들의 범위를 나타내기 위해 사용
> 
- [ ] 내부의 메타 캐릭터는 캐릭터 자체를 나타냄
- [abck] : a or b or c or k
- [abc.^] : a or b or rc or . or ^
- [a-d] : -와 함께 사용되면 해당 문자 사이의 범위에 속하는 문자 중 하나
- [0-9] : 모든 숫자
- [a-z] : 모든 소문자
- [A-Z] : 모든 대문자
- [a-zA-Z0-9] : 모든 알파벳 문자 및 숫자
- [^0-9] : ^가 맨 앞에 사용 되는 경우 해당 문자 패턴이 아닌 것과 매칭

```python
m = re.search(r'[cbm]at','cat')
m # <re.Match object; span=(0, 3), match='cat'>

m = re.search(r'[cbm]at','bat')
m # <re.Match object; span=(0, 3), match='bat'>

m = re.search(r'[cbm]at','mat')
m # <re.Match object; span=(0, 3), match='mat'>

m = re.search(r'[cbm]at','aat')
m # 

m = re.search(r'[^abc]aron', '#aron')
m #  <re.Match object; span=(0, 5), match='#aron'>
```

### \

1. 다른 문자와 함께 사용되어 특수한 의미를 지님
    1. \d : 숫자를 [0-9]와 동일
    2. \D : 숫자가 아닌 문자 [^0-9]와 동일
    3. \s : 공백 문자(띄어쓰기, 탭, 엔터 등)
    4. \S : 공백이 아닌 문자
    5. \w : 알파벳 대소문자, 숫자 [0-9a-zA-Z]와 동일
    6. \W : non alpha-numeric 문자 [^0-9a-zA-Z]와 동일
2. 메타 캐릭터가 캐릭터 자체를 표현하도록 할 경우 사용
    1. \., \\

```python
re.search(r'\sand', 'apple and banana')
# <re.Match object; span=(5, 9), match=' and'>
```

### .

- 모든 문자를 의미

```python
re.search(r'p.g', 'pig')
# <re.Match object; span=(0, 3), match='pig'>
```

### 반복패턴

- 패턴 뒤에 위치하는 *, +, ?는 해당 패턴을 반복적으로 존재하는지 검사
    - + → 1번 이상의 패턴이 발생
    - * → 0번 이상의 패턴이 발생
    - ? → 0 혹은 1번의 패턴이 발생
- 반복을 패턴의 경우 greedy하게 검색 함, 즉 가능한 많은 부분이 매칭되도록 함
    - e.g) a[bcd]*b 패턴을 acddccb에서 검색하는 경우
        - ab, abcb, abcbdccb 전부 가능 하지만 최대한 많은 부분이 매칭된 abcbdccb가 검색된 패턴

```python
re.search(r'a[bcd]*b', 'abcbdccb')
# <re.Match object; span=(0, 8), match='abcbdccb'>

re.search(r'pi+g', 'pg') # i 1번 이상
re.search(r'pi*g', 'pg') # <re.Match object; span=(0, 2), match='pg'> # i 0번 이상

re.search(r'https?', 'http://www.naver.com')
# <re.Match object; span=(0, 4), match='http'>
re.search(r'https?', 'https://www.naver.com')
# <re.Match object; span=(0, 5), match='https'>
```

### ^*, *$

- ^ 문자열의 맨 앞부터 일치하는 경우 검색
- $ 문자열의 맨 뒤부터 일치하는 경우 검색

```python
re.search(r'^b\w+a', 'cabana') # 
re.search(r'^b\w+a', 'babana') # <re.Match object; span=(0, 6), match='babana'>
re.search(r'^b\w+a', 'cabana') #
re.search(r'^b\w+a', 'cabanap') #
```

### Grouping

- ()을 사용하여 그루핑
- 매칭 결과를 각 그룹별 분리 가능
- 패턴 명시 할 때, 각 그룹을 괄호() 안에 넣어 분리하여 사용

```python
m = re.search(r'(\w+)@(.+)\.com', 'test@gmail.com')
print(m.group(1)) # test
print(m.group(2)) # gmail
print(m.group(0)) # test@gmail.com
```

### {}

- *, +, ?을 사용하여 반복적인 패턴을 찾는 것이 가능하나, 반복의 횟수 제한은 불가
- 패턴 뒤에 위치하는 중괄호{}에 숫자를 명시하면 해당 숫자 만큼의 반복인 경우에만 매칭
- {4} - 4번 반복
- {3, 4} - 3 ~ 4번 반복

```python
re.search(r'pi{3,4}g', 'piiig')
# <re.Match object; span=(0, 5), match='piiig'>
```

### 마나멈 매칭(non-greedy way)

- 기본적으로 *, +, ?를 사용하면 greedy(맥시멈 매칭)하게 동작함
- *?, +?을 이용하여 해당 기능을 구현

```python
re.search(r'<.+>', '<html>haha</html>') # <re.Match object; span=(0, 17), match='<html>haha</html>'>
re.search(r'<.+?>', '<html>haha</html>') # <re.Match object; span=(0, 6), match='<html>'>
```

### {}?

- {m, n}의 경우 m번 에서 n번 반복하나 greddy하게 동작
- {m, n}?로 사용하면 non-greedy하게 동작. 즉, 최소 m번만 매칭하면 만족

```python
re.search(r'a{3,5}', 'aaaaa') # <re.Match object; span=(0, 5), match='aaaaa'>
re.search(r'a{3,5}?','aaaaa') # <re.Match object; span=(0, 3), match='aaa'> # 최소 만족
```

### Match

- search와 유사하나, 주어진 문자열의 시작부터 비교하여 패턴이 있는지 확인
- 시작부터 해당 패턴이 존재하지 않다면 None 반환

```python
re.match(r'\d\d\d', 'my number is 123')
re.match(r'\d\d\d', '123 my number is 123') # <re.Match object; span=(0, 3), match='123'>
```

### Findall

- search가 최초로 매칭되는 패턴만 반환한다면, findall은 매칭되는 전체의 패턴을 반환
- 매칭되는 모든 결과를 리스트 형태로 반환

```python
re.findall(r'[\w-]+@[\w.]+', 'test@gmail.com haha test2@gmail.com nice test test')
# ['test@gmail.com', 'test2@gmail.com']
```

### sub

- 주어진 문자열에서 일치하는 모든 패턴을 replace
- 그 결과를 문자열로 다시 반환함
- 두번째 인자는 특정 문자열이 될 수도 있고, 함수가 될 수 도 있음
- count가 0인 경우는 전체를, 1이상이면 해당 숫자만큼 치환 됨

```python
re.sub(r'[\w-]+@[\w.]+', 'great', 'test@gmail.com haha test2@gmail.com nice test test', count = 1)
# great haha test2@gmail.com nice test test
```

### compile

- 동일한 정규표현식을 매번 다시쓰기 번거로움을 해결
- compile로 해당표현식을 re.RegexObjcet 객체로 저장하여 사용가능

```python
email_reg = re.compile(r'[\w-]+@[\w.]+')
email_reg.findall('test@gmail.com haha test2@gmail.com nice test test')
# ['test@gmail.com', 'test2@gmail.com']
```
