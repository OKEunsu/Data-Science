


# 클래스

## 클래스 용어 정리

클래스 : 제품의 설계도

객체 : 설계도로 만든 제품

속성 : 클래스안의 변수

메서드 : 클래스 안의 함수

생성자 : 객체를 만들 때 실행되는 함수

인스턴스 : 메모리에 살아있는 객체

```python
class 클래스 이름:
	def 메서드 이름(self):
		명령블록

# ----

class Monster:
	def say(self):
		print("나는 몬스터다")

# ----

객체 = 클래스이름()
객체.메서드()

# ----

shark = Monster()
shark.say()

# ----

class Monster:
	def __init__(self, name): # 생성자 함수
		self.name = name

	def say(self):
		print(f"나는 {self.name}")

# ----

shark = Monster('상어')
shark.say()
```

---

### Class란?

- 실세계의 것을 모델링 하여 속성(attribute)와 동작(method)를 갖는 데이터 타입
- python에서의 string, int, list, dict 모두가 다 클래스로 존재
- 예를 들어 학생이라는 클래스를 만든다면, 학생을 나타내는 속성과 학생이 행하는 행동을 함께 정의 할 수 있음
- 따라서, 다루고자 하는 데이터(변수)와 데이터를 다루는 연산(함수)를 하나로 캡슐화하여 클래스로 표현
- 모델링에서 중요하시 하는 속성에 따라 클래스의 속성과 행동이 각각 달라짐

### Object란

- 클래스로 생성되어 구체화된 객체(인스턴스)
- 파이썬의 모든 것(intm str, list, etc)은 객체(인스턴스)
- 실제로 class가 인스턴스화 되어 메모리에 상주하는 상태를 의미
- class가 빵틀이라면, object는 실제로 빵틀로 찍어낸 빵이라고 비유 가능

### 생성자(__**init__**)

- 생성자, 클래스 인스턴스가 생성될 때 호출됨
- self인자는 항상 첫번째에 오며 자기 자신을 가리킴
- 이름이 꼭 self일 필요는 없지만, 관례적으로 self로 사용
- 생성자에서는 해당 클래스가 다루는 데이터를 정의
    - 이 데이터를 멤버 변수 또는 속성이라고 함

```python
class Person:
    def __init__(self):
        self.name = 'Kate'
        self.age = 10

p1 = Person()
print(p1.name, p1.age)
# Kate 10
p1.name = 'aaron'
p1.age = 30
print(p1.name, p1.age)
# aaron 30

# --- 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Bob', 30)
p2 = Person('Kate', 20)
print(p1.name, p1.age)
# Bob 30
print(p2.name, p2.age)
# Kate 20

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
      print(self.name, '은 잠을 잡니다.')

a = Person(self,'Aaron', 20)
a.sleep()
```

### Mehtod 정의

- 멤버 함수라고도 하며, 해당 클래스의 object에서만 호출 가능
- 메소드는 객체 레벨에서 호출되며, 해당 객체의 속성에 대한 연산을 행함
- {obj}.{method}() 형태로 호출됨

```python
# 1. 숫자를 하나 증가
# 2. 숫자를 0으로 초기화

class Counter:
  def __init__(self):
    self.num = 0

  def increment(self):
    self.num += 1

  def reset(self):
    self.num = 0

  def print_current_value(self):
    print('현재값은 :',self.num)

c1 = Counter()
c1.print_current_value() # 0
c1.increment() # +1
c1.increment() # +1
c1.print_current_value() # 2
c1.reset() # 0
c1.print_current_value() # 0
# 현재값은 : 0
# 현재값은 : 2
# 현재값은 : 0
```

### Method type

- instance method - 객체로 호출
    - 메소드는 객체 레벨로 호출 되기 때문에, 해당 메소드를 호출한 객체에만 영향을 미침
- class  method(static method) - class로 호출
    - 클래스 메소드의 경우, 클래스 레벨로 호출 되기 때문에, 클래스 멤버 변수만 변경 가능

### Class Inheritance(상속)

- 기존에 정의해둔 클래스의 기능을 그대로 물려받을 수 있다.
- 기존 클래스에 기능 일부를 추가하거나, 변경하여 새로운 클래스를 정의한다.
- 코드를 재사용할 수 있게 된다.
- 상속 받고자 하는 대상인 기존 클래스는 (Parent, Super, Base class 라고 부른다)
- 상속 받는 새로운 클래스는(Child, Sub, Derived class 라고 부른다.)
- 의미적으로 is-a 관계를 갖는다.

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def eat(self, food):
    print('{}은 {}를 먹습니다.'.format(self.name, food))

  def sleep(self, minute):
    print('{}은 {}분동안 잡니다.'.format(self.name, minute))

  def work(self, minute):
    print(self.name, '은', minute, '분 동안 일을 합니다.')

class Student(Person):
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee(Person):
  def __init__(self, name, age):
    self.name = name
    self.age = age

bob = Student('bob', 25)
bob.eat('pizza')
bob.sleep(3)
bob.work(5)
# bob은 pizza를 먹습니다.
# bob은 3분동안 잡니다.
# bob 은 5 분 동안 일을 합니다.

bob = Employee('bob', 25)
bob.eat('pizza')
bob.sleep(3)
bob.work(5)
# bob은 pizza를 먹습니다.
# bob은 3분동안 잡니다.
# bob 은 5 분 동안 일을 합니다.
```

### Method override

- 부모 클래스의 method를 재정의
- 하위 클래스(자식 클래스)의 인스턴스로 호출시, 재정의된 메소드가 호출됨

```python
class Student(Person):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def work(self, minute):
		print('{}은 {}분 동안 공부합니다.'.format(self.name, minute))

bob = Student('bob', 25)
bob.eat('pizza')
bob.sleep(3)
bob.work(5)
# bob은 pizza를 먹습니다.
# bob은 3분동안 잡니다.
# bob은 5분 동안 공부합니다.
```

### Super

- 하위클래스(자식 클래스)에서 부모클래스의 method를 호출할 때 사용
- override를 하면 부모 클래스 메소드를 사용하지 못함

```python
class Student(Person):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def work(self, minute):
		super().work(minute)
		print('{}은 {}분 동안 공부합니다.'.format(self.name, minute))

bob = Student('bob', 25)
bob.eat('pizza')
bob.sleep(3)
bob.work(5)
```

### Special method

- __로 시작 __로 끝나는 특수 함수
- 해당 메소드를 구현하면, 커스텀 객체에 여러가지 파이썬 내장 함수나 연산자를 적용 가능
- 오버라이딩 가능한 함수 목록은 https://docs.python.org/3/reference/datamodel.html 에서 확인

```python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, pt):
    new_x = self.x + pt.x
    new_y = self.y + pt.y
    return Point(new_x, new_y)
  
  def __sub__(self, pt):
    new_x = self.x - pt.x
    new_y = self.y - pt.y
    return Point(new_x, new_y)

  def __mul__(self, factor):
    return Point(self.x * factor , self.y * factor)

  def distance_from_origin(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

  def __getitem__(self, index):
    if index == 0:
      return self.x
    elif index == 1:
      return self.y
    else:
      raise IndexError("Index out of range")

  def __str__(self):
    return '({}, {})'.format(self.x, self.y)

p1 = Point(3, 4)
p2 = Point(2, 7)

p3 = p1 + p2
print(p3) # (5, 11)

p4 = p1 - p2
print(p4) # (1, -3)

p5 = p1 * 3
print(p5) # (9, 12)

p6 = p1.distance_from_origin()
print(p6) # 5.0

print(p1.x) # 3
print(p1[0]) # 3
```

---

## 클래스와 객체의 개념

- 클래스 : 객체를 만들기 위한 설계도
- 객체 : 설계도로부터 만들어낸 제품

# 디버깅
assert은 python에서 주어진 조건이 True인지 확인하고 그렇지 않으면 AssertionError를 발생시키는 명령어 입니다. 주로 디버깅이나 코드의 예상된 동작을 검증하기 위해 사용

```python
assert 조건, "오류 메세지"
```

```python
# 기본 사용법
x = 10
assert x == 10 # x가 10인지 확인, 조건이 True이므로 아무 오류도 발생하지 않음

# 조건이 False일 떄
x = 5
assert x == 10, "x는 10이어야 합니다."
```

### 활용방법

- 디버깅 : 코드의 가정이나 특정 상태가 예상대로 유지되는지 확인할 때 유용합니다.
- 테스트 : 단위 테스트에서 조건을 검증하고,  예상 결과가 실제 결과와 일치하는지 확인하는 데 사용됩니다.
- 문서화 : 코드의 특정 조건이나 가정이 명확하게 문서화되어 있음을 보장할 수 있습니다.
