https://docs.python.org/3.5/tutorial/introduction.html#numbers
#关键字
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise

来源： https://docs.python.org/3.5/reference/lexical_analysis.html
#基本数据类型
##list
```
>>> word1=["a","b"]
>>> word1
['a', 'b']
>>> word2=word1[:]   #会生成一个新的数组，对新的数组做修改，不会影响原来的数据
>>> word2.insert(0,"c")
>>> word2
['c', 'a', 'b']
>>> word1
['a', 'b']
>>>
```
1. list切割
2. 循环
```
>>> a,b=0,1
>>> while b<10:
	print (b)
	a,b=b,a+b
1
1
2
3
5
8
>>>
```

3. 判断
```
x=20
if x < 0:
    x=0
    print("x=0")
elif x==0:
    print("x=0")
else:
    print("else")

```
4. for
```
words=["abc","def"]
for w in words:
    print(w,len(w))

```
5 range()
```
>>> list(range(6))
[0, 1, 2, 3, 4, 5]
>>> range(6)
range(0, 6)
```
6. def
```
>>> def fib(n):
	a,b=0,1
	while a<n:
		print(a,end='  ')
		a,b=b,a+b


>>> fib(10)
0112358
>>>
```
设置默认值
```
def ask_ok(prompt,retries=4,reminder="try again"):
    while True:
        ok=input(prompt)
        if ok in ("y","ye","ues"):
            return True
        if ok in ("n","no"):
            return False
        retries=retries-1
        if retries<0:
            raise ValueError("invalid response")
        print (reminder)
```
默认值的更新:**The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.**
```
def change(a=10):
    print(a)
    a=11
change()
change()
>>>
10
10
```

```
def change(a=[]):
    print(a)
    a.append(1)
change()
change()
>>>
[]
[1]
```

7. 匿名函数
```
def make_increment(n):
    return lambda x:x+n
f=make_increment(10)
>>> f(0)
10
>>> f(1)
11
>>>
```
8. 自定义方法属性：_annotations_
#数据结构
1. list
list.append(x)#添加一个元素到list
list.extend(L)#添加一个列表到list
list.insert(i,x)#在第i处插入x（插入之后，x是第i个元素，即list[i]==x）
list.remove(x)#删除**第一个**元素x
list.pop(i)#删除第i个元素,返回被移除后的list
list.clear()
list.index(x)
list.count(x)#返回x元素出现的个数
list.sort()
list.reverse()
list.copy()
del
2. list公式
```
list(x**2 for x in range(10))
list(map(lambda x: x**2, range(10)))
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
[x**2 for x in range(10)]
```
3. tuple
4. sets
```
>>> seta={"abc","def"}
>>> seta
{'def', 'abc'}
>>> a=set("abc")   #创建set
>>> a
{'a', 'c', 'b'}
>>> setb={"abc","abc","def"}
>>> setb
{'def', 'abc'}
>>>
```
```
>>> a=set("abcdefabc")
>>> b=set("abc")
>>> a-b
{'f', 'd', 'e'}
>>> c={x for x in a if x not in b}   #同list相似的语法
>>> c
{'f', 'd', 'e'}
>>>
```
5. dictionaries
```
>>> tel={"a":1,"b":2}
>>> tel["a"]
1
>>> tel
{'a': 1, 'b': 2}
>>> del tel["a"]
>>> tel
{'b': 2}
>>> list(tel.keys())
['b']
>>> "b" in tel
True
>>> "a" in tel
False
>>> "a" not in tel
True
>>>
```
dict构造函数
```
>>> dict([("a",1),("b",2),("c",3)])
{'a': 1, 'c': 3, 'b': 2}
>>> dict(a=1,b=2,c=3)   #只适用于key为string的dict
{'a': 1, 'c': 3, 'b': 2}
>>> {x:x**2 for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>>
```
```
>>> a=dict(a="a",b="b",c="c")
>>> b=dict(d="d",e="e",f="f")
>>> for k,v in a.items():
	print(k,v)


a a
c c
b b
>>> for a1,b1 in zip (a,b):
	print(a1,b1)


a f
c d
b e
>>> for k,v in enumerate(["a","b"]):
	print (k,v)


0 a
1 b
>>>
```
#模块化：脚本编程
包引入
```
import a.b.c
a.b.c.f()
```
```
from a.b import c
c.f()
```
```
from a.b.c import f
f()
```
#异常处理
```
while True:
    try:
        x=int (input("input a num\n"))
        print (x)
        break

    except ValueError:
        print("error\n")
```
```
import sys
try:
    f = open('data.txt')
    s = f.readline()
    i = int(s.strip())
    print (i)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise   #重新抛出异常
```
**The try ... except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception**
···
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
···
**The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances**
```
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```
```
def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("divide zero")
    else:
        print("result",result)
    finally:
        print("divide end")

>>> divide(10,1)
result 10.0
divide end
>>> divide(1,0)
divide zero
divide end
>>> divide("1","2")
divide end
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    divide("1","2")
  File "C:/Users/hp/Desktop/1.py", line 3, in divide
    result=x/y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>>
```



```
def count():
    fs=[]
    for i in range (1,4):
        def f(j):
##            def g():
##                return j*j
##            return g
            return lambda :j*j
        fs.append(f(i))
    return fs
f1,f2,f3=count()
#分析下这个代码，首先明确f(j)是一个函数指针，对应的，f1,f2,f3也是三个函数指针，f1()调用的时候，会调用f(j)这个函数，对应的调用匿名函数j*j,这里的j是通过函数f传进来的
```
#map&reduce()
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])#把传入的参数分别计算返回结果的list
reduce( lambda x, y: x * y, range( 1, n + 1 ), m ) #迭代每次的返回结果
#__name__   获取函数的名字
