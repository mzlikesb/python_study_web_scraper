def plus(a,b):
  if(IsNumber(a) and IsNumber(b)):
    return a + b
  return 0

def minus(a,b):
  if(IsNumber(a) and IsNumber(b)):
    return a - b
  return 0

def times(a,b):
  if(IsNumber(a) and IsNumber(b)):
    return a * b
  return 0

def division(a,b):
  if(IsNumber(a) and IsNumber(b)):
    if(b != 0):
      return a / b
    else:
      print("you can't divide by 0")
  return 0

def negation(a):
  if(IsNumber(a)):
    return a * -1
  return 0

def power(a,b):
  if(IsNumber(a) and IsNumber(b)):
    return a ** b
  return 0

def remainder(a,b):
  if(IsNumber(a) and IsNumber(b)):
    return a % b
  return 0

def IsNumber(n):  
  result = type(n) == int
  if result != True:
    print(f"{n} is not number")
  return result

print(plus(4,5))
print(minus(6,3))
print(times(8,8))
print(division(30,7))
print(negation(123))
print(power(2,5))
print( remainder(3333,12))