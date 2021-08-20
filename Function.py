# create a function
def func():
    print("Inner Area")

print("Out Area")

func()

def sum1():
    print(30+20)

sum1()

def sum2():
    return 40+10
v = sum2()
print(v)

def sum3(num1,num2):
    return num1 +num2
print(sum3(10,20))
print(sum3(10,21.8))
print(sum3("Wali","Ullah"))

def manyvalueprint(*num):
    sum=0
    for i in num:
        sum = sum+i
    print(sum)
manyvalueprint(10,20,30,40,50)
def nested_func(a,b):
    a = a+10
    b = b+20
    return a+b


print(nested_func(100, 200))