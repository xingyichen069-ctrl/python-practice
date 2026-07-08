#函数返回第n个斐波那契数
def n_fib(n):
    if n==0:return 1
    if n==1:return 1
    else:return n_fib(n-1)+n_fib(n-2)

n= int(input("Please input the position of your wanted number: "))
print(f"Your wanted number is: {n_fib(n)}")

#or:

def k_fib(k):
    a,b=1,1
    for i in range(k-1):
        a,b = b,a+b
        return a

n= int(input("Please input the position of your wanted number: "))
print(f"Your wanted number is: {k_fib(n)}")

#意义等级 ：1⭐
