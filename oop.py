
# *args, **kwargs

def func1(*args, **kwargs):
  r1=0
  for a in args:
    r1+=a
  print(r1)
  print(args, kwargs)

#func1(1,2,3,4,5,7, a=True, b=False, c=False)

class Car():
  name = "Car"
  doors = 4
  wheels = 4

  def __init__(self, **kwargs):
    self.doors = 4
    self.wheels = 4
    self.color = kwargs.get("color","black") # dict에서 값을 가져오고 없으면 기본값 지정
    self.price = kwargs.get("price","$500")
    self.name = kwargs.get("name", "Car")

  # 기본 메서드 override
  def __str__(self):
    return f"doors:{self.doors}, wheels:{self.wheels}, color:{self.color}, price:{self.price}"


# 클래스 상속
class Convertible(Car):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.time = kwargs.get("time",10)

  def take_off(self):
    return f"taking off {self.name}"



# __main__

mini = Car()
print(dir(Car)) # 클래스 안에 들어있는 내용물 확인
print(mini) # mini.__str__()
mini.seats = 10 # 클래스 확장

print(dir(Car)) # 클래스 안에 들어있는 내용물 확인
c1 = Car(color="yellow")
print(c1)

c2 = Convertible()
print(c2)
print(c2.take_off())