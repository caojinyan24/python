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
while (True):
    print("input num a")
    a = input("a=")
    if (a.isdigit()):
        a = int(a)
        break
while (True):
    print("input num b")
    b = input("b=")
    if (b.isdigit()):
        b = int(b)
        break
divide(a, b)
