# 涉及:函数定义，简单运算，用户交互，异常处理

def divide(x, y):
    try:
        result = x / y
    except:
        print("error occur")
    else:
        print('result=', result)
    finally:
        print("divide end")


print("calculate a/b")
print("input num a")
a = input("a=")
while not a.isdigit():
    print("pleas input digit")
    a = input("a=")

print("input num b")
b = input("b=")
while not b.isdigit():
    print("pleas input digit")
    b = input("b=")

divide(int(a), int(b))
