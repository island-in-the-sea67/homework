'''
def add()
    result = 1 + 2
    print(f"1+2的结果是：{result}")

add()


def add(x, y):
    result = x + y
    print(f"{x}+{y}的结果是:{result}")

# 调用函数
add(6, 7)

print('6799','1299',sep='>=',end=' ')  # sep= 同print用什么符号进行隔开   end=两句print之间用什么隔开
print('3499')

# 定义一个函数，形参param1，默认参数param2=2
def fun_default_parameters(param1, param2=2):
    print(param1+param2)
fun_default_parameters(1)
fun_default_parameters(1, 5)
'''
'''
# 关键字参数的正常调用
def fun_keyword_parameters(param1, param2=2):
    print(param1-param2)
fun_keyword_parameters(param1=5, param2=2)
'''
# 关键字参数不按顺序传递
'''
def fun_keyword_parameters(param1, param2=2):
    print(param1-param2)
    
fun_keyword_parameters(param2=2, param1=5)
 print(name)
   print(tw)
   print(fs)

# 位置参数在前，关键字在后，关键字在前取值会冲突，
# fun_keyword_parameters(param1=5， 2)
# 实例
def fun_parameters(name,tem,fs='居家隔离'):

    if tem <= 37.5:
        print(f"{name}的体温是{tem}小于37.5，正常")
    else:
        print(f"{name}的体温是{tem}大于37.5，隔离方式{fs}")
name1=input("姓名：")
tem1=float(input("体温："))
fs1='居家隔离'
fun_parameters(name1,tem1,fs1)

# 什么是返回值
def add(a, b):
    result= a +b
    return result
r = add(1, 2)
print(r)



def fun_num(t, z):
    count = 0
    for c in t:
        if c == z:
            count += 1
    return count


# 使用函数
t = "sea island"
z = "a"
count = fun_num(t, z)
print(f"字符 '{z}' 在字符串中出现了 {count} 次。")
# 位置传递，没有默认值 关键字有。
# 位置传递
def user_info(*args):
    print(args)
# ('TOM')
user_info('TOM')
# ('TOM', 18)
user_info('TOM', 18)
# 传递进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是位置传递

# 关键字传递
def user_info(**kwargs):
    print(kwargs)

# {'name':'TOM','age':'18','id':'110'}
user_info(name='TOM',age=18,id=110)
# 参数是“键=值”形式的形式的情况下，所有的“键=值”都会被kwargs接受，同时会根据“键=值”组成字典

def sum(*nums):
    # *nums: 一个包含任意数量数字的元组。 定义一个变量，来保存结果
    result=0
    # 遍历元组，并将
    for n in nums:
        result += n
    print(result)

sum(123,456,67)

# 递归函数 什么是函数的嵌套
# 一个函数里面又调用了另外一个函数
# 例子1
def func_b():
    print("---2---")
def func_a():
    print("---1---")

    func_b()
    print("---3---")
# 调用函数func_a
func_a()

# 例子2
def fun1(x,y):
    print("这是函数一")
    sum=x+y
    return sum

def fun2():
    print("这是函数二")
    sum=fun1(2,3)
    print(sum)
fun2()
例子3.1
def max(x,y):
    return x 
    if x>y
    else y;

# 例子3.2
def maxs(a,b,c,d):
    res1 = max(a,b);
    res2 = max(res1,c);
    res3 = max(res2,d);
    return res3;
print(maxs(5,2,420,299))
'''
# 递归函数python代码示例
# 示例一 定义一个函数'factorial',用于计算给定数值的阶乘。如果输入值'n'等于1
# 则认为阶乘的结果是1 ，因此我们返回1。否则，'n'与'factorical(n-1)'的结果相乘递归计算阶乘
def factorial(n):
    if n ==1:
        return 1    # 边界
    else:
        return  n*factorial(n-1)    # 递归函数
# 测试
num=5
result=factorial(num)
print(f"The factorial of {num} is:{result}")